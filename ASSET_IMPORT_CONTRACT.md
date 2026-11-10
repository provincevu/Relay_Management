# Asset Import Contract (Draft)

> **Status:** Draft for review. This document proposes a consistent import contract for the new backend; it does not claim that these rules existed in the legacy application. Any default marked as configurable can be changed before implementation.
>
> **Evidence boundary:** Legacy behavior below is based only on the import code included in `repomix-backend.md`. The source is a packed/partly elided representation, so omitted implementation details are explicitly marked **Unknown**.

## 1. Purpose and scope

Provide a predictable way for an authorized operator to load catalog and electrical asset records into the new RMS without creating orphaned Station, Bay, or Relay records. The proposed flow validates the whole file before writing and reports row-level errors.

The first version covers one entity type per file:

1. `catalog_item`
2. `station`
3. `bay`
4. `relay`

Import in dependency order: catalog items, stations, bays, then relays. Organization and CatalogType records are prerequisites and are not created by this import contract.

## 2. What the legacy source shows

| Legacy operation | Behavior visible in `repomix-backend.md` | Not determinable from the source excerpt |
|---|---|---|
| Relay bulk create under a Bay | Admin-only view; accepts CSV upload decoded as UTF-8 and comma-delimited, with positional columns `relay_code`, `relay_name`, `manufacturer`; also accepts tab-separated pasted text with the same positional interpretation. No header skip is shown in the CSV loop. | Whether blank rows are ignored, exact validation, duplicate handling, transaction/rollback behavior, and exact response/error behavior. |
| Global bulk create | Admin-only view; reads the active worksheet of an uploaded Excel workbook with `data_only=True`, skips row 1 as a header, and reads positional columns for Station code/name, Bay code/name, Relay code/name, and manufacturer. Caches Station and Bay lookups while processing. | Required/optional fields beyond visible fallbacks, exact creation/update semantics, duplicate handling, atomicity, and exact response/error behavior. |
| Legacy identifier mapping | Source excerpt names the above fields and models. | A canonical external-system identifier mapping for every imported field is **Unknown**. |

The new contract below intentionally replaces the different positional formats with one explicit format. It must not be presented as a backward-compatible parser for old files.

## 3. Proposed file format

### 3.1 CSV rules

- One UTF-8 CSV file, accepting an optional UTF-8 BOM.
- Comma delimiter and standard CSV quoting rules.
- A header row is required. Header names are exact, lowercase `snake_case` as listed below; unknown, missing, or duplicate headers reject the file.
- Values are trimmed at the edges. Codes remain case-sensitive unless a future domain rule explicitly changes this.
- Empty values are allowed only for optional fields. For a new record, an empty optional field maps to its model's empty/null representation. For an existing record, an empty optional field is treated as the desired empty/null value during comparison; it does not mean “leave unchanged.”
- Boolean values use `true` or `false` only. Integer values use base-10 digits. Date-time values use ISO 8601 with an explicit timezone. Invalid values are row errors.
- File size, row count, and processing timeout limits: **Unknown / to be configured before production**.

### 3.2 Entity schemas

Fields named here map to the current RMS model fields. `external_id` is an optional import column used to create an `ExternalReference`; it is not a field on the asset model.

| Entity type | Required columns | Optional columns |
|---|---|---|
| `catalog_item` | `catalog_type_code`, `code`, `name` | `description`, `sort_order`, `is_active`, `external_id` |
| `station` | `code`, `name`, `organization_code` | `location`, `voltage_level_code`, `commissioned_at`, `installed_at`, `is_active`, `external_id` |
| `bay` | `station_code`, `code`, `name` | `rated_voltage`, `rated_current`, `legacy_sdm`, `is_active`, `external_id` |
| `relay` | `station_code`, `bay_code`, `code`, `name` | `model_name`, `manufacturer_code`, `is_active`, `external_id` |

Mapping notes:

- `organization_code` resolves to an existing `Organization.code`.
- `catalog_type_code` resolves to an existing `CatalogType.code`; `voltage_level_code` must resolve to a `CatalogItem` under type `VOLTAGE_LEVEL`; `manufacturer_code` must resolve to a `CatalogItem` under type `MANUFACTURER`.
- `station_code` and `bay_code` together identify the Bay parent for Relay rows. The Bay must belong to the specified Station.
- The source of `organization_code` and the actual catalog values to preload are **Unknown**. The implementation must not silently create them.
- `is_active` defaults to the model default (`true`) when omitted for a new record. Explicit `false` is retained. This is a proposed default based on current model defaults, not a legacy import rule.
- `external_id` requires request-level `source_system`. Proposed supported source identifiers are stable codes up to 64 characters; allowed values/list are **Unknown / to be configured**.
- Proposed `ExternalReference.entity_type` values are `catalog.catalogitem`, `assets.station`, `assets.bay`, and `assets.relay`. These are contract identifiers, not Django content-type IDs, and must stay stable once imports are persisted.
- External-reference records are scoped uniquely by `(source_system, entity_type, external_id)`, matching the current `ExternalReference` uniqueness rule. Existing references cannot be reassigned to a different local entity by import.

## 4. Record identity and duplicate policy (proposed defaults)

Natural keys use the uniqueness constraints in the current models:

| Entity | Natural key |
|---|---|
| CatalogItem | `(catalog_type_code, code)` |
| Station | `code` |
| Bay | `(station_code, code)` |
| Relay | `(station_code, bay_code, code)` |

Proposed behavior:

1. A repeated natural key inside the same file is a row error for each repeated occurrence after the first. The importer does not choose a “last row wins” result.
2. If the natural key already exists and all imported writable values match after normalization, report `unchanged`.
3. If the natural key exists but any imported writable value differs, report a conflict. Import does not overwrite existing data. A separate, explicitly authorized update mode can be designed later.
4. If an `external_id` is already linked to another local entity under the same source and entity type, report a conflict.
5. Parent records are never auto-created. Missing Organization, CatalogType, CatalogItem, Station, or Bay references are row errors.

These are new-backend safety defaults; legacy duplicate and overwrite behavior is **Unknown**.

## 5. Proposed API contract

### `POST /api/v2/assets/imports/`

Content type: `multipart/form-data`

| Input | Type | Required | Meaning |
|---|---|---:|---|
| `entity_type` | string | Yes | One of `catalog_item`, `station`, `bay`, `relay`. |
| `mode` | string | Yes | `preview` or `apply`. |
| `file` | file | Yes | CSV matching that entity's schema. |
| `source_system` | string | Only when any row contains `external_id` | Source namespace for `ExternalReference`. |
| `Idempotency-Key` | header | For `apply` | Prevents duplicate apply requests when clients retry after a connection failure. Key retention period: **Unknown / to be configured**. |

Authorization: **Exact role/capability is Unknown**. The existing architecture calls for scoped access checks and import audit/SyncRun; the endpoint must enforce them server-side. It must not assume that Django `is_staff` alone grants asset-import permission.

Proposed response: `202 Accepted` with an import-run resource because the architecture defines imports as jobs. Exact synchronous/asynchronous threshold is **Unknown / to be configured**; this draft proposes that both preview and apply use the job flow for a consistent status/result interface.

```json
{
  "id": "<run-id>",
  "entity_type": "station",
  "mode": "preview",
  "status": "QUEUED",
  "created_at": "<ISO-8601 timestamp>",
  "status_url": "/api/v2/assets/imports/<run-id>/"
}
```

The example illustrates the shape only. ID representation and timestamps are governed by the implementation's standard API serialization.

### `GET /api/v2/assets/imports/{run_id}/`

Proposed response fields:

- Run identity: `id`, `entity_type`, `mode`, `status`, `created_at`, `started_at`, `finished_at`.
- Counts: `total_rows`, `created_count`, `unchanged_count`, `error_count`.
- Row results: CSV row number (header is row 1), outcome (`created`, `unchanged`, `error`, or `conflict`), stable error code, human-readable message, and affected natural key when resolvable.
- Never return uploaded file contents or secret material in the response.

Proposed run statuses: `QUEUED`, `PROCESSING`, `PREVIEWED`, `COMPLETED`, `REJECTED`, `FAILED`. `PREVIEWED` means validation completed and no database writes were made. `REJECTED` means apply was requested but validation/conflicts prevented all writes. `FAILED` means an unexpected processing failure; exact retry/recovery policy is **Unknown / to be configured**.

### Error envelope

Use the common RMS error envelope in `BACKEND_NEW_ARCHITECTURE.md` for request-level errors. Proposed cases:

| HTTP status | Case |
|---|---|
| `400` | Missing/invalid form fields, unsupported entity type/mode, malformed CSV/header, missing `source_system` when required. |
| `401` | No valid authenticated identity. |
| `403` | Authenticated identity lacks the configured import capability or asset scope. |
| `404` | Requested import run does not exist or is not visible in the caller's scope. |
| `409` | Idempotency key reused with a different request, or apply conflicts with an existing run/request state. |
| `413` | Configured file-size limit exceeded. Actual limit: **Unknown**. |
| `422` | File parsed, but one or more rows fail validation or reference resolution; row details are available from the run resource. |

The legacy source excerpt does not establish HTTP statuses or response schemas. These are proposed new API behavior.

## 6. Preview and apply transaction rules (proposed defaults)

- `preview` parses and validates the complete file, resolves every parent/reference, returns row outcomes, and performs no writes to assets or `ExternalReference`.
- `apply` performs the same validation first. If any row has an error or conflict, write no asset or external-reference rows and finish as `REJECTED`.
- If all rows are valid, apply the full file in one database transaction. Any unexpected database failure rolls back all rows in that import run.
- The atomicity boundary is one file/entity type, not a multi-file hierarchy. The caller imports each type in dependency order.
- A preview is advisory: apply revalidates against current database state, so changes after preview may turn into conflicts.
- Import run/audit metadata may persist even when asset writes are rejected or rolled back, so operators can inspect what happened. Exact audit model/storage is **Unknown** in the current code and belongs to implementation design.

## 7. Data placement and retention

- Imported business records are written to PostgreSQL tables for `CatalogItem`, `Station`, `Bay`, and `Relay`.
- External IDs are written to `ExternalReference`, not copied into asset primary keys.
- Import run/report persistence model and uploaded-file storage location/retention are **Unknown** in the current implementation and must be decided before production. Proposed minimum: retain run metadata and row-level error report for audit; avoid retaining duplicate upload copies longer than operationally required.
- Do not put full row payloads containing unnecessary personal or secret data into logs.

## 8. Completion criteria for the first implementation slice

The contract can be implemented incrementally. For the first small vertical slice, support `catalog_item` **preview only**:

1. Validate request fields, CSV encoding/header, required values, types, and references to existing `CatalogType`.
2. Detect duplicate natural keys within the file and conflicts against existing `CatalogItem` values.
3. Return a run/status/result resource with row numbers and stable error codes.
4. Prove preview makes no database writes.
5. Do not implement `apply` or Station/Bay/Relay import until this slice is reviewed and verified.

## 9. Open decisions before production apply

- Import roles/capabilities and scope behavior: **Unknown**.
- Maximum upload bytes, row count, and job timeout: **Unknown**.
- Allowed `source_system` codes and ownership/approval: **Unknown**.
- Run/report retention and upload-object storage/cleanup: **Unknown**.
- Whether a later explicit update mode is needed: **Unknown**.
- Whether imports need cancellation or operator retry after `FAILED`: **Unknown**.
- Exact API ID and datetime representation: follow the existing RMS API convention when implemented; **not established by this draft**.
