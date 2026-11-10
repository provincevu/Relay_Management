# Rà soát frontend cũ — EVN RMS

> **Nguồn:** chỉ `repomix-frontend.md` và tài liệu đối chiếu `BACKEND_AUDIT.md` theo yêu cầu. Repomix frontend gồm template HTML và tài liệu thiết kế, không gồm mã views/JS đầy đủ hoặc `urls.py`. Tên route `{% url %}` được trích nguyên văn; đường dẫn URL thật chỉ ghi khi template hardcode. Một số mô tả trong `docs/` là thiết kế dự kiến, không mặc định là hành vi đã chạy.

## 1. Màn hình/route và luồng người dùng

| Màn hình / tên route frontend | Vai trò / mục đích | Luồng chính |
|---|---|---|
| `login` | Người dùng đăng nhập | Gửi form đăng nhập → vào `dashboard`; trạng thái xác thực dùng chung trong sidebar/base. |
| `dashboard` cùng `dashboard_admin`, `dashboard_dispatcher`, `dashboard_station_leader`, `dashboard_supervisor`, `dashboard_technician`, `dashboard_a0` | Trang tổng quan theo vai trò | Lọc khoảng thời gian/KPI → mở danh sách phiếu, trạm, danh mục hoặc chi tiết phiếu. Các template vai trò có phần trình bày/metric khác nhau. |
| `station_list` | Điều độ/trạm tra cứu cây tài sản | Tìm kiếm → tải danh sách trạm → mở rộng trạm lấy Bay → mở rộng Bay lấy Relay → mở modal thông tin/đối chiếu. Có bulk create/import-related controls trong template. |
| `relay_status_dashboard` | Xem trạng thái thiết bị và tình trạng có/không có phiếu | Chọn tab/nhóm → xem danh sách rơ-le. |
| `autocheck_dashboard` | Theo dõi kiểm tra tự động | Lọc/tải bảng → chạy kiểm tra ngay, sửa lịch → xem kết quả và sai lệch → tạo/tiến hành correction ticket. |
| `check_list`, `check_create`, `check_detail` | Lập và cập nhật kiểm tra định kỳ thủ công | Chọn rơ-le/ngày → tạo phiếu và các item → nhập trị số đo, cập nhật từng dòng → hoàn tất kiểm tra. |
| `sheet_list`, `my_sheets`, `updated_sheets`, `dispatcher_routed_relays` | Điều độ/KTV/giám sát lọc và theo dõi phiếu | Lọc theo trạng thái/từ khóa/điện áp → mở chi tiết → nhận/giao/phân tuyến hoặc xem phiếu cập nhật. |
| `sheet_create` (`sheet_form`) | Tạo phiếu từ PDF scan | Chọn/tải một hoặc nhiều file và metadata → tạo phiếu → OCR nền → tới chi tiết hoặc màn hình job. |
| `sheet_detail` | Rà soát phiếu split-view | Xem PDF và dữ liệu OCR → sửa thông tin trạm/rơ-le/thông số → phân tuyến/giao việc → ký theo bước; có thể xem modal Relay và rerun OCR. |
| `ocr_job_list` | Theo dõi OCR | Lọc job theo trạng thái/chế độ thiết bị/tìm kiếm → xem tiến độ/lỗi → retry theo job hoặc retry all → xem JSON. |
| `bulk_create_ui`, `bulk_create_execute` | Công cụ tạo phiếu hàng loạt | Chọn file → gửi job bulk → hiển thị đang tải/đang xử lý → refresh danh sách và báo lỗi/thành công. Template ghi rõ là tiện ích/test. |
| `api_extract_test_ui`, `api_extract_test_execute` | Công cụ thử API trích xuất | Nhập URL/chọn file → gửi request → hiển thị JSON hoặc lỗi mạng/API. Template ghi đây là test utility. |
| `category_dashboard`, `category_list`, `category_create`, `category_edit`, `category_delete` | Quản trị danh mục | Chọn loại danh mục → tìm kiếm/phân trang → mở modal tạo/sửa → lưu hoặc xác nhận xóa → refresh partial. |
| `asset_line_list`, `asset_location_list`, `asset_project_list` | Tra cứu đường dây/vị trí/công trình | Tìm/lọc → tải bảng → mở slide-over chi tiết theo `detail` query parameter. |
| `user_list`, `user_create`, `user_toggle_status` | Quản trị người dùng | Tìm kiếm/phân trang → tạo user hoặc bật/tắt trạng thái tài khoản. |
| `role_matrix`, `role_matrix_update` | Quản trị quyền | Xem permission theo group → bật/tắt permission qua HTMX. |
| `manage_team` | Trưởng trạm phân công | Chọn KTV/giám sát và nhiều phiếu → gửi phân công. |
| `profile` | Xem hồ sơ người dùng | Hiển thị thông tin tài khoản. |
| `system_config`, `system_config_create`, `system_config_update`, `system_config_bulk_create` | Cấu hình API đồng bộ | Tìm cấu hình → thêm/sửa/xóa/bulk add → đồng bộ từng dòng hoặc “đồng bộ tất cả” theo thứ tự hiển thị. |
| `ticket_sign` trong partial `_ticket_workflow.html` | Xử lý ticket sai lệch | Xem thông số lệch/stepper → nhập ghi chú → ký/chuyển bước → xem lịch sử ký. Partial ghi rõ “Bản Demo”. |

**Điều hướng dùng chung:** `base.html` chứa sidebar, toast, WebSocket notification, progress bar toàn trang, modal category và các hàm OCR job; `partials/pagination.html` tái sử dụng phân trang; badge gọi `/system/api/badges/`. Có light/dark mode và menu theo quyền/nhóm trong sidebar. Tên menu và quyền chính xác theo runtime: Không xác định nếu chỉ dựa trên template.

## 2. Màn hình gọi dữ liệu/API và trạng thái UI

Trong template Django, “API” thường là view trả HTML/partial qua HTMX. Tên route không cho biết URL HTTP thật; xem mục 3 để biết các route không khớp hoặc không xác minh được.

| Màn hình | Request frontend và dữ liệu gửi | Dữ liệu/response mong đợi | Trạng thái loading/lỗi/rỗng thể hiện |
|---|---|---|---|
| Base/toast | WebSocket `ws(s)://<host>/ws/notifications/`; GET `/system/api/badges/` | Notification, badge theo user | WebSocket lỗi/đóng không có UI lỗi rõ trong template; global progress bar và toast. |
| Category list/modal | GET route `category_list(category_id)` với query tìm kiếm/page; GET `category_edit(category_id,id)`; POST `category_create` hoặc `category_edit`; POST `category_delete` | HTML partial/form; JS đọc JSON hoặc status, đóng modal/refresh danh sách | Loading indicator; field/non-field errors; confirm xóa; empty row theo `{% empty %}`. Fetch lỗi được log, thông báo/modal fallback. |
| Line/Location/Project asset list | GET route tương ứng với q/filter/page; JS GET cùng trang `?detail=<id>&_panel=1&_=<timestamp>` | Bảng partial hoặc HTML detail panel | HTMX loading indicator; `{% empty %}` cho bảng; fetch detail lỗi: không thấy thông báo lỗi nhất quán. |
| Dashboard các vai trò | Chủ yếu render server-side; query `period`, `start_date`, `end_date`; link tới sheet/station/category | KPI, chart, phiếu gần đây/chờ xử lý/hoạt động | Các danh sách có `{% empty %}`; chart có nhãn “Không có dữ liệu”; loading/error request riêng không thể hiện vì phần lớn không phải fetch. |
| Station tree | GET route `station_list` với `q/page`; GET partial `htmx_bays(station.id)` và `htmx_relays(bay.id)` khi expand; có auto-load nếu `auto_expand` | HTML danh sách Bays/Relays | Spinner khi expand; thông báo không có dữ liệu/trạm phù hợp; một số fetch JS không có `.catch()` nên lỗi mạng có thể để vùng trống. |
| Relay detail modal từ sheet | GET hardcode `/stations/htmx/relay/<relayId>/detail/?sheet_id=<id>` (có thể ID hoặc text); dữ liệu từ `STATIONS_DATA`, `BAYS_DATA`, `RELAYS_DATA`, `PAGE1_FIELDS` được nhúng vào trang | HTML modal: relay, metadata, đối chiếu OCR | Có spinner; fetch non-2xx/network thay bằng khung lỗi và nút đóng; thiếu relay thì alert. |
| Sheet detail gợi ý relay | GET hardcode `/stations/api/station/<stationId>/relays/` | JSON list relay theo station, cho bộ chọn relay | Loading/auto-suggest message; code bắt network ở một số nhánh, chi tiết empty/error không nhất quán. |
| Sheet list/my/updated/routed | Trang được server render với filters; các links mở `sheet_detail(id)` | Rows, KPI và pagination | `{% empty %}` cho danh sách; trạng thái/empty message khác nhau theo template. |
| Sheet create | Form upload `scan_file`/file list, title, relative path/relay metadata tùy chế độ; submit route `sheet_create` | HTML/redirect hoặc response tạo job; cụ thể Không xác định từ frontend | Disable nút khi `loading`/không có file; spinner. Error response chi tiết phụ thuộc view; không thấy empty state cần thiết. |
| Sheet detail OCR/retry | POST route `run_mock_ocr` hoặc `sheet_rerun_ocr`; OCR job global JS POST hardcode `/sheets/ocr-job/<id>/retry/`, `/sheets/ocr-job/retry-all/`, DELETE `/sheets/ocr-job/<id>/delete/`, GET `/sheets/ocr-job/<id>/data/` | JSON cho retry/job data; HTML cho modal/partial | Job list có trạng thái pending/processing/success/failed, spinner, lỗi modal có code/stage/detail; retry có toast lỗi; JSON load lỗi hiển thị text. |
| Sheet detail assignments/status | POST HTMX route `sheet_route_to_station`, `sheet_assign`, `sheet_update_status`; form gửi station/relay/execution station, assignee/supervisor/status, đôi khi OCC timestamp | Partial `#assignment-card` cùng OOB cập nhật signature panel, stepper, badge | Nút/HTMX loading; server partial thay vùng; error state riêng không thể xác định từ template. |
| Ký phiếu | POST fetch `initiate_signature(sheet.pk)` với role; POST HTMX `confirm_signature(sheet.pk)` | Initiate JSON/session; confirm HTML partial | Alpine states `input/loading/success`; spinner; trong JS có delay giả 2 giây; lỗi initiation/confirm UI cụ thể không đồng nhất. |
| OCR jobs | Lấy danh sách HTML/JSON qua route `ocr_job_list`; global JS lắng nghe WebSocket; retry POST; get JSON; retry-all POST; delete dùng DELETE | Job records, stage, error fields, JSON data | “Đang tải dữ liệu”, progress, status chips; error modal (code/stage/detail), GPU/CPU branch, toast khi request lỗi. Empty state không thấy rõ ở tất cả nhánh. |
| Periodic checks | POST `check_create` với relay/ngày; POST HTMX `check_update_item` với item/value; POST `check_complete` | HTML redirect/detail hoặc item row cập nhật deviation | Item rows; empty state trong detail/list; validation errors hiển thị qua form nếu server trả context. Loading per-row chưa thấy rõ. |
| Auto-check dashboard | GET `autocheck_dashboard` với filters; GET `autocheck_row(relay.id)`; POST `run_autocheck_now(relay.id)`; POST `update_relay_schedule(relay.id)` | HTML dashboard/table/row/results | Loading row/table; empty table; submit schedule spinner và đóng modal khi success; lỗi giữ modal và reset submitting. |
| Ticket workflow | POST `ticket_sign(ticket.id)` với `notes` | HTML fragment/modal result | Stepper trạng thái, signature history, demo notice; trạng thái lỗi submit Không xác định. |
| User/role/team | GET/HTMX `user_list`; POST `user_toggle_status`; POST `role_matrix_update`; POST `manage_team` | Table/form partial hoặc refresh | Loading indicator user list; `{% empty %}`; permission toggle state; error handling chủ yếu do server messages/partial. |
| System config | GET `system_config` với q; POST create/update/bulk create; HTMX POST sync endpoint động trên từng row; JS tuần tự trigger từng nút cách nhau 3 giây | Config row HTML, trạng thái tiến độ/sync result | Loading text, status/progress poll 2s, per-row result/error; sync-all state và alert; lỗi JS trong vòng lặp bị nuốt (`catch(e) {}`). |
| Bulk create / API extract test | POST multipart qua fetch tới `bulk_create_execute` (idempotency key, files); API test gửi `api_url`, files tới `api_extract_test_execute` | JSON result/progress hoặc mock | Disable/loading; polling/refresh; toast cho lỗi HTTP/mạng; API test JSON error panel. |

## 3. Frontend gọi API nào không khớp backend audit?

`BACKEND_AUDIT.md` ghi tên view/handler nhưng nhiều URL bị đánh dấu “Không xác định” vì `urlpatterns` trong repomix backend bị lược bỏ. Vì vậy “không khớp” dưới đây phân loại theo khả năng đối chiếu; không khẳng định endpoint chắc chắn hỏng nếu chỉ thiếu route map.

| Frontend gọi | Đối chiếu backend audit | Kết quả |
|---|---|---|
| Route `sheet_sign` (POST) trong partial | Backend audit có `initiate_signature` và `confirm_signature`, nhưng không có handler `sheet_sign`; hai handler có vai trò tương tự nhưng khác tên và giao thức (khởi tạo + confirm). | **Không khớp tên handler; URL thực tế Không xác định.** Có thể là alias/route cũ, hoặc template/backend lệch. |
| Route `category_edit` và `category_create` | Backend audit ghi một handler `category_form(category_id, pk=None)`; names khác. | **Tên route không khớp trực tiếp**; có thể map hai URL tới cùng view, cần urls.py để xác nhận. |
| Route `htmx_relay_detail` | Backend audit có `get_relay_detail_modal(relay_id)` và `relay_parameters_modal`, không thấy tên `htmx_relay_detail`. | **Tên route không khớp trực tiếp;** cần xác nhận view/URL alias và response partial. |
| Hardcode `/stations/htmx/relay/<id>/detail/?sheet_id=...` | Backend audit nêu handler `get_relay_detail_modal`, nhưng đường dẫn URL **Không xác định**. | **Chưa xác minh khớp đường dẫn.** Handler tương tự tồn tại. |
| Hardcode `/stations/api/station/<id>/relays/` | Backend audit có `get_station_relays_json(station_id)` với JSON relay list, URL không xác định. | **Chưa xác minh khớp đường dẫn**, nội dung/shape có vẻ tương ứng nhưng contract JSON chưa đối chiếu được. |
| Hardcode `/system/api/badges/` | Backend audit có `get_badges_api`; route không xác định. | **Chưa xác minh khớp đường dẫn.** |
| Hardcode `/sheets/ocr-job/<id>/delete/` dùng HTTP DELETE | Backend audit liệt kê `ocr_job_json`, retry, retry-all, rerun; không có handler xóa OcrJob. | **Không thấy API backend tương ứng trong audit.** Đây là thiếu đối ứng rõ nhất; có thể delete view bị bỏ khỏi repomix backend, cần xác nhận. |
| `/sheets/ocr-job/<id>/data/` | Backend audit có handler `ocr_job_json(pk)` nhưng URL không xác định. | **Có thể tương ứng**, path chưa xác minh. |
| `/sheets/ocr-job/<id>/retry/`, `/sheets/ocr-job/retry-all/` | Backend audit có `ocr_job_retry(pk)` và `ocr_job_retry_all`; tên/path không được khẳng định. | Handler tương ứng có; **path/method chưa xác minh**. |
| `sheet_route_to_station`, `sheet_assign`, `sheet_update_status`, `initiate_signature`, `confirm_signature`, `run_mock_ocr`, `sheet_rerun_ocr` | Các handler tương ứng được liệt kê trong backend audit. | Khớp theo handler/ý nghĩa; URLs và method thực tế vẫn cần route map. `sheet_update_status` và `run_mock_ocr` phía backend được đánh dấu mock. |
| Station/check/category/config/user/team/autocheck/ticket named routes | Backend audit nêu các view tương tự (vd. `station_list`, `check_update_item`, `system_config_update`), nhưng có alias khác ở một số route. | Phần lớn **khớp theo ý nghĩa**, không đủ bằng chứng đối chiếu path chính xác. |
| `global_bulk_create` trong sidebar/tool | Backend audit chỉ nêu `relay_bulk_create`/`global_bulk_create` là handler; không có route chi tiết. | **Không xác định path/method và việc handler có được route hay không.** |

**Kết luận đối chiếu:** không thể tạo danh sách URL hỏng chắc chắn chỉ từ hai bản đóng gói. Có dấu hiệu lệch tên giữa template và tên view backend (ký phiếu, sửa/tạo category, relay detail), cùng request DELETE OCR job không có handler tương ứng trong backend audit. Cần so `urls.py` thật trước khi kết luận lỗi tích hợp.

## 4. State dùng chung và logic nghiệp vụ trong UI

### State dùng chung

- `base.html`: toast/message queue, WebSocket notification, badge count, progress bar request, hàm show toast; nhiều template phụ thuộc các global này.
- `sheet_detail.html`: globals trên `window`: `STATIONS_DATA`, `BAYS_DATA`, `RELAYS_DATA`, `PAGE1_FIELDS`, `currentStationId`, `currentRelayId`, `currentRelayBayId`, `currentRelayText`; modal và Alpine metadata form cùng truy cập chúng.
- `ocr_job_list.html` + scripts trong `base.html`: dữ liệu job, pagination/filter, error modal, device mode, WebSocket event; retry/retry-all/delete/get JSON được triển khai bằng JS global logic.
- Các trang dùng Alpine local state: `loading`, `isProcessing`, `syncing`, `expanded/loaded`, modal open, form submission, signature state. State này thường theo từng component, không phải server state bền vững.
- HTMX partials tự phát/nhận event để cập nhật table/row/assignment; trạng thái hiển thị bị chia giữa Alpine, HTMX và Django context.

### Logic nghiệp vụ đang nằm trong UI, nên cân nhắc chuyển hoặc gom về backend

| Logic trong template/JS | Vì sao nên chuyển/chuẩn hóa phía server |
|---|---|
| `getEffectiveRelayId()` có nhiều fallback từ TomSelect, DOM item, OCR text và server ID. | Đây là quyết định định danh nghiệp vụ; backend cần nhận một định danh rõ, validate và trả kết quả ghép thay vì UI tự đoán ID/text. |
| Tạo `autoSuggestMessage`/quyết định ứng viên theo OCR station/bay/relay (kèm request danh sách relay). | Ghép tài sản ảnh hưởng dữ liệu phiếu; quyết định cuối, ngưỡng match và cảnh báo phải là logic backend. |
| Sync-all tìm nút theo `title`, sắp theo thứ tự DOM, trigger lần lượt và delay 3s. | Thứ tự ưu tiên, concurrency, retry và trạng thái tổng hợp thuộc service/task backend; thao tác DOM không đáng tin cậy. |
| UI đổi sync interval phút thành năm/tháng/ngày/giờ và ngược lại. | Định dạng hiển thị có thể ở UI, nhưng chuẩn hóa/validate chu kỳ cần backend làm nguồn chuẩn. |
| OCR retry chọn CPU khi error có GPU/CUDA; parsing status/error text để đổi hành vi. | Chính sách retry/device và phân loại lỗi phải dùng cấu trúc error code server-side, không dựa chuỗi hiển thị. |
| Signature state, delay giả 2s và stepper/status hiển thị theo logic template. | Trạng thái ký và thứ tự phê duyệt cần server authoritative; animation/loading chỉ nên là UI. |
| Phần trăm/nhóm trạng thái/charts/KPI render điều kiện theo status ở template. | Nếu ảnh hưởng quyết định vận hành, backend phải trả KPI/status aggregate có định nghĩa nhất quán. |
| Route phân công form hiển thị candidate theo station/role và status. | Quyền, phạm vi Station và transition phải validate server-side; UI chỉ nên phản ánh quyền. |
| Schedule UI đổi đơn vị và tự đóng modal theo success event. | Chu kỳ thật và tính hợp lệ phải kiểm tra backend; close modal là UI-only. |

## 5. Thành phần UI lặp lại, có thể dùng chung

| Thành phần lặp | Bằng chứng trong template | Đề xuất component dùng chung |
|---|---|---|
| Status badge và status stepper | `sheets/partials/_status_badge.html`, `_status_stepper.html`; hiển thị ở header/detail/assignment | `SheetStatusBadge`, `WorkflowStepper` nhận status map từ backend. |
| Pagination | `partials/pagination.html` được include ở category, asset, station và user pages | `Pagination` có mode link thường/HTMX, giữ query/filter. |
| Search/filter toolbar + loading indicator | Category/asset/station/user/OCR/autocheck lists | `ListToolbar` + `LoadingIndicator`, cùng debounce, clear filter, accessibility. |
| Data table row/empty state | Category row, line/location/project tables, relay rows, OCR rows | `DataTable`, `EmptyState`, `TableSkeleton`; chỉ chuẩn hóa hành vi chung, giữ cell nghiệp vụ riêng. |
| Modal/dialog | Category form, relay detail, schedule config, ticket workflow, signature/error modal | `ModalShell` có close, Escape, backdrop, focus trap, loading/error body. |
| Form field/error rendering | Category dynamic form, login/user, config, sheet metadata | `FormField`, `FormErrors`, `FormActions`, CSRF/OCC field helper. |
| Toast/notification | Global `base.html` + request handlers gọi `showToast` | Một notification store/API thống nhất; phân biệt server message, websocket event, network error. |
| Loading/error panel | Relay modal, OCR errors, upload, table refresh | `RequestState` với loading/success/empty/error; hiện trạng thái lỗi chưa nhất quán giữa fetch và HTMX. |
| Assignment panel | Station route, technician/supervisor assignment, status actions | `SheetAssignmentPanel` render theo capability và state transition từ backend. |
| Signature history/item | Sheet signature panel và ticket signature history | `SignatureHistory` dùng schema chung nếu business xác nhận cùng contract; chữ ký ticket và sheet hiện là hai entity khác nhau. |
| Expandable station/bay tree | `_station_tree_page`, `bay_list`, `relay_list` | `LazyTreeNode` với cache loaded/error/retry, tránh mỗi template tự viết fetch-expand. |
| Chart cards/KPI cards | Nhiều role dashboard lặp pattern card/chart/date filter | `KpiCard`, `DateRangeFilter`, `ChartPanel` nhận dữ liệu đã tổng hợp. |

## Giới hạn và việc cần xác minh

- `repomix-frontend.md` gồm templates và tài liệu thiết kế, không có đầy đủ JavaScript/runtime view context; do đó payload chính xác của một số request, error code và response contract là **Không xác định**.
- Đường dẫn route/backend map thực tế cần đối chiếu `urls.py`; backend audit cũng ghi chúng là **Không xác định** do Repomix đã lược bỏ.
- Tài liệu thiết kế MVT có route ví dụ cũ (ví dụ `sheet_sign`, `station_detail`, `station_import`) không thấy tương ứng trong tập handler backend được kiểm kê. Không dùng tài liệu thiết kế đó để khẳng định route runtime.
