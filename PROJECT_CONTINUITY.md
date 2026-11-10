# RMS Project Continuity

> **Mục đích:** Tài liệu bàn giao liên tục cho các phiên làm việc và Agent khác. Đọc tài liệu này trước khi thay đổi mã. Nó nêu ranh giới giữa những gì đã chạy, việc đang dở và thiết kế chưa triển khai.
>
> **Cập nhật gần nhất:** 2026-11-11 (Asia/Bangkok)
>
> **Quy ước trạng thái:** `DONE` = đã triển khai và đã có kiểm tra kỹ thuật được ghi nhận; `IN PROGRESS` = mã đã có nhưng chưa hoàn tất xác minh/handoff; `PLANNED` = đã được duyệt ở mức kiến trúc, chưa triển khai; `DECISION NEEDED` = không được tự suy đoán.

## 1. Điểm bắt đầu bắt buộc

Đọc theo thứ tự sau trước khi lập kế hoạch hoặc sửa mã:

1. [`AGENTS.md`](AGENTS.md): quy ước mã nguồn bắt buộc.
2. Tài liệu này: trạng thái bàn giao và ranh giới công việc.
3. [`BACKEND_NEW_ARCHITECTURE.md`](BACKEND_NEW_ARCHITECTURE.md): kiến trúc mục tiêu, quy tắc nghiệp vụ đã chốt, roadmap và tiêu chí MVP.
4. [`API_CONTRACT.md`](API_CONTRACT.md): hợp đồng OCR local đang tồn tại.
5. [`ASSET_IMPORT_CONTRACT.md`](ASSET_IMPORT_CONTRACT.md): hợp đồng nhập tài sản được đề xuất và phạm vi lát cắt hiện tại.

Tài liệu khảo cứu mã cũ chỉ dùng để truy vết bằng chứng, không dùng để suy ra quy tắc mới nếu tài liệu không thể hiện rõ:

- [`BACKEND_AUDIT.md`](BACKEND_AUDIT.md), [`FRONTEND_AUDIT.md`](FRONTEND_AUDIT.md)
- [`repomix-backend.md`](repomix-backend.md), [`repomix-frontend.md`](repomix-frontend.md), [`repomix-urls.md`](repomix-urls.md)

Khi hai tài liệu mâu thuẫn, ưu tiên theo thứ tự: quyết định trực tiếp của chủ sản phẩm trong `BACKEND_NEW_ARCHITECTURE.md` → contract hiện hành → mã đã triển khai → audit mã cũ. Không tự chuyển một nội dung `Unknown`/`Không xác định` thành quy tắc.

## 2. Quy tắc làm việc bắt buộc

### 2.1. Ngôn ngữ, tên và chú thích

- Dùng tiếng Anh đơn giản, rõ nghĩa cho biến, hàm, class, module, file và URL.
- Chỉ dùng tiếng Việt không dấu cho biến/field/key/test khi tên miền quá khó diễn đạt bằng tiếng Anh; luôn giải thích nghĩa gần đó bằng comment hoặc contract.
- Viết comment tiếng Việt giải thích mục đích hàm và điều kiện/vòng lặp không hiển nhiên.
- Giao diện hướng người dùng ghi theo dạng `English (Tiếng Việt)`, ví dụ `Relay (Rơ-le)`. Không dùng nhãn chỉ tiếng Anh như `Bays`, `Relays`, `Stations`, `Audit Event`.
- Không đổi tên public API/model/interface đang có chỉ để chỉnh style.

### 2.2. Kiến trúc và dữ liệu

- Kiến trúc là **modular monolith** Django/DRF với PostgreSQL, Redis, Celery, Channels/Daphne và Docker Compose. OCR local là dịch vụ HTTP độc lập, không nhúng OCR engine vào Django.
- HTTP view, serializer và WebSocket consumer chỉ xử lý giao tiếp/DTO/xác thực. Nghiệp vụ đặt ở application service; Celery task gọi service, không chép lại rule.
- Mỗi thay đổi nghiệp vụ phải có `AuditEvent`; event bất đồng bộ đi qua `OutboxEvent` trong cùng transaction khi tính năng cần phát event.
- `identity` và `catalog` không phụ thuộc `assets`, `sheets`, `ocr`; `assets` có thể phụ thuộc `identity`/`catalog`; `sheets` mới phụ thuộc `assets`/`ocr` qua service/interface.
- Không để UI/JavaScript quyết định quyền, workflow transition hoặc ghi trực tiếp dữ liệu nghiệp vụ.
- Không log secret, token OCR, nội dung tệp không cần thiết hoặc trả secret qua API/UI.

### 2.3. Cách làm một lát cắt

1. Chọn đúng một kết quả người dùng có thể kiểm chứng, không mở rộng sang lát cắt sau.
2. Kiểm tra các quyết định nghiệp vụ tác động trực tiếp. Nếu chưa chốt, đặt policy/config/interface thay thế được hoặc dừng ở `DECISION NEEDED`; không tự bịa rule.
3. Cập nhật migration, API contract và UI cùng lúc nếu thay đổi model/API có người dùng sử dụng.
4. Giữ lỗi theo common error envelope; quyền/scope phải kiểm tra phía backend.
5. Chạy kiểm tra tương xứng trước khi bàn giao. Không tự thêm test khi chủ sản phẩm chưa yêu cầu, nhưng luôn chạy `python manage.py check` và kiểm tra migration khi có thay đổi model/migration.
6. Sau mỗi lát cắt, cập nhật tài liệu này: trạng thái, bằng chứng kiểm tra, rủi ro, và **một** công việc nhỏ kế tiếp.

### 2.4. Lệnh local và vận hành

```powershell
docker compose up --build
docker compose exec web python manage.py migrate
docker compose exec web python manage.py check
docker compose exec web python manage.py makemigrations --check --dry-run
docker compose exec worker celery -A rms.config inspect ping --timeout=5
Invoke-RestMethod http://localhost:8000/health/
Invoke-RestMethod http://localhost:8000/ready/
```

Docker Compose không bind mount mã nguồn. Sau khi thay đổi code/static/template, cần `docker compose up --build -d web`; thay đổi task Celery cần dựng lại `worker` (và `beat` nếu có lịch mới).

## 3. Kiến thức dự án và quyết định đã chốt

RMS là hệ thống quản lý rơ-le. Luồng MVP hướng tới: quản lý cây trạm/ngăn lộ/rơ-le → tạo phiếu và upload PDF → OCR local → Điều độ rà soát → phân công/ký/duyệt → công bố baseline cấu hình rơ-le. UI cũ không phải thứ phải giữ nguyên; chỉ kế thừa pattern tốt và mọi màn hình MVP phải có loading/error/empty state.

### 3.1. Quy trình phiếu đã chốt

1. Điều độ hoặc Admin tạo phiếu.
2. Điều độ rà soát OCR, chọn Trạm/Ngăn lộ/Rơ-le, xác nhận toàn bộ candidate; có thể sửa từng dòng.
3. Điều độ xác nhận phiếu.
4. Trưởng trạm tiếp nhận và phân công KTV, Giám sát.
5. KTV xử lý thông số được giao, ký ảo.
6. Giám sát kiểm tra và ký ảo.
7. Admin duyệt cuối. Chỉ khi đó phiếu thành `COMPLETED` và baseline rơ-le thay đổi.

Phiếu bị từ chối bắt buộc có lý do, quay về đúng vai trò cần sửa, giữ lịch sử chữ ký cũ, và sau khi sửa phải ký lại từ đầu. `COMPLETED` bất biến; thay đổi sau đó tạo phiếu mới.

### 3.2. OCR và phiếu tạm đã chốt

- OCR failure không auto retry. Điều độ/Admin upload lại PDF để có attempt mới.
- RMS phải lưu PDF gốc và OCR result vô hạn; OCR service chỉ giữ mặc định 7 ngày. Browser không gọi OCR trực tiếp và không biết `OCR_API_TOKEN`.
- Ký MVP là `VIRTUAL`, phải hiển thị rõ đây không phải chữ ký SmartCA đã xác minh.
- Phiếu tạm thuộc MVP. Mỗi rơ-le có tối đa một phiếu tạm đang hiệu lực. Khi Admin duyệt, lưu snapshot baseline; hết hạn tự hoàn tác và audit. Admin có thể hoàn tác sớm, bắt buộc nêu lý do. Không xóa phiếu/lịch sử.
- Auto-check thiết bị và đồng bộ PMIS không thuộc MVP.

### 3.3. Quyền asset đã chốt

- `RoleGrant` hỗ trợ `GLOBAL`, `ORGANIZATION`, `STATION`; grant cộng gộp. `is_superuser` bypass quản trị; `is_staff` không tự cấp quyền nghiệp vụ.
- Organization scope chỉ áp dụng đúng đơn vị, không tự kế thừa xuống đơn vị con. Station scope áp dụng đúng trạm và Bay/Relay bên dưới.
- `UserProfile.organization` chỉ là đơn vị mặc định, không tự cấp quyền.
- Lát cắt asset import hiện yêu cầu superuser hoặc `GLOBAL` grant có role trong `ASSET_IMPORT_ROLE_CODES` (mặc định `ADMIN`).

## 4. Trạng thái thực tế hiện tại

### 4.1. Nền tảng — `DONE`

Đã có cấu hình Django, Docker Compose cho `db`, `redis`, `web` (Daphne), `worker`, `beat`; migrations PostgreSQL; health/readiness; session auth; request ID/common error envelope; audit/outbox/idempotency; Channels notification socket.

Bằng chứng đã được chủ sản phẩm chạy thành công trong phiên trước:

- migration, `python manage.py check`, `makemigrations --check --dry-run`;
- Celery `inspect ping`;
- `/health/` trả `ok`, `/ready/` trả database/Redis/Celery `ok`;
- `/admin/` đăng nhập, `/api/v2/identity/me/` trả user;
- WebSocket `/ws/notifications/` nhận `connection.ready`.

### 4.2. Asset: mô hình, quyền và tra cứu — `DONE`

Đã có `Organization`, `UserProfile`, `RoleGrant`, `CatalogType`, `CatalogItem`, `ExternalReference`, `Station`, `Bay`, `Relay`, với FK/unique constraint ngăn Bay/Relay mồ côi. Đã có API danh sách/cây Trạm có phân trang, lọc và scope server-side, cùng trang tra cứu `/assets/`.

Các migration asset hiện có là `0001` đến `0006`; identity `0001` đến `0004`; audit `0001` đến `0003`. Không tự sửa migration đã áp dụng; mọi thay đổi schema mới tạo migration tiếp theo.

### 4.3. Asset Import: Catalog Item preview — `IN PROGRESS`

Đây là lát cắt đang dở. Mã đã triển khai nhưng cần người dùng xác minh bằng phiên đăng nhập thật.

**Phạm vi đã có**

- `POST /api/v2/assets/imports/`: chỉ nhận `multipart/form-data`, `entity_type=catalog_item`, `mode=preview`, CSV và `source_system` tùy chọn.
- `GET /api/v2/assets/imports/{run_id}/`: trả trạng thái/báo cáo cho người tạo job hoặc superuser có quyền import.
- `AssetImportRun` lưu metadata job/report; Celery validate CSV; `AuditEvent` được tạo khi preview hoàn tất; file upload tạm được xóa sau xử lý.
- Validate CSV UTF-8/BOM, header, required field, số cột, row limit, boolean/integer, duplicate natural key, `CatalogType`, conflict với `CatalogItem` và `ExternalReference`.
- Preview **không tạo/sửa** `CatalogItem` hoặc `ExternalReference`. Nó chỉ báo `would_create`, `would_link_reference`, `unchanged`, `error`, `conflict`.
- UI tại `/assets/imports/` có tải CSV, drag/drop, polling report, loading/error/empty state và link CSV mẫu. API route không phải trang web: mở trực tiếp `/api/v2/assets/imports/` bằng browser gửi `GET` và đúng thiết kế sẽ trả `405 Allow: POST, OPTIONS`.

**Tệp/mô-đun quan trọng**

| Mục | Vị trí |
|---|---|
| Model và run status | `rms/apps/assets/models.py` (`AssetImportRun`) |
| Nghiệp vụ validate preview | `rms/apps/assets/application/import_preview.py` |
| API create/detail | `rms/apps/assets/api/imports.py`, `rms/apps/assets/api/urls.py` |
| Celery entry | `rms/apps/assets/tasks.py` |
| UI nhập CSV | `rms/apps/assets/ui/views.py`, `rms/templates/assets/catalog_import.html` |
| Static thuộc app | `rms/apps/assets/static/assets/catalog-import.css`, `catalog-import.js`, `catalog-item-preview.csv` |
| Contract | `ASSET_IMPORT_CONTRACT.md` |

**Kiểm tra đã chạy sau thay đổi UI**

- `docker compose up --build -d web` thành công.
- `docker compose exec web python manage.py check` thành công.
- Resolve route thành công: `/assets/imports/` và `/api/v2/assets/imports/`.
- `findstatic` tìm thấy đủ CSS, JavaScript và CSV mẫu bên trong `rms/apps/assets/static/assets/`.

**Việc còn lại để đóng lát cắt**

Chủ sản phẩm cần thực hiện do đây cần browser session đã đăng nhập:

1. Đăng nhập `/admin/` bằng superuser hoặc user có active `GLOBAL` `RoleGrant` phù hợp.
2. Mở `http://localhost:8000/assets/imports/`.
3. Tải CSV mẫu, không điền `Source System (Hệ thống nguồn)`, chọn `Preview Import (Xem trước nhập liệu)`.
4. Kỳ vọng: job thành `PREVIEWED`; một dòng `would_create`; `would_create_count=1`; `error_count=0`; không có `CatalogItem` mới trong Django admin.

Nếu UI không tải CSS/JS sau rebuild, hard-refresh trình duyệt. Nếu job ở `QUEUED` lâu, kiểm tra `worker` đang chạy: `docker compose ps` và `docker compose logs worker`.

### 4.4. Worktree hiện tại

Worktree có các thay đổi chưa commit từ quá trình xây dựng trước đó, trong đó có UI Asset Import mới. Không dùng `git reset --hard`, `git checkout --` hoặc xóa thay đổi chưa kiểm tra. Trước khi Agent sau chỉnh sửa, chạy `git status --short` và chỉ chạm vào tệp thuộc lát cắt được giao.

## 5. Lát cắt dài hạn bắt buộc

Các lát cắt này theo thứ tự phụ thuộc. Chi tiết tiêu chí đầy đủ nằm tại phần 7 và 8 của `BACKEND_NEW_ARCHITECTURE.md`.

| Thứ tự | Lát cắt | Trạng thái | Kết quả bắt buộc |
|---:|---|---|---|
| 0 | Nền tảng | `DONE` | Runtime, auth tối thiểu, audit/outbox/idempotency, health, worker/beat/WebSocket. |
| 1 | Asset và quyền scope | `IN PROGRESS` | Cây asset/scope đã có; cần đóng Catalog Item preview, sau đó xây theo contract nhập asset. |
| 2 | Upload phiếu và OCR local | `PLANNED` | PDF → attempt → OCR submit/poll/result snapshot lâu dài, notification, không auto retry. |
| 3 | Review OCR và version phiếu | `PLANNED` | Candidate chuẩn hóa, bulk confirm/sửa từng dòng, provenance và diff revision. |
| 4 | Phân công và workflow phiếu | `PLANNED` | State machine, scope role, ký ảo, từ chối/quay lại/ký lại, `COMPLETED` bất biến. |
| 5 | Publish baseline và phiếu tạm | `PLANNED` | Admin duyệt mới publish; snapshot và expiry/early rollback an toàn, audit. |
| 6 | Auto-check và correction case | `PLANNED — sau MVP` | Device adapter, policy/run/difference/case có audit. |
| 7 | PMIS/catalog integration | `PLANNED — sau MVP` | Sync run/checkpoint/mapping/resume, secret an toàn. |
| 8 | Chuyển đổi và hardening | `PLANNED` | Migrate frontend, backup/retention/observability, API contract/OpenAPI, retire mock. |

Không bắt đầu lát cắt 2 trước khi Asset 1 được đóng, trừ khi chủ sản phẩm chủ động thay đổi ưu tiên.

## 6. Kế hoạch ngắn hạn được phép lập lúc này

Kế hoạch này cố ý dừng sau công việc cần một quyết định nghiệp vụ quan trọng. Không tự mở rộng sang `apply` hoặc import Station/Bay/Relay.

### Kế hoạch A: đóng Catalog Item preview

1. **Xác minh màn hình upload** — Chủ sản phẩm chạy checklist ở mục 4.3. Tiêu chí xong: report hiển thị đúng và database không có Catalog Item mới.
2. **Sửa lỗi phát hiện nếu có** — Chỉ sửa lỗi từ kết quả xác minh; rebuild `web`, và `worker` nếu sửa task; chạy Django check. Tiêu chí xong: checklist bước 1 thành công.
3. **Chốt lát cắt** — Cập nhật status của mục 4.3 thành `DONE`, ghi ngày và output xác minh thực tế. Tiêu chí xong: Agent sau biết preview được xác nhận, không phải chạy lại từ đầu.

### Điểm dừng cần quyết định: Asset Import apply

Trước khi làm `mode=apply`, cần chủ sản phẩm chốt ít nhất:

- Ai được phép **áp dụng** dữ liệu (chưa thể suy ra chỉ từ quyền preview `ADMIN`).
- `source_system` code nào hợp lệ và ai sở hữu chúng.
- Có cần update mode hay chỉ cho phép create/link/unchanged; hiện contract đề xuất conflict thì không overwrite.
- Retention của run/report và chính sách lưu file import gốc.
- Idempotency key retention cho apply.

Đây là điểm dừng có chủ ý. `ASSET_IMPORT_CONTRACT.md` chứa default đề xuất, nhưng không được coi là quyết định đã duyệt.

## 7. Các quyết định mở ảnh hưởng tới lát cắt sau

Không để các câu hỏi này làm chậm Asset preview. Chỉ hỏi lại khi chuẩn bị triển khai lát cắt có liên quan trực tiếp.

| Quyết định | Ảnh hưởng | Trạng thái |
|---|---|---|
| Có được hoàn tất review khi candidate OCR rỗng? | Validation review OCR và workflow | `DECISION NEEDED` |
| Ma trận capability cuối theo action/scope | Workflow, assignment, UI/API authorization | `DECISION NEEDED` |
| Backup/mã hóa/quy trình khôi phục cho PDF/OCR retention vô hạn | OCR storage và vận hành production | `DECISION NEEDED` |
| Mapping JSON OCR đến parameter chuẩn | OCR normalizer/review UI | `DECISION NEEDED`; chỉ `API_CONTRACT.md` mô tả schema tổng quát |
| Format/layout chính xác của phiếu PDF đầu vào | OCR review và sheet model | `DECISION NEEDED` |
| Chính sách apply/update/import retention | Asset import apply | `DECISION NEEDED`; xem mục 6 |

## 8. Handoff checklist cho Agent tiếp theo

1. Đọc mục 1 của tài liệu này và kiểm tra `git status --short`.
2. Xác nhận lát cắt hiện tại từ mục 4.3. Không coi `PLANNED` là mã đã có.
3. Nếu chủ sản phẩm báo kết quả upload, xử lý Kế hoạch A trước. Nếu báo lỗi, yêu cầu output/report cụ thể hoặc đọc `docker compose logs worker` theo lỗi.
4. Nếu Kế hoạch A đã `DONE`, **dừng và hỏi quyết định apply** ở mục 6 trước khi mở rộng import.
5. Khi làm lát cắt mới, cập nhật `PROJECT_CONTINUITY.md` trong cùng thay đổi để tài liệu luôn phản ánh trạng thái thật.
