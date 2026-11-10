This file is a merged representation of a subset of the codebase, containing specifically included files, combined into a single document by Repomix.

# File Summary

## Purpose
This file contains a packed representation of a subset of the repository's contents that is considered the most important context.
It is designed to be easily consumable by AI systems for analysis, code review,
or other automated processes.

## File Format
The content is organized as follows:
1. This summary section
2. Repository information
3. Directory structure
4. Repository files (if enabled)
5. Multiple file entries, each consisting of:
  a. A header with the file path (## File: path/to/file)
  b. The full contents of the file in a code block

## Usage Guidelines
- This file should be treated as read-only. Any changes should be made to the
  original repository files, not this packed version.
- When processing this file, use the file path to distinguish
  between different files in the repository.
- Be aware that this file may contain sensitive information. Handle it with
  the same level of security as you would the original repository.

## Notes
- Some files may have been excluded based on .gitignore rules and Repomix's configuration
- Binary files are not included in this packed representation. Please refer to the Repository Structure section for a complete list of file paths, including binary files
- Only files matching these patterns are included: **/urls.py
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
```
categories/
  urls.py
checks/
  urls.py
core/
  urls.py
rms_project/
  urls.py
sheets/
  urls.py
stations/
  urls.py
```

# Files

## File: categories/urls.py
```python
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'management-units', views.ManagementUnitViewSet)
router.register(r'manufacturing-countries', views.ManufacturingCountryViewSet)
router.register(r'manufacturers', views.ManufacturerViewSet)
router.register(r'ownerships', views.OwnershipViewSet)
router.register(r'voltage-levels', views.VoltageLevelViewSet)
router.register(r'equipment-types', views.EquipmentTypeViewSet)
router.register(r'operational-statuses', views.OperationalStatusViewSet)
router.register(r'lines', views.LineViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'locations', views.LocationViewSet)

# Include existing stations app categories for consistency in the API namespace
router.register(r'stations', views.StationViewSet)
router.register(r'bays', views.BayViewSet)
router.register(r'equipments', views.RelayViewSet) # Exposing Relay as equipment

urlpatterns = [
    # UI endpoints
    path('dashboard/', views.category_dashboard, name='category_dashboard'),
    path('ui/<str:category_id>/', views.category_list, name='category_list'),
    path('ui/<str:category_id>/new/', views.category_form, name='category_create'),
    path('ui/<str:category_id>/<int:pk>/edit/', views.category_form, name='category_edit'),
    path('ui/<str:category_id>/<int:pk>/delete/', views.category_delete, name='category_delete'),
    
    # Asset Management UI
    path('assets/lines/', views.asset_line_list, name='asset_line_list'),
    path('assets/locations/', views.asset_location_list, name='asset_location_list'),
    path('assets/projects/', views.asset_project_list, name='asset_project_list'),
    
    # API endpoints
    path('', include(router.urls)),
]
```

## File: checks/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_list, name='check_list'),
    path('new/', views.check_create, name='check_create'),
    path('<int:pk>/', views.check_detail, name='check_detail'),
    path('<int:pk>/items/', views.check_update_item, name='check_update_item'),
    path('<int:pk>/complete/', views.check_complete, name='check_complete'),
]
```

## File: core/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:user_id>/update/', views.user_update, name='user_update'),
    path('users/<int:user_id>/toggle-status/', views.user_toggle_status, name='user_toggle_status'),
    path('roles/', views.role_matrix, name='role_matrix'),
    path('roles/update/', views.role_matrix_update, name='role_matrix_update'),
    path('dispatcher/routed-relays/', views.dispatcher_routed_relays, name='dispatcher_routed_relays'),
    path('profile/', views.profile, name='profile'),
    path('api-config/', views.system_config_view, name='system_config'),
    path('api-config/create/', views.system_config_create, name='system_config_create'),
    path('api-config/bulk-create/', views.system_config_bulk_create, name='system_config_bulk_create'),
    path('api-config/update/', views.system_config_update, name='system_config_update'),
    path('api-config/delete/<int:config_id>/', views.system_config_delete, name='system_config_delete'),
    path('api-config/row/<int:config_id>/', views.system_config_row, name='system_config_row'),
    path('api-config/sync/', views.api_sync_endpoint, name='api_sync_endpoint'),
    path('api/badges/', views.get_badges_api, name='get_badges_api'),
    path('manage-team/', views.manage_team, name='manage_team'),
]
```

## File: rms_project/urls.py
```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import dashboard, custom_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('sheets/', include('sheets.urls')),
    path('checks/', include('checks.urls')),
    path('stations/', include('stations.urls')),
    path('system/', include('core.urls')),
    path('accounts/logout/', custom_logout, name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/v1/categories/', include('categories.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## File: sheets/urls.py
```python
from django.urls import path
from . import views
from . import views_bulk

urlpatterns = [
    path('', views.sheet_list, name='sheet_list'),
    path('my-sheets/', views.my_sheets, name='my_sheets'),
    path('create/', views.sheet_create, name='sheet_create'),
    path('<int:pk>/', views.sheet_detail, name='sheet_detail'),
    path('<int:pk>/update-status/', views.sheet_update_status, name='sheet_update_status'),
    path('<int:pk>/assign/', views.sheet_assign, name='sheet_assign'),
    path('<int:pk>/sign/initiate/', views.initiate_signature, name='initiate_signature'),
    path('<int:pk>/sign/confirm/', views.confirm_signature, name='confirm_signature'),
    path('<int:pk>/run-mock-ocr/', views.run_mock_ocr, name='run_mock_ocr'),
    path('<int:pk>/save-actual-data/', views.sheet_save_actual_data, name='sheet_save_actual_data'),
    path('<int:pk>/update-metadata/', views.sheet_update_metadata, name='sheet_update_metadata'),
    path('<int:pk>/rerun-ocr/', views.sheet_rerun_ocr, name='sheet_rerun_ocr'),
    path('ocr-progress/', views.ocr_job_list, name='ocr_job_list'),
    path('ocr-job/<int:pk>/json/', views.ocr_job_json, name='ocr_job_json'),
    path('ocr-job/<int:pk>/retry/', views.ocr_job_retry, name='ocr_job_retry'),
    path('ocr-job/retry-all/', views.ocr_job_retry_all, name='ocr_job_retry_all'),
    path('<int:pk>/route-to-station/', views.sheet_route_to_station, name='sheet_route_to_station'),
    path('updated/', views.updated_sheets, name='updated_sheets'),
    
    # Bulk create (Test Utility)
    path('bulk-create/', views_bulk.bulk_create_ui, name='bulk_create_ui'),
    path('bulk-create/execute/', views_bulk.bulk_create_execute, name='bulk_create_execute'),
    
    # API Extract (Test Utility)
    path('api-extract-test/', views_bulk.api_extract_test_ui, name='api_extract_test_ui'),
    path('api-extract-test/execute/', views_bulk.api_extract_test_execute, name='api_extract_test_execute'),
]
```

## File: stations/urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.station_list, name='station_list'),
    path('create/', views.station_create, name='station_create'),
    path('<int:station_id>/bays/create/', views.bay_create, name='bay_create'),
    path('bays/<int:bay_id>/relays/create/', views.relay_create, name='relay_create'),
    path('bays/<int:bay_id>/relays/bulk_create/', views.relay_bulk_create, name='relay_bulk_create'),
    path('global_bulk_create/', views.global_bulk_create, name='global_bulk_create'),
    path('relay-status/', views.relay_status_dashboard, name='relay_status'),
    path('htmx/station/<int:station_id>/bays/', views.get_bays_htmx, name='htmx_bays'),
    path('htmx/bay/<int:bay_id>/relays/', views.get_relays_htmx, name='htmx_relays'),
    path('autochecks/now/<int:relay_id>/', views.run_autocheck_now, name='run_autocheck_now'),
    path('relay/<int:relay_id>/update_schedule/', views.update_relay_schedule, name='update_relay_schedule'),
    
    # Workflow URLs
    path('relay/<int:relay_id>/workflow/continue/', views.workflow_continue, name='workflow_continue'),
    path('relay/<int:relay_id>/workflow/create_ticket/', views.workflow_create_ticket, name='workflow_create_ticket'),
    path('ticket/<int:ticket_id>/sign/', views.ticket_sign, name='ticket_sign'),
    
    path('relay/<int:relay_id>/parameters/', views.relay_parameters_modal, name='relay_parameters_modal'),
    path('relay/<int:relay_id>/upload_pdf_compare/', views.upload_relay_pdf_compare, name='upload_relay_pdf_compare'),
    path('relay/<int:relay_id>/row/', views.autocheck_row, name='autocheck_row'),
    path('autochecks/', views.autocheck_dashboard, name='autocheck_dashboard'),
    path('htmx/search-suggestions/', views.search_suggestions, name='search_suggestions'),
    path('htmx/relay/<str:relay_id>/detail/', views.get_relay_detail_modal, name='htmx_relay_detail'),
    path('api/station/<int:station_id>/relays/', views.get_station_relays_json, name='api_station_relays'),
]
```
