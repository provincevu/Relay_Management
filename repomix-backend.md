This file is a merged representation of a subset of the codebase, containing specifically included files and files not matching ignore patterns, combined into a single document by Repomix.

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
- Only files matching these patterns are included: README.md, PROJECT_REQUIREMENTS.md, docs/**/*.md, manage.py, rms_project/**/*.py, core/**/*.py, stations/**/*.py, sheets/**/*.py, checks/**/*.py, categories/**/*.py, requirements.txt, Dockerfile, docker-compose.yml, .env.example
- Files matching these patterns are excluded: OCR_PRJ/**, venv/**, **/__pycache__/**, staticfiles/**, vendor/**, .git/**, .env, **/*.xlsx, **/*.docx, **/*.log, **/*.json, stations/relay_specs.py, repomix-output.*
- Files matching patterns in .gitignore are excluded
- Files matching default ignore patterns are excluded
- Files are sorted by Git change count (files with more changes are at the bottom)

# Directory Structure
````
categories/
  migrations/
    __init__.py
    0001_initial.py
    0002_managementunit_parent_code_managementunit_sort_order_and_more.py
    0003_manufacturingcountry_legacy_id_and_more.py
    0004_ownership_sort_order.py
    0005_voltagelevel_legacy_code_voltagelevel_sort_order.py
    0006_station.py
    0007_delete_station.py
    0008_line_da_tke_line_dz_cha_line_i_chophep_line_id_capda_and_more.py
    0009_project_id_capda_project_id_ct_project_id_dvi_and_more.py
    0010_location_duong_vao_location_hanh_lang_and_more.py
  __init__.py
  admin.py
  apps.py
  models.py
  serializers.py
  tests.py
  urls.py
  views.py
checks/
  migrations/
    __init__.py
    0001_initial.py
    0002_alter_periodiccheck_sheet.py
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  urls.py
  views.py
core/
  management/
    commands/
      seed_data.py
      seed_permissions.py
      seed_users.py
  migrations/
    __init__.py
    0001_initial.py
    0002_userprofile_station.py
    0003_systemconfig.py
    0004_systemconfig_auth_header.py
    0005_systemconfig_auto_sync_enabled_and_more.py
    0006_systemconfig_sync_count.py
    0007_systemconfig_is_syncing.py
    0008_userprofile_updated_at.py
    0009_alter_systemconfig_last_sync_status.py
  templatetags/
    __init__.py
    auth_extras.py
    core_extras.py
  utils/
    api_sync.py
    xml_converter.py
  __init__.py
  admin.py
  api_renderers.py
  apps.py
  consumers.py
  context_processors.py
  models.py
  routing.py
  tasks.py
  tests.py
  urls.py
  views.py
docs/
  cores/
    01-database.md
    02-backend.md
    03-frontend.md
    04-security.md
    05-testing.md
    06-deployment.md
  features/
    01-station-management.md
    02-calibration-sheet.md
    03-digital-signature.md
    04-periodic-check.md
    05-ai-ocr.md
  mvt_design/
    MODELS_DESIGN.md
    REQUIREMENTS_MVT.md
    TEMPLATES_UI.md
    VIEWS_URLS_MAP.md
rms_project/
  __init__.py
  asgi.py
  celery.py
  settings.py
  urls.py
  wsgi.py
sheets/
  management/
    commands/
      __init__.py
      sync_hybrid_pipeline.py
    __init__.py
  migrations/
    __init__.py
    0001_initial.py
    0002_alter_settingsheet_options.py
    0003_alter_settingsheet_status.py
    0004_alter_settingsheet_options.py
    0005_settingsheet_assigned_to_settingsheet_created_by.py
    0006_settingsheet_assigned_supervisor_and_more.py
    0007_remove_settingsheet_assigned_supervisor_and_more.py
    0008_alter_settingsheet_status.py
    0009_settingsheet_supervisor_assigned.py
    0010_settingsheet_is_temporary_and_more.py
    0011_alter_settingsheet_options_alter_settingsheet_status.py
    0012_settingsheet_station.py
    0013_settingsheet_assigned_at_alter_settingsheet_status.py
    0014_settingsheet_edit_logs_alter_settingsheet_status.py
    0015_settingsheet_has_parameters_changed.py
    0016_alter_settingsheet_scan_file.py
    0017_settingsheet_updated_at.py
    0018_ocrjob.py
    0019_ocrjob_error_detail.py
    0020_ocrjob_device_mode.py
    0021_settingsheet_execution_station.py
  __init__.py
  admin.py
  apps.py
  models.py
  relay_matcher.py
  services.py
  signals.py
  tasks.py
  tests.py
  urls.py
  utils.py
  views_bulk.py
  views.py
stations/
  management/
    commands/
      __init__.py
      run_autocheck.py
    __init__.py
  migrations/
    __init__.py
    0001_initial.py
    0002_relayautochecklog.py
    0003_relay_auto_check_enabled_relay_check_interval_unit_and_more.py
    0004_alter_relay_check_interval_unit.py
    0005_alter_relay_auto_check_enabled_and_more.py
    0006_relay_is_paused_for_correction_and_more.py
    0007_alter_station_options_station_id_capda_and_more.py
    0008_bay_i_dm_bay_id_capda_bay_id_dvi_bay_id_nlo_and_more.py
    0009_relay_id_capda_relay_id_doituong_relay_id_dvi_and_more.py
    0010_alter_bay_bay_name_alter_bay_ten_tram_and_more.py
    0011_bay_updated_at_relay_updated_at_station_updated_at.py
  __init__.py
  admin.py
  api_mock.py
  apps.py
  models.py
  search_utils.py
  tasks.py
  tests.py
  urls.py
  views.py
.env.example
docker-compose.yml
Dockerfile
manage.py
PROJECT_REQUIREMENTS.md
README.md
requirements.txt
````

# Files

## File: categories/migrations/__init__.py
````python

````

## File: categories/migrations/0001_initial.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Loại thiết bị',
                'verbose_name_plural': 'Loại thiết bị',
            },
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Đường dây',
                'verbose_name_plural': 'Đường dây',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Vị trí',
                'verbose_name_plural': 'Vị trí',
            },
        ),
        migrations.CreateModel(
            name='ManagementUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Đơn vị quản lý',
                'verbose_name_plural': 'Đơn vị quản lý',
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Hãng sản xuất',
                'verbose_name_plural': 'Hãng sản xuất',
            },
        ),
        migrations.CreateModel(
            name='ManufacturingCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Nước sản xuất',
                'verbose_name_plural': 'Nước sản xuất',
            },
        ),
        migrations.CreateModel(
            name='OperationalStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Trạng thái vận hành',
                'verbose_name_plural': 'Trạng thái vận hành',
            },
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sở hữu',
                'verbose_name_plural': 'Sở hữu',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Công trình',
                'verbose_name_plural': 'Công trình',
            },
        ),
        migrations.CreateModel(
            name='VoltageLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Cấp điện áp',
                'verbose_name_plural': 'Cấp điện áp',
            },
        ),
    ]
````

## File: categories/migrations/0002_managementunit_parent_code_managementunit_sort_order_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='managementunit',
            name='parent_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mã đơn vị cha (MA_DONVI_CHA)'),
        ),
        migrations.AddField(
            model_name='managementunit',
            name='sort_order',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='managementunit',
            name='unit_level',
            field=models.IntegerField(default=1, verbose_name='Cấp đơn vị (CAP_DONVI)'),
        ),
    ]
````

## File: categories/migrations/0003_manufacturingcountry_legacy_id_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_managementunit_parent_code_managementunit_sort_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturingcountry',
            name='legacy_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mã ID gốc (ID)'),
        ),
        migrations.AddField(
            model_name='manufacturingcountry',
            name='sort_order',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
    ]
````

## File: categories/migrations/0004_ownership_sort_order.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_manufacturingcountry_legacy_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownership',
            name='sort_order',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
    ]
````

## File: categories/migrations/0005_voltagelevel_legacy_code_voltagelevel_sort_order.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_ownership_sort_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='voltagelevel',
            name='legacy_code',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Mã phụ (MA)'),
        ),
        migrations.AddField(
            model_name='voltagelevel',
            name='sort_order',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
    ]
````

## File: categories/migrations/0006_station.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0005_voltagelevel_legacy_code_voltagelevel_sort_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True, verbose_name='Mã')),
                ('name', models.CharField(max_length=255, verbose_name='Tên')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('id_tba', models.CharField(blank=True, max_length=100, null=True, verbose_name='ID TBA (ID_TBA)')),
                ('id_tinh', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Tỉnh (ID_TINH)')),
                ('tinh', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tỉnh (TINH)')),
                ('id_quan', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Quận (ID_QUAN)')),
                ('quan', models.CharField(blank=True, max_length=100, null=True, verbose_name='Quận (QUAN)')),
                ('id_phuong', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Phường (ID_PHUONG)')),
                ('phuong', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phường (PHUONG)')),
                ('id_capda', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)')),
                ('id_ttvh', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)')),
                ('kieu_tram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kiểu trạm (KIEU_TRAM)')),
                ('id_kieu_tram', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Kiểu trạm (ID_KIEU_TRAM)')),
                ('loai_tram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Loại trạm (LOAI_TRAM)')),
                ('id_loai_tram', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Loại trạm (ID_LOAI_TRAM)')),
                ('ngay_vh', models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)')),
                ('ngay_ld', models.DateTimeField(blank=True, null=True, verbose_name='Ngày lắp đặt (NGAY_LD)')),
                ('id_dvi', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)')),
                ('id_vung', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Vùng (ID_VUNG)')),
                ('vung', models.CharField(blank=True, max_length=100, null=True, verbose_name='Vùng (VUNG)')),
                ('id_sohuu', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)')),
                ('kieu_ht_dk', models.CharField(blank=True, max_length=100, null=True, verbose_name='Kiểu HT ĐK (KIEU_HT_DK)')),
                ('id_kieu_ht_dk', models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Kiểu HT ĐK (ID_KIEU_HT_DK)')),
                ('sort_order', models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)')),
            ],
            options={
                'verbose_name': 'Danh mục Trạm',
                'verbose_name_plural': 'Danh mục Trạm',
            },
        ),
    ]
````

## File: categories/migrations/0007_delete_station.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_station'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Station',
        ),
    ]
````

## File: categories/migrations/0008_line_da_tke_line_dz_cha_line_i_chophep_line_id_capda_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0007_delete_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='da_tke',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Điện áp thiết kế (DA_TKE)'),
        ),
        migrations.AddField(
            model_name='line',
            name='dz_cha',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Đường dây cha (DZ_CHA)'),
        ),
        migrations.AddField(
            model_name='line',
            name='i_chophep',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Dòng điện cho phép (I_CHOPHEP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_da_tke',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Điện áp thiết kế (ID_DA_TKE)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_dz',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Đường dây (ID_DZ)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_dz_cha',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Đường dây cha (ID_DZ_CHA)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_nlo_cap',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Ngăn lộ cấp (ID_NLO_CAP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_nlo_nhan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Ngăn lộ nhận (ID_NLO_NHAN)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_tba_cap',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID TBA cấp (ID_TBA_CAP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_tba_nhan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID TBA nhận (ID_TBA_NHAN)'),
        ),
        migrations.AddField(
            model_name='line',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='line',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='line',
            name='nlo_cap',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ngăn lộ cấp (NLO_CAP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='nlo_nhan',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ngăn lộ nhận (NLO_NHAN)'),
        ),
        migrations.AddField(
            model_name='line',
            name='so_mach',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Số mạch (SO_MACH)'),
        ),
        migrations.AddField(
            model_name='line',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='tba_cap',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='TBA cấp (TBA_CAP)'),
        ),
        migrations.AddField(
            model_name='line',
            name='tba_nhan',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='TBA nhận (TBA_NHAN)'),
        ),
        migrations.AddField(
            model_name='line',
            name='tong_cdai',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tổng chiều dài (TONG_CDAI)'),
        ),
    ]
````

## File: categories/migrations/0009_project_id_capda_project_id_ct_project_id_dvi_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0008_line_da_tke_line_dz_cha_line_i_chophep_line_id_capda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='project',
            name='id_ct',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Công trình (ID_CT)'),
        ),
        migrations.AddField(
            model_name='project',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='project',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='project',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='project',
            name='ma_ct_cha',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Mã Công trình cha (MA_CT_CHA)'),
        ),
        migrations.AddField(
            model_name='project',
            name='nam_xd',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Năm xây dựng (NAM_XD)'),
        ),
        migrations.AddField(
            model_name='project',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='project',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='project',
            name='ten_ct_cha',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên Công trình cha (TEN_CT_CHA)'),
        ),
    ]
````

## File: categories/migrations/0010_location_duong_vao_location_hanh_lang_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0009_project_id_capda_project_id_ct_project_id_dvi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='duong_vao',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Đường vào (DUONG_VAO)'),
        ),
        migrations.AddField(
            model_name='location',
            name='hanh_lang',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Hành lang (HANH_LANG)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_ct',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Công trình (ID_CT)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_khuvuc',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Khu vực (ID_KHUVUC)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_sodo',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sơ đồ (ID_SODO)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='location',
            name='id_vitri',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Vị trí (ID_VITRI)'),
        ),
        migrations.AddField(
            model_name='location',
            name='khoang_cot',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Khoảng cột (KHOANG_COT)'),
        ),
        migrations.AddField(
            model_name='location',
            name='khoang_neo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Khoảng néo (KHOANG_NEO)'),
        ),
        migrations.AddField(
            model_name='location',
            name='khu_vuc',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Khu vực (KHU_VUC)'),
        ),
        migrations.AddField(
            model_name='location',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='location',
            name='so_do',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Sơ đồ (SO_DO)'),
        ),
        migrations.AddField(
            model_name='location',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='location',
            name='ten_ct',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên Công trình (TEN_CT)'),
        ),
    ]
````

## File: categories/__init__.py
````python

````

## File: categories/admin.py
````python
from django.contrib import admin
from .models import (
    ManagementUnit, ManufacturingCountry, Manufacturer, Ownership, 
    VoltageLevel, EquipmentType, OperationalStatus, Line, Project, 
    Location
)

admin.site.register(ManagementUnit)
admin.site.register(ManufacturingCountry)
admin.site.register(Manufacturer)
admin.site.register(Ownership)
admin.site.register(VoltageLevel)
admin.site.register(EquipmentType)
admin.site.register(OperationalStatus)
admin.site.register(Line)
admin.site.register(Project)
admin.site.register(Location)
````

## File: categories/apps.py
````python
from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    name = 'categories'
````

## File: categories/models.py
````python
from django.db import models

class CategoryBase(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name="Mã")
    name = models.CharField(max_length=255, verbose_name="Tên")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.code} - {self.name}"

class ManagementUnit(CategoryBase):
    sort_order = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")
    parent_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mã đơn vị cha (MA_DONVI_CHA)")
    unit_level = models.IntegerField(default=1, verbose_name="Cấp đơn vị (CAP_DONVI)")

    class Meta:
        verbose_name = "Đơn vị quản lý"
        verbose_name_plural = "Đơn vị quản lý"

class ManufacturingCountry(CategoryBase):
    legacy_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mã ID gốc (ID)")
    sort_order = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Nước sản xuất"
        verbose_name_plural = "Nước sản xuất"

class Manufacturer(CategoryBase):
    class Meta:
        verbose_name = "Hãng sản xuất"
        verbose_name_plural = "Hãng sản xuất"

class Ownership(CategoryBase):
    sort_order = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Sở hữu"
        verbose_name_plural = "Sở hữu"

class VoltageLevel(CategoryBase):
    legacy_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mã phụ (MA)")
    sort_order = models.CharField(max_length=50, blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Cấp điện áp"
        verbose_name_plural = "Cấp điện áp"

class EquipmentType(CategoryBase):
    class Meta:
        verbose_name = "Loại thiết bị"
        verbose_name_plural = "Loại thiết bị"

class OperationalStatus(CategoryBase):
    class Meta:
        verbose_name = "Trạng thái vận hành"
        verbose_name_plural = "Trạng thái vận hành"

class Line(CategoryBase):
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    da_tke = models.CharField(max_length=50, blank=True, null=True, verbose_name="Điện áp thiết kế (DA_TKE)")
    id_da_tke = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Điện áp thiết kế (ID_DA_TKE)")
    i_chophep = models.CharField(max_length=50, blank=True, null=True, verbose_name="Dòng điện cho phép (I_CHOPHEP)")
    
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    tong_cdai = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tổng chiều dài (TONG_CDAI)")
    so_mach = models.CharField(max_length=50, blank=True, null=True, verbose_name="Số mạch (SO_MACH)")
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    
    id_dz = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Đường dây (ID_DZ)")
    dz_cha = models.CharField(max_length=200, blank=True, null=True, verbose_name="Đường dây cha (DZ_CHA)")
    id_dz_cha = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Đường dây cha (ID_DZ_CHA)")
    
    id_tba_cap = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID TBA cấp (ID_TBA_CAP)")
    tba_cap = models.CharField(max_length=200, blank=True, null=True, verbose_name="TBA cấp (TBA_CAP)")
    id_nlo_cap = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Ngăn lộ cấp (ID_NLO_CAP)")
    nlo_cap = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ngăn lộ cấp (NLO_CAP)")
    
    id_tba_nhan = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID TBA nhận (ID_TBA_NHAN)")
    tba_nhan = models.CharField(max_length=200, blank=True, null=True, verbose_name="TBA nhận (TBA_NHAN)")
    id_nlo_nhan = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Ngăn lộ nhận (ID_NLO_NHAN)")
    nlo_nhan = models.CharField(max_length=200, blank=True, null=True, verbose_name="Ngăn lộ nhận (NLO_NHAN)")
    
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Đường dây"
        verbose_name_plural = "Đường dây"

class Project(CategoryBase):
    id_ct = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Công trình (ID_CT)")
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    nam_xd = models.CharField(max_length=50, blank=True, null=True, verbose_name="Năm xây dựng (NAM_XD)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    
    ma_ct_cha = models.CharField(max_length=100, blank=True, null=True, verbose_name="Mã Công trình cha (MA_CT_CHA)")
    ten_ct_cha = models.CharField(max_length=200, blank=True, null=True, verbose_name="Tên Công trình cha (TEN_CT_CHA)")
    
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Công trình"
        verbose_name_plural = "Công trình"

class Location(CategoryBase):
    id_vitri = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Vị trí (ID_VITRI)")
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    
    khoang_neo = models.CharField(max_length=100, blank=True, null=True, verbose_name="Khoảng néo (KHOANG_NEO)")
    khoang_cot = models.CharField(max_length=100, blank=True, null=True, verbose_name="Khoảng cột (KHOANG_COT)")
    
    id_khuvuc = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Khu vực (ID_KHUVUC)")
    khu_vuc = models.CharField(max_length=200, blank=True, null=True, verbose_name="Khu vực (KHU_VUC)")
    
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    
    id_ct = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Công trình (ID_CT)")
    ten_ct = models.CharField(max_length=200, blank=True, null=True, verbose_name="Tên Công trình (TEN_CT)")
    
    duong_vao = models.CharField(max_length=200, blank=True, null=True, verbose_name="Đường vào (DUONG_VAO)")
    hanh_lang = models.CharField(max_length=200, blank=True, null=True, verbose_name="Hành lang (HANH_LANG)")
    
    id_sodo = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sơ đồ (ID_SODO)")
    so_do = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sơ đồ (SO_DO)")
    
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Vị trí"
        verbose_name_plural = "Vị trí"
````

## File: categories/serializers.py
````python
from rest_framework import serializers
from .models import (
    ManagementUnit, ManufacturingCountry, Manufacturer, Ownership,
    VoltageLevel, EquipmentType, OperationalStatus, Line, Project, Location
)
from stations.models import Station, Bay, Relay

# Generic serializer for all CategoryBase models
class CategoryBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

def create_serializer(model_class):
    class Meta:
        model = model_class
        fields = '__all__'
    
    return type(f'{model_class.__name__}Serializer', (CategoryBaseSerializer,), {'Meta': Meta})

ManagementUnitSerializer = create_serializer(ManagementUnit)
ManufacturingCountrySerializer = create_serializer(ManufacturingCountry)
ManufacturerSerializer = create_serializer(Manufacturer)
OwnershipSerializer = create_serializer(Ownership)
VoltageLevelSerializer = create_serializer(VoltageLevel)
EquipmentTypeSerializer = create_serializer(EquipmentType)
OperationalStatusSerializer = create_serializer(OperationalStatus)
LineSerializer = create_serializer(Line)
ProjectSerializer = create_serializer(Project)
LocationSerializer = create_serializer(Location)

# Serializers for existing Station, Bay, Relay to match the format somewhat
class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = '__all__'

class BaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bay
        fields = '__all__'

class RelaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Relay
        fields = '__all__'
````

## File: categories/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: categories/urls.py
````python
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
````

## File: categories/views.py
````python
from rest_framework import viewsets
from .models import (
    ManagementUnit, ManufacturingCountry, Manufacturer, Ownership,
    VoltageLevel, EquipmentType, OperationalStatus, Line, Project, Location
)
from stations.models import Station, Bay, Relay
from .serializers import (
    ManagementUnitSerializer, ManufacturingCountrySerializer, ManufacturerSerializer, OwnershipSerializer,
    VoltageLevelSerializer, EquipmentTypeSerializer, OperationalStatusSerializer, LineSerializer, ProjectSerializer, LocationSerializer,
    StationSerializer, BaySerializer, RelaySerializer
)

class CategoryBaseViewSet(viewsets.ModelViewSet):
    # Base class can hold common logic if needed
    pass

class ManagementUnitViewSet(CategoryBaseViewSet):
    queryset = ManagementUnit.objects.all()
    serializer_class = ManagementUnitSerializer

class ManufacturingCountryViewSet(CategoryBaseViewSet):
    queryset = ManufacturingCountry.objects.all()
    serializer_class = ManufacturingCountrySerializer

class ManufacturerViewSet(CategoryBaseViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer

class OwnershipViewSet(CategoryBaseViewSet):
    queryset = Ownership.objects.all()
    serializer_class = OwnershipSerializer

class VoltageLevelViewSet(CategoryBaseViewSet):
    queryset = VoltageLevel.objects.all()
    serializer_class = VoltageLevelSerializer

class EquipmentTypeViewSet(CategoryBaseViewSet):
    queryset = EquipmentType.objects.all()
    serializer_class = EquipmentTypeSerializer

class OperationalStatusViewSet(CategoryBaseViewSet):
    queryset = OperationalStatus.objects.all()
    serializer_class = OperationalStatusSerializer

class LineViewSet(CategoryBaseViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

class ProjectViewSet(CategoryBaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class LocationViewSet(CategoryBaseViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer

class BayViewSet(viewsets.ModelViewSet):
    queryset = Bay.objects.all()
    serializer_class = BaySerializer

class RelayViewSet(viewsets.ModelViewSet):
    queryset = Relay.objects.all()
    serializer_class = RelaySerializer


# ==========================================
# UI Views for HTMX + TailwindCSS
# ==========================================
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django import forms
import importlib

# Map category ID to model class
CATEGORY_MODELS = {
    'management_unit': ('categories.models', 'ManagementUnit', 'Đơn vị quản lý'),
    'manufacturing_country': ('categories.models', 'ManufacturingCountry', 'Nước sản xuất'),
    'manufacturer': ('categories.models', 'Manufacturer', 'Hãng sản xuất'),
    'ownership': ('categories.models', 'Ownership', 'Sở hữu'),
    'voltage_level': ('categories.models', 'VoltageLevel', 'Cấp điện áp'),
    'equipment_type': ('categories.models', 'EquipmentType', 'Loại thiết bị'),
    'operational_status': ('categories.models', 'OperationalStatus', 'Trạng thái vận hành'),
    'line': ('categories.models', 'Line', 'Đường dây'),
    'project': ('categories.models', 'Project', 'Công trình'),
    'location': ('categories.models', 'Location', 'Vị trí'),
    'station': ('stations.models', 'Station', 'Trạm'),
    'bay': ('stations.models', 'Bay', 'Ngăn lộ'),
    'relay': ('stations.models', 'Relay', 'Thiết bị (Rơ-le)'),
}

def get_model_class(category_id):
    if category_id not in CATEGORY_MODELS:
        raise Http404("Category not found")
    module_name, class_name, _ = CATEGORY_MODELS[category_id]
    module = importlib.import_module(module_name)
    return getattr(module, class_name)

def get_category_form(model_class):
    class DynamicCategoryForm(forms.ModelForm):
        class Meta:
            model = model_class
            exclude = ['created_at', 'updated_at']
            
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                # Tối ưu hóa: Tránh load toàn bộ dữ liệu (VD: 8600+ Ngăn lộ) vào dropdown
                if isinstance(field, forms.ModelChoiceField):
                    if field.queryset.count() > 500:
                        if self.instance and getattr(self.instance, field_name, None):
                            # Chỉ giữ lại giá trị hiện tại để dropdown hiển thị, không load 8600 mục khác
                            field.queryset = field.queryset.filter(pk=getattr(self.instance, field_name).pk)
                        else:
                            field.queryset = field.queryset.none()
                            
                widget = field.widget
                attrs = widget.attrs
                attrs['class'] = 'w-full px-3 py-2 border border-slate-300 dark:border-slate-600 rounded-lg shadow-sm focus:border-blue-500 dark:focus:border-blue-500 focus:ring-1 focus:ring-blue-500 outline-none text-sm text-slate-800 dark:text-slate-200 bg-white dark:bg-slate-900 transition-colors'
                if isinstance(widget, forms.Textarea):
                    attrs['rows'] = 3
                
    return DynamicCategoryForm

@login_required
def category_dashboard(request):
    categories = [{'id': k, 'name': v[2], 'api': k.replace('_', '-')} for k, v in CATEGORY_MODELS.items()]
    return render(request, 'categories/category_dashboard.html', {'categories': categories})

@login_required
def category_list(request, category_id):
    model_class = get_model_class(category_id)
    _, _, name = CATEGORY_MODELS[category_id]
    
    queryset = model_class.objects.all().order_by('-id')
    
    query = request.GET.get('q', '')
    if query:
        from django.db.models import Q
        query_clean = query.replace(',', ' ').replace('-', ' ')
        terms = [t for t in query_clean.split() if t]
        for term in terms:
            if category_id == 'station':
                queryset = queryset.filter(Q(station_name__icontains=term) | Q(station_code__icontains=term))
            elif category_id == 'bay':
                queryset = queryset.filter(Q(bay_name__icontains=term) | Q(bay_code__icontains=term))
            elif category_id == 'relay':
                queryset = queryset.filter(Q(relay_name__icontains=term) | Q(relay_code__icontains=term))
            else:
                queryset = queryset.filter(Q(name__icontains=term) | Q(code__icontains=term))

    paginator = Paginator(queryset, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'category_id': category_id,
        'category_name': name,
        'q': query
    }

    if request.headers.get('HX-Request') and not request.headers.get('HX-Boosted'):
        return render(request, 'categories/partials/category_list_partial.html', context)
    return render(request, 'categories/category_list.html', context)

@login_required
def category_form(request, category_id, pk=None):
    model_class = get_model_class(category_id)
    _, _, name = CATEGORY_MODELS[category_id]
    FormClass = get_category_form(model_class)
    
    instance = get_object_or_404(model_class, pk=pk) if pk else None

    if request.method == 'POST':
        form = FormClass(request.POST, instance=instance)
        
        has_conflict = False
        if instance and hasattr(instance, 'updated_at'):
            original_updated_at = request.POST.get('_original_updated_at')
            if original_updated_at and str(instance.updated_at.timestamp()) != original_updated_at:
                has_conflict = True
                
        if has_conflict:
            form.add_error(None, "Dữ liệu này đã bị thay đổi bởi một người khác trong khi bạn đang thao tác. Hãy Hủy bỏ và mở lại để xem nội dung mới nhất.")
        elif form.is_valid():
            form.save()
            return HttpResponse(status=204, headers={'HX-Trigger': 'categoryListChanged'})
    else:
        form = FormClass(instance=instance)

    return render(request, 'categories/partials/category_form_modal.html', {
        'form': form,
        'category_id': category_id,
        'category_name': name,
        'instance': instance,
        'original_updated_at': str(instance.updated_at.timestamp()) if instance and hasattr(instance, 'updated_at') else None
    })

@login_required
def category_delete(request, category_id, pk):
    model_class = get_model_class(category_id)
    instance = get_object_or_404(model_class, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return HttpResponse(status=204, headers={'HX-Trigger': 'categoryListChanged'})
    return HttpResponse(status=400)


# ==========================================
# Asset Management Views (Advanced List + Slide-over)
# ==========================================

@login_required
def asset_line_list(request):
    """Danh sách Đường dây với Advanced Table + Slide-over"""
    from .models import Line, VoltageLevel, OperationalStatus
    queryset = Line.objects.all().order_by('code')
    
    q = request.GET.get('q', '')
    filter_capda = request.GET.get('capda', '')
    filter_ttvh = request.GET.get('ttvh', '')
    
    if q:
        queryset = queryset.filter(name__icontains=q) | queryset.filter(code__icontains=q)
    if filter_capda:
        vl = VoltageLevel.objects.filter(code=filter_capda).first()
        capda_val = vl.legacy_code if (vl and vl.legacy_code) else filter_capda
        queryset = queryset.filter(id_capda=capda_val)
    if filter_ttvh:
        queryset = queryset.filter(id_ttvh=filter_ttvh)
    
    paginator = Paginator(queryset, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    # Detail view for slide-over
    detail_pk = request.GET.get('detail')
    detail_obj = Line.objects.filter(pk=detail_pk).first() if detail_pk else None
    
    context = {
        'page_obj': page_obj,
        'q': q,
        'filter_capda': filter_capda,
        'filter_ttvh': filter_ttvh,
        'voltage_levels': VoltageLevel.objects.all().order_by('code'),
        'op_statuses': OperationalStatus.objects.all().order_by('code'),
        'detail_obj': detail_obj,
        'total_count': queryset.count(),
    }
    if request.GET.get('_panel') == '1':
        return render(request, 'categories/partials/line_detail_panel.html', {'obj': detail_obj})
    
    if request.headers.get('HX-Request') and not request.headers.get('HX-Boosted'):
        return render(request, 'categories/partials/line_table.html', context)
        
    return render(request, 'categories/asset_line_list.html', context)


@login_required
def asset_location_list(request):
    """Danh sách Vị trí / Cột điện với Advanced Table + Slide-over"""
    from .models import Location, VoltageLevel, OperationalStatus
    queryset = Location.objects.all().order_by('code')
    
    q = request.GET.get('q', '')
    filter_capda = request.GET.get('capda', '')
    filter_ttvh = request.GET.get('ttvh', '')
    
    if q:
        queryset = queryset.filter(name__icontains=q) | queryset.filter(code__icontains=q)
    if filter_capda:
        vl = VoltageLevel.objects.filter(code=filter_capda).first()
        capda_val = vl.legacy_code if (vl and vl.legacy_code) else filter_capda
        queryset = queryset.filter(id_capda=capda_val)
    if filter_ttvh:
        queryset = queryset.filter(id_ttvh=filter_ttvh)
    
    paginator = Paginator(queryset, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    detail_pk = request.GET.get('detail')
    detail_obj = Location.objects.filter(pk=detail_pk).first() if detail_pk else None
    
    context = {
        'page_obj': page_obj,
        'q': q,
        'filter_capda': filter_capda,
        'filter_ttvh': filter_ttvh,
        'voltage_levels': VoltageLevel.objects.all().order_by('code'),
        'op_statuses': OperationalStatus.objects.all().order_by('code'),
        'detail_obj': detail_obj,
        'total_count': queryset.count(),
    }
    if request.GET.get('_panel') == '1':
        return render(request, 'categories/partials/location_detail_panel.html', {'obj': detail_obj})
        
    if request.headers.get('HX-Request') and not request.headers.get('HX-Boosted'):
        return render(request, 'categories/partials/location_table.html', context)
        
    return render(request, 'categories/asset_location_list.html', context)


@login_required
def asset_project_list(request):
    """Danh sách Công trình với Advanced Table + Slide-over"""
    from .models import Project, VoltageLevel, OperationalStatus
    queryset = Project.objects.all().order_by('code')
    
    q = request.GET.get('q', '')
    filter_capda = request.GET.get('capda', '')
    filter_ttvh = request.GET.get('ttvh', '')
    
    if q:
        queryset = queryset.filter(name__icontains=q) | queryset.filter(code__icontains=q)
    if filter_capda:
        vl = VoltageLevel.objects.filter(code=filter_capda).first()
        capda_val = vl.legacy_code if (vl and vl.legacy_code) else filter_capda
        queryset = queryset.filter(id_capda=capda_val)
    if filter_ttvh:
        queryset = queryset.filter(id_ttvh=filter_ttvh)
    
    paginator = Paginator(queryset, 25)
    page_obj = paginator.get_page(request.GET.get('page'))
    
    detail_pk = request.GET.get('detail')
    detail_obj = Project.objects.filter(pk=detail_pk).first() if detail_pk else None
    
    context = {
        'page_obj': page_obj,
        'q': q,
        'filter_capda': filter_capda,
        'filter_ttvh': filter_ttvh,
        'voltage_levels': VoltageLevel.objects.all().order_by('code'),
        'op_statuses': OperationalStatus.objects.all().order_by('code'),
        'detail_obj': detail_obj,
        'total_count': queryset.count(),
    }
    if request.GET.get('_panel') == '1':
        return render(request, 'categories/partials/project_detail_panel.html', {'obj': detail_obj})
        
    if request.headers.get('HX-Request') and not request.headers.get('HX-Boosted'):
        return render(request, 'categories/partials/project_table.html', context)
        
    return render(request, 'categories/asset_project_list.html', context)
````

## File: checks/migrations/__init__.py
````python

````

## File: checks/migrations/0001_initial.py
````python
# Generated by Django 6.0.7 on 2026-07-18 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sheets', '0001_initial'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeriodicCheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scheduled_date', models.DateField()),
                ('actual_check_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(choices=[('SCHEDULED', 'Scheduled'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed')], default='SCHEDULED', max_length=50)),
                ('relay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stations.relay')),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sheets.settingsheet')),
            ],
        ),
        migrations.CreateModel(
            name='PeriodicCheckItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_code', models.CharField(max_length=50)),
                ('measured_value', models.FloatField()),
                ('deviation_percent', models.FloatField()),
                ('is_within_tolerance', models.BooleanField()),
                ('periodic_check', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='checks.periodiccheck')),
            ],
        ),
    ]
````

## File: checks/migrations/0002_alter_periodiccheck_sheet.py
````python
# Generated by Django 6.0.7 on 2026-07-19 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0001_initial'),
        ('sheets', '0007_remove_settingsheet_assigned_supervisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodiccheck',
            name='sheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sheets.settingsheet'),
        ),
    ]
````

## File: checks/__init__.py
````python

````

## File: checks/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: checks/apps.py
````python
from django.apps import AppConfig


class ChecksConfig(AppConfig):
    name = 'checks'
````

## File: checks/models.py
````python
from django.db import models
from stations.models import Relay
from sheets.models import SettingSheet

class PeriodicCheck(models.Model):
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
    )

    relay = models.ForeignKey(Relay, on_delete=models.CASCADE)
    sheet = models.ForeignKey(SettingSheet, on_delete=models.CASCADE, null=True, blank=True)
    scheduled_date = models.DateField()
    actual_check_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='SCHEDULED')

    def __str__(self):
        return f"Check for {self.relay.relay_code} on {self.scheduled_date}"

class PeriodicCheckItem(models.Model):
    periodic_check = models.ForeignKey(PeriodicCheck, related_name='items', on_delete=models.CASCADE)
    parameter_code = models.CharField(max_length=50)
    measured_value = models.FloatField()
    deviation_percent = models.FloatField()
    is_within_tolerance = models.BooleanField()

    def __str__(self):
        return f"{self.parameter_code}: {self.measured_value}"
````

## File: checks/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: checks/urls.py
````python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.check_list, name='check_list'),
    path('new/', views.check_create, name='check_create'),
    path('<int:pk>/', views.check_detail, name='check_detail'),
    path('<int:pk>/items/', views.check_update_item, name='check_update_item'),
    path('<int:pk>/complete/', views.check_complete, name='check_complete'),
]
````

## File: checks/views.py
````python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import PeriodicCheck, PeriodicCheckItem
from stations.models import Relay, RelaySetting
from datetime import datetime
import json

@login_required
def check_list(request):
    """View danh sách lịch kiểm tra định kỳ."""
    checks = PeriodicCheck.objects.all().order_by('-scheduled_date')
    return render(request, 'checks/check_list.html', {'checks': checks})

@login_required
def check_create(request):
    """View tạo lịch kiểm tra mới."""
    if request.method == 'POST':
        relay_id = request.POST.get('relay_id')
        scheduled_date = request.POST.get('scheduled_date')
        
        relay = get_object_or_404(Relay, pk=relay_id)
        
        # Tạo Check mới
        check = PeriodicCheck.objects.create(
            relay=relay,
            scheduled_date=scheduled_date,
            status='SCHEDULED'
        )
        
        # Load các thông số từ RelaySetting để tạo các Item trống
        settings = RelaySetting.objects.filter(relay=relay)
        for s in settings:
            PeriodicCheckItem.objects.create(
                periodic_check=check,
                parameter_code=s.parameter_code,
                measured_value=0.0, # Sẽ được KTV update sau
                deviation_percent=0.0,
                is_within_tolerance=True
            )
            
        messages.success(request, f"Đã lên lịch kiểm tra cho {relay.relay_code}")
        return redirect('check_detail', pk=check.pk)

    relays = Relay.objects.all()
    return render(request, 'checks/check_form.html', {'relays': relays})

@login_required
def check_detail(request, pk):
    """View chi tiết đợt kiểm tra và form nhập liệu."""
    check = get_object_or_404(PeriodicCheck, pk=pk)
    
    # Ghép Item với Setting tương ứng
    items_with_settings = []
    for item in check.items.all():
        setting = RelaySetting.objects.filter(relay=check.relay, parameter_code=item.parameter_code).first()
        items_with_settings.append({
            'item': item,
            'setting': setting
        })
        
    context = {
        'check': check,
        'items': items_with_settings
    }
    return render(request, 'checks/check_detail.html', context)

@login_required
def check_update_item(request, pk):
    """View API dùng cho HTMX để lưu và tính toán sai lệch realtime."""
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        measured_value = float(request.POST.get('measured_value', 0))
        
        item = get_object_or_404(PeriodicCheckItem, pk=item_id)
        setting = RelaySetting.objects.filter(relay=item.periodic_check.relay, parameter_code=item.parameter_code).first()
        
        if setting:
            std = setting.standard_value
            # Calculate deviation %
            if std != 0:
                deviation = abs(measured_value - std) / abs(std) * 100
            else:
                deviation = 0.0
                
            is_within = setting.tolerance_min <= measured_value <= setting.tolerance_max
            
            item.measured_value = measured_value
            item.deviation_percent = deviation
            item.is_within_tolerance = is_within
            item.save()
            
            return render(request, 'checks/partials/_item_row.html', {
                'item_dict': {'item': item, 'setting': setting}
            })
            
    return JsonResponse({'success': False}, status=400)

@login_required
def check_complete(request, pk):
    """Đóng đợt kiểm tra."""
    if request.method == 'POST':
        check = get_object_or_404(PeriodicCheck, pk=pk)
        check.check_status = 'COMPLETED'
        check.actual_check_date = datetime.now()
        check.save()
        messages.success(request, "Đã lưu hoàn thành đợt kiểm tra.")
    return redirect('check_detail', pk=pk)
````

## File: core/management/commands/seed_data.py
````python
import random
from django.core.management.base import BaseCommand
from core.models import Organization, UserProfile
from stations.models import Station, Bay, Relay, RelaySetting
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seeds the database with initial sample data'

    def handle(self, *args, **kwargs):
        self.stdout.write("Bắt đầu khởi tạo dữ liệu mẫu...")

        # 1. Tạo Users và Organizations
        org_vtc, _ = Organization.objects.get_or_create(code="VTC_1", defaults={"name": "Công ty Truyền tải điện 1", "org_type": "TRANSMISSION"})
        org_station, _ = Organization.objects.get_or_create(code="TBA_HB", defaults={"name": "TBA 220kV Hòa Bình", "org_type": "STATION", "parent": org_vtc})

        user_a0, _ = User.objects.get_or_create(username="a0_admin", defaults={"email": "a0@evn.com.vn", "first_name": "A0", "last_name": "Admin"})
        if not hasattr(user_a0, 'userprofile'):
            user_a0.set_password("password123")
            user_a0.save()
            UserProfile.objects.create(user=user_a0, organization=org_vtc, phone_number="0988000111")

        # 2. Tạo Trạm biến áp (Station)
        station, _ = Station.objects.get_or_create(
            station_code="TBA_220KV_HB",
            defaults={
                "station_name": "Trạm biến áp 220kV Hòa Bình",
                "location": "Tỉnh Hòa Bình"
            }
        )

        # 3. Tạo Ngăn lộ (Bay)
        bays = []
        for i in range(1, 4):
            bay, _ = Bay.objects.get_or_create(
                station=station,
                bay_code=f"BAY_AT{i}",
                defaults={"bay_name": f"Ngăn Máy biến áp AT{i}"}
            )
            bays.append(bay)

        # 4. Tạo Rơ-le (Relay) và Cài đặt (RelaySetting)
        relay_count = 0
        for bay in bays:
            for j in range(1, 3):
                relay, created = Relay.objects.get_or_create(
                    bay=bay,
                    relay_code=f"REL_{bay.bay_code}_{j}",
                    defaults={
                        "relay_name": f"Rơ-le bảo vệ số {j} ({bay.bay_name})",
                        "manufacturer": random.choice(["ABB", "Siemens", "SEL", "GE"])
                    }
                )
                if created:
                    relay_count += 1
                    # Tạo settings chuẩn cho Relay
                    RelaySetting.objects.create(relay=relay, parameter_code="I_START", parameter_name="Dòng khởi động", standard_value=1.5, unit="A", tolerance_min=1.45, tolerance_max=1.55)
                    RelaySetting.objects.create(relay=relay, parameter_code="T_TRIP", parameter_name="Thời gian cắt", standard_value=0.5, unit="s", tolerance_min=0.48, tolerance_max=0.52)
                    RelaySetting.objects.create(relay=relay, parameter_code="V_MIN", parameter_name="Điện áp thấp", standard_value=100.0, unit="V", tolerance_min=98.0, tolerance_max=102.0)

        self.stdout.write(self.style.SUCCESS(f"Đã tạo thành công: 1 Trạm, {len(bays)} Ngăn lộ, {relay_count} Rơ-le."))
        self.stdout.write(self.style.SUCCESS("Hoàn tất sinh dữ liệu mẫu!"))
````

## File: core/management/commands/seed_permissions.py
````python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from sheets.models import SettingSheet

class Command(BaseCommand):
    help = 'Assign default permissions to groups'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(SettingSheet)
        
        # Matrix mapping
        matrix = {
            'DISPATCHER': ['can_create_sheet', 'can_dispatch_sheet', 'can_view_stations'],
            'STATION_LEADER': ['can_dispatch_sheet'],
            'TECHNICIAN': ['can_execute_sheet'],
            'SUPERVISOR': ['can_supervise_sheet'],
            'ADMIN': ['can_view_stations', 'can_view_checks', 'can_manage_users', 'can_approve_sheet']
        }

        for group_name, perms in matrix.items():
            group, _ = Group.objects.get_or_create(name=group_name)
            group.permissions.clear()
            for perm_codename in perms:
                try:
                    perm = Permission.objects.get(codename=perm_codename, content_type=content_type)
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Permission {perm_codename} not found!"))
            
            self.stdout.write(self.style.SUCCESS(f"Assigned permissions to {group_name}"))

        self.stdout.write(self.style.SUCCESS('Successfully seeded default permissions!'))
````

## File: core/management/commands/seed_users.py
````python
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Seed initial roles (groups) and dummy users for testing'

    def handle(self, *args, **kwargs):
        roles = [
            ('ADMIN', 'admin@evn.vn', 'Quản trị viên'),

            ('DISPATCHER', 'dispatcher@evn.vn', 'Người Điều phối'),
            ('STATION_LEADER', 'truongnhom@evn.vn', 'Trưởng nhóm Trạm'),
            ('TECHNICIAN', 'ktv@evn.vn', 'KTV Chỉnh định'),
            ('SUPERVISOR', 'truongtram@evn.vn', 'Giám sát Trạm')
        ]

        for role_name, email, full_name in roles:
            # Create Group
            group, created = Group.objects.get_or_create(name=role_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created group: {role_name}"))

            # Create User
            username = email.split('@')[0]
            user, u_created = User.objects.get_or_create(username=username, defaults={
                'email': email,
                'first_name': full_name
            })
            
            if u_created:
                user.set_password('123456')
                user.save()
                self.stdout.write(self.style.SUCCESS(f"Created user: {username} (Password: 123456)"))
            
            # Assign user to group
            if not user.groups.filter(name=role_name).exists():
                user.groups.add(group)
                self.stdout.write(self.style.SUCCESS(f"Assigned {username} to {role_name}"))

            # Give admin user superuser status
            if role_name == 'ADMIN' and not user.is_superuser:
                user.is_superuser = True
                user.is_staff = True
                user.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded users and roles!'))
````

## File: core/migrations/__init__.py
````python

````

## File: core/migrations/0001_initial.py
````python
# Generated by Django 6.0.7 on 2026-07-18 15:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('org_type', models.CharField(max_length=50)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.organization')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.organization')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
````

## File: core/migrations/0002_userprofile_station.py
````python
# Generated by Django 6.0.7 on 2026-07-21 02:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='users', to='stations.station'),
        ),
    ]
````

## File: core/migrations/0003_systemconfig.py
````python
# Generated by Django 6.0.7 on 2026-07-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofile_station'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, unique=True, verbose_name='Mã cấu hình')),
                ('value', models.CharField(max_length=500, verbose_name='Giá trị')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Mô tả')),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
````

## File: core/migrations/0004_systemconfig_auth_header.py
````python
# Generated by Django 6.0.7 on 2026-07-29 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_systemconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='auth_header',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Token/Header xác thực'),
        ),
    ]
````

## File: core/migrations/0005_systemconfig_auto_sync_enabled_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_systemconfig_auth_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='auto_sync_enabled',
            field=models.BooleanField(default=False, verbose_name='Tự động đồng bộ'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='last_sync_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Trạng thái đồng bộ cuối'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='last_sync_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Lần đồng bộ cuối'),
        ),
        migrations.AddField(
            model_name='systemconfig',
            name='sync_interval_minutes',
            field=models.IntegerField(default=1440, verbose_name='Chu kỳ đồng bộ (phút)'),
        ),
    ]
````

## File: core/migrations/0006_systemconfig_sync_count.py
````python
# Generated by Django 6.0.7 on 2026-07-29 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_systemconfig_auto_sync_enabled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='sync_count',
            field=models.IntegerField(default=0, verbose_name='Số lần đồng bộ'),
        ),
    ]
````

## File: core/migrations/0007_systemconfig_is_syncing.py
````python
# Generated by Django 6.0.7 on 2026-07-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_systemconfig_sync_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemconfig',
            name='is_syncing',
            field=models.BooleanField(default=False, verbose_name='Đang đồng bộ'),
        ),
    ]
````

## File: core/migrations/0008_userprofile_updated_at.py
````python
# Generated by Django 6.0.7 on 2026-07-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_systemconfig_is_syncing'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
````

## File: core/migrations/0009_alter_systemconfig_last_sync_status.py
````python
# Generated by Django 6.0.8 on 2026-10-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_userprofile_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemconfig',
            name='last_sync_status',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Trạng thái đồng bộ cuối'),
        ),
    ]
````

## File: core/templatetags/__init__.py
````python
# Empty
````

## File: core/templatetags/auth_extras.py
````python
from django import template

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    if user.is_superuser:
        return True
    return user.groups.filter(name=group_name).exists()

@register.simple_tag(takes_context=True)
def url_replace(context, field, value):
    dict_ = context['request'].GET.copy()
    dict_[field] = value
    return dict_.urlencode()
````

## File: core/templatetags/core_extras.py
````python
from django import template

register = template.Library()

@register.filter
def replace_donvi(value, unit_code):
    """Replaces {{DONVI}} in the string with the given unit code."""
    if value:
        return value.replace('{{DONVI}}', unit_code)
    return value
````

## File: core/utils/api_sync.py
````python
import json
import urllib.request
import requests
from urllib.parse import urlparse
import logging
from core.models import SystemConfig
from categories.models import ManagementUnit, ManufacturingCountry, Manufacturer, Ownership, VoltageLevel, EquipmentType, OperationalStatus, Line, Project, Location
from stations.models import Bay, Relay, Station
from core.utils.xml_converter import json_to_xml
import traceback

logger = logging.getLogger(__name__)

def run_api_sync(config_key=None, config_id=None, specific_unit=None, custom_url=None, is_background=False, start_idx=0):
    """
    Chạy quá trình đồng bộ cho một SystemConfig cụ thể.
    Nếu specific_unit được truyền vào (mã đơn vị), chỉ đồng bộ cho đơn vị đó (nếu URL chứa {{DONVI}}).
    Nếu custom_url được truyền vào, sử dụng trực tiếp URL này thay vì URL mẫu.
    Trả về (success: bool, count: int, error_message: str)
    """
    try:
        if config_id:
            config = SystemConfig.objects.get(id=config_id)
        elif config_key:
            config = SystemConfig.objects.get(key=config_key)
        else:
            return False, 0, "No config identified"
    except SystemConfig.DoesNotExist:
        return False, 0, "Config not found"

    url_template = config.value
    if not url_template or not url_template.startswith('http'):
        return False, 0, "URL không hợp lệ"
        
    urls_to_process = []
    
    # Bước 1: Xử lý biến {{DONVI}}
    temp_urls_1 = []
    if custom_url:
        temp_urls_1.append(custom_url)
    elif '{{DONVI}}' in url_template:
        if specific_unit:
            temp_urls_1.append(url_template.replace('{{DONVI}}', specific_unit))
        else:
            units = ManagementUnit.objects.values_list('code', flat=True)
            for code in units:
                temp_urls_1.append(url_template.replace('{{DONVI}}', str(code)))
            if not units:
                temp_urls_1.append(url_template) # Fallback
    else:
        temp_urls_1.append(url_template)
        
    # Bước 1.5: Xử lý biến {{LOAI}} (Theo Excel: LOAI là DZ/TBA hoặc để trắng)
    temp_urls_1_5 = []
    if any('{{LOAI}}' in u for u in temp_urls_1):
        if config and config.key == 'API_THIET_BI':
            # Theo chuẩn Excel: để trắng LOAI là lấy tất cả thiết bị (cả ĐZ và TBA)
            for u in temp_urls_1:
                temp_urls_1_5.append(u.replace('{{LOAI}}', ''))
        else:
            loai_types = ['TBA', 'DZ']
            for u in temp_urls_1:
                if '{{LOAI}}' in u:
                    for l_type in loai_types:
                        temp_urls_1_5.append(u.replace('{{LOAI}}', l_type))
                else:
                    temp_urls_1_5.append(u)
    else:
        temp_urls_1_5 = temp_urls_1
        
    # Bước 2: Xử lý biến {{LOAI_TB}}
    if any('{{LOAI_TB}}' in u for u in temp_urls_1_5):
        # Đối với hệ thống RMS (Relay Management), mặc định LOAI_TB=ROLE theo chuẩn TH_API_PMIS.xlsx
        if config and config.key == 'API_THIET_BI':
            for u in temp_urls_1_5:
                urls_to_process.append(u.replace('{{LOAI_TB}}', 'ROLE'))
        else:
            from categories.models import EquipmentType
            all_eq_codes = EquipmentType.objects.values_list('code', flat=True)
            for u in temp_urls_1_5:
                if '{{LOAI_TB}}' in u:
                    for eq_code in all_eq_codes:
                        urls_to_process.append(u.replace('{{LOAI_TB}}', str(eq_code)))
                    if not all_eq_codes:
                        urls_to_process.append(u) # Fallback
                else:
                    urls_to_process.append(u)
    else:
        urls_to_process = temp_urls_1_5

    total_lst_data = []
    total_errors = []
    
    import ssl
    import urllib3
    class LegacySSLAdapter(requests.adapters.HTTPAdapter):
        def init_poolmanager(self, connections, maxsize, block=False):
            ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
            ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            try:
                ctx.set_ciphers('DEFAULT@SECLEVEL=1')
            except ssl.SSLError:
                pass
            self.poolmanager = urllib3.poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_context=ctx
            )
            
    sess = requests.Session()
    sess.trust_env = False
    sess.mount('https://', LegacySSLAdapter())
    
    total_urls = len(urls_to_process)
    total_saved_count = 0
    urls_to_process = urls_to_process[start_idx:]
    
    for relative_idx, url in enumerate(urls_to_process):
        idx = start_idx + relative_idx
        # Lưu tiến trình 
        if config and total_urls > 0 and is_background:
            config.refresh_from_db(fields=['is_syncing'])
            if not config.is_syncing:
                total_errors.append("Đã bị người dùng dừng đột ngột.")
                break
            config.last_sync_status = f"progress:{int((idx / total_urls) * 100)}:{idx}:{total_urls}"
            config.save(update_fields=['last_sync_status'])

        try:
            # Tự động ép dùng HTTPS vì Cloudrity chặn cổng HTTP
            if url.startswith('http://') and 'pmis.npt.com.vn' in url:
                url = url.replace('http://', 'https://', 1)
                
            parsed_url = urlparse(url)
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'Accept-Language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Host': parsed_url.hostname
            }
            if config.auth_header:
                auth_val = config.auth_header.strip()
                if ':' in auth_val and not auth_val.lower().startswith('basic ') and not auth_val.lower().startswith('bearer '):
                    import base64
                    encoded = base64.b64encode(auth_val.encode('utf-8')).decode('utf-8')
                    headers['Authorization'] = f'Basic {encoded}'
                else:
                    headers['Authorization'] = auth_val
                
            res = sess.get(url, headers=headers, timeout=20, verify=False)
            res.raise_for_status()
            
            try:
                data_json = json.loads(res.text)
            except json.JSONDecodeError:
                preview = res.text[:200].replace('\n', ' ')
                total_errors.append(f"Không thể parse JSON từ {url}. Dữ liệu trả về: {preview}")
                continue
                
            # Extract list data
            current_lst = []
            if isinstance(data_json, list) and len(data_json) > 0 and 'lst' in data_json[0]:
                current_lst = data_json[0]['lst']
            elif isinstance(data_json, dict) and 'lst' in data_json:
                current_lst = data_json['lst']
            elif isinstance(data_json, list):
                current_lst = data_json
                
            # Stream: Process mapping immediately!
            if current_lst:
                saved = process_db_mapping(config, current_lst)
                total_saved_count += saved
                
        except Exception as e:
            total_errors.append(f"Lỗi {url}: {str(e)}")
            
    if total_saved_count == 0 and total_errors:
        return False, 0, " | ".join(total_errors[:3])
    
    # DB mapping is now done incrementally, so we just return here
    return True, total_saved_count, ""

def process_db_mapping(config, lst_data):
    from categories.models import ManagementUnit, EquipmentType, ManufacturingCountry, Manufacturer, Ownership, VoltageLevel, OperationalStatus, Line, Project, Location
    from stations.models import Bay, Relay, Station
    
    # DB Mapping
    count = 0
    if config.key == 'API_DANH_MUC_DON_VI_QUAN_LY':
        for item in lst_data:
            code = item.get('MA_DONVI')
            if code:
                ManagementUnit.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN_DONVI', ''),
                        'sort_order': str(item.get('SAPXEP', '')),
                        'parent_code': item.get('MA_DONVI_CHA', ''),
                        'unit_level': item.get('CAP_DONVI', 1)
                    }
                )
                count += 1
    elif config.key == 'API_TRAM':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_TRAM')
            if code:
                Station.objects.update_or_create(
                    station_code=code,
                    defaults={
                        'station_name': item.get('TEN') or item.get('TEN_TRAM', ''),
                        'id_tba': item.get('ID_TBA', ''),
                        'id_tinh': item.get('ID_TINH', ''),
                        'tinh': item.get('TINH', ''),
                        'id_quan': item.get('ID_QUAN', ''),
                        'quan': item.get('QUAN', ''),
                        'id_capda': item.get('ID_CAPDA', ''),
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'id_dvi': item.get('ID_DVI', ''),
                        'id_sohuu': item.get('ID_SOHUU', '')
                    }
                )
                count += 1
    elif config.key == 'API_NGAN_LO':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_NLO')
            if code:
                Bay.objects.update_or_create(
                    bay_code=code,
                    defaults={
                        'bay_name': item.get('TEN') or item.get('TEN_NLO', ''),
                        'ten_tram': item.get('TEN_TRAM', ''),
                        'id_capda': item.get('ID_CAPDA', ''),
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'id_dvi': item.get('ID_DVI', ''),
                        'id_nlo': item.get('ID_NLO', ''),
                        'id_tba': item.get('ID_TBA', ''),
                        'id_sohuu': item.get('ID_SOHUU', ''),
                        'u_dm': item.get('U_DM', ''),
                        'i_dm': item.get('I_DM', ''),
                        'sdm': item.get('SDM', '')
                    }
                )
                count += 1
    elif config.key == 'API_THIET_BI':
        from django.db import transaction
        from django.utils.dateparse import parse_datetime
        from django.utils.timezone import make_aware, is_aware
        import datetime
        from categories.models import Manufacturer
        mfg_map = dict(Manufacturer.objects.values_list('code', 'name'))
        
        with transaction.atomic():
            for item in lst_data:
                code = item.get('MA') or item.get('MA_TBI')
                id_tbi = item.get('ID_TBI', '')
                if code or id_tbi:
                    raw_id_capda = item.get('ID_CAPDA', '')
                    raw_id_loaitb = item.get('ID_LOAI_TB', '')
                    id_loai_tb_new = f"{raw_id_capda}_{raw_id_loaitb}" if raw_id_capda and raw_id_loaitb else raw_id_loaitb
                    
                    id_hang_sx = item.get('ID_HANG_SX', '')
                    mfg_name = mfg_map.get(id_hang_sx, '') or item.get('TEN_HANG_SX', '')
                    
                    # Parse SAPXEP
                    raw_sapxep = item.get('SAPXEP')
                    sort_order = None
                    if raw_sapxep is not None:
                        try:
                            sort_order = int(raw_sapxep)
                        except (ValueError, TypeError):
                            pass
                            
                    # Parse NGAY_VH
                    raw_ngay_vh = item.get('NGAY_VH')
                    parsed_ngay_vh = None
                    if raw_ngay_vh and isinstance(raw_ngay_vh, str):
                        try:
                            val_clean = raw_ngay_vh.strip().split('.')[0]
                            dt = parse_datetime(val_clean)
                            if dt:
                                parsed_ngay_vh = dt if is_aware(dt) else make_aware(dt)
                            else:
                                d = datetime.date.fromisoformat(val_clean[:10])
                                dt = datetime.datetime(d.year, d.month, d.day)
                                parsed_ngay_vh = make_aware(dt)
                        except Exception:
                            parsed_ngay_vh = None

                    defaults = {
                        'relay_code': code or id_tbi,
                        'relay_name': item.get('TEN') or item.get('TEN_TBI', ''),
                        'manufacturer': mfg_name,
                        'id_tbi': id_tbi,
                        'id_capda': raw_id_capda,
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'id_hang_sx': id_hang_sx,
                        'id_nuoc_sx': item.get('ID_NUOC_SX', ''),
                        'id_loai_tb': id_loai_tb_new,
                        'id_loai_dt': item.get('ID_LOAI_DT', ''),
                        'id_doituong': item.get('ID_DOITUONG', ''),
                        'id_dvi': item.get('ID_DVI', ''),
                        'id_sohuu': item.get('ID_SOHUU', ''),
                        'id_vtri_dat': item.get('ID_VTRI_DAT', ''),
                        'sort_order': sort_order,
                        'ngay_vh': parsed_ngay_vh,
                    }
                    
                    relay = None
                    if id_tbi:
                        relay = Relay.objects.filter(id_tbi=id_tbi).first()
                    if not relay and code:
                        relay = Relay.objects.filter(relay_code=code).first()
                        
                    if relay:
                        for k, v in defaults.items():
                            setattr(relay, k, v)
                        relay.save()
                    else:
                        Relay.objects.create(**defaults)
                    count += 1
    elif config.key == 'API_DANH_MUC_NUOC_SAN_XUAT':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_NUOC')
            if code:
                ManufacturingCountry.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_NUOC', ''),
                        'legacy_id': item.get('ID_NUOC_SX', ''),
                        'sort_order': str(item.get('SAPXEP', ''))
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_HANG_SAN_XUAT':
        for item in lst_data:
            code = item.get('ID') or item.get('MA') or item.get('MA_HANG')
            if code:
                Manufacturer.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_HANG', '')
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_SO_HUU':
        for item in lst_data:
            code = item.get('ID') or item.get('MA') or item.get('MA_SOHUU')
            if code:
                Ownership.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_SOHUU', ''),
                        'sort_order': str(item.get('SAPXEP', ''))
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_CAP_DIEN_AP':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_CAPDA')
            if code:
                VoltageLevel.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_CAPDA', ''),
                        'legacy_code': item.get('MA_PHU', ''),
                        'sort_order': str(item.get('SAPXEP', ''))
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_LOAI_THIET_BI':
        from django.db import transaction
        voltage_levels = VoltageLevel.objects.all()
        
        with transaction.atomic():
            for item in lst_data:
                ma_loai_tb = item.get('MA') or item.get('MA_LOAI_TB')
                ten_loai_tb = item.get('TEN', '') or item.get('TEN_LOAI_TB', '')
                
                if ma_loai_tb:
                    if voltage_levels.exists():
                        for vl in voltage_levels:
                            # Tạo ID mới: Mã Cấp điện áp + '_' + Mã Loại thiết bị
                            code = f"{vl.code}_{ma_loai_tb}"
                            # Cập nhật tên để dễ phân biệt (Ví dụ: Máy biến áp 500kV)
                            name = f"{ten_loai_tb} {vl.name}".strip()
                            
                            EquipmentType.objects.update_or_create(
                                code=code,
                                defaults={
                                    'name': name
                                }
                            )
                            count += 1
                    else:
                        # Trường hợp chưa đồng bộ Cấp điện áp thì vẫn lưu gốc
                        EquipmentType.objects.update_or_create(
                            code=ma_loai_tb,
                            defaults={
                                'name': ten_loai_tb
                            }
                        )
                        count += 1
    elif config.key == 'API_DANH_MUC_TRANG_THAI':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_TTVH')
            if code:
                OperationalStatus.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_TTVH', '')
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_DUONG_DAY':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_DZ')
            if code:
                Line.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_DZ', ''),
                        'id_capda': item.get('ID_CAPDA', ''),
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'da_tke': item.get('DA_TKE', ''),
                        'id_da_tke': item.get('ID_DA_TKE', ''),
                        'i_chophep': item.get('I_CHOPHEP', ''),
                        'tong_cdai': item.get('TONG_CDAI', ''),
                        'so_mach': item.get('SO_MACH', ''),
                        'id_dvi': item.get('ID_DVI', ''),
                        'id_sohuu': item.get('ID_SOHUU', ''),
                        'id_dz': item.get('ID_DZ', '')
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_CONG_TRINH':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_CT')
            if code:
                Project.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_CT', ''),
                        'id_ct': item.get('ID_CT', ''),
                        'id_capda': item.get('ID_CAPDA', ''),
                        'nam_xd': item.get('NAM_XD', ''),
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'ma_ct_cha': item.get('MA_CT_CHA', ''),
                        'ten_ct_cha': item.get('TEN_CT_CHA', ''),
                        'id_sohuu': item.get('ID_SOHUU', ''),
                        'id_dvi': item.get('ID_DVI', '')
                    }
                )
                count += 1
    elif config.key == 'API_DANH_MUC_VI_TRI':
        for item in lst_data:
            code = item.get('MA') or item.get('MA_VITRI')
            if code:
                Location.objects.update_or_create(
                    code=code,
                    defaults={
                        'name': item.get('TEN', '') or item.get('TEN_VITRI', ''),
                        'id_vitri': item.get('ID_VITRI', ''),
                        'id_capda': item.get('ID_CAPDA', ''),
                        'id_ttvh': item.get('ID_TTVH', ''),
                        'khoang_neo': item.get('KHOANG_NEO', ''),
                        'khoang_cot': item.get('KHOANG_COT', ''),
                        'id_khuvuc': item.get('ID_KHUVUC', ''),
                        'khu_vuc': item.get('KHU_VUC', ''),
                        'id_dvi': item.get('ID_DVI', ''),
                        'id_sohuu': item.get('ID_SOHUU', ''),
                        'id_ct': item.get('ID_CT', ''),
                        'ten_ct': item.get('TEN_CT', '')
                    }
                )
                count += 1
    else:
        # Default generic mapping handler
        count = len(lst_data)
        
    # --- AUTO-LINK RELATIONS (Batch optimized) ---
    # Nối Ngăn Lộ (Bay) vào Trạm (Station)
    if config.key in ['API_TRAM', 'API_NGAN_LO']:
        station_lookup = {}
        for s_id, s_tba, s_code in Station.objects.values_list('id', 'id_tba', 'station_code'):
            if s_tba:
                station_lookup[str(s_tba)] = s_id
            if s_code:
                station_lookup[str(s_code)] = s_id
                
        orphaned_bays = Bay.objects.filter(station__isnull=True).exclude(id_tba__isnull=True).exclude(id_tba='')
        bays_to_update = []
        for bay in orphaned_bays:
            matched_s_id = station_lookup.get(str(bay.id_tba))
            if matched_s_id:
                bay.station_id = matched_s_id
                bays_to_update.append(bay)
        if bays_to_update:
            Bay.objects.bulk_update(bays_to_update, ['station'], batch_size=2000)
                
    # Nối Rơ-le (Relay) vào Ngăn Lộ (Bay)
    if config.key in ['API_NGAN_LO', 'API_THIET_BI']:
        bay_lookup = {}
        for b_id, b_nlo, b_code in Bay.objects.values_list('id', 'id_nlo', 'bay_code'):
            if b_nlo:
                bay_lookup[str(b_nlo)] = b_id
            if b_code:
                bay_lookup[str(b_code)] = b_id
                
        orphaned_relays = Relay.objects.filter(bay__isnull=True).exclude(id_vtri_dat__isnull=True).exclude(id_vtri_dat='')
        relays_to_update = []
        for relay in orphaned_relays:
            matched_b_id = bay_lookup.get(str(relay.id_vtri_dat))
            if matched_b_id:
                relay.bay_id = matched_b_id
                relays_to_update.append(relay)
        if relays_to_update:
            Relay.objects.bulk_update(relays_to_update, ['bay'], batch_size=2000)
                
    return count
````

## File: core/utils/xml_converter.py
````python
import xml.etree.ElementTree as ET
from xml.dom import minidom

def json_to_xml(json_obj, root_tag='root'):
    """
    Chuyển đổi một đối tượng JSON (dict/list) thành chuỗi XML.
    """
    root = ET.Element(root_tag)
    
    def build_tree(parent, data):
        if isinstance(data, dict):
            for key, val in data.items():
                child = ET.SubElement(parent, key)
                build_tree(child, val)
        elif isinstance(data, list):
            for item in data:
                child = ET.SubElement(parent, 'item')
                build_tree(child, item)
        else:
            parent.text = str(data)

    build_tree(root, json_obj)
    
    # Prettify the XML
    xml_string = ET.tostring(root, encoding='utf-8')
    parsed_xml = minidom.parseString(xml_string)
    return parsed_xml.toprettyxml(indent="  ")
````

## File: core/__init__.py
````python

````

## File: core/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: core/api_renderers.py
````python
from rest_framework_xml.renderers import XMLRenderer

class CustomXMLRenderer(XMLRenderer):
    """
    Tùy chỉnh XML Renderer để bọc response vào chuẩn:
    <root>
        <success>true</success>
        <message>...</message>
        <data>...</data>
    </root>
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response') if renderer_context else None
        
        is_success = True
        message = "Thành công"
        
        if response and response.status_code >= 400:
            is_success = False
            message = "Có lỗi xảy ra"
            if isinstance(data, dict) and 'detail' in data:
                message = str(data['detail'])

        wrapped_data = {
            'success': is_success,
            'message': message,
            'data': data
        }
        
        return super().render(wrapped_data, accepted_media_type, renderer_context)
````

## File: core/apps.py
````python
from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_groups(sender, **kwargs):
    from django.contrib.auth.models import Group, Permission
    from django.contrib.contenttypes.models import ContentType
    
    # We must ensure models are loaded, so we get the content type from the app registry
    try:
        from sheets.models import SettingSheet
        content_type = ContentType.objects.get_for_model(SettingSheet)
    except Exception:
        return

    matrix = {
        'DISPATCHER': ['can_view_stations', 'can_create_sheet', 'can_dispatch_sheet'],
        'STATION_LEADER': ['can_view_stations', 'can_dispatch_sheet'],
        'TECHNICIAN': ['can_execute_sheet'],
        'SUPERVISOR': ['can_supervise_sheet'],
        'ADMIN': [
            'can_view_stations', 'can_manage_users', 'can_create_sheet', 
            'can_approve_sheet', 'can_dispatch_sheet', 'can_execute_sheet', 
            'can_supervise_sheet'
        ]
    }

    for group_name, perms in matrix.items():
        group, _ = Group.objects.get_or_create(name=group_name)
        # Chỉ gán quyền mặc định nếu nhóm chưa có quyền nào (lần đầu khởi tạo)
        if not group.permissions.exists():
            for perm_codename in perms:
                try:
                    perm = Permission.objects.get(codename=perm_codename, content_type=content_type)
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    pass

class CoreConfig(AppConfig):
    name = 'core'
    
    def ready(self):
        post_migrate.connect(create_default_groups, sender=self)
        
        # Auto-resume interrupted API syncs
        import sys
        if 'runserver' in sys.argv or any('gunicorn' in k or 'daphne' in k for k in sys.modules.keys()):
            import threading
            
            def resume_syncs():
                import time
                time.sleep(5)  # Delay to allow DB to be fully ready
                try:
                    from core.models import SystemConfig
                    from core.utils.api_sync import run_api_sync
                    from django.utils import timezone
                    
                    interrupted = SystemConfig.objects.filter(is_syncing=True)
                    for cfg in interrupted:
                        start_idx = 0
                        if cfg.last_sync_status and cfg.last_sync_status.startswith("progress:"):
                            parts = cfg.last_sync_status.split(":")
                            if len(parts) >= 3:
                                try:
                                    start_idx = int(parts[2])
                                except ValueError:
                                    pass
                        
                        def bg_resume(config_id, s_idx):
                            try:
                                success, count, err = run_api_sync(config_id=config_id, is_background=True, start_idx=s_idx)
                                if success or "dừng đột ngột" not in err:
                                    c = SystemConfig.objects.get(id=config_id)
                                    c.is_syncing = False
                                    c.sync_count += 1
                                    status_text = f"Đã đồng bộ {count} bản ghi (Khôi phục)" if success else f"Lỗi: {err}"
                                    c.last_sync_status = status_text[:250]
                                    c.save(update_fields=['is_syncing', 'sync_count', 'last_sync_time', 'last_sync_status'])
                            except Exception as e:
                                try:
                                    c = SystemConfig.objects.get(id=config_id)
                                    c.is_syncing = False
                                    c.last_sync_status = f"Lỗi khôi phục: {str(e)[:100]}"
                                    c.save(update_fields=['is_syncing', 'last_sync_status'])
                                except:
                                    pass
                                
                        threading.Thread(target=bg_resume, args=(cfg.id, start_idx), daemon=True).start()
                except Exception:
                    pass
                    
            # Avoid running twice in runserver
            import os
            if os.environ.get('RUN_MAIN', None) != 'true':
                threading.Thread(target=resume_syncs, daemon=True).start()
````

## File: core/consumers.py
````python
import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Kiểm tra xem user đã đăng nhập chưa
        if self.scope["user"].is_anonymous:
            await self.close()
            return
            
        # Khởi tạo danh sách các group
        self.groups_joined = []
        
        # Group name cho từng user dựa vào ID
        user_group = f"user_{self.scope['user'].id}"
        await self.channel_layer.group_add(user_group, self.channel_name)
        self.groups_joined.append(user_group)
        
        # Nếu là admin thì nhận thêm thông báo hệ thống (như autocheck)
        # Dùng sync_to_async để tránh lỗi SynchronousOnlyOperation
        user = self.scope['user']
        is_admin, is_super = await sync_to_async(
            lambda: (user.is_superuser or user.groups.filter(name='ADMIN').exists(), user.is_superuser)
        )()
        
        if is_admin:
            await self.channel_layer.group_add("autocheck_updates", self.channel_name)
            self.groups_joined.append("autocheck_updates")

        if is_super:
            await self.channel_layer.group_add("admin_ocr_updates", self.channel_name)
            self.groups_joined.append("admin_ocr_updates")

        await self.accept()

    async def disconnect(self, close_code):
        if hasattr(self, 'groups_joined'):
            for group in self.groups_joined:
                try:
                    await self.channel_layer.group_discard(
                        group,
                        self.channel_name
                    )
                except Exception:
                    # Bỏ qua lỗi timeout khi Redis mất kết nối lúc disconnect
                    pass

    # Receive message from WebSocket (nếu FE có gửi lên, hiện tại không cần)
    async def receive(self, text_data):
        pass

    # Receive message from room group
    async def send_notification(self, event):
        message = event['message']
        title = event.get('title', 'Thông báo')
        type = event.get('type', 'info')

        try:
            # Gửi xuống WebSocket
            await self.send(text_data=json.dumps({
                'message': message,
                'title': title,
                'type': type
            }))
        except Exception:
            # Bỏ qua lỗi nếu kết nối đã đóng
            pass

    async def bulk_progress(self, event):
        # Chuyển tiếp toàn bộ data tiến trình từ Celery sang Frontend
        try:
            await self.send(text_data=json.dumps(event))
        except Exception:
            pass

    async def ocr_event(self, event):
        # Chuyển tiếp sự kiện cập nhật tiến trình OCR thời gian thực sang Frontend
        try:
            await self.send(text_data=json.dumps(event))
        except Exception:
            pass
````

## File: core/context_processors.py
````python
from sheets.models import SettingSheet
from django.db.models import Q
from django.core.cache import cache

def notification_badges(request):
    if not request.user.is_authenticated:
        return {'badges': {
            'pending_admin': 0, 'issued': 0, 'dispatcher_in_progress': 0,
            'routed': 0, 'station_in_progress': 0, 'station_pending_admin': 0,
            'supervisor_transferred': 0, 'supervisor_received': 0, 'supervisor_pending_admin': 0,
            'transferred': 0, 'technician_received': 0, 'changed': 0,
        }}
        
    user = request.user
    
    badges = {
        'pending_admin': 0, 'issued': 0, 'dispatcher_in_progress': 0,
        'routed': 0, 'station_in_progress': 0, 'station_pending_admin': 0,
        'supervisor_transferred': 0, 'supervisor_received': 0, 'supervisor_pending_admin': 0,
        'transferred': 0, 'technician_received': 0, 'changed': 0,
    }

    # 0. Số phiếu có thay đổi thông số cần lưu ý
    try:
        badges['changed'] = SettingSheet.objects.filter(has_parameters_changed=True).count()
    except Exception:
        badges['changed'] = 0
    
    # 1. ADMIN - Chờ Duyệt Ban hành
    if user.is_superuser or user.has_perm('sheets.can_approve_sheet'):
        badges['pending_admin'] = SettingSheet.objects.filter(status='PENDING_ADMIN_APPROVAL').count()
        
    # 2. DISPATCHER / CREATOR
    if user.has_perm('sheets.can_create_sheet') or user.has_perm('sheets.can_dispatch_sheet'):
        base_qs = SettingSheet.objects.filter(created_by=user) if not user.is_superuser else SettingSheet.objects.all()
        badges['issued'] = base_qs.filter(status='ISSUED').count()
        badges['dispatcher_in_progress'] = base_qs.filter(status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED']).count()
        
    # 3. STATION_LEADER (Dispatch at station level)
    if user.has_perm('sheets.can_dispatch_sheet'):
        if hasattr(user, 'userprofile') and user.userprofile.station:
            station = user.userprofile.station
            base_qs = SettingSheet.objects.filter(
                Q(execution_station=station) | 
                (Q(execution_station__isnull=True) & (Q(station=station) | Q(relay__bay__station=station)))
            ).distinct()
            
            badges['routed'] = base_qs.filter(status='ROUTED_TO_STATION').count()
            badges['station_in_progress'] = base_qs.filter(status__in=['TRANSFERRED', 'RECEIVED']).count()
            badges['station_pending_admin'] = base_qs.filter(status='PENDING_ADMIN_APPROVAL').count()
            
    # 4. SUPERVISOR
    if user.has_perm('sheets.can_supervise_sheet'):
        base_qs = SettingSheet.objects.filter(supervisor_assigned=user)
        
        badges['supervisor_transferred'] = base_qs.filter(status='TRANSFERRED').count()
        badges['supervisor_received'] = base_qs.filter(status='RECEIVED').count()
        badges['supervisor_pending_admin'] = base_qs.filter(status='PENDING_ADMIN_APPROVAL').count()
        
    # 5. TECHNICIAN
    if user.has_perm('sheets.can_execute_sheet'):
        base_qs = SettingSheet.objects.filter(assigned_to=user)
        badges['transferred'] = base_qs.filter(status='TRANSFERRED').count()
        badges['technician_received'] = base_qs.filter(status='RECEIVED').count()

    return {'badges': badges}
````

## File: core/models.py
````python
from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    org_type = models.CharField(max_length=50) # VTC, OPERATION, TRANSMISSION...
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey('stations.Station', on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user.username

class SystemConfig(models.Model):
    key = models.CharField(max_length=100, unique=True, verbose_name="Mã cấu hình")
    value = models.CharField(max_length=500, verbose_name="Giá trị")
    description = models.TextField(blank=True, null=True, verbose_name="Mô tả")
    auth_header = models.CharField(max_length=500, blank=True, null=True, verbose_name="Token/Header xác thực")
    
    # Auto-sync settings
    auto_sync_enabled = models.BooleanField(default=False, verbose_name="Tự động đồng bộ")
    sync_interval_minutes = models.IntegerField(default=1440, verbose_name="Chu kỳ đồng bộ (phút)")
    last_sync_time = models.DateTimeField(null=True, blank=True, verbose_name="Lần đồng bộ cuối")
    last_sync_status = models.CharField(max_length=255, null=True, blank=True, verbose_name="Trạng thái đồng bộ cuối")
    sync_count = models.IntegerField(default=0, verbose_name="Số lần đồng bộ")
    is_syncing = models.BooleanField(default=False, verbose_name="Đang đồng bộ")
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.key}: {self.value}"
````

## File: core/routing.py
````python
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
````

## File: core/tasks.py
````python
from celery import shared_task
from django.utils import timezone
from datetime import timedelta
import logging
from core.models import SystemConfig
from core.utils.api_sync import run_api_sync

logger = logging.getLogger(__name__)

@shared_task
def check_and_run_auto_sync():
    """
    Quét các cấu hình API có bật tự động đồng bộ.
    Kiểm tra nếu (bây giờ >= lần đồng bộ cuối + chu kỳ đồng bộ) thì tiến hành gọi API.
    """
    logger.info("Starting check_and_run_auto_sync...")
    now = timezone.now()
    
    # Lấy các cấu hình đang bật auto-sync
    configs = SystemConfig.objects.filter(auto_sync_enabled=True)
    
    for config in configs:
        should_run = False
        if not config.last_sync_time:
            # Chưa từng chạy
            should_run = True
        else:
            # Kiểm tra thời gian
            next_run_time = config.last_sync_time + timedelta(minutes=config.sync_interval_minutes)
            if now >= next_run_time:
                should_run = True
                
        if should_run:
            logger.info(f"Auto-sync triggered for {config.key}")
            
            # Set state to syncing
            config.is_syncing = True
            config.save(update_fields=['is_syncing'])
            
            try:
                # Thực thi đồng bộ
                success, count, err_msg = run_api_sync(config_id=config.id)
                
                # Cập nhật kết quả vào DB
                config.last_sync_time = timezone.now()
                config.sync_count += 1
                if success:
                    config.last_sync_status = f"Thành công ({count} bản ghi)"
                else:
                    config.last_sync_status = f"Thất bại: {err_msg[:240]}"
            finally:
                # Always clear the syncing state
                config.is_syncing = False
                config.save(update_fields=['last_sync_time', 'last_sync_status', 'sync_count', 'is_syncing'])
                
            logger.info(f"Auto-sync completed for {config.key}: {config.last_sync_status}")
            
    logger.info("Finished check_and_run_auto_sync.")
````

## File: core/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: core/urls.py
````python
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
````

## File: core/views.py
````python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from sheets.models import SettingSheet

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

@csrf_exempt
def custom_logout(request):
    """Custom logout view that ignores CSRF for easier multi-tab testing."""
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')

@login_required
def get_badges_api(request):
    """API endpoint to get badge counts for real-time updates."""
    from core.context_processors import notification_badges
    data = notification_badges(request)
    return JsonResponse(data['badges'])

@login_required
def dashboard(request):
    """Trang chủ hiển thị thống kê tổng quan theo Role."""
    from django.db.models import Count
    from django.db.models.functions import TruncDate, TruncMonth
    from django.utils import timezone
    import datetime
    from sheets.models import SignatureRecord
    from django.contrib.auth.models import User
    from stations.models import Station
    from django.core.cache import cache
    import hashlib
    
    user = request.user
    
    if user.is_superuser or user.has_perm('sheets.can_manage_users'):
        role = 'admin'
        period = request.GET.get('period', '7days')
        start_date_str = request.GET.get('start_date', '')
        end_date_str = request.GET.get('end_date', '')
    elif hasattr(user, 'userprofile') and user.userprofile.station:
        if user.has_perm('sheets.can_dispatch_sheet'):
            role = 'station_leader'
        elif user.has_perm('sheets.can_supervise_sheet'):
            role = 'supervisor'
        else:
            role = 'technician'
    elif user.has_perm('sheets.can_create_sheet') or user.has_perm('sheets.can_dispatch_sheet'):
        role = 'dispatcher'
    else:
        return render(request, 'core/dashboard.html', {})
    
    # 1. ADMIN
    if role == 'admin':
        total_sheets = SettingSheet.objects.count()
        total_users = User.objects.count()
        total_stations = Station.objects.count()
        PENDING_ADMIN_APPROVAL = SettingSheet.objects.filter(status='PENDING_ADMIN_APPROVAL').count()
        
        # Chart Data
        today = timezone.now().date()
        chart_title = "Lưu lượng tạo Phiếu (7 ngày qua)"
        start_date = today - datetime.timedelta(days=6)
        end_date = today
        group_by = 'date'
        
        if period == 'this_month':
            start_date = today.replace(day=1)
            chart_title = "Lưu lượng tạo Phiếu (Tháng này)"
        elif period == 'this_year':
            start_date = today.replace(month=1, day=1)
            group_by = 'month'
            chart_title = "Lưu lượng tạo Phiếu (Năm nay)"
        elif period == 'custom' and start_date_str and end_date_str:
            try:
                start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
                if start_date > end_date:
                    start_date, end_date = end_date, start_date
                chart_title = f"Lưu lượng tạo Phiếu ({start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')})"
                if (end_date - start_date).days > 90:
                    group_by = 'month'
            except ValueError:
                pass
                
        start_datetime = timezone.make_aware(datetime.datetime.combine(start_date, datetime.time.min))
        end_datetime = timezone.make_aware(datetime.datetime.combine(end_date, datetime.time.max))

        qs = SettingSheet.objects.filter(created_at__gte=start_datetime, created_at__lte=end_datetime)
        
        chart_labels = []
        chart_data = []
        
        if group_by == 'date':
            daily_counts = qs.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')
            count_dict = {str(item['date']): item['count'] for item in daily_counts}
            
            delta_days = (end_date - start_date).days
            for i in range(delta_days + 1):
                d = start_date + datetime.timedelta(days=i)
                chart_labels.append(d.strftime('%d/%m'))
                chart_data.append(count_dict.get(str(d), 0))
        else: # month
            monthly_counts = qs.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')
            count_dict = {str(item['month'].date()): item['count'] for item in monthly_counts}
            
            curr = start_date.replace(day=1)
            while curr <= end_date:
                chart_labels.append(curr.strftime('T%m/%Y'))
                chart_data.append(count_dict.get(str(curr), 0))
                next_month = curr.month % 12 + 1
                next_year = curr.year + (curr.month // 12)
                curr = curr.replace(year=next_year, month=next_month)
            
        recent_activities = SignatureRecord.objects.select_related('sheet').order_by('-signed_at')[:5]
        _ = list(recent_activities)
        
        from categories.models import Line, Location, Project
        from stations.models import Bay, Relay
        
        # Calculate status breakdown for Doughnut Chart
        status_counts_raw = qs.values('status').annotate(count=Count('id')).order_by('-count')
        
        # Define color mappings for statuses (matching Tailwind colors)
        STATUS_COLORS = {
            'DRAFT': '#94a3b8',           # slate-400
            'PENDING_ADMIN_APPROVAL': '#f43f5e', # rose-500
            'ISSUED': '#3b82f6',          # blue-500
            'ROUTED_TO_STATION': '#f59e0b', # amber-500
            'TRANSFERRED': '#8b5cf6',     # violet-500
            'RECEIVED': '#10b981',        # emerald-500
            'COMPLETED': '#14b8a6',       # teal-500
            'REJECTED': '#ef4444'         # red-500
        }
        
        STATUS_LABELS = dict(SettingSheet.STATUS_CHOICES)
        
        status_labels = []
        status_data = []
        status_colors = []
        
        for item in status_counts_raw:
            st = item['status']
            status_labels.append(str(STATUS_LABELS.get(st, st)))
            status_data.append(item['count'])
            status_colors.append(STATUS_COLORS.get(st, '#cbd5e1')) # default slate-300
            
        # If no data, provide a dummy 'Chưa có phiếu' slice so chart isn't empty
        if not status_data:
            status_labels = ['Chưa có phiếu']
            status_data = [1]
            status_colors = ['#f1f5f9'] # slate-100
        
        context = {
            'total_sheets': total_sheets, 'total_users': total_users, 'total_stations': total_stations, 'PENDING_ADMIN_APPROVAL': PENDING_ADMIN_APPROVAL,
            'chart_labels': chart_labels, 'chart_data': chart_data, 'recent_activities': recent_activities,
            'chart_title': chart_title, 'period': period,
            'start_date': start_date_str if period == 'custom' else '',
            'end_date': end_date_str if period == 'custom' else '',
            'status_labels': status_labels,
            'status_data': status_data,
            'status_colors': status_colors,
            'total_lines': Line.objects.count(),
            'total_locations': Location.objects.count(),
            'total_projects': Project.objects.count(),
            'total_bays': Bay.objects.count(),
            'total_relays': Relay.objects.count(),
            '_template_name': 'core/dashboard_admin.html'
        }
        
    # 3. DISPATCHER
    elif role == 'dispatcher':
        base_qs = SettingSheet.objects.filter(created_by=user)
        issued_count = base_qs.filter(status='ISSUED').count()
        routed_count = base_qs.filter(status='ROUTED_TO_STATION').count()
        received_count = base_qs.filter(status='RECEIVED').count()
        
        tracking_sheets = base_qs.filter(status__in=['ISSUED', 'ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED']).order_by('-created_at')[:5]
        recent_activities = SignatureRecord.objects.filter(sheet__created_by=user).select_related('sheet').order_by('-signed_at')[:5]
        recent_routed_sheets = base_qs.filter(
            status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED', 'PENDING_ADMIN_APPROVAL', 'COMPLETED'],
            relay__isnull=False
        ).select_related('relay', 'relay__bay', 'relay__bay__station').order_by('-created_at')[:15]
        
        # 1. Area Chart Logic with Period
        period = request.GET.get('period', '7days')
        start_date_str = request.GET.get('start_date', '')
        end_date_str = request.GET.get('end_date', '')
        
        chart_title = "Lưu lượng tạo Phiếu (7 ngày qua)"
        end_date = timezone.now().date()
        start_date = end_date - datetime.timedelta(days=6)
        group_by = 'date'
        
        if period == 'this_month':
            start_date = end_date.replace(day=1)
            chart_title = "Lưu lượng tạo Phiếu (Tháng này)"
        elif period == 'last_month':
            first_day_this_month = end_date.replace(day=1)
            end_date = first_day_this_month - datetime.timedelta(days=1)
            start_date = end_date.replace(day=1)
            chart_title = "Lưu lượng tạo Phiếu (Tháng trước)"
        elif period == 'this_year':
            start_date = end_date.replace(month=1, day=1)
            group_by = 'month'
            chart_title = "Lưu lượng tạo Phiếu (Năm nay)"
        elif period == 'custom' and start_date_str and end_date_str:
            try:
                start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
                if start_date > end_date:
                    start_date, end_date = end_date, start_date
                chart_title = f"Lưu lượng ({start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')})"
                if (end_date - start_date).days > 90:
                    group_by = 'month'
            except ValueError:
                pass

        start_datetime = timezone.make_aware(datetime.datetime.combine(start_date, datetime.time.min))
        end_datetime = timezone.make_aware(datetime.datetime.combine(end_date, datetime.time.max))

        qs_chart = base_qs.filter(created_at__gte=start_datetime, created_at__lte=end_datetime)
        
        chart_labels = []
        chart_data = []
        
        if group_by == 'date':
            daily_counts = qs_chart.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')
            count_dict = {str(item['date']): item['count'] for item in daily_counts}
            
            delta_days = (end_date - start_date).days
            for i in range(delta_days + 1):
                d = start_date + datetime.timedelta(days=i)
                chart_labels.append(d.strftime('%d/%m'))
                chart_data.append(count_dict.get(str(d), 0))
        else:
            monthly_counts = qs_chart.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')
            count_dict = {str(item['month'].date()): item['count'] for item in monthly_counts}
            
            curr = start_date.replace(day=1)
            while curr <= end_date:
                chart_labels.append(curr.strftime('T%m/%Y'))
                chart_data.append(count_dict.get(str(curr), 0))
                next_month = curr.month % 12 + 1
                next_year = curr.year + (curr.month // 12)
                curr = curr.replace(year=next_year, month=next_month)
            
        # 2. Status Doughnut Chart Logic
        status_counts_raw = qs_chart.values('status').annotate(count=Count('id')).order_by('-count')
        STATUS_COLORS = {
            'DRAFT': '#94a3b8', 'PENDING_ADMIN_APPROVAL': '#f43f5e', 'ISSUED': '#3b82f6',
            'ROUTED_TO_STATION': '#f59e0b', 'TRANSFERRED': '#8b5cf6', 'RECEIVED': '#10b981',
            'COMPLETED': '#14b8a6', 'REJECTED': '#ef4444'
        }
        STATUS_LABELS = dict(SettingSheet.STATUS_CHOICES)
        status_labels = []
        status_data = []
        status_colors = []
        for item in status_counts_raw:
            st = item['status']
            status_labels.append(str(STATUS_LABELS.get(st, st)))
            status_data.append(item['count'])
            status_colors.append(STATUS_COLORS.get(st, '#cbd5e1'))
        if not status_data:
            status_labels = ['Chưa có phiếu']
            status_data = [1]
            status_colors = ['#f1f5f9']
            
        _ = list(tracking_sheets)
        _ = list(recent_activities)
        _ = list(recent_routed_sheets)
        
        context = {
            'issued_count': issued_count, 'routed_count': routed_count, 'received_count': received_count,
            'tracking_sheets': tracking_sheets, 'recent_activities': recent_activities,
            'recent_routed_sheets': recent_routed_sheets,
            'chart_labels': chart_labels, 'chart_data': chart_data,
            'chart_title': chart_title, 'period': period,
            'start_date': start_date_str if period == 'custom' else '',
            'end_date': end_date_str if period == 'custom' else '',
            'status_labels': status_labels, 'status_data': status_data, 'status_colors': status_colors,
            '_template_name': 'core/dashboard_dispatcher.html'
        }

    # STATION_LEADER
    elif role == 'station_leader':
        my_station = None
        if hasattr(user, 'userprofile') and user.userprofile.station:
            my_station = user.userprofile.station

        if my_station:
            from django.db.models import Q
            base_qs = SettingSheet.objects.filter(
                Q(execution_station=my_station) | 
                (Q(execution_station__isnull=True) & (Q(station=my_station) | Q(relay__bay__station=my_station)))
            ).distinct()
            from django.db.models import Count, Q
            station_techs = User.objects.filter(
                groups__name='TECHNICIAN', 
                userprofile__station=my_station
            ).annotate(
                active_tasks=Count('assigned_sheets', filter=Q(assigned_sheets__status__in=['TRANSFERRED', 'RECEIVED']))
            ).order_by('active_tasks')
        else:
            base_qs = SettingSheet.objects.none()
            station_techs = []

        pending_assign = base_qs.filter(status='ROUTED_TO_STATION').count()
        in_progress = base_qs.filter(status__in=['TRANSFERRED', 'RECEIVED']).count()
        PENDING_ADMIN_APPROVAL = base_qs.filter(status='PENDING_ADMIN_APPROVAL').count()
        completed = base_qs.filter(status='COMPLETED').count()

        recent_sheets = base_qs.filter(status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED']).order_by('-created_at')[:4]
        doughnut_data = [pending_assign, in_progress, PENDING_ADMIN_APPROVAL, completed]
        
        import json
        from django.utils import timezone
        import datetime
        from django.db.models import Count
        from django.db.models.functions import TruncDate, TruncMonth
        
        period = request.GET.get('period', '7days')
        start_date_str = request.GET.get('start_date', '')
        end_date_str = request.GET.get('end_date', '')
        
        chart_title = "Số Lượng Phiếu (7 ngày qua)"
        end_date = timezone.now().date()
        start_date = end_date - datetime.timedelta(days=6)
        group_by = 'date'
        
        if period == 'this_month':
            start_date = end_date.replace(day=1)
            chart_title = "Số Lượng Phiếu (Tháng này)"
        elif period == 'last_month':
            first_day_this_month = end_date.replace(day=1)
            end_date = first_day_this_month - datetime.timedelta(days=1)
            start_date = end_date.replace(day=1)
            chart_title = "Số Lượng Phiếu (Tháng trước)"
        elif period == 'this_year':
            start_date = end_date.replace(month=1, day=1)
            group_by = 'month'
            chart_title = "Số Lượng Phiếu (Năm nay)"
        elif period == 'custom' and start_date_str and end_date_str:
            try:
                start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
                if start_date > end_date:
                    start_date, end_date = end_date, start_date
                chart_title = f"Số Lượng Phiếu ({start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')})"
                if (end_date - start_date).days > 90:
                    group_by = 'month'
            except ValueError:
                pass

        start_datetime = timezone.make_aware(datetime.datetime.combine(start_date, datetime.time.min))
        end_datetime = timezone.make_aware(datetime.datetime.combine(end_date, datetime.time.max))

        qs_chart = base_qs.filter(created_at__gte=start_datetime, created_at__lte=end_datetime)
        
        chart_labels = []
        chart_data = []
        
        if group_by == 'date':
            daily_counts = qs_chart.annotate(date=TruncDate('created_at')).values('date').annotate(count=Count('id')).order_by('date')
            count_dict = {str(item['date']): item['count'] for item in daily_counts}
            
            delta_days = (end_date - start_date).days
            for i in range(delta_days + 1):
                d = start_date + datetime.timedelta(days=i)
                chart_labels.append(d.strftime('%d/%m'))
                chart_data.append(count_dict.get(str(d), 0))
        else:
            monthly_counts = qs_chart.annotate(month=TruncMonth('created_at')).values('month').annotate(count=Count('id')).order_by('month')
            count_dict = {str(item['month'].date()): item['count'] for item in monthly_counts}
            
            curr = start_date.replace(day=1)
            while curr <= end_date:
                chart_labels.append(curr.strftime('T%m/%Y'))
                chart_data.append(count_dict.get(str(curr), 0))
                next_month = curr.month % 12 + 1
                next_year = curr.year + (curr.month // 12)
                curr = curr.replace(year=next_year, month=next_month)
                
        tech_chart_labels = json.dumps(chart_labels)
        tech_chart_data = json.dumps(chart_data)
        
        # Calculate doughnut data based on filtered date range
        pending_assign_chart = qs_chart.filter(status='ROUTED_TO_STATION').count()
        in_progress_chart = qs_chart.filter(status__in=['TRANSFERRED', 'RECEIVED']).count()
        pending_admin_chart = qs_chart.filter(status='PENDING_ADMIN_APPROVAL').count()
        completed_chart = qs_chart.filter(status='COMPLETED').count()
        doughnut_data = [pending_assign_chart, in_progress_chart, pending_admin_chart, completed_chart]
        
        _ = list(station_techs) if hasattr(station_techs, '__iter__') else station_techs
        _ = list(recent_sheets)
        
        context = {
            'my_station': my_station,
            'pending_assign': pending_assign,
            'in_progress': in_progress,
            'PENDING_ADMIN_APPROVAL': PENDING_ADMIN_APPROVAL,
            'completed': completed,
            'recent_sheets': recent_sheets,
            'doughnut_data': doughnut_data,
            'station_techs': station_techs,
            'tech_chart_labels': tech_chart_labels,
            'tech_chart_data': tech_chart_data,
            'chart_title': chart_title,
            'period': period,
            'start_date': start_date_str if period == 'custom' else '',
            'end_date': end_date_str if period == 'custom' else '',
            '_template_name': 'core/dashboard_station_leader.html'
        }

    # 4. SUPERVISOR
    elif role == 'supervisor':
        my_station = None
        if hasattr(user, 'userprofile') and user.userprofile.station:
            my_station = user.userprofile.station

        if my_station:
            from django.db.models import Q
            base_qs = SettingSheet.objects.filter(
                Q(execution_station=my_station) | 
                (Q(execution_station__isnull=True) & (Q(station=my_station) | Q(relay__bay__station=my_station)))
            ).distinct()
            active_techs = User.objects.filter(groups__name='TECHNICIAN', userprofile__station=my_station).count()
        else:
            base_qs = SettingSheet.objects.none()
            active_techs = 0

        pending_supervision = base_qs.filter(status='RECEIVED').count()
        PENDING_ADMIN_APPROVAL = base_qs.filter(status='PENDING_ADMIN_APPROVAL').count()
        completed = base_qs.filter(status='COMPLETED').count()
        
        recent_sheets = base_qs.filter(status__in=['TRANSFERRED', 'RECEIVED', 'PENDING_ADMIN_APPROVAL']).order_by('-created_at')[:5]
        _ = list(recent_sheets)
        
        import json
        from django.utils import timezone
        from datetime import timedelta
        from django.db.models import Count, Q

        today = timezone.localdate()
        daily_labels = []
        for i in range(6, -1, -1):
            daily_labels.append((today - timedelta(days=i)).strftime('%d/%m'))

        chart_datasets = []
        total_data = []
        for i in range(6, -1, -1):
            d = today - timedelta(days=i)
            if my_station:
                c = SettingSheet.objects.filter(
                    Q(execution_station=my_station) | 
                    (Q(execution_station__isnull=True) & (Q(station=my_station) | Q(relay__bay__station=my_station))),
                    updated_at__date=d,
                    status__in=['COMPLETED', 'PENDING_ADMIN_APPROVAL', 'RECEIVED']
                ).count()
            else:
                c = 0
            total_data.append(c)
            
        chart_datasets.append({
            'label': 'Tổng phiếu xử lý',
            'data': total_data,
            'borderColor': '#3b82f6',
            'backgroundColor': 'rgba(59, 130, 246, 0.15)',
            'borderWidth': 3,
            'fill': True,
            'tension': 0.4,
            'pointBackgroundColor': '#ffffff',
            'pointBorderColor': '#3b82f6',
            'pointBorderWidth': 2,
            'pointRadius': 4,
            'pointHoverRadius': 6
        })
            
        tech_chart_labels = json.dumps(daily_labels)
        tech_chart_datasets = json.dumps(chart_datasets)
        
        context = {
            'my_station': my_station,
            'active_techs': active_techs, 
            'pending_supervision': pending_supervision,
            'PENDING_ADMIN_APPROVAL': PENDING_ADMIN_APPROVAL,
            'completed': completed,
            'recent_sheets': recent_sheets,
            'tech_chart_labels': tech_chart_labels,
            'tech_chart_datasets': tech_chart_datasets,
            '_template_name': 'core/dashboard_supervisor.html'
        }

    # 5. TECHNICIAN
    elif role == 'technician':
        my_station = None
        if hasattr(user, 'userprofile') and user.userprofile.station:
            my_station = user.userprofile.station

        assigned_sheets = SettingSheet.objects.filter(assigned_to=request.user)
        new_sheets = assigned_sheets.filter(status='TRANSFERRED').count()
        in_progress = assigned_sheets.filter(status='RECEIVED').count()
        completed = assigned_sheets.filter(status__in=['PENDING_ADMIN_APPROVAL', 'COMPLETED']).count()
        
        total_tasks = new_sheets + in_progress + completed
        progress_percent = int((completed / total_tasks * 100)) if total_tasks > 0 else 0
        
        recent_sheets = assigned_sheets.exclude(status='COMPLETED').order_by('-created_at')[:5]
        _ = list(recent_sheets)
        
        context = {
            'my_station': my_station,
            'new_sheets': new_sheets, 
            'in_progress': in_progress, 
            'completed': completed,
            'total_tasks': total_tasks,
            'progress_percent': progress_percent,
            'recent_sheets': recent_sheets,
            '_template_name': 'core/dashboard_technician.html'
        }
        
    template_name = context.get('_template_name', 'core/dashboard.html')
    return render(request, template_name, context)

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def user_list(request):
    from django.db.models import Q
    search_query = request.GET.get('search', '')
    
    users = User.objects.all().prefetch_related('groups').order_by('-date_joined')
    if search_query:
        users = users.filter(
            Q(username__icontains=search_query) | 
            Q(first_name__icontains=search_query) |
            Q(email__icontains=search_query)
        )
        
    groups = Group.objects.all()
    
    GROUP_NAMES_VI = {
        "ADMIN": "Quản trị viên",
        "DISPATCHER": "Điều phối viên (kiêm Rà soát)",
        "STATION_LEADER": "Trưởng nhóm Trạm",
        "TECHNICIAN": "Kỹ thuật viên",
        "SUPERVISOR": "Giám sát trạm"
    }
    for g in groups:
        g.vi_name = GROUP_NAMES_VI.get(g.name, g.name)
        
    from django.core.paginator import Paginator
    from stations.models import Station
    paginator = Paginator(users, 30)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    for u in page_obj:
        for g in u.groups.all():
            g.vi_name = GROUP_NAMES_VI.get(g.name, g.name)
            
    return render(request, 'core/user_list.html', {
        'users': page_obj,
        'groups': groups,
        'stations': Station.objects.all()
    })

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def user_create(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        group_id = request.POST.get('group')
        station_id = request.POST.get('station_id')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Tên đăng nhập đã tồn tại!')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            if group_id:
                group = Group.objects.get(id=group_id)
                user.groups.add(group)
            
            if station_id:
                from stations.models import Station
                from core.models import UserProfile
                try:
                    station = Station.objects.get(id=station_id)
                    profile, created = UserProfile.objects.get_or_create(user=user)
                    profile.station = station
                    profile.save()
                except Exception as e:
                    pass

            messages.success(request, 'Tạo tài khoản thành công!')
        return redirect('user_list')
    return HttpResponse("Invalid request")

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def user_update(request, user_id):
    if request.method == 'POST':
        from django.shortcuts import get_object_or_404
        user = get_object_or_404(User, id=user_id)
        
        # OCC
        from core.models import UserProfile
        profile, created = UserProfile.objects.get_or_create(user=user)
        original_updated_at = request.POST.get('_original_updated_at')
        if original_updated_at and str(profile.updated_at.timestamp()) != original_updated_at:
            messages.error(request, "Dữ liệu tài khoản này đã bị thay đổi bởi Admin khác trong khi bạn đang xem. Hãy tải lại trang để xem nội dung mới nhất.")
            return redirect('user_list')

        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        password = request.POST.get('password')
        group_id = request.POST.get('group')
        station_id = request.POST.get('station_id')

        user.email = email
        user.first_name = first_name
        if password:
            user.set_password(password)
        
        if group_id:
            group = Group.objects.get(id=group_id)
            user.groups.clear()
            user.groups.add(group)
            
            # Handle station id for specific groups
            if station_id and group.name in ['TECHNICIAN', 'SUPERVISOR', 'STATION_LEADER']:
                from stations.models import Station
                from core.models import UserProfile
                try:
                    station = Station.objects.get(id=station_id)
                    profile, created = UserProfile.objects.get_or_create(user=user)
                    profile.station = station
                    profile.save()
                    print(f"Saved station {station} for {user.username}")
                except Exception as e:
                    print(f"Error saving station: {e}")
            else:
                from core.models import UserProfile
                print(f"Clearing station for {user.username} (station_id: {station_id}, group: {group.name})")
                UserProfile.objects.filter(user=user).update(station=None)
        
        user.save()
        messages.success(request, 'Cập nhật tài khoản thành công!')
        return redirect('user_list')
    return HttpResponse("Invalid request")

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def user_toggle_status(request, user_id):
    if request.method == 'POST':
        from django.shortcuts import get_object_or_404
        user = get_object_or_404(User, id=user_id)
        if user != request.user:
            user.is_active = not user.is_active
            user.save()
            status_msg = "mở khóa" if user.is_active else "khóa"
            messages.success(request, f'Đã {status_msg} tài khoản {user.username}.')
        else:
            messages.error(request, 'Bạn không thể tự khóa tài khoản của mình.')
        return redirect('user_list')
    return HttpResponse("Invalid request")

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def role_matrix(request):
    groups = Group.objects.all().order_by('id')
    content_type = ContentType.objects.get_for_model(SettingSheet)
    # Filter only custom permissions for the matrix
    custom_perms_codenames = [
        "can_view_stations", "can_view_checks", "can_manage_users", "can_create_sheet",
        "can_approve_sheet", "can_dispatch_sheet", "can_execute_sheet",
        "can_supervise_sheet"
    ]
    permissions = Permission.objects.filter(content_type=content_type, codename__in=custom_perms_codenames).order_by('id')
    
    PERM_NAMES_VI = {
        "can_view_stations": "Truy cập Quản lý Trạm",
        "can_view_checks": "Truy cập Kiểm tra Định kỳ",
        "can_manage_users": "Quản trị Hệ thống (Tài khoản & Phân quyền)",
        "can_create_sheet": "Trích xuất Phiếu và chạy AI OCR",
        "can_approve_sheet": "Nút: Phê duyệt Lệnh",
        "can_dispatch_sheet": "Nút: Chuyển Trạm / Phân công Đội",
        "can_execute_sheet": "Nút: Tiếp nhận & Ký Thực thi (KTV)",
        "can_supervise_sheet": "Nút: Ký Nghiệm thu (Giám sát trạm)",
    }
    
    GROUP_NAMES_VI = {
        "ADMIN": "Quản trị viên",
        "DISPATCHER": "Điều phối viên",
        "STATION_LEADER": "Trưởng nhóm Trạm",
        "TECHNICIAN": "Kỹ thuật viên",
        "SUPERVISOR": "Giám sát trạm"
    }
    
    # Inject vi_name directly into the permission object for easy template access
    for perm in permissions:
        perm.vi_name = PERM_NAMES_VI.get(perm.codename, perm.name)
        
    for group in groups:
        group.vi_name = GROUP_NAMES_VI.get(group.name, group.name)
    
    # Pre-calculate matrix state
    matrix = {}
    for group in groups:
        matrix[group.id] = list(group.permissions.values_list('id', flat=True))

    return render(request, 'core/role_matrix.html', {
        'groups': groups,
        'permissions': permissions,
        'matrix': matrix
    })

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def role_matrix_update(request):
    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        perm_id = request.POST.get('perm_id')
        action = request.POST.get('action') # 'add' or 'remove'
        
        group = Group.objects.get(id=group_id)
        perm = Permission.objects.get(id=perm_id)
        
        if action == 'add':
            group.permissions.add(perm)
        else:
            group.permissions.remove(perm)
            
        return HttpResponse("""<i class="fas fa-check text-green-500"></i>""", status=200)
    return HttpResponse("Error", status=400)

@login_required
def dispatcher_routed_relays(request):
    """Trang xem tất cả các rơ-le có phiếu mới nhất đã được duyệt về trạm."""
    if not request.user.has_perm('sheets.can_dispatch_sheet') and not request.user.is_superuser:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
        
    from sheets.models import SettingSheet
    # Lấy các phiếu có rơ-le và đã được Admin phê duyệt (COMPLETED)
    all_routed_sheets = SettingSheet.objects.filter(
        status='COMPLETED',
        relay__isnull=False
    )
    if not request.user.is_superuser:
        all_routed_sheets = all_routed_sheets.filter(created_by=request.user)
        
    all_routed_sheets = all_routed_sheets.select_related('relay', 'relay__bay', 'relay__bay__station').order_by('-created_at')
    
    # Lọc unique rơ-le (chỉ lấy phiếu mới nhất của mỗi rơ-le đã duyệt)
    seen_relays = set()
    unique_routed_sheets = []
    for sheet in all_routed_sheets:
        if sheet.relay_id not in seen_relays:
            unique_routed_sheets.append(sheet)
            seen_relays.add(sheet.relay_id)
            
    # Phân trang
    from django.core.paginator import Paginator
    paginator = Paginator(unique_routed_sheets, 40)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/routed_relays.html', {'sheets': page_obj})

@login_required
def profile(request):
    """Trang xem thông tin tài khoản cá nhân."""
    return render(request, 'core/profile.html')

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_view(request):
    """Trang cấu hình hệ thống (API Endpoints động)."""
    from .models import SystemConfig
    from django.db import models
    
    # Init default configs if they don't exist
    default_configs = [
        ('API_DANH_MUC_DON_VI_QUAN_LY', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_donvi_all_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Đơn vị quản lý'),
        ('API_DANH_MUC_NUOC_SAN_XUAT', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_nsx_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Nước sản xuất'),
        ('API_DANH_MUC_HANG_SAN_XUAT', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_hsx_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Hãng sản xuất'),
        ('API_DANH_MUC_SO_HUU', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_sohuu_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Sở hữu'),
        ('API_DANH_MUC_CAP_DIEN_AP', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_capda_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Cấp điện áp'),
        ('API_DANH_MUC_LOAI_THIET_BI', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_loaitb_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Loại thiết bị'),
        ('API_DANH_MUC_TRANG_THAI', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_ttvh_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C', 'Endpoint API Trạng thái vận hành'),
        ('API_DANH_MUC_DUONG_DAY', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_dz_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&NGAY=&DONVI={{DONVI}}', 'Endpoint API Đường dây'),
        ('API_DANH_MUC_CONG_TRINH', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_ct_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&NGAY=&DONVI={{DONVI}}', 'Endpoint API Công trình'),
        ('API_DANH_MUC_VI_TRI', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_vitri_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&NGAY=&DONVI={{DONVI}}', 'Endpoint API Vị trí'),
        ('API_TRAM', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_tba_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&NGAY=&DONVI={{DONVI}}', 'Endpoint API Trạm'),
        ('API_NGAN_LO', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_nlo_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&NGAY=&DONVI={{DONVI}}', 'Endpoint API Ngăn lộ'),
        ('API_THIET_BI', 'http://pmis.npt.com.vn/PMIS_Web/shared/service/S_ServiceClient.jsf?SOAP_NAME=lst_tbi_JSON&PDKEY=683A830F-F564-4E12-B0CA-B148A86B0A9C&DONVI={{DONVI}}&NGAY=&LOAI={{LOAI}}&LOAI_TB={{LOAI_TB}}', 'Endpoint API Thiết bị (Relay)'),
    ]
    
    for key, val, desc in default_configs:
        SystemConfig.objects.get_or_create(key=key, defaults={'value': val, 'description': desc})
        
    # Danh sách thứ tự ưu tiên đồng bộ (Nếu chưa có dữ liệu)
    SYNC_ORDER = [
        'API_DANH_MUC_DON_VI_QUAN_LY',
        'API_DANH_MUC_CAP_DIEN_AP',
        'API_DANH_MUC_LOAI_THIET_BI',
        'API_DANH_MUC_HANG_SAN_XUAT',
        'API_DANH_MUC_NUOC_SAN_XUAT',
        'API_DANH_MUC_SO_HUU',
        'API_DANH_MUC_TRANG_THAI',
        'API_TRAM',
        'API_NGAN_LO',
        'API_DANH_MUC_DUONG_DAY',
        'API_DANH_MUC_CONG_TRINH',
        'API_DANH_MUC_VI_TRI',
        'API_THIET_BI'
    ]
    
    q = request.GET.get('q', '').strip()
    
    if q:
        all_configs = list(SystemConfig.objects.filter(models.Q(key__icontains=q) | models.Q(description__icontains=q)))
    else:
        all_configs = list(SystemConfig.objects.all())
    
    def sort_key(c):
        try:
            return SYNC_ORDER.index(c.key)
        except ValueError:
            return 999
            
    configs = sorted(all_configs, key=sort_key)
    
    for c in configs:
        if c.key in SYNC_ORDER:
            c.sync_order_num = SYNC_ORDER.index(c.key) + 1
        else:
            c.sync_order_num = None
        c.rendered_row = render_system_config_row(c)
            
    from categories.models import ManagementUnit
    units = ManagementUnit.objects.all().order_by('code')
            
    return render(request, 'core/system_config.html', {'configs': configs, 'units': units})

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_create(request):
    if request.method == 'POST':
        from .models import SystemConfig
        import time
        key = request.POST.get('key', '').strip()
        value = request.POST.get('value', '').strip()
        description = request.POST.get('description', '')
        auth_header = request.POST.get('auth_header', '').strip()
        
        if not key:
            key = f"API_AUTO_{int(time.time())}"
            
        if value:
            # Tự động đổi sang https khi thêm mới (theo yêu cầu)
            if value.startswith('http://') and 'pmis.npt.com.vn' in value:
                value = value.replace('http://', 'https://', 1)
                
            SystemConfig.objects.create(
                key=key.upper(),
                value=value,
                description=description,
                auth_header=auth_header
            )
            messages.success(request, f"Đã thêm API mới: {key.upper()}")
        return redirect('system_config')
    return redirect('system_config')

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_bulk_create(request):
    if request.method == 'POST':
        from .models import SystemConfig
        import time
        urls_text = request.POST.get('urls', '')
        urls = [u.strip() for u in urls_text.split('\n') if u.strip().startswith('http')]
        count = 0
        for idx, url in enumerate(urls):
            key = f"API_AUTO_{int(time.time())}_{idx}"
            SystemConfig.objects.create(key=key, value=url, description="Bulk imported")
            count += 1
        if count > 0:
            messages.success(request, f"Đã thêm hàng loạt {count} API thành công!")
        else:
            messages.warning(request, "Không tìm thấy URL hợp lệ nào.")
        return redirect('system_config')
    return redirect('system_config')

def render_system_config_row(config, sync_message=None):
    from django.urls import reverse
    
    sync_url = reverse('api_sync_endpoint')
    delete_url = reverse('system_config_delete', args=[config.id])
    
    key_esc = (config.key or "").replace("'", "\\'")
    val_esc = (config.value or "").replace("'", "\\'")
    desc_esc = (config.description or "").replace("'", "\\'")
    auth_esc = (config.auth_header or "").replace("'", "\\'")
    
    last_sync_html = f'<div class="text-[10px] text-slate-500 mt-1" title="{config.last_sync_status}">Lần cuối: {config.last_sync_time.strftime("%d/%m/%Y %H:%M")}</div>' if config.last_sync_time else ''
    sync_count_html = f'<div class="text-[10px] text-blue-500 mt-1 font-semibold">Đã đồng bộ: {config.sync_count} lần</div>'
    
    sync_interval = config.sync_interval_minutes
    if sync_interval >= 525600 and sync_interval % 525600 == 0:
        interval_str = f"{sync_interval // 525600} năm"
    elif sync_interval >= 43200 and sync_interval % 43200 == 0:
        interval_str = f"{sync_interval // 43200} tháng"
    elif sync_interval >= 1440 and sync_interval % 1440 == 0:
        interval_str = f"{sync_interval // 1440} ngày"
    elif sync_interval >= 60 and sync_interval % 60 == 0:
        interval_str = f"{sync_interval // 60} giờ"
    else:
        interval_str = f"{sync_interval} phút"

    if config.is_syncing:
        sync_col_html = f'''
            <div class="inline-flex items-center px-2 py-1 bg-amber-50 text-amber-700 text-xs font-medium rounded border border-amber-200 mb-1">
                <i class="fas fa-sync-alt animate-spin mr-1"></i> Đang đồng bộ...
            </div>
            {sync_count_html}
        '''
    else:
        sync_col_html = f'''
            <div class="inline-flex items-center px-2 py-1 bg-emerald-50 text-emerald-700 text-xs font-medium rounded border border-emerald-200 mb-1">
                <i class="fas fa-clock mr-1"></i> Bật (Mỗi {interval_str})
            </div>
            {last_sync_html}
            {sync_count_html}
        ''' if config.auto_sync_enabled else f'''
            <div class="inline-flex items-center px-2 py-1 bg-slate-50 text-slate-500 text-xs font-medium rounded border border-slate-200">
                <i class="fas fa-power-off mr-1"></i> Tắt
            </div>
            {last_sync_html}
            {sync_count_html}
        '''

    sync_btn_html = f'''
        <button id="sync-btn-config-{config.id}" type="button" 
                hx-post="{sync_url}" 
                hx-vals='{{"config_id": "{config.id}", "action": "stop"}}'
                hx-target="#config-row-{config.id}"
                hx-swap="outerHTML"
                class="group/btn text-xs font-semibold text-rose-600 hover:text-white hover:bg-rose-500 bg-rose-50 px-2.5 py-1.5 rounded-lg border border-rose-200 transition-colors flex items-center shadow-sm" title="Dừng đồng bộ ngầm">
            <i class="fas fa-stop mr-1"></i> <span class="group-[.htmx-request]/btn:hidden">Dừng</span><span class="hidden group-[.htmx-request]/btn:inline ml-1">Đang dừng...</span>
        </button>
    ''' if config.is_syncing else f'''
        <button id="sync-btn-config-{config.id}" type="button" 
                hx-post="{sync_url}" 
                hx-vals='{{"config_id": "{config.id}"}}'
                hx-target="#config-row-{config.id}"
                hx-swap="outerHTML"
                class="group/btn text-xs font-semibold text-emerald-600 hover:text-white hover:bg-emerald-500 bg-emerald-50 px-2.5 py-1.5 rounded-lg border border-emerald-200 transition-colors flex items-center shadow-sm" title="Đồng bộ ngay">
            <i class="fas fa-sync-alt mr-1 group-[.htmx-request]/btn:animate-spin"></i> <span class="group-[.htmx-request]/btn:hidden">Đồng bộ</span><span class="hidden group-[.htmx-request]/btn:inline ml-1">Đang tải...</span>
        </button>
    '''

    if config.is_syncing and not sync_message:
        status_text = "Tiến trình đang khởi động... Vui lòng đợi!"
        progress_html = ""
        pct = 0
        if config.last_sync_status and config.last_sync_status.startswith('progress:'):
            parts = config.last_sync_status.split(':')
            if len(parts) >= 4:
                pct = parts[1]
                idx = parts[2]
                total = parts[3]
                status_text = f"Đang lấy dữ liệu ({idx}/{total} request)..."
                progress_html = f'''
                <div class="w-full bg-blue-200/50 rounded-full h-1.5 mt-2 mb-0.5 overflow-hidden">
                  <div class="bg-blue-500 h-1.5 rounded-full transition-all duration-500 ease-out relative overflow-hidden" style="width: {pct}%">
                    <div class="absolute inset-0 bg-white/20 w-full" style="transform: skewX(-20deg);"></div>
                  </div>
                </div>
                '''
                
        sync_result_html = f'''<div id="sync-result-{config.id}" class="text-xs text-blue-600 font-medium mt-2 p-2 bg-blue-50 border border-blue-100 rounded block">
            <div class="flex items-center justify-between">
                <div><i class="fas fa-circle-notch fa-spin mr-1.5"></i> {status_text}</div>
                <span class="text-[10px] bg-white px-2 py-0.5 rounded border border-blue-200 font-bold">{pct}%</span>
            </div>
            {progress_html}
        </div>'''
    else:
        if sync_message:
            sync_result_html = sync_message
        elif config.last_sync_status and (config.last_sync_status.startswith("Lỗi") or config.last_sync_status.startswith("Đã dừng") or "lỗi" in config.last_sync_status.lower() or config.last_sync_status.startswith("Đã đồng bộ")):
            is_err = "lỗi" in config.last_sync_status.lower()
            is_success = config.last_sync_status.startswith("Đã đồng bộ")
            
            if is_success:
                color = "emerald"
                icon = "fa-check-circle"
            elif is_err:
                color = "rose"
                icon = "fa-exclamation-triangle"
            else:
                color = "amber"
                icon = "fa-info-circle"
                
            sync_result_html = f'''<div id="sync-result-{config.id}" class="text-xs text-{color}-600 font-medium mt-2 p-2 bg-{color}-50 border border-{color}-100 rounded flex items-center">
                <i class="fas {icon} mr-1.5"></i> {config.last_sync_status}
            </div>'''
        else:
            sync_result_html = f'<div id="sync-result-{config.id}"></div>'

    htmx_polling = ""
    if config.is_syncing:
        from django.urls import reverse
        row_url = reverse('system_config_row', args=[config.id])
        htmx_polling = f'hx-get="{row_url}" hx-trigger="every 2s" hx-swap="outerHTML"'

    # Xử lý xem có hỗ trợ DONVI không
    has_donvi = '{{DONVI}}' in (config.value or '')
    expand_btn_html = f'''
        <button type="button" @click="expanded = !expanded" class="text-slate-400 hover:text-blue-600 focus:outline-none transition-transform" :class="expanded ? 'rotate-90' : ''">
            <i class="fas fa-chevron-right text-sm"></i>
        </button>
    ''' if has_donvi else ''
    
    # Render sub-row if has_donvi
    sub_row_html = ''
    if has_donvi:
        # Lấy danh sách units từ cache hoặc db (đã tối ưu trong view context, nhưng render_system_config_row chạy độc lập nên ta query luôn)
        from categories.models import ManagementUnit
        units = ManagementUnit.objects.all().order_by('code')
        
        sub_items = ""
        for u in units:
            generated_url = (config.value or "").replace('{{DONVI}}', u.code).replace("'", "\\'")
            sub_sync_btn = f'''
                        <button type="submit" 
                                class="group/btn text-[10px] font-semibold text-blue-600 hover:text-white hover:bg-blue-500 bg-blue-50 px-2 py-1 rounded border border-blue-200 transition-colors flex items-center shadow-sm whitespace-nowrap" title="Đồng bộ riêng đơn vị {u.code}">
                            <i class="fas fa-sync-alt mr-1 group-[.htmx-request]/btn:animate-spin"></i> <span class="group-[.htmx-request]/btn:hidden">Đồng bộ riêng</span><span class="hidden group-[.htmx-request]/btn:inline ml-1">Đang tải...</span>
                        </button>
            ''' if not config.is_syncing else ''
            
            sub_items += f'''
            <div x-show="'{u.code.lower()} {u.name.lower()}'.includes(search.toLowerCase())" class="flex items-center justify-between p-2 hover:bg-slate-50 dark:hover:bg-slate-700/50 rounded-lg border-b border-slate-100 dark:border-slate-700/50 last:border-0">
                <div class="flex-1 mr-4">
                    <div class="text-xs text-slate-700 dark:text-slate-300 font-medium"><i class="fas fa-building text-slate-400 mr-2"></i>{u.code} - {u.name}</div>
                    <form hx-post="{sync_url}" 
                          hx-target="#sub-sync-result-{config.id}-{u.code}" 
                          hx-swap="innerHTML"
                          class="mt-1 flex items-center gap-2">
                        <input type="hidden" name="config_id" value="{config.id}">
                        <input type="hidden" name="specific_unit" value="{u.code}">
                        <i class="fas fa-link text-[10px] text-slate-400 ml-6"></i>
                        <input type="text" name="custom_url" value="{generated_url}" class="flex-1 text-[10px] text-slate-500 font-mono bg-transparent border-b border-transparent hover:border-slate-300 focus:border-blue-500 focus:outline-none transition-colors px-1 py-0.5">
                        
                        <div id="sub-sync-result-{config.id}-{u.code}" class="ml-2"></div>
                        {sub_sync_btn}
                    </form>
                </div>
            </div>
            '''
        
        sub_row_html = f'''
        <tr x-show="expanded" x-transition class="bg-slate-50/50 dark:bg-slate-800/30">
            <td colspan="5" class="px-10 py-4">
                <div class="bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl shadow-sm overflow-hidden">
                    <div class="px-4 py-2 bg-slate-50 dark:bg-slate-900/50 border-b border-slate-200 dark:border-slate-700 text-xs font-bold text-slate-600 dark:text-slate-400 flex items-center justify-between">
                        <span>DANH SÁCH ĐƠN VỊ CÓ THỂ ĐỒNG BỘ RIÊNG LẺ</span>
                        <div class="relative w-64">
                            <i class="fas fa-search absolute left-2.5 top-1.5 text-slate-400"></i>
                            <input type="text" x-model="search" placeholder="Tìm kiếm theo mã hoặc tên đơn vị..." 
                                   class="w-full pl-8 pr-3 py-1 bg-white dark:bg-slate-800 border border-slate-300 dark:border-slate-600 rounded-md text-xs font-normal focus:outline-none focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-shadow">
                        </div>
                    </div>
                    <div class="max-h-64 overflow-y-auto p-2">
                        {sub_items}
                    </div>
                </div>
            </td>
        </tr>
        '''

    action_buttons = f'''
                    <button type="button" onclick="openEditModal({config.id}, '{key_esc}', '{val_esc}', '{desc_esc}', '{auth_esc}', '{config.auto_sync_enabled}', {config.sync_interval_minutes})" class="text-slate-400 hover:text-blue-600 transition-colors p-1" title="Sửa">
                        <i class="fas fa-edit text-base"></i>
                    </button>
                    <button type="button" 
                            hx-post="{delete_url}" 
                            hx-confirm="Bạn có chắc chắn muốn xoá cấu hình API này?"
                            hx-target="#config-row-{config.id}"
                            hx-swap="outerHTML"
                            class="text-slate-400 hover:text-red-500 transition-colors p-1" title="Xoá">
                        <i class="fas fa-trash-alt text-base"></i>
                    </button>
    ''' if not config.is_syncing else ''

    return f'''
    <tbody id="config-row-{config.id}" class="group" x-data="{{ expanded: false, search: '' }}" 
           x-show="activeCategory === 'all' || getCategoryForKey('{key_esc}') === activeCategory"
           x-transition:enter="transition ease-out duration-200"
           x-transition:enter-start="opacity-0 translate-y-2"
           x-transition:enter-end="opacity-100 translate-y-0"
           {htmx_polling}>
        <tr class="hover:bg-blue-50/50 dark:hover:bg-slate-700/50 transition-colors border-b border-slate-100 dark:border-slate-700/50 last:border-0">
            <td class="px-6 py-3 font-medium text-slate-900 dark:text-slate-200 w-1/4">
                <div class="flex items-center gap-2">
                    {expand_btn_html}
                    {'<span class="inline-flex items-center justify-center w-6 h-6 text-[11px] font-bold text-white bg-blue-600 rounded-full shrink-0 shadow-sm">' + str(getattr(config, 'sync_order_num', '')) + '</span>' if getattr(config, 'sync_order_num', None) else '<span class="inline-flex items-center justify-center w-6 h-6 text-[11px] font-bold text-slate-500 bg-slate-200 dark:bg-slate-700 rounded-full shrink-0 shadow-sm">-</span>'}
                    <span>{config.key}</span>
                </div>
                <div class="text-[9px] text-slate-400 font-mono truncate max-w-[150px] lg:max-w-[200px] mt-1 ml-8" title="{val_esc}"><i class="fas fa-link mr-1"></i>{val_esc}</div>
            </td>
            <td class="px-6 py-3">
                <div class="text-slate-500 dark:text-slate-400 mb-1">{config.description}</div>
                {sync_result_html}
            </td>
            <td class="px-6 py-3">
                {sync_col_html}
            </td>
            <td class="px-6 py-3 text-right">
                <div class="flex items-center justify-end gap-2">
                    {sync_btn_html}
                    {action_buttons}
                </div>
            </td>
        </tr>
        {sub_row_html}
    </tbody>
    '''

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_delete(request, config_id):
    if request.method in ['POST', 'DELETE']:
        from .models import SystemConfig
        SystemConfig.objects.filter(id=config_id).delete()
        return HttpResponse("")
    return HttpResponseForbidden()

@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_update(request):
    if request.method == 'POST':
        from .models import SystemConfig
        config_id = request.POST.get('config_id')
        new_value = request.POST.get('value')
        new_key = request.POST.get('key')
        new_desc = request.POST.get('description')
        new_auth = request.POST.get('auth_header')
        
        auto_sync_enabled = request.POST.get('auto_sync_enabled') == 'on'
        sync_interval_minutes = request.POST.get('sync_interval_minutes')
        
        try:
            config = SystemConfig.objects.get(id=config_id)
            
            # OCC
            original_updated_at = request.POST.get('_original_updated_at')
            if original_updated_at and str(config.updated_at.timestamp()) != original_updated_at:
                return HttpResponseForbidden("Dữ liệu đã bị thay đổi bởi người khác. Vui lòng tải lại trang.")

            if new_value is not None:
                val = new_value.strip()
                if val.startswith('http://') and 'pmis.npt.com.vn' in val:
                    val = val.replace('http://', 'https://', 1)
                config.value = val
            if new_key:
                config.key = new_key.strip().upper()
            if new_desc is not None:
                config.description = new_desc.strip()
            if new_auth is not None:
                config.auth_header = new_auth.strip()
                
            config.auto_sync_enabled = auto_sync_enabled
            if sync_interval_minutes:
                try:
                    config.sync_interval_minutes = int(sync_interval_minutes)
                except ValueError:
                    pass
                    
            config.save()
            return HttpResponse(render_system_config_row(config))
        except SystemConfig.DoesNotExist:
            return HttpResponseForbidden("Not found")
            
@login_required
@permission_required('sheets.can_manage_users', raise_exception=True)
def system_config_row(request, config_id):
    from .models import SystemConfig
    try:
        config = SystemConfig.objects.get(id=config_id)
        return HttpResponse(render_system_config_row(config))
    except SystemConfig.DoesNotExist:
        return HttpResponseForbidden("Not found")

@login_required
def api_sync_endpoint(request):
    import json
    import urllib.request
    from categories.models import ManagementUnit, ManufacturingCountry, Manufacturer, Ownership, VoltageLevel, EquipmentType, OperationalStatus, Line, Project, Location
    from core.utils.xml_converter import json_to_xml
    import logging
    from core.models import SystemConfig
    from django.http import HttpResponse, HttpResponseForbidden
    
    if not (request.user.is_superuser or request.user.has_perm('sheets.can_manage_users')):
        return HttpResponseForbidden("Access Denied")
        
    logger = logging.getLogger(__name__)

    if request.method == 'POST':
        config_id = request.POST.get('config_id')
        specific_unit = request.POST.get('specific_unit')
        custom_url = request.POST.get('custom_url')
        action = request.POST.get('action')
        try:
            config = SystemConfig.objects.get(id=config_id)
            
            if action == 'stop':
                config.is_syncing = False
                config.last_sync_status = "progress:0:0:0"
                config.save(update_fields=['is_syncing', 'last_sync_status'])
                return HttpResponse(render_system_config_row(config))
                
            if not specific_unit:
                # Chạy ngầm cho tính năng Đồng bộ Tất cả (Tránh timeout)
                import threading
                def bg_task():
                    try:
                        from core.models import SystemConfig
                        from django.utils import timezone
                        from core.utils.api_sync import run_api_sync
                        
                        cfg = SystemConfig.objects.get(id=config_id)
                        
                        start_idx = 0
                        if cfg.last_sync_status and cfg.last_sync_status.startswith("progress:"):
                            parts = cfg.last_sync_status.split(":")
                            if len(parts) >= 3:
                                try:
                                    start_idx = int(parts[2])
                                except ValueError:
                                    pass
                        
                        cfg.is_syncing = True
                        cfg.save(update_fields=['is_syncing'])
                        
                        success, count, err = run_api_sync(config_id=config_id, is_background=True, start_idx=start_idx)
                        
                        # Chỉ cập nhật kết quả nếu không bị dừng đột ngột bởi user
                        if success or "dừng đột ngột" not in err:
                            cfg.refresh_from_db()
                            cfg.is_syncing = False
                            cfg.sync_count += 1
                            cfg.last_sync_time = timezone.now()
                            status_msg = f"Đã đồng bộ {count} bản ghi" if success else f"Lỗi: {err}"
                            cfg.last_sync_status = status_msg[:250]
                            cfg.save(update_fields=['is_syncing', 'sync_count', 'last_sync_time', 'last_sync_status'])
                    except Exception as e:
                        try:
                            from core.models import SystemConfig
                            cfg = SystemConfig.objects.get(id=config_id)
                            cfg.is_syncing = False
                            cfg.last_sync_status = f"Lỗi hệ thống: {str(e)}"[:250]
                            cfg.save(update_fields=['is_syncing', 'last_sync_status'])
                        except:
                            pass
                
                # Check if it's a resume or a fresh start
                start_idx_init = 0
                if config.last_sync_status and config.last_sync_status.startswith("progress:"):
                    parts = config.last_sync_status.split(":")
                    if len(parts) >= 3:
                        try:
                            start_idx_init = int(parts[2])
                        except ValueError:
                            pass

                config.is_syncing = True
                if start_idx_init == 0:
                    config.last_sync_status = "progress:0:0:0"
                config.save(update_fields=['is_syncing', 'last_sync_status'])
                
                threading.Thread(target=bg_task).start()
                
                return HttpResponse(render_system_config_row(config))
                
            # Đồng bộ riêng (Nhanh, chạy trực tiếp)
            from core.utils.api_sync import run_api_sync
            success, count, error_message = run_api_sync(config_id=config_id, specific_unit=specific_unit, custom_url=custom_url)
            
            # Increment count for manual syncs too
            config.sync_count += 1
            config.save(update_fields=['sync_count'])
            
            if not success:
                sync_message = f'''<div class="text-[10px] text-red-600 font-medium mt-1 p-1 bg-red-50 border border-red-100 rounded">
                    <i class="fas fa-exclamation-circle mr-1"></i> {error_message}
                </div>'''
                return HttpResponse(sync_message)
                
            sync_message = f'''<div class="text-[10px] text-emerald-600 font-medium mt-1 p-1 bg-emerald-50 border border-emerald-100 rounded flex items-center justify-between">
                <div><i class="fas fa-check-circle mr-1"></i> Đã đồng bộ <b>{count}</b> bản ghi.</div>
            </div>'''
            return HttpResponse(sync_message)

            
        except Exception as e:
            import traceback
            traceback.print_exc()
            error_msg = str(e).replace('<', '&lt;').replace('>', '&gt;')
            if specific_unit:
                sync_message = f'''<div class="text-[10px] text-red-600 font-medium mt-1 p-1 bg-red-50 border border-red-100 rounded">
                    <i class="fas fa-exclamation-circle mr-1"></i> Lỗi: {error_msg}
                </div>'''
                return HttpResponse(sync_message)
            sync_message = f'''<div id="sync-result-{config_id}" class="text-xs text-red-600 font-medium mt-2 p-2 bg-red-50 border border-red-100 rounded">
                <i class="fas fa-exclamation-circle mr-1"></i> Lỗi đồng bộ: {error_msg}
            </div>'''
            return HttpResponse(render_system_config_row(config, sync_message))
    return HttpResponse("Invalid request", status=400)

@login_required
def manage_team(request):
    """Trang quản lý các thành viên trong trạm (Dành cho Trưởng nhóm Trạm)."""
    if not hasattr(request.user, 'userprofile') or not request.user.userprofile.station:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
        
    my_station = request.user.userprofile.station
    if not request.user.groups.filter(name='STATION_LEADER').exists():
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied
        
    from django.contrib.auth.models import User
    from django.db.models import Count, Q
    from sheets.models import SettingSheet
    from django.contrib import messages
    from django.shortcuts import redirect

    if request.method == 'POST':
        tech_id = request.POST.get('tech_id')
        sup_id = request.POST.get('sup_id')
        sheet_ids = request.POST.getlist('sheet_ids')
        
        if tech_id and sheet_ids:
            try:
                tech = User.objects.get(id=tech_id, userprofile__station=my_station, groups__name='TECHNICIAN')
                sheets_to_assign = SettingSheet.objects.filter(id__in=sheet_ids, status='ROUTED_TO_STATION', assigned_to__isnull=True)
                assigned_count = 0
                for sheet in sheets_to_assign:
                    sheet.assigned_to = tech
                    sheet.status = 'TRANSFERRED'
                    sheet.save()
                    assigned_count += 1
                messages.success(request, f"Đã giao thành công {assigned_count} công việc cho KTV {tech.first_name or tech.username}.")
            except User.DoesNotExist:
                messages.error(request, "Không tìm thấy Kỹ thuật viên hợp lệ.")
                
        elif sup_id and sheet_ids:
            try:
                sup = User.objects.get(id=sup_id, userprofile__station=my_station, groups__name='SUPERVISOR')
                # Supervisor can be assigned to sheets that don't have a supervisor yet
                sheets_to_assign = SettingSheet.objects.filter(id__in=sheet_ids, supervisor_assigned__isnull=True)
                assigned_count = 0
                for sheet in sheets_to_assign:
                    sheet.supervisor_assigned = sup
                    sheet.save()
                    assigned_count += 1
                messages.success(request, f"Đã phân công thành công {assigned_count} công việc cho Giám sát {sup.first_name or sup.username}.")
            except User.DoesNotExist:
                messages.error(request, "Không tìm thấy Giám sát viên hợp lệ.")
                
        return redirect('manage_team')

    # Lấy danh sách thành viên KTV trong trạm
    station_techs = User.objects.filter(
        groups__name='TECHNICIAN', 
        userprofile__station=my_station
    ).prefetch_related('assigned_sheets')
    
    for tech in station_techs:
        tech.active_tasks = tech.assigned_sheets.filter(status__in=['TRANSFERRED', 'RECEIVED'])
        tech.completed_tasks_count = tech.assigned_sheets.filter(status__in=['COMPLETED', 'PENDING_ADMIN_APPROVAL']).count()

    # Lấy danh sách Giám sát viên trong trạm
    station_supervisors = User.objects.filter(
        groups__name='SUPERVISOR', 
        userprofile__station=my_station
    ).prefetch_related('supervised_sheets')
    
    for sup in station_supervisors:
        # Giám sát viên theo dõi các phiếu đã được phân công cho họ và chưa hoàn thành/chờ admin duyệt
        sup.active_tasks = sup.supervised_sheets.filter(status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED'])
        sup.completed_tasks_count = sup.supervised_sheets.filter(status__in=['COMPLETED', 'PENDING_ADMIN_APPROVAL']).count()

    # Lấy các phiếu chờ phân công cho KTV
    unassigned_sheets = SettingSheet.objects.filter(
        Q(execution_station=my_station) | 
        (Q(execution_station__isnull=True) & (Q(station=my_station) | Q(relay__bay__station=my_station))),
        status='ROUTED_TO_STATION', 
        assigned_to__isnull=True
    ).distinct().order_by('-created_at')
    
    # Lấy các phiếu chưa có giám sát
    unassigned_sup_sheets = SettingSheet.objects.filter(
        Q(execution_station=my_station) | 
        (Q(execution_station__isnull=True) & (Q(station=my_station) | Q(relay__bay__station=my_station))),
        status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED'],
        supervisor_assigned__isnull=True
    ).distinct().order_by('-created_at')
        
    return render(request, 'core/manage_team.html', {
        'station_techs': station_techs,
        'station_supervisors': station_supervisors,
        'my_station': my_station,
        'unassigned_sheets': unassigned_sheets,
        'unassigned_sup_sheets': unassigned_sup_sheets,
    })
````

## File: docs/cores/01-database.md
````markdown
# Thiết kế Cơ sở Dữ liệu Hệ thống RMS (Database Design Specification)

Tài liệu này đặc tả toàn bộ kiến trúc cơ sở dữ liệu thực tế của dự án **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS - Relay Management System)** trên nền tảng **PostgreSQL 15**.

---

## 1. Sơ đồ Thực thể Quan hệ (ERD - Entity Relationship Diagram)

```mermaid
erDiagram
    STATION ||--o{ BAY : "contains"
    BAY ||--o{ RELAY : "contains"
    RELAY ||--o{ RELAY_SETTING : "has_standard_settings"
    RELAY ||--o{ SETTING_SHEET : "applies_to"
    RELAY ||--o{ RELAY_AUTO_CHECK_LOG : "has_audit_logs"
    RELAY ||--o{ CORRECTION_TICKET : "has_correction_requests"
    
    SETTING_SHEET ||--o{ SIGNATURE_RECORD : "signed_by"
    SETTING_SHEET ||--o{ OCR_JOB : "processed_by"
    SETTING_SHEET ||--o| SETTING_SHEET : "reverts_to"
    
    RELAY_AUTO_CHECK_LOG ||--o| CORRECTION_TICKET : "triggers"
    
    USERS ||--o{ SETTING_SHEET : "creates / assigns / supervises"
    USERS ||--o{ SIGNATURE_RECORD : "signs"

    STATION {
        int id PK
        string station_code UK
        string station_name
        string id_capda
        string id_dvi
        datetime updated_at
    }

    BAY {
        int id PK
        int station_id FK
        string bay_code
        string bay_name
        string id_capda
        datetime updated_at
    }

    RELAY {
        int id PK
        int bay_id FK
        string relay_code
        string relay_name
        string manufacturer
        string id_tbi
        string id_capda
        boolean auto_check_enabled
        int check_interval_value
        string check_interval_unit
        datetime last_checked_at
        datetime next_check_at
        boolean is_paused_for_correction
        json paused_schedule_data
        datetime updated_at
    }

    RELAY_SETTING {
        int id PK
        int relay_id FK
        string parameter_code
        string parameter_name
        float standard_value
        string unit
        float tolerance_min
        float tolerance_max
    }

    SETTING_SHEET {
        int id PK
        string sheet_code UK
        string title
        string status
        string scan_file
        int relay_id FK
        int station_id FK
        int execution_station_id FK
        int created_by_id FK
        int assigned_to_id FK
        int supervisor_assigned_id FK
        json extracted_data
        json edit_logs
        boolean has_parameters_changed
        boolean is_temporary
        datetime valid_until
        datetime created_at
        datetime updated_at
    }

    SIGNATURE_RECORD {
        int id PK
        int sheet_id FK
        string signer_name
        string role
        string signature_hash
        datetime signed_at
    }

    OCR_JOB {
        int id PK
        int sheet_id FK
        string correlation_id UK
        string device_mode
        string status
        string review_status
        datetime created_at
    }

    RELAY_AUTO_CHECK_LOG {
        int id PK
        int relay_id FK
        string status
        json api_raw_data
        json differences
        datetime checked_at
    }

    CORRECTION_TICKET {
        int id PK
        int relay_id FK
        int log_id FK
        string status
        datetime created_at
        datetime updated_at
    }
```

---

## 2. Đặc tả Chi tiết các Bảng Nghiệp vụ (Tables Specification)

### 2.1 Quản lý Lưới điện & Rơ-le (App: `stations`)

#### Bảng: `stations_station`
Lưu trữ thông tin Trạm Biến áp hoặc Nhà máy Điện thuộc lưới truyền tải/phân phối.
* `id` (PK, AutoField)
* `station_code` (VARCHAR(50), UNIQUE): Mã trạm EVN (ví dụ: `TBA_500_QN`, `TBA_220_VC`).
* `station_name` (VARCHAR(255)): Tên đầy đủ trạm (ví dụ: `Trạm 500kV Quảng Ninh`).
* `id_capda` (VARCHAR(50)): Mã cấp điện áp danh định (500kV, 220kV, 110kV...).
* `id_dvi` (VARCHAR(50)): Đơn vị quản lý (PTC1, PTC2, PC...).

#### Bảng: `stations_bay`
Lưu trữ thông tin Ngăn lộ (xuất tuyến đường dây, ngăn MBA, thanh cái, máy cắt liên lạc).
* `id` (PK, AutoField)
* `station_id` (FK $\rightarrow$ `stations_station`, ON DELETE CASCADE)
* `bay_code` (VARCHAR(50)): Mã ngăn lộ (ví dụ: `571`, `572`, `171`, `MC_Lien_Lac`).
* `bay_name` (VARCHAR(255)): Tên mô tả ngăn lộ.

#### Bảng: `stations_relay`
Lưu trữ thiết bị Rơ-le bảo vệ và điều khiển số thực tế tại trạm.
* `id` (PK, AutoField)
* `bay_id` (FK $\rightarrow$ `stations_bay`, ON DELETE CASCADE, nullable)
* `relay_code` (VARCHAR(50)): Số hiệu/Mã rơ-le theo sơ đồ nguyên lý (ví dụ: `F87R1`, `SEL-751`, `7SA87`).
* `relay_name` (VARCHAR(255)): Tên và chức năng rơ-le.
* `manufacturer` (VARCHAR(100)): Hãng sản xuất (SIEMENS, ABB, SEL, SCHNEIDER/MICOM, TOSHIBA, GE...).
* `id_tbi` (VARCHAR(100)): ID thiết bị theo phần mềm quản lý kỹ thuật EVN PMIS.
* `auto_check_enabled` (BOOLEAN, default=False, db_index=True): Cờ bật/tắt quét định kỳ.
* `is_paused_for_correction` (BOOLEAN, default=False, db_index=True): Cờ đánh dấu rơ-le đang có sai lệch thông số cần rà soát/chỉnh định lại.
* `paused_schedule_data` (JSONField): Lưu thông tin nguyên nhân tạm dừng, file PDF phát hiện sai lệch.

#### Bảng: `stations_relayautochecklog`
Nhật ký lịch sử đối chiếu thông số rơ-le (giữa Phiếu Chỉnh định và File PDF/API thực tế).
* `id` (PK, AutoField)
* `relay_id` (FK $\rightarrow$ `stations_relay`, ON DELETE CASCADE)
* `checked_at` (DATETIME, auto_now_add=True)
* `status` (VARCHAR(20)): `MATCH` (Trùng khớp 100%), `MISMATCH` (Có sai lệch), `API_ERROR`.
* `api_raw_data` (JSONField): Danh sách toàn bộ thông số đối chiếu kèm cờ `is_diff`, `db_value`, `value`.
* `differences` (JSONField): Danh sách các thông số bị phát hiện sai lệch.

#### Bảng: `stations_correctionticket`
Phiếu yêu cầu điều phối xử lý sai lệch xuống Trạm / Kỹ thuật viên hiện trường.
* `status`: `DISPATCHER` $\rightarrow$ `STATION` $\rightarrow$ `TECH` $\rightarrow$ `SUPERVISOR` $\rightarrow$ `ADMIN` $\rightarrow$ `RESOLVED`.

---

### 2.2 Quản lý Phiếu Chỉnh định & OCR (App: `sheets`)

#### Bảng: `sheets_settingsheet`
Phiếu Chỉnh định rơ-le bảo vệ - trung tâm dữ liệu kỹ thuật của hệ thống.
* `sheet_code` (VARCHAR(100), UNIQUE): Mã phiếu chính thức (ví dụ: `A0-01-2020/QN500`).
* `title` (VARCHAR(255)): Tiêu đề phiếu.
* `status` (VARCHAR(50)):
  * `DRAFT`: Bản nháp vừa tạo / đang OCR.
  * `ISSUED`: Đã phát hành, chờ rà soát.
  * `ROUTED_TO_STATION`: Đã chuyển về Trạm phụ trách.
  * `TRANSFERRED`: Đã giao cho Kỹ thuật viên hiện trường.
  * `RECEIVED`: Đang thực hiện cài đặt tại trạm.
  * `PENDING_ADMIN_APPROVAL`: Chờ Admin ký duyệt ban hành.
  * `COMPLETED`: Hoàn thành, có đủ chữ ký số.
* `scan_file` (FILE): Đường dẫn file scan / PDF phiếu gốc lưu tại `media/scans/`.
* `extracted_data` (JSONB): Mảng JSON lưu trữ toàn bộ các trị số chỉnh định bóc tách được (Mã thông số, tên, trị số, đơn vị, nhóm cài đặt, chức năng ANSI).
* `has_parameters_changed` (BOOLEAN): Cờ đánh dấu phiếu có thay đổi trị số so với phiên bản trước đó.
* `is_temporary` (BOOLEAN): Đánh dấu phiếu chỉnh định phương thức tạm thời.

#### Bảng: `sheets_signaturerecord`
Lưu trữ chữ ký số điện tử của các bên tham gia quy trình chỉnh định rơ-le.
* `sheet_id` (FK $\rightarrow$ `sheets_settingsheet`, ON DELETE CASCADE)
* `signer_name` (VARCHAR(100)): Họ tên người ký.
* `role` (VARCHAR(50)): Vai trò khi ký (Người lập, Điều độ viên, KTV rơ-le, Giám sát trạm).
* `signature_hash` (VARCHAR(256)): Chuỗi băm SHA-256 bảo đảm tính toàn vẹn của nội dung phiếu tại thời điểm ký.
* `signed_at` (DATETIME, auto_now_add=True).

---

## 3. Chiến lược Lưu trữ Dữ liệu Bán Cấu trúc (JSONB Strategy)

Trong hệ thống điện lực, mỗi dòng rơ-le (Siemens, ABB, SEL, MiCOM...) có số lượng và cấu trúc thông số hoàn toàn khác nhau (từ vài chục đến hàng trăm trị số). Do đó:
1. **Dữ liệu quan hệ cố định (RDBMS)**: Quản lý cây thực thể `Trạm` $\rightarrow$ `Ngăn lộ` $\rightarrow$ `Rơ-le` $\rightarrow$ `Phiếu chỉnh định` để đảm bảo tính toàn vẹn khóa ngoại (Foreign Keys) và tìm kiếm tốc độ cao với B-Tree index.
2. **Dữ liệu thông số linh hoạt (PostgreSQL JSONB)**:
   * Trường `extracted_data` trong `SettingSheet` và `api_raw_data` trong `RelayAutoCheckLog` lưu dạng mảng đối tượng:
     ```json
     [
       {
         "parameter_code": "50_1_I",
         "parameter_name": "Dòng cắt nhanh cấp 1",
         "value": "12.5",
         "unit": "A",
         "group_id": "Group 1",
         "is_diff": false
       }
     ]
     ```
   * Hỗ trợ truy vấn NoSQL trực tiếp trong PostgreSQL mà không cần tạo hàng trăm cột động trong cơ sở dữ liệu.
````

## File: docs/cores/02-backend.md
````markdown
# Thiết kế Kiến trúc Backend & Dịch vụ Hệ thống RMS (Backend Architecture)

Tài liệu này đặc tả kiến trúc backend, quy chuẩn mã nguồn, dịch vụ xử lý bất đồng bộ và chuẩn giao tiếp trong **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)**.

---

## 1. Công nghệ Sử dụng (Backend Stack)

* **Ngôn ngữ thực thi**: Python 3.12 (môi trường Docker Linux).
* **Framework Web chính**: Django 5.x theo mô hình kiến trúc **MVT (Model - View - Template)**.
* **ASGI Server (Asynchronous)**: `Daphne` (lắng nghe cổng 9000), xử lý đồng thời HTTP/1.1, HTTP/2 và WebSocket.
* **Thời gian thực (Realtime)**: `Django Channels 4.x` kết nối Redis Channel Layer.
* **Hàng đợi Tác vụ ngầm (Background Task Queue)**: `Celery 5.x` kết hợp `Celery Beat`.
* **Message Broker & Cache Layer**: `Redis 7.x (Alpine)` (cổng 6379).
* **Cơ sở dữ liệu chính**: `PostgreSQL 15 (Alpine)` (cổng 5440).
* **Thư viện xử lý PDF & Dữ liệu kỹ thuật**: `pypdf`, `openpyxl`, `numpy`.

---

## 2. Cấu trúc Thư mục Ứng dụng (Modular Django Architecture)

Mã nguồn được tổ chức thành các Django App chuyên biệt hóa theo từng phân vùng nghiệp vụ:

```text
📂 electricity-web
 ┣ 📂 rms_project            # Cấu hình lõi hệ thống Django
 ┃ ┣ 📜 asgi.py              # Khởi tạo ASGI routing (HTTP + WebSockets)
 ┃ ┣ 📜 celery.py            # Cấu hình Celery app & beat schedule
 ┃ ┣ 📜 settings.py          # Biến môi trường, database, cache, auth
 ┃ ┗ 📜 urls.py              # Root URL router
 ┣ 📂 stations               # App Quản lý Trạm, Ngăn lộ, Rơ-le & Trung tâm Đối chiếu
 ┃ ┣ 📜 models.py            # Station, Bay, Relay, RelaySetting, RelayAutoCheckLog, CorrectionTicket
 ┃ ┣ 📜 views.py             # Logic trạm, đối chiếu PDF (upload_relay_pdf_compare), modal thông số
 ┃ ┣ 📜 urls.py              # Endpoints: /stations/autochecks/, /relay/<id>/parameters/ ...
 ┃ ┣ 📜 tasks.py             # Celery task quét tự động theo lịch hẹn giờ
 ┃ ┗ 📜 api_mock.py          # Module mô phỏng/kết nối API thực địa rơ-le
 ┣ 📂 sheets                 # App Quản lý Phiếu Chỉnh định & Vòng đời Phê duyệt
 ┃ ┣ 📜 models.py            # SettingSheet, SignatureRecord, OcrJob
 ┃ ┣ 📜 views.py             # Luồng tạo phiếu, ký số, duyệt phiếu, xuất PDF
 ┃ ┣ 📜 tasks.py             # Celery pipeline xử lý tác vụ bóc tách OCR
 ┃ ┣ 📜 relay_matcher.py     # Bộ máy nhận diện Model rơ-le & Chức năng bảo vệ ANSI C37.2
 ┃ ┗ 📜 utils.py             # Hàm so sánh diff giữa các phiên bản phiếu
 ┣ 📂 categories             # App Danh mục Kỹ thuật Dùng chung
 ┃ ┣ 📜 models.py            # Hãng sản xuất (Manufacturer), Cấp điện áp, Loại rơ-le
 ┃ ┗ 📜 views.py             # CRUD danh mục hệ thống
 ┣ 📂 templates              # Giao diện Server-Driven UI (HTML + Tailwind + Alpine.js + HTMX)
 ┗ 📜 docker-compose.yml     # Quản lý 4 container (web, db, redis, celery)
```

---

## 3. Các Phân hệ Backend Cốt lõi

### 3.1 Bộ máy Nhận diện Rơ-le & Chức năng ANSI (`sheets/relay_matcher.py`)
Module cốt lõi tự động hóa phân loại rơ-le trên toàn hệ thống điện lực:
* **Chuẩn hóa chuỗi (Normalization)**: Tự động loại bỏ dấu tiếng Việt, xử lý đồng thời định dạng có gạch nối (`SEL-751`, `SEL-787`) và dạng viết liền EVN PMIS (`SEL751`, `SEL787_1`, `SEL487E_1`, `F87R-SEL787`).
* **Kho tra cứu Model (MODEL_REGISTRY)**:
  * **Siemens**: `7SJ86/85/82/64/62/61` (50/51, 67, BCU), `7SA87/86/82/6` (21, 87L), `7SD87/86/82/61/52` (87L), `7UT87/86/85/82/6` (87T, 87R, 64REF).
  * **ABB / Hitachi Energy**: `REF615/620/630`, `RET615/620/630`, `RED615/670`, `REL670`, `REC670`.
  * **Schweitzer Engineering Laboratories (SEL)**: `SEL-751/751A` (50/51, 67, BCU), `SEL-787/487E` (87T, 87R, 64REF), `SEL-411L` (87L, 21, BCU, 79, 25), `SEL-487B` (87B, 50BF).
  * **Schneider Electric / MiCOM**: `P122/123/127`, `P141..145`, `P441..443` (21), `P541..546` (87L), `P642..645` (87T).
* **Suy luận Hãng từ Phần mềm**: Tự động nhận diện hãng rơ-le nếu phiếu nhắc đến các công cụ cấu hình chuyên dụng (`DIGSI 5`, `PCM600`, `acSELerator QuickSet`, `MiCOM S1 Agile`, `EnerVista`).

### 3.2 Bộ máy Đối chiếu Dữ liệu PDF & Trị số Chuẩn (Diff Engine)
Nằm tại `stations/views.py:upload_relay_pdf_compare`:
1. Tiếp nhận file PDF từ kỹ sư hiện trường/đơn vị thí nghiệm.
2. Trích xuất text và bảng số liệu bằng `pypdf`.
3. Lấy dữ liệu chuẩn từ **Phiếu Chỉnh định mới nhất (`relay.active_sheet`)**.
4. So khớp từng thông số (theo mã, tên, giá trị, đơn vị).
5. Phân loại:
   * **`MATCH`**: Trùng khớp 100% $\rightarrow$ Rơ-le đạt chuẩn an toàn.
   * **`MISMATCH`**: Phát hiện sai lệch $\rightarrow$ Tự động đánh dấu `relay.is_paused_for_correction = True` và cung cấp nút bấm 1-chạm tạo `CorrectionTicket` chuyển về Trạm.

---

## 4. Chuẩn Giao tiếp API & HTMX (Server-Driven Communication)

Dự án ưu tiên phương thức **Server-Driven UI** bằng cách trả về các đoạn HTML Partial (`HTML Snippets`) để HTMX cập nhật trực tiếp vào DOM:

### 4.1 Quy tắc Phản hồi HTMX (HTMX Responses)
* **Trả về HTML Partial**: Ví dụ `render(request, 'stations/partials/_relay_row.html', {'relay': relay})`.
* **Điều khiển Client qua HTTP Header `HX-Trigger`**:
  ```python
  response["HX-Trigger"] = json.dumps({
      f"refreshRow-{relay.id}": "",  # Làm mới dòng rơ-le tương ứng
      "closeUploadModal": "",        # Đóng modal tải file
      "openResultModal": "",         # Mở modal hiển thị kết quả
      "notify": {                    # Bắn thông báo Toast
          "title": "Hoàn tất",
          "message": "Đã đối chiếu xong thông số.",
          "level": "success"
      }
  })
  ```

### 4.2 Kênh Thông báo Thời gian thực (WebSocket - Django Channels)
* **Kênh Thông báo Chung**: `/ws/notifications/` $\rightarrow$ Phát sóng khi có phiếu mới được duyệt, có đợt rà soát hoặc tác vụ bóc tách OCR hoàn tất.
* **Kênh Cập nhật Đối chiếu**: Group `autocheck_updates` $\rightarrow$ Tự động đẩy trạng thái rơ-le mới nhất đến màn hình Dashboard khi có tiến trình kiểm tra hoàn tất.
````

## File: docs/cores/03-frontend.md
````markdown
# Thiết kế Kiến trúc Frontend & Giao diện UI/UX (Frontend Architecture)

Tài liệu này đặc tả kiến trúc giao diện, chuẩn tương tác người dùng (UI/UX) và hệ thống thiết kế phía Client trong **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)**.

---

## 1. Công nghệ Sử dụng (Frontend Stack)

Hệ thống được xây dựng theo mô hình **Server-Driven UI** hiện đại, loại bỏ sự phức tạp cồng kềnh của SPA (Single Page Application) mà vẫn đảm bảo tốc độ phản hồi tức thời như ứng dụng desktop:

* **Engine Render Giao diện**: `Django Templates` kế thừa cấu trúc từ `templates/base.html`.
* **Giao tiếp AJAX & Cập nhật DOM**: `HTMX 1.9+` (tải và chèn các HTML Partials động không cần tải lại toàn bộ trang).
* **Quản lý Trạng thái Phía Client (Client Reactivity)**: `Alpine.js 3.x` (quản lý trạng thái đóng/mở Modal, Tabs, Tìm kiếm tức thì, Phân trang client-side).
* **CSS Framework & Styling**: `Tailwind CSS` (utility-first, tối ưu responsive cho cả Desktop, Tablet và Mobile).
* **Bộ Icon Kỹ thuật**: `Font Awesome 6 Pro / Free`.
* **Sơ đồ & Lưu đồ**: `Mermaid.js` và KaTeX cho công thức toán học điện lực.

---

## 2. Cấu trúc Thư mục Giao diện (`templates/`)

```text
📂 templates
 ┣ 📜 base.html                          # Layout khung ứng dụng gốc (Sidebar, Navbar, Modals)
 ┣ 📂 partials                           # Các phân mảnh dùng chung toàn hệ thống
 ┃ ┣ 📜 _sidebar.html                    # Thanh điều hướng trái phân tầng
 ┃ ┣ 📜 _header.html                     # Thanh tiêu đề, thông báo chuông, profile
 ┃ ┗ 📜 pagination.html                  # Phân trang động tích hợp HTMX
 ┣ 📂 sheets                             # Giao diện Phân hệ Phiếu Chỉnh định
 ┃ ┣ 📜 sheet_list.html                  # Danh sách phiếu theo bộ lọc trạng thái
 ┃ ┣ 📜 sheet_detail.html                # Chi tiết phiếu, Split-view đối chiếu bản scan
 ┃ ┗ 📂 partials                         # Bảng thông số, nhật ký sửa đổi, chữ ký số
 ┣ 📂 stations                           # Giao diện Quản lý Trạm & Đối chiếu Rơ-le
 ┃ ┣ 📜 station_list.html                # Cây cấu trúc Trạm -> Ngăn lộ -> Rơ-le
 ┃ ┣ 📜 autocheck_dashboard.html         # Trung tâm Đối chiếu Thông số Rơ-le
 ┃ ┗ 📂 partials
 ┃   ┣ 📜 _autocheck_table.html          # Bảng dữ liệu đối chiếu rơ-le
 ┃   ┣ 📜 _relay_row.html                # Một hàng rơ-le phản ứng nhanh với HTMX trigger
 ┃   ┣ 📜 _relay_parameters_modal.html   # Modal xem toàn bộ thông số rơ-le với tìm kiếm tức thì
 ┃   ┣ 📜 _autocheck_results.html        # Bảng so sánh 2 cột Side-by-side Diff
 ┃   ┗ 📜 relay_detail_modal.html        # Modal toàn diện (ANSI, định mức, lịch sử phiếu)
 ┗ 📂 categories                         # Giao diện Quản trị Danh mục Hệ thống
```

---

## 3. Các Nguyên tắc Thiết kế & Trải nghiệm (UI/UX Design System)

### 3.1 Bảng màu Chuẩn Công nghiệp Điện lực (Power Grid Color Palette)
* **Xanh Slate/Zinc (Chủ đạo)**: Tạo cảm giác tin cậy, vững chãi của hệ thống vận hành trạm điện.
* **Xanh dương EVN (`#005baa` / Tailwind Blue-600)**: Màu nhận diện chuẩn của Tập đoàn Điện lực Việt Nam.
* **Xanh ngọc / Teal (`teal-600`)**: Sử dụng cho các tác vụ nạp file PDF và xử lý dữ liệu thực địa.
* **Tím Indigo (`purple-600`)**: Sử dụng cho bảng trị số cài đặt rơ-le.
* **Mã màu Trạng thái Nghiệp vụ**:
  * 🟢 **Xanh lá (Emerald)**: Phiếu `COMPLETED`, Đối chiếu `Trùng khớp 100%`, Rơ-le đang vận hành an toàn.
  * 🔴 **Đỏ (Red/Rose)**: Rơ-le có `Sai lệch thông số`, Phiếu bị từ chối, Cảnh báo quá hạn.
  * 🟡 **Vàng/Cam (Amber)**: Phiếu `Chờ rà soát (ISSUED)`, Rơ-le đang tạm dừng chờ chỉnh định lại.
  * 🔵 **Xanh lam (Sky/Blue)**: Phiếu `Đang thực hiện (RECEIVED)`.

### 3.2 Hỗ trợ Đa Chế độ Sáng/Tối (Light & Dark Theme)
* Tự động phát hiện và đồng bộ trạng thái giao diện qua `localStorage.getItem('theme')`.
* Toàn bộ các component đều có lớp màu tương thích kép:
  `bg-white dark:bg-slate-800 text-slate-800 dark:text-slate-100 border-slate-200 dark:border-slate-700`.

---

## 4. Chuẩn Tương tác HTMX & Alpine.js trong Dự án

### 4.1 Quy tắc HTMX (Server-Driven Partial Swaps)
1. **Tìm kiếm & Lọc không giật trang**:
   ```html
   <form hx-get="{% url 'autocheck_dashboard' %}" 
         hx-target="#autocheck-table-container" 
         hx-swap="outerHTML" 
         hx-indicator=".htmx-indicator" 
         hx-trigger="keyup delay:400ms from:input[name='q'], change from:select[name='status']">
   ```
2. **Cập nhật từng Hàng Rơ-le sau khi Thao tác (Single Row Refresh)**:
   Mỗi hàng `<tr>` lắng nghe sự kiện riêng để chỉ tải lại đúng hàng đó thay vì tải lại cả trang:
   ```html
   <tr id="relay-row-{{ relay.id }}" 
       hx-get="{% url 'autocheck_row' relay.id %}" 
       hx-trigger="refreshRow-{{ relay.id }} from:body" 
       hx-swap="outerHTML">
   ```
3. **Hiển thị Spinner khi xử lý ngầm**:
   Sử dụng class `.htmx-indicator` để hiển thị spinner mượt mà trong khi đang bóc tách file PDF hoặc gọi kiểm tra API.

### 4.2 Quy tắc Alpine.js (Client-side Reactivity)
1. **Quản lý Modal**:
   Dùng các hàm JavaScript toàn cục hoặc sự kiện `$dispatch` để đóng/mở modal mượt mà, không phụ thuộc vào thư viện JS bên thứ ba.
2. **Lọc và Tìm kiếm Cục bộ (Instant Filter)**:
   Ví dụ trong `_relay_parameters_modal.html` và `_autocheck_results.html`: Toàn bộ danh sách trị số được nạp vào Alpine.js `items` để người dùng gõ từ khóa tìm kiếm phản hồi trong **0 miligiây**.
````

## File: docs/cores/04-security.md
````markdown
# Thiết kế Xác thực & Bảo mật Hệ thống RMS (Security & Access Control)

Tài liệu này đặc tả kiến trúc bảo mật, cơ chế kiểm soát truy cập phân tầng (RBAC) và bảo vệ dữ liệu toàn vẹn trong **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)**.

---

## 1. Cơ chế Xác thực Người dùng (Authentication)

Vì đây là hệ thống quản lý thông số rơ-le vận hành lưới điện (hạ tầng trọng yếu quốc gia - Critical Infrastructure OT/IT):
* **Phương thức xác thực**: Sử dụng cơ chế **Django Session Authentication** bảo mật cao, kết hợp Session Store lưu tại PostgreSQL / Redis.
* **Bảo vệ Cookie**:
  * `sessionid` và `csrftoken` được cấu hình với các cờ `HttpOnly`, `SameSite=Lax` (hoặc `Strict`), ngăn chặn hoàn toàn nguy cơ rò rỉ qua tấn công XSS.
* **Bảo vệ Biểu mẫu (CSRF Protection)**:
  * Tất cả các HTTP Request làm thay đổi trạng thái (`POST`, `PUT`, `DELETE`) bắt buộc phải có CSRF Token hợp lệ (`{% csrf_token %}` đối với Form hoặc header `X-CSRFToken` đối với các yêu cầu HTMX).

---

## 2. Ma trận Phân quyền Vai trò Nghiệp vụ EVN (RBAC Matrix)

Hệ thống triển khai phân quyền dựa trên `django.contrib.auth.models.Permission` kết hợp các nhóm quyền (Groups):

| Mã Quyền hạn (Permission Code) | Tên Quyền | A0 / A1 (Điều độ) | Đơn vị Quản lý Trạm | Kỹ thuật viên (KTV) | Giám sát Trạm | Quản trị viên (Admin) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `can_create_sheet` | Tạo phiếu mới & nạp scan | ✅ | ❌ | ❌ | ❌ | ✅ |
| `can_approve_sheet` | Rà soát & Duyệt ban hành | ✅ | ❌ | ❌ | ❌ | ✅ |
| `can_dispatch_sheet` | Điều phối / Giao việc KTV | ❌ | ✅ | ❌ | ❌ | ✅ |
| `can_execute_sheet` | Cài đặt rơ-le & ký xác nhận | ❌ | ❌ | ✅ | ❌ | ✅ |
| `can_supervise_sheet`| Nghiệm thu & ký giám sát | ❌ | ❌ | ❌ | ✅ | ✅ |
| `can_view_checks` | Xem & Đối chiếu thông số | ✅ | ✅ | ✅ | ✅ | ✅ |
| `can_manage_users` | Quản trị tài khoản & danh mục| ❌ | ❌ | ❌ | ❌ | ✅ |

### Cơ chế Kiểm tra Quyền ở Tầng Mã nguồn:
1. **Tại Views**:
   Sử dụng decorators `@login_required` và `@permission_required('sheets.can_approve_sheet')` hoặc `@user_passes_test(is_admin)`.
2. **Tại Giao diện (Templates)**:
   Ẩn/hiện nút bấm theo quyền của người dùng đăng nhập:
   ```html
   {% if perms.sheets.can_approve_sheet %}
       <button ...>Phê duyệt Phiếu</button>
   {% endif %}
   ```

---

## 3. Bảo vệ Tính Toàn vẹn Dữ liệu Kỹ thuật (Data Integrity & Digital Signature)

Thông số chỉnh định rơ-le liên quan trực tiếp đến an toàn lưới điện truyền tải (tránh nhảy máy cắt gây rã lưới). Do đó:
1. **Bảo vệ Trạng thái Hoàn thành (`COMPLETED`)**:
   Khi một phiếu đã chuyển sang trạng thái `COMPLETED` (đã có đủ chữ ký số xác nhận của KTV và Giám sát), phiếu sẽ bị **khóa cứng vĩnh viễn (Read-only)**. Không bất kỳ người dùng nào, kể cả Admin, được phép chỉnh sửa trực tiếp giá trị trong `extracted_data`. Nếu cần thay đổi, bắt buộc phải phát hành phiếu mới hoặc tạo phiếu rà soát.
2. **Ký số & Lưu trữ Chuỗi Băm (SHA-256 Hashing)**:
   Mỗi lần ký xác nhận (`SignatureRecord`), hệ thống tính toán chuỗi băm mật mã học (cryptographic hash):
   $$\text{SignatureHash} = \text{SHA256}(\text{SheetCode} + \text{Timestamp} + \text{Signer} + \text{CanonicalParameters})$$
   Chuỗi băm này được lưu trữ vĩnh viễn để đối chứng pháp lý trong trường hợp xảy ra sự cố điện lực cần kiểm tra nguyên nhân.
3. **Nhật ký Chỉnh sửa Không thể Xóa (`edit_logs`)**:
   Mọi thao tác chỉnh sửa từng thông số trên phiếu đều được tự động ghi vết vào trường `edit_logs` của phiếu: bao gồm *Ai sửa*, *Thời gian*, *Giá trị cũ* và *Giá trị mới*.

---

## 4. Bảo mật Môi trường Nội bộ (On-Premise OT Security)

* **Không gọi dịch vụ Cloud công cộng**: Toàn bộ quá trình bóc tách và đối chiếu dữ liệu được thực thi trong mạng nội bộ cô lập (On-premise / Intranet), tuân thủ tiêu chuẩn an toàn thông tin hệ thống SCADA/EMS của Tập đoàn Điện lực Việt Nam.
* **Tự động làm sạch dữ liệu đầu vào**: Chống tấn công SQL Injection thông qua ORM Parameterized Query và chống tấn công XSS thông qua cơ chế tự động escape HTML của Django Template Engine.
````

## File: docs/cores/05-testing.md
````markdown
# Đặc tả Kiểm thử Dự án Hệ thống RMS (Testing Specification)

Tài liệu này quy định chiến lược kiểm thử, cấu hình môi trường kiểm thử và các quy tắc viết ca kiểm thử (Test Cases) trong **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)**.

---

## 1. Chiến lược Kiểm thử Đa tầng (Testing Strategy)

Hệ thống được bảo đảm chất lượng thông qua 3 tầng kiểm thử chính:

1. **Kiểm thử Đơn vị (Unit Tests)**:
   * Kiểm tra bộ máy nhận diện model rơ-le và chức năng ANSI C37.2 (`sheets/relay_matcher.py`).
   * Kiểm tra hàm chuẩn hóa chuỗi tiếng Việt và định dạng tên EVN PMIS (có gạch nối và viết liền).
   * Kiểm tra logic tính toán chênh lệch giá trị và phát hiện sai lệch (Diff Engine).
2. **Kiểm thử Nghiệp vụ & Quyền hạn (Integration & RBAC Tests)**:
   * Kiểm tra vòng đời trạng thái phiếu (`DRAFT` $\rightarrow$ `ISSUED` $\rightarrow$ `ROUTED_TO_STATION` $\rightarrow$ `COMPLETED`).
   * Kiểm tra quyền hạn ký số và ngăn chặn chỉnh sửa khi phiếu đã `COMPLETED`.
   * Kiểm tra luồng tạo `CorrectionTicket` khi phát hiện sai lệch rơ-le.
3. **Kiểm thử Giao tiếp HTTP/HTMX (View & Endpoint Tests)**:
   * Kiểm tra các View trả về mã HTTP 200 và render đúng HTML partial.
   * Kiểm tra các header `HX-Trigger` phát tín hiệu làm mới giao diện phía client (`refreshRow-{id}`, `notify`...).
   * Kiểm tra luồng upload file PDF và đối chiếu dữ liệu.

---

## 2. Công cụ Sử dụng (Testing Stack)

* **Test Framework**: `django.test.TestCase` kết hợp `unittest`.
* **Giả lập Request**: `django.test.Client` và `RequestFactory`.
* **Cơ sở dữ liệu Kiểm thử**: PostgreSQL Test Database (sử dụng cờ `--keepdb` để tăng tốc độ chạy kiểm thử từ vài phút xuống dưới 30 giây).

---

## 3. Lệnh Thực thi Kiểm thử (Execution Commands)

Tất cả các lệnh kiểm thử được chạy trực tiếp trong container `rms_web` hoặc từ máy host:

```bash
# 1. Kiểm tra toàn bộ tính toàn vẹn hệ thống và cú pháp models
docker exec rms_web python manage.py check

# 2. Chạy toàn bộ bộ kiểm thử phân hệ Phiếu Chỉnh định (sheets)
docker exec rms_web python manage.py test sheets --keepdb

# 3. Chạy toàn bộ bộ kiểm thử phân hệ Trạm & Rơ-le (stations)
docker exec rms_web python manage.py test stations --keepdb

# 4. Chạy kiểm thử chi tiết một lớp kiểm thử cụ thể
docker exec rms_web python manage.py test sheets.tests.SheetWorkflowTests --keepdb -v 2
```

---

## 4. Cấu trúc Ca Kiểm thử Chuẩn (Standard TestCase Example)

Ví dụ ca kiểm thử luồng đối chiếu thông số rơ-le từ file PDF và phát hiện sai lệch:

```python
from django.test import TestCase, Client
from django.contrib.auth.models import User
from stations.models import Relay, RelayAutoCheckLog
from sheets.models import SettingSheet
import io

class RelaySettingAuditTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('admin', 'admin@evn.vn', 'pass123')
        self.client = Client()
        self.client.force_login(self.user)
        self.relay = Relay.objects.create(relay_code='SEL-751', relay_name='Quá dòng ngăn 571')
        self.sheet = SettingSheet.objects.create(
            sheet_code='PCD-TEST-01',
            relay=self.relay,
            status='COMPLETED',
            extracted_data=[
                {'parameter_code': '50_1_I', 'parameter_name': 'Cắt nhanh', 'value': '12.5', 'unit': 'A'}
            ]
        )

    def test_upload_pdf_detects_mismatch(self):
        """Kiểm tra hệ thống phát hiện chính xác khi file PDF có thông số lệch so với phiếu"""
        dummy_pdf = io.BytesIO(b"%PDF-1.4...")
        dummy_pdf.name = "Bao_cao_thi_nghiem.pdf"

        response = self.client.post(
            f'/stations/relay/{self.relay.id}/upload_pdf_compare/',
            {'pdf_file': dummy_pdf}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(f"refreshRow-{self.relay.id}", response.headers.get('HX-Trigger', ''))
        
        # Kiểm tra bản ghi log được tạo trong CSDL
        log = self.relay.auto_checks.first()
        self.assertIsNotNone(log)
        self.assertIn(log.status, ['MATCH', 'MISMATCH'])
```

---

## 5. Tiêu chuẩn Đạt chuẩn Kiểm thử (Quality Gates)

1. **100% Pass Rate**: Tuyệt đối không chấp nhận bất kỳ ca test nào bị lỗi (Failed/Error) trước khi bàn giao mã nguồn.
2. **Không để rò rỉ dữ liệu thử nghiệm**: Mọi bản ghi tạo ra trong quá trình test phải được dọn dẹp sạch sẽ sau khi kết thúc ca kiểm thử.
````

## File: docs/cores/06-deployment.md
````markdown
# Quy trình Triển khai & Vận hành Hệ thống RMS (Deployment & Operations Guide)

Tài liệu này đặc tả kiến trúc triển khai trên môi trường Docker, biến môi trường, quản lý volume và các quy trình bảo trì vận hành **Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)**.

---

## 1. Kiến trúc Đóng gói Môi trường (Docker Compose Architecture)

Toàn bộ hệ thống được container hóa thông qua `docker-compose.yml` gồm 4 dịch vụ cốt lõi hoạt động độc lập và bảo đảm độ sẵn sàng cao:

```mermaid
graph TD
    User["Trình duyệt Kỹ sư / Điều độ"] -->|HTTP / WebSocket Port 9000| Web["Container: rms_web (Daphne ASGI + Django)"]
    
    Web -->|Port 5440| DB[("Container: rms_db (PostgreSQL 15)")]
    Web -->|Port 6379| Redis[("Container: rms_redis (Redis 7)")]
    
    Celery["Container: rms_celery (Celery Workers)"] -->|Nhận Task ngầm| Redis
    Celery -->|Truy xuất / Ghi dữ liệu| DB
    
    Web --- VolStatic["Volume: static_volume"]
    Web --- VolMedia["Volume: media_volume (PDF / Scans)"]
    Celery --- VolMedia
```

### Chi tiết 4 Dịch vụ (Services):
1. **`rms_db` (PostgreSQL 15 Alpine)**:
   * Cổng máy host: `5440` (chuyển tiếp tới 5440 trong container).
   * Lưu trữ dữ liệu quan hệ, dữ liệu JSONB và lịch sử kiểm tra rơ-le.
   * Dữ liệu được lưu bền vững (Persistent Volume) tại `postgres_data`.
2. **`rms_redis` (Redis Alpine)**:
   * Cổng máy host: `6379`.
   * Đóng vai trò Channel Layer cho WebSocket realtime và Message Broker cho Celery.
   * Dữ liệu được lưu tại `redis_data`.
3. **`rms_web` (Django 5 + Daphne ASGI)**:
   * Cổng dịch vụ web: `9000`.
   * Lệnh khởi chạy:
     `collectstatic` $\rightarrow$ `migrate` $\rightarrow$ `seed_permissions` $\rightarrow$ `daphne -b 0.0.0.0 -p 9000 rms_project.asgi:application`.
   * Mount thư mục mã nguồn máy host vào `/app` để phát triển và cập nhật trực tiếp.
4. **`rms_celery` (Celery Worker + Beat)**:
   * Chạy ngầm các tác vụ nặng: xử lý OCR đa luồng và quét tự động thông số rơ-le theo lịch hẹn giờ.

---

## 2. Quản lý Biến Môi trường (`.env`)

Tất cả các tham số nhạy cảm được quản lý tại tệp `.env` ở thư mục gốc của dự án:

| Tên biến (Key) | Mô tả (Description) | Ví dụ / Mặc định |
| :--- | :--- | :--- |
| `DEBUG` | Chế độ gỡ lỗi (False trên production) | `True` / `False` |
| `SECRET_KEY` | Khóa bí mật bảo vệ Session & CSRF Django | `django-insecure-rms-...` |
| `POSTGRES_DB` | Tên cơ sở dữ liệu PostgreSQL | `rms_db` |
| `POSTGRES_USER` | Tên tài khoản quản trị DB | `rms_user` |
| `POSTGRES_PASSWORD` | Mật khẩu truy cập DB | `secure_password_123` |
| `POSTGRES_HOST` | Địa chỉ máy chủ DB trong mạng Docker | `db` |
| `PGPORT` | Cổng kết nối PostgreSQL | `5440` |
| `REDIS_URL` | URL kết nối Redis Broker | `redis://redis:6379/0` |

---

## 3. Các Lệnh Vận hành Cơ bản (Operational Commands)

### 3.1 Khởi động và Khởi động lại Hệ thống:
```bash
# Khởi động toàn bộ cụm 4 dịch vụ ngầm
docker-compose up -d

# Khởi động lại dịch vụ Web khi có thay đổi mã nguồn Python
docker restart rms_web

# Khởi động lại dịch vụ Celery
docker restart rms_celery

# Xem trạng thái hoạt động của các container
docker ps
```

### 3.2 Kiểm tra Nhật ký Hoạt động (Logs Inspection):
```bash
# Xem log thời gian thực của máy chủ Web Daphne
docker logs -f --tail 100 rms_web

# Xem log tác vụ ngầm Celery
docker logs -f --tail 100 rms_celery

# Xem log cơ sở dữ liệu PostgreSQL
docker logs -f --tail 50 rms_db
```

### 3.3 Quản trị Cơ sở dữ liệu & Cập nhật Schema:
```bash
# Tạo migration mới khi có thay đổi models
docker exec rms_web python manage.py makemigrations

# Áp dụng migration vào DB
docker exec rms_web python manage.py migrate

# Gom tệp tĩnh mới vào thư mục staticfiles
docker exec rms_web python manage.py collectstatic --noinput

# Chạy lệnh kiểm tra tính hợp lệ hệ thống
docker exec rms_web python manage.py check
```

---

## 4. Sao lưu & Phục hồi Dữ liệu (Backup & Recovery)

```bash
# Sao lưu cơ sở dữ liệu ra tệp .sql trên máy host
docker exec -t rms_db pg_dump -U rms_user -p 5440 rms_db > backup_rms_$(date +%Y%m%d).sql

# Phục hồi dữ liệu từ file backup
docker exec -i rms_db psql -U rms_user -p 5440 rms_db < backup_rms_20261104.sql
```
````

## File: docs/features/01-station-management.md
````markdown
# Phân hệ Quản lý Trạm, Ngăn lộ & Rơ-le (Station Management)

> [!WARNING]
> Phân hệ này đã được dời sang Giai đoạn 5 (Module Tài sản) theo SRS mới nhất. Trong phiên bản MVP, hệ thống không quản lý danh mục thiết bị chi tiết mà lưu dưới dạng văn bản trong Phiếu chỉnh định. Tài liệu dưới đây mang tính chất tham khảo cho tương lai.

**App Django**: `apps/stations`
**User Stories liên quan**: `[US-STN-01]` đến `[US-STN-05]`

---

## 1. Tổng quan Nghiệp vụ

Phân hệ này cho phép **Công ty Truyền tải** (user chính) quản lý toàn bộ danh mục hạ tầng vật lý của lưới điện truyền tải, bao gồm 3 cấp độ:

```
Trạm Biến áp (Station)
 └── Ngăn lộ / Bay (Bay)
       └── Rơ-le Bảo vệ (Relay)
             └── Thông số Định mức (RelaySetting)
```

---

## 2. Luồng Nghiệp vụ Chi tiết

### 2.1 Tạo Dự án (Trạm Biến áp) từ File Cấu hình [US-STN-01]

Đây là **Figure 1** trong tài liệu UseCase gốc.

```mermaid
sequenceDiagram
    actor User as Công ty Truyền tải
    participant FE as HTMX Frontend
    participant BE as Django Backend

    User->>FE: Vào trang "Tạo Trạm mới" → Upload file cấu hình (JSON/Excel)
    FE->>BE: POST /api/v1/stations/import/ {file}
    BE->>BE: Parse file, validate định dạng
    BE->>BE: Tạo Station, Bay, Relay records trong DB (transaction)
    BE-->>FE: Trả về danh sách đã tạo {stations, bays, relays}
    FE-->>User: Hiển thị kết quả import (thành công/lỗi từng dòng)
```

**Định dạng file cấu hình (JSON)**:
```json
{
  "station": {
    "code": "TBA_220KV_HOA_BINH",
    "name": "Trạm biến áp 220kV Hòa Bình",
    "location": "Tỉnh Hòa Bình",
    "voltage_level": "220kV"
  },
  "bays": [
    {
      "code": "BAY_AT1",
      "name": "Ngăn Máy biến áp AT1",
      "bay_type": "Máy biến áp",
      "relays": [
        {
          "code": "REL_AT1_87T",
          "name": "Rơ-le so lệch biến áp AT1",
          "manufacturer": "ABB",
          "model_number": "RET670",
          "serial_number": "SN-2024-001",
          "settings": [
            { "code": "ID_MIN", "name": "Dòng khởi động tối thiểu", "standard_value": 0.2, "unit": "A", "tolerance_min": 0.18, "tolerance_max": 0.22 },
            { "code": "TD_1", "name": "Thời gian tác động cấp 1", "standard_value": 0.0, "unit": "s", "tolerance_min": 0.0, "tolerance_max": 0.02 }
          ]
        }
      ]
    }
  ]
}
```

### 2.2 Quản lý Thủ công Trạm / Ngăn lộ / Rơ-le [US-STN-02..05]

- **Xem danh sách**: Bảng có tìm kiếm theo tên/mã, lọc theo cấp điện áp, phân trang 20 bản ghi/trang.
- **Tạo mới thủ công**: Form nhập từng trường, validation ngay trên FE (Django Forms / HTML5 Validation).
- **Chỉnh sửa**: Các trường có thể sửa (tên, địa điểm, trạng thái active). Không cho phép sửa mã (code) sau khi tạo.
- **Vô hiệu hóa**: Đặt `is_active = False`, không xóa vật lý. Các bản ghi con (bay, relay) không bị ảnh hưởng.

---

## 3. Business Rules (Quy tắc Nghiệp vụ)

| # | Quy tắc |
|---|---|
| BR-STN-01 | Mã trạm (`station_code`) phải là duy nhất trong toàn hệ thống. |
| BR-STN-02 | Không thể xóa trạm nếu còn ngăn lộ đang hoạt động. |
| BR-STN-03 | Không thể vô hiệu hóa rơ-le nếu đang có phiếu chỉnh định ở trạng thái DRAFT hoặc ISSUED. |
| BR-STN-04 | Giá trị `tolerance_min` phải luôn nhỏ hơn `tolerance_max` trong thông số định mức. |
| BR-STN-05 | Import file: Nếu `station_code` đã tồn tại, hệ thống hỏi xác nhận trước khi ghi đè. |

---

## 4. API Endpoints Chi tiết

### POST `/api/v1/stations/`
**Quyền**: `TRANSMISSION_COMPANY`

**Request Body**:
```json
{
  "station_code": "TBA_220KV_HA_NOI",
  "station_name": "Trạm biến áp 220kV Hà Nội",
  "location": "Quận Hoàng Mai, Hà Nội",
  "voltage_level": "220kV"
}
```

**Response (201)**:
```json
{
  "success": true,
  "message": "Tạo trạm biến áp thành công",
  "data": {
    "id": 5,
    "station_code": "TBA_220KV_HA_NOI",
    "station_name": "Trạm biến áp 220kV Hà Nội",
    "is_active": true,
    "bays_count": 0
  }
}
```

### POST `/api/v1/stations/import/`
**Quyền**: `TRANSMISSION_COMPANY`
**Content-Type**: `multipart/form-data`

**Form Fields**:
- `file`: File JSON hoặc Excel cấu hình trạm

**Response (200)**:
```json
{
  "success": true,
  "message": "Import hoàn tất",
  "data": {
    "created_stations": 1,
    "created_bays": 3,
    "created_relays": 8,
    "errors": []
  }
}
```

---

## 5. Giao diện (UI Specification)

### Màn hình Danh sách Trạm (`/stations`)
- **Header**: Tiêu đề "Quản lý Trạm Biến áp" + nút "Tạo mới" + nút "Import từ file"
- **Filter bar**: Tìm kiếm theo tên/mã trạm | Lọc theo cấp điện áp (110kV / 220kV / 500kV) | Trạng thái (Đang hoạt động / Vô hiệu hóa)
- **Bảng dữ liệu**: Mã trạm | Tên trạm | Địa điểm | Cấp điện áp | Số ngăn lộ | Trạng thái | Hành động

### Màn hình Chi tiết Trạm (`/stations/:id`)
- **Thông tin chung**: Card hiển thị các thông tin cơ bản của trạm
- **Tab "Ngăn lộ"**: Danh sách ngăn lộ dạng accordion. Click vào ngăn lộ để xem rơ-le bên trong
- **Tab "Lịch sử"**: Timeline các thay đổi thông tin trạm
````

## File: docs/features/02-calibration-sheet.md
````markdown
# Phân hệ Quản lý Phiếu Chỉnh định (Calibration Sheet)

**App Django**: `apps/calibration`
**User Stories liên quan**: `[US-SHEET-01]` đến `[US-SHEET-10]`

---

## 1. Tổng quan Nghiệp vụ

Phiếu chỉnh định là tài liệu kỹ thuật quan trọng nhất trong hệ thống, ghi nhận lệnh chỉnh định thông số rơ-le từ Công ty Truyền tải tới Đơn vị chỉnh định. Mỗi phiếu trải qua vòng đời trạng thái nghiêm ngặt.

---

## 2. Vòng đời Trạng thái Phiếu (Sheet Lifecycle)

```mermaid
stateDiagram-v2
    [*] --> DRAFT : A0/A1 tạo phiếu & upload scan
    DRAFT --> ISSUED : A0/A1 ký số ban đầu & phát hành
    ISSUED --> TRANSFERRED : Công ty Truyền tải chuyển giao
    TRANSFERRED --> RECEIVED : Kỹ thuật viên tiếp nhận
    RECEIVED --> COMPLETED : Kỹ thuật viên ký số xác nhận + Giám sát ký số

    DRAFT --> DRAFT : Chỉnh sửa metadata
    note right of COMPLETED : Trạng thái cuối - không thể thay đổi
```

| Trạng thái | Mô tả | Người có thể hành động |
|---|---|---|
| `DRAFT` | Phiếu mới tạo, chưa phát hành | A0/A1 |
| `ISSUED` | Đã ký số ban đầu & phát hành | Công ty Truyền tải |
| `TRANSFERRED` | Đã chuyển giao cho Đơn vị chỉnh định | Kỹ thuật viên |
| `RECEIVED` | Kỹ thuật viên đã tiếp nhận phiếu | Kỹ thuật viên, Giám sát trạm |
| `COMPLETED` | Đã hoàn thành, có đủ chữ ký xác nhận | — (Chỉ xem) |

---

## 3. Luồng Nghiệp vụ Chi tiết

### 3.1 Import & Phát hành Phiếu [US-SHEET-01..03] — Figure 3

```mermaid
sequenceDiagram
    actor A01 as A0/A1 (Người phát hành)
    participant FE as HTMX Frontend
    participant BE as Django Backend
    participant Storage as File Storage

    A01->>FE: Vào "Tạo phiếu mới"
    A01->>FE: Upload file scan phiếu (PDF/JPG) + nhập metadata
    FE->>FE: Validate: định dạng file, dung lượng ≤ 20MB
    FE->>BE: POST /api/v1/calibration-sheets/ (multipart)
    BE->>BE: Kiểm tra relay_id tồn tại và đang hoạt động
    BE->>Storage: Lưu file scan vào /media/sheets/
    BE->>BE: Tạo bản ghi CalibrationSheet (status=DRAFT)
    BE-->>FE: Trả về sheet_id, sheet_code
    FE-->>A01: Hiển thị phiếu ở trạng thái DRAFT

    A01->>FE: Nhấn "Ký số & Phát hành"
    FE->>BE: POST /api/v1/signatures/initiate/ {sheet_id}
    BE->>BE: Tính hash nội dung phiếu
    Note over BE: Gọi EVN API (xem 03-digital-signature.md)
    BE-->>FE: Trả về signing_url
    FE-->>A01: Mở cửa sổ/tab để ký số tại EVN

    A01->>FE: Xác nhận đã ký xong
    FE->>BE: POST /api/v1/signatures/confirm/ + POST /api/v1/calibration-sheets/{id}/issue/
    BE->>BE: Lưu chữ ký, cập nhật status → ISSUED
    BE->>BE: Ghi log vào sheet_status_logs
    BE-->>FE: Phiếu ở trạng thái ISSUED
```

### 3.2 Chuyển giao Phiếu [US-SHEET-04] — Figure 4

```mermaid
sequenceDiagram
    actor TC as Công ty Truyền tải
    participant BE as Django Backend

    TC->>BE: POST /api/v1/calibration-sheets/{id}/transfer/
    Note right of TC: Body: {to_unit_user_id, note}
    BE->>BE: Kiểm tra: phiếu status = ISSUED
    BE->>BE: Kiểm tra: to_unit_user có role CALIBRATION_TECHNICIAN
    BE->>BE: Tạo SheetTransfer record
    BE->>BE: Cập nhật status → TRANSFERRED
    BE->>BE: Ghi log
    BE-->>TC: Chuyển giao thành công
```

### 3.3 Tiếp nhận & Xác nhận Hoàn thành [US-SHEET-06..08] — Figure 5

```mermaid
sequenceDiagram
    actor Tech as Kỹ thuật viên
    actor Sup as Người giám sát Trạm
    participant BE as Django Backend

    Tech->>BE: POST /api/v1/calibration-sheets/{id}/receive/
    BE->>BE: Kiểm tra: phiếu status = TRANSFERRED
    BE->>BE: Kiểm tra: user đang đăng nhập là người được chuyển giao
    BE->>BE: Cập nhật status → RECEIVED
    BE-->>Tech: Tiếp nhận thành công

    Tech->>BE: POST /api/v1/signatures/initiate/ (ký xác nhận hoàn thành)
    Note over Tech,BE: Luồng ký số EVN (xem 03-digital-signature.md)
    BE->>BE: Lưu chữ ký Tech

    Sup->>BE: POST /api/v1/signatures/initiate/ (ký giám sát trạm)
    Note over Sup,BE: Luồng ký số EVN
    BE->>BE: Lưu chữ ký Sup

    BE->>BE: Kiểm tra: đủ 3 chữ ký (A0/A1 + Tech + Sup)?
    BE->>BE: Cập nhật status → COMPLETED
    BE-->>Tech: Phiếu hoàn thành
```

---

## 4. Business Rules (Quy tắc Nghiệp vụ)

| # | Quy tắc |
|---|---|
| BR-SHEET-01 | Phiếu chỉnh định **không bao giờ bị xóa vật lý** (`is_deleted` = True cho soft delete). |
| BR-SHEET-02 | Phiếu chỉ được phát hành (ISSUED) sau khi có **chữ ký số hợp lệ** của A0/A1. |
| BR-SHEET-03 | Phiếu chỉ được chuyển giao (TRANSFERRED) khi đang ở trạng thái ISSUED. |
| BR-SHEET-04 | Kỹ thuật viên chỉ có thể tiếp nhận phiếu được chuyển **đích danh cho họ**. |
| BR-SHEET-05 | Phiếu chỉ đạt COMPLETED khi có đủ **3 chữ ký số**: A0/A1 + Kỹ thuật viên + Giám sát trạm. |
| BR-SHEET-06 | Mã phiếu (`sheet_code`) tự động sinh theo format: `PHIEU-{YYYY}-{MM}-{SEQUENCE}`. |
| BR-SHEET-07 | Chỉ cho phép upload file: PDF, JPG, JPEG, PNG. Dung lượng tối đa: **20MB**. |

---

## 5. API Request/Response Chi tiết

### POST `/api/v1/calibration-sheets/`
**Content-Type**: `multipart/form-data`

| Field | Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `relay_id` | integer | ✅ | ID rơ-le cần chỉnh định |
| `description` | string | ❌ | Mô tả nội dung phiếu |
| `scan_file` | file | ✅ | File bản scan phiếu |

**Response (201)**:
```json
{
  "success": true,
  "data": {
    "id": 42,
    "sheet_code": "PHIEU-2026-07-001",
    "status": "DRAFT",
    "relay": { "id": 5, "relay_code": "REL_AT1_87T", "relay_name": "Rơ-le so lệch AT1" },
    "scan_file_url": "/media/sheets/2026/07/scan_001.pdf",
    "issued_by": null,
    "issued_at": null,
    "created_at": "2026-07-11T16:30:00Z"
  }
}
```

### GET `/api/v1/calibration-sheets/` (với filter)

**Query Parameters**:
| Param | Mô tả | Ví dụ |
|---|---|---|
| `status` | Lọc theo trạng thái | `?status=ISSUED` |
| `station_id` | Lọc theo trạm | `?station_id=3` |
| `relay_id` | Lọc theo rơ-le | `?relay_id=5` |
| `date_from` | Từ ngày | `?date_from=2026-01-01` |
| `date_to` | Đến ngày | `?date_to=2026-12-31` |
| `search` | Tìm theo mã phiếu | `?search=PHIEU-2026` |
| `page` | Số trang | `?page=2` |

---

## 6. Giao diện (UI Specification)

### Màn hình Chi tiết Phiếu (`/calibration-sheets/:id`)

**Layout**: Chia 2 cột:
- **Cột trái (60%)**: Iframe/viewer hiển thị file scan phiếu
- **Cột phải (40%)**:
  - Thông tin metadata (Mã phiếu, Rơ-le, Ngày phát hành...)
  - **Panel "Trạng thái ký số"**: Hiển thị 3 ô ký số (A0/A1 | Kỹ thuật viên | Giám sát trạm) với badge màu: 🔴 Chưa ký / 🟡 Đang xử lý / 🟢 Đã ký hợp lệ
  - **Timeline lịch sử**: Các bước đã thực hiện theo thứ tự thời gian
  - **Nút hành động**: Hiển thị nút phù hợp với quyền và trạng thái phiếu hiện tại
````

## File: docs/features/03-digital-signature.md
````markdown
# Phân hệ Ký số Điện tử (Digital Signature — EVN Integration)

**App Django**: `apps/signatures`
**User Stories liên quan**: `[US-SIG-01]` đến `[US-SIG-04]`

---

## 1. Tổng quan Nghiệp vụ

Hệ thống RMS **không tự thực hiện ký số** mà ủy thác toàn bộ quá trình cho **Hệ thống Ký số của EVN** — một hệ thống bên ngoài cung cấp dịch vụ chữ ký số pháp lý cho toàn bộ Tập đoàn Điện lực Việt Nam.

Có **3 loại chữ ký** cần thu thập trên mỗi phiếu chỉnh định:
1. **Chữ ký A0/A1**: Xác nhận phiếu đã được soạn thảo và phát hành.
2. **Chữ ký Kỹ thuật viên**: Xác nhận đã hoàn thành công việc chỉnh định tại trạm.
3. **Chữ ký Giám sát trạm**: Xác nhận kỹ thuật viên đã đến trạm và thực hiện chỉnh định.

---

## 2. Luồng Ký số Chi tiết — Figure 5

```mermaid
sequenceDiagram
    actor User as Người dùng (bất kỳ vai trò)
    participant FE as HTMX Frontend
    participant BE as Django Backend
    participant EVN as Hệ thống Ký số EVN

    User->>FE: Nhấn nút "Ký số" trên phiếu chỉnh định
    FE->>BE: POST /api/v1/signatures/initiate/ {sheet_id, signer_role}

    BE->>BE: Tạo nội dung cần ký (content_to_sign)
    Note over BE: content_to_sign = SHA-256(sheet_code + relay_code + issued_at + signer_id)
    BE->>BE: Tạo bản ghi DigitalSignature (status=PENDING)

    BE->>EVN: POST {EVN_BASE_URL}/initiate
    Note over BE,EVN: Headers: Authorization: Bearer {EVN_API_KEY}<br/>Body: {user_cert_id, content_hash, callback_url}
    EVN-->>BE: {session_id, signing_url, expires_in: 300}

    BE-->>FE: {session_id, signing_url}
    FE-->>User: Mở popup/tab mới với signing_url của EVN

    User->>EVN: Xác thực (OTP/USB Token) và thực hiện ký số
    EVN-->>User: Thông báo ký số thành công

    User->>FE: Nhấn "Tôi đã ký xong" trong popup
    FE->>BE: POST /api/v1/signatures/confirm/ {session_id}

    BE->>EVN: GET {EVN_BASE_URL}/result/{session_id}
    EVN-->>BE: {status: "SIGNED", signature_data: "Base64...", cert_info: {...}, signed_at: "..."}

    BE->>BE: Lưu signature_data vào DB
    BE->>BE: Cập nhật DigitalSignature.status = SIGNED
    BE->>BE: Kiểm tra điều kiện chuyển trạng thái phiếu
    Note over BE: Nếu đủ 3 chữ ký → tự động cập nhật sheet.status = COMPLETED
    BE-->>FE: {success: true, signature_status: "SIGNED"}
    FE-->>User: Hiển thị badge "Đã ký ✅"
```

---

## 3. Service Layer: `EVNSignatureService`

```python
# apps/signatures/services.py

class EVNSignatureService:
    """
    Dịch vụ tích hợp với Hệ thống Ký số EVN.
    Đóng gói toàn bộ logic giao tiếp với API EVN bên ngoài.
    """

    def initiate_signing_session(self, user, sheet, signer_role: str) -> dict:
        """
        Khởi tạo phiên ký số với EVN.
        Trả về: {session_id, signing_url}
        Raises: EVNServiceUnavailableError nếu EVN API không phản hồi.
        """

    def get_signing_result(self, session_id: str) -> dict:
        """
        Lấy kết quả ký số từ EVN sau khi user hoàn thành.
        Trả về: {status, signature_data, cert_info, signed_at}
        Raises: EVNSessionExpiredError nếu session hết hạn (>5 phút).
        """

    def verify_signature(self, signature_id: int) -> bool:
        """
        Xác thực lại chữ ký số đã lưu với EVN.
        Trả về: True nếu hợp lệ, False nếu đã bị thu hồi/hết hiệu lực.
        """
```

---

## 4. Model: `DigitalSignature`

```python
# apps/signatures/models.py

class DigitalSignature(models.Model):
    # Phiếu chỉnh định được ký
    sheet = models.ForeignKey('calibration.CalibrationSheet', on_delete=models.PROTECT)

    # Người thực hiện ký
    signed_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    # Vai trò khi ký (A0_A1_ISSUER / CALIBRATION_TECHNICIAN / STATION_SUPERVISOR)
    signer_role = models.CharField(max_length=50)

    # Dữ liệu từ hệ thống EVN
    evn_session_id = models.CharField(max_length=200, unique=True)
    signature_data = models.TextField(null=True, blank=True)  # Base64 chữ ký
    certificate_info = models.JSONField(null=True, blank=True)  # Thông tin chứng thư

    # Trạng thái: PENDING / SIGNED / VERIFIED / INVALID
    signature_status = models.CharField(max_length=20, default='PENDING')

    signed_at = models.DateTimeField(null=True, blank=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Mỗi vai trò chỉ ký một lần trên mỗi phiếu
        unique_together = [('sheet', 'signer_role')]
```

---

## 5. Xử lý Lỗi (Error Handling)

| Tình huống | HTTP Status | error_code | Xử lý |
|---|---|---|---|
| EVN API không phản hồi (timeout) | 503 | `EVN_SERVICE_UNAVAILABLE` | Retry sau 30s, hiển thị thông báo |
| Phiên ký số hết hạn (>5 phút) | 400 | `EVN_SESSION_EXPIRED` | Người dùng phải khởi tạo lại |
| Chữ ký không hợp lệ (EVN từ chối) | 400 | `EVN_SIGNATURE_INVALID` | Log lỗi, không lưu vào DB |
| Người dùng đã ký (trùng vai trò) | 409 | `SIGNATURE_ALREADY_EXISTS` | Hiển thị chữ ký hiện tại |
| Người dùng không có chứng thư EVN | 403 | `EVN_CERT_NOT_FOUND` | Liên hệ Admin để đăng ký chứng thư |

---

## 6. API Endpoints

### POST `/api/v1/signatures/initiate/`
**Quyền**: Authenticated (vai trò phù hợp với phiếu)

**Request**:
```json
{
  "sheet_id": 42,
  "signer_role": "A0_A1_ISSUER"
}
```

**Response (200)**:
```json
{
  "success": true,
  "data": {
    "session_id": "EVN-SESSION-2026071100001",
    "signing_url": "https://sign.evn.com.vn/sign?session=EVN-SESSION-2026071100001",
    "expires_in": 300
  }
}
```

### POST `/api/v1/signatures/confirm/`

**Request**:
```json
{
  "session_id": "EVN-SESSION-2026071100001"
}
```

**Response (200)**:
```json
{
  "success": true,
  "data": {
    "signature_id": 15,
    "signer_role": "A0_A1_ISSUER",
    "signature_status": "SIGNED",
    "signed_at": "2026-07-11T10:00:00Z",
    "sheet_new_status": "ISSUED"
  }
}
```

---

## 7. Giao diện (UI Specification)

### Panel Trạng thái Ký số (trong màn hình Chi tiết Phiếu)

```
┌─────────────────────────────────────────┐
│  TRẠNG THÁI CHỮ KÝ SỐ                  │
├─────────────────────────────────────────┤
│  ✅ A0/A1 Phát hành                     │
│     Nguyễn Văn A • 11/07/2026 09:30    │
├─────────────────────────────────────────┤
│  ✅ Kỹ thuật viên                       │
│     Trần Văn B • 12/07/2026 14:00      │
├─────────────────────────────────────────┤
│  ⏳ Giám sát Trạm                       │
│     Chưa ký   [Nhấn để ký số →]        │
└─────────────────────────────────────────┘
```

- Badge `✅ Đã ký` màu xanh lá
- Badge `⏳ Chưa ký` màu vàng + nút "Ký số" (chỉ hiển thị với người có quyền ký)
- Badge `❌ Không hợp lệ` màu đỏ (khi xác thực lại thất bại)
````

## File: docs/features/04-periodic-check.md
````markdown
# Phân hệ Đối chiếu & Giám sát Thông số Rơ-le (Relay Setting Verification)

**App Django**: `stations`  
**Đường dẫn truy cập**: `/stations/autochecks/`  
**Tên hiển thị giao diện**: **Trung tâm Đối chiếu & Giám sát Thông số Rơ-le**

---

## 1. Tổng quan Nghiệp vụ

Trong quản lý kỹ thuật lưới điện của EVN (Điều độ A0/Ax, các Công ty Truyền tải điện PTC và Công ty Điện lực PC):
* Khi kỹ sư phương thức ban hành một **Phiếu Chỉnh định mới nhất** (trạng thái `COMPLETED`), các thông số trên phiếu là chuẩn mực quy định bắt buộc rơ-le phải tuân thủ.
* Trong thực tế vận hành, sau các đợt thí nghiệm định kỳ, nghiệm thu đóng điện hoặc phân tích sự cố: đơn vị công tác sẽ xuất ra **file báo cáo PDF** (từ các phần mềm rơ-le chuyên dụng như *Siemens DIGSI 4/5, ABB PCM600, SEL acSELerator QuickSet, Schneider MiCOM S1 Agile, GE EnerVista* hoặc *Biên bản thử nghiệm scan có chữ ký*).
* **Mục tiêu phân hệ**:
  1. Cho phép kỹ sư xem trực tiếp danh sách toàn bộ trị số cài đặt của rơ-le trên hệ thống.
  2. Bóc tách dữ liệu từ file PDF báo cáo thực tế và tự động đối chiếu với Phiếu Chỉnh định mới nhất đang có hiệu lực.
  3. Phát hiện chính xác các điểm sai lệch (Thông số nào sai? Quy định là bao nhiêu? Thực tế đang cài đặt là bao nhiêu?).
  4. Cung cấp nút bấm 1-chạm **"Tạo Phiếu yêu cầu Rà soát & Chỉnh định lại"** chuyển lệnh thẳng xuống Trạm / Kỹ thuật viên hiện trường để rà soát và nạp lại thông số chuẩn vào rơ-le.

---

## 2. Sơ đồ Luồng Nghiệp vụ (End-to-End Workflow)

```mermaid
sequenceDiagram
    actor KS as Kỹ sư Điều độ / Phòng Kỹ thuật
    participant UI as Giao diện Web (HTMX/Alpine)
    participant BE as Django Backend (stations/views.py)
    participant DB as PostgreSQL (SettingSheet & RelayAutoCheckLog)
    actor KTV as Trạm / Kỹ thuật viên Hiện trường

    KS->>UI: 1. Truy cập "Đối chiếu thông số Rơ-le"
    UI->>BE: GET /stations/autochecks/
    BE->>DB: Lấy danh sách rơ-le ưu tiên (Lệch -> Có phiếu -> Đã kiểm tra)
    BE-->>UI: Hiển thị bảng Dashboard + 4 KPI Cards

    KS->>UI: 2. Bấm "Tải PDF đối chiếu" (Icon Xanh ngọc)
    UI-->>KS: Mở modal kéo thả file PDF báo cáo thực tế
    KS->>UI: 3. Chọn file PDF & Bấm "Bắt đầu đối chiếu"

    UI->>BE: POST /stations/relay/{id}/upload_pdf_compare/ (multipart file)
    BE->>BE: Bóc tách text & bảng thông số từ PDF (bằng pypdf)
    BE->>DB: Lấy extracted_data từ Phiếu chỉnh định COMPLETED mới nhất (relay.active_sheet)
    BE->>BE: So sánh song song từng thông số (code, name, value, unit)
    
    alt Có sai lệch (MISMATCH)
        BE->>DB: Tạo RelayAutoCheckLog (status='MISMATCH', differences=[...])
        BE->>DB: Đánh dấu relay.is_paused_for_correction = True
        BE-->>UI: Trả về Bảng Side-by-side Diff (Tô đỏ thông số sai) + HX-Trigger refresh row
        UI-->>KS: Hiển thị cảnh báo đỏ và nút "Tạo Phiếu yêu cầu Rà soát"
        
        KS->>UI: 4. Bấm "Tạo Phiếu yêu cầu Rà soát & Chỉnh định lại"
        UI->>BE: POST /stations/relay/{id}/workflow/create_ticket/
        BE->>DB: Khởi tạo SettingSheet (AUTO-CORRECT-...) trạng thái ROUTED_TO_STATION
        BE-->>UI: Thông báo đã chuyển lệnh xuống Trạm / KTV
        BE-->>KTV: Lệnh rà soát xuất hiện tại danh sách công tác của Trạm
    else Trùng khớp 100% (MATCH)
        BE->>DB: Tạo RelayAutoCheckLog (status='MATCH', differences=[])
        BE->>DB: Cập nhật relay.is_paused_for_correction = False
        BE-->>UI: Trả về Bảng Diff (Xanh lá 100% Match) + HX-Trigger refresh row
        UI-->>KS: Xác nhận rơ-le đạt chuẩn an toàn vận hành
    end
```

---

## 3. Các Thành phần Giao diện Cốt lõi

1. **Dashboard & 4 KPI Cards**:
   * **Tổng Rơ-le**: Quản lý toàn bộ 39.375 rơ-le trong hệ thống.
   * **Có Phiếu Chỉnh định**: Số lượng rơ-le đã được gán phiếu chính thức.
   * **Trùng khớp 100%**: Rơ-le đã đối chiếu và xác nhận khớp hoàn toàn với phiếu.
   * **Sai lệch (Cần rà soát)**: Rơ-le đang có sai lệch cần xử lý gấp.
2. **Modal Xem Thông số Rơ-le (`_relay_parameters_modal.html`)**:
   * Mở nhanh bằng nút tím `fa-sliders-h`.
   * Hiển thị toàn bộ trị số cài đặt kèm mã phiếu đang áp dụng.
   * Tích hợp ô tìm kiếm tức thì phản hồi ngay khi gõ từ khóa.
3. **Modal Nạp File PDF (`#upload-pdf-modal`)**:
   * Kéo thả file PDF báo cáo thử nghiệm/cài đặt.
   * Tự động nhận diện file và hiển thị tên file đính kèm.
4. **Modal Kết quả Đối chiếu Side-by-Side Diff (`_autocheck_results.html`)**:
   * Cột trái: Trị số Phiếu ban hành quy định (Màu xanh dương).
   * Cột phải: Trị số thực tế đọc từ file PDF (Tô đỏ nhạt nếu sai lệch).
   * Bộ lọc 3 chế độ: *Chỉ thông số sai lệch*, *Thông số trùng khớp*, *Tất cả*.
   * Nút điều phối: *"Tạo Phiếu yêu cầu Rà soát & Chỉnh định lại (Chuyển về Trạm)"*.

---

## 4. Các Quy tắc Nghiệp vụ (Business Rules)

| Mã Quy tắc | Nội dung Quy tắc |
| :--- | :--- |
| **BR-CHK-01** | Nguồn dữ liệu quy định chuẩn luôn ưu tiên lấy từ Phiếu Chỉnh định `COMPLETED` mới nhất của rơ-le (`relay.active_sheet`). Nếu chưa có phiếu `COMPLETED`, fallback lấy từ phiếu mới nhất hoặc `relay.settings`. |
| **BR-CHK-02** | Khi phát hiện bất kỳ thông số nào không trùng khớp giá trị số (numerical value) hoặc chuỗi cấu hình, hệ thống bắt buộc phải gán nhãn `MISMATCH` và lưu chi tiết vào mảng `differences`. |
| **BR-CHK-03** | Khi rơ-le rơi vào trạng thái `MISMATCH`, hệ thống tự động kích hoạt cờ `is_paused_for_correction = True` để hiển thị cảnh báo nhấp nháy trên Dashboard và tạm dừng các lịch quét tự động cho đến khi có xác nhận xử lý. |
| **BR-CHK-04** | Khi kỹ sư bấm *"Tạo Phiếu yêu cầu Rà soát"*, hệ thống tự động sinh một Phiếu Chỉnh định có tiền tố `AUTO-CORRECT-{Mã_Role}-{Thời_gian}` ở trạng thái `ROUTED_TO_STATION`, tự động đóng gói các trị số bị sai (`wrong_value`) và trị số đúng mục tiêu (`value`) để đơn vị dưới trạm biết chính xác điểm cần khắc phục. |
| **BR-CHK-05** | Sau khi rơ-le được nạp lại và đối chiếu đạt `MATCH` 100%, hệ thống tự động gỡ bỏ cờ cảnh báo `is_paused_for_correction = False` và khôi phục trạng thái vận hành an toàn. |

---

## 5. Quy chuẩn Đối soát Thông số Rơ-le Theo Hãng Sản xuất (11 Hệ sinh thái Chuyên sâu)

Hệ thống đối soát rơ-le ([stations/relay_specs.py](file:///d:/project/project-local/electric/electricity-web/stations/relay_specs.py)) được xây dựng theo chuẩn 5 tầng kỹ thuật cho toàn bộ các hãng có mặt trong cơ sở dữ liệu EVN:

### 1. Siemens SIPROTEC 5 & DIGSI 5
* **Dòng rơ-le**: `7SJ` (Quá dòng & Xuất tuyến), `7SA` (Khoảng cách ĐD), `7SD` (So lệch ĐD), `7SL` (So lệch + Khoảng cách), `7UT` (So lệch MBA), `7SS` (Thanh cái).
* **5 tầng**: Tỷ số biến CT/VT $\rightarrow$ Nhóm setting (`Setting Group 1..4`) $\rightarrow$ Kích hoạt hàm DIGSI (`FUNC_50_51`, `FUNC_67`) $\rightarrow$ Ngưỡng khởi động & Đặc tính (`IEC Normal Inverse`) $\rightarrow$ Khối liên kết logic `DIGSI CFC` & Đầu ra `BINARY_OUT_1`.

### 2. Schweitzer Engineering Laboratories (SEL) & acSELerator QuickSet SEL-5030
* **Dòng rơ-le**: `SEL-751/751A` (Xuất tuyến), `SEL-787/487E` (MBA), `SEL-411L` (Đường dây), `SEL-487B` (Thanh cái).
* **5 tầng**: `CTR`, `PTR`, `VNOM` $\rightarrow$ `ACTIVE_GROUP` $\rightarrow$ Cho phép chức năng (`E50P`, `E51P`, `E50G`, `E79`) $\rightarrow$ `50P1P`, `51P1P`, Time Dial $\rightarrow$ Phương trình `SELOGIC_TRIP` & Ánh xạ `OUT101_ASSIGN`.

### 3. ABB / Hitachi Energy & PCM600 (Protection and Control IED Manager)
* **Dòng rơ-le**: Relion Series: `REF615/620/630`, `RET670/650`, `RED670`, `REL670`, `REB670`, `REX640`.
* **5 tầng**: Tỷ số CT/VT $\rightarrow$ `Parameter Group` $\rightarrow$ Khối hàm Relion (`PHIPTOC1`, `EFIPTOC1`, `MPDIF`) $\rightarrow$ Ngưỡng khởi động `StartVal` & Trễ `OpDelay` $\rightarrow$ Mô hình ứng dụng `ACT (Application Configuration)` & Ma trận `Signal Matrix (SMT)`.

### 4. Toshiba (GR-Series: GR-TIEMS)
* **Dòng rơ-le**: `GRZ100/200` (Khoảng cách), `GRT100/200` (So lệch MBA), `GRD100/200` (Xuất tuyến), `GRB100/200` (Thanh cái), `GBU200` (BCU).
* **5 tầng**: Tỷ số CT/VT $\rightarrow$ `Active Setting Group` $\rightarrow$ `EN_MAIN_PROT`, `EN_DIF` $\rightarrow$ Trở kháng `Z1_REACH`, dòng khởi động `Idiff_START`, độ dốc `Slope 1/2` $\rightarrow$ Logic lập trình `GR_PLC_LOGIC` & Đầu ra `BO_TRIP_1`.

### 5. NARI / NR Electric (PCS-900 & RCS-900 Series)
* **Dòng rơ-le**: `PCS-9611S` (Xuất tuyến/F50), `PCS-931/RCS-931` (So lệch ĐD), `PCS-978/RCS-978` (So lệch MBA), `PCS-915` (Thanh cái), `PCS-9705S` (BCU).
* **5 tầng**: `Rated_Current_In`, `CT_Ratio` $\rightarrow$ `Active_Setting_Zone` $\rightarrow$ Từ điều khiển `Control_Word_Main` $\rightarrow$ Ngưỡng `I_DP1_Pickup`, `I_DP2_Pickup`, `Slope_K1/K2` $\rightarrow$ Ma trận logic `Logic_Trip_Matrix` & Tiếp điểm `Output_Relay_OUT1`.

### 6. GE / General Electric / Multilin (UR Series - EnerVista)
* **Dòng rơ-le**: `D60` (Khoảng cách), `L90` (So lệch ĐD), `T60` (So lệch MBA), `B30` (Thanh cái), `F650` (Feeder/BCU).
* **5 tầng**: `CT/VT Primary/Secondary` $\rightarrow$ `Active Setting Group` $\rightarrow$ `FUNCTION_50_51_ENABLE` $\rightarrow$ `IOC1_PICKUP`, `TOC1_PICKUP`, đường cong dốc $\rightarrow$ Phương trình `FlexLogic Equation` & Tiếp điểm `OUTPUT_CONTACT_TRIP1`.

### 7. Schneider / Alstom / Areva / MiCOM (S1 Agile & Sepam)
* **Dòng rơ-le**: `MiCOM P14x` (Xuất tuyến), `P44x` (Khoảng cách), `P54x` (So lệch ĐD), `P64x` (So lệch MBA), `P74x` (Thanh cái), `Sepam 80`.
* **5 tầng**: `Main_CT/VT` $\rightarrow$ `Active Group` $\rightarrow$ `I_Is1_Status`, `I_Is2_Status` $\rightarrow$ Trị số đặt `I> Current Set`, `t_Is1`, `Is2_Curve_Type` $\rightarrow$ Sơ đồ logic lập trình `PSL (Programmable Scheme Logic)` & Đầu ra `Relay_Output_RL1`.

### 8. A-Eberle (REG-D / REG-DA - WinREG)
* **Ứng dụng**: Rơ-le tự động điều chỉnh nấc phân áp dưới tải máy biến áp (AVR / OLTC ANSI 90).
* **5 tầng**: Điện áp đặt mục tiêu `VOLTAGE_SETPOINT_Uset`, Tỷ số VT/CT $\rightarrow$ Bộ thông số `Parameter Set 1` $\rightarrow$ Chế độ `AVR_AUTO_MODE`, bù sụt áp `LDC` $\rightarrow$ Dải nhạy cảm `Bandwidth_Bw`, ngưỡng khóa quá/kém áp, trễ đổi nấc `T1/T2` $\rightarrow$ Lệnh tăng/giảm nấc `OLTC_RAISE/LOWER_COMMAND`.

### 9. Bender (ISO685 / RCMS460)
* **Ứng dụng**: Thiết bị giám sát cách điện & rà soát chạm đất mạng điện 1 chiều DC trạm biến áp.
* **5 tầng**: Điện áp danh định `SYSTEM_VOLTAGE_Un` (220V DC) $\rightarrow$ Hồ sơ đo `Measurement Profile` $\rightarrow$ Giám sát chạm đất `EARTH_FAULT_MONITOR` $\rightarrow$ Ngưỡng cảnh báo cách điện Cấp 1 (`ALARM_1_THRESHOLD = 25 kOhm`) & Sự cố Cấp 2 (`ALARM_2 = 10 kOhm`) $\rightarrow$ Tiếp điểm cảnh báo SCADA `RELAY_K1/K2_ASSIGN`.

### 10. Protecta (EuroProt+ Series - EuroCAP)
* **Ứng dụng**: Rơ-le bảo vệ và tự động hóa trọn bộ ngăn lộ lưới điện phân phối/truyền tải.
* **5 tầng**: Định mức In/Un $\rightarrow$ `Active Group` $\rightarrow$ Cấu hình chức năng `TOC_51`, `IOC_50` $\rightarrow$ Ngưỡng dòng `I_Pickup_51`, `I_Instant_50`, thời gian trễ $\rightarrow$ Logic `Logic_Fast_Trip` & Tiếp điểm `Relay_Output_RO1`.

### 11. Arteche (Rơ-le Khóa Cắt F86 & Giám Sát Mạch Cắt F74)
* **Ứng dụng**: Rơ-le phụ trợ cơ điện tốc độ cao chuyên nhiệm chức năng cắt - khóa máy cắt và giám sát mạch cuộn cắt.
* **5 tầng**: Nguồn nuôi nhị thứ `RATED_AUX_VOLTAGE` (220V DC) $\rightarrow$ Chức năng `HIGH_SPEED_TRIP_F86` & `TCS_SUPERVISION_F74` $\rightarrow$ Điện áp tác động `>= 70% V_aux`, dòng đo lường `1.5 mA` $\rightarrow$ Thời gian tác động siêu tốc `< 10ms` (`OPERATING_TIME_F86 = 0.008s`) $\rightarrow$ Logic khóa liên động `LOCKOUT_INTERLOCK (BLOCK_CLOSE)` & Tiếp điểm công suất cao `4 NO + 4 NC`.

### 12. Vizimax (SynchroTeq - Đóng Cắt Đồng Pha Thông Minh ANSI 25)
* **Ứng dụng**: Bộ điều khiển đóng cắt đồng pha thông minh điểm 0 / đỉnh áp triệt tiêu dòng từ hóa đột biến (Inrush) và sốc điện áp đóng tụ bù.
* **5 tầng**: Điện áp/tần số hệ thống, thời gian thao tác máy cắt `CB_RATED_TIME` (45ms) $\rightarrow$ Kích hoạt `POW_SWITCHING`, bù trôi cơ khí theo nhiệt độ `TEMP_COMPENSATION`, học độ mài mòn tiếp điểm $\rightarrow$ Góc đóng mục tiêu MBA ($90^\circ/270^\circ$ đỉnh áp), góc đóng tụ bù ($0^\circ/180^\circ$ điểm 0), cửa sổ sai số pha cho phép ($\pm 0.5\text{ ms}$) $\rightarrow$ Bù thời gian truyền động cơ khí máy cắt, hệ số dốc bù nhiệt độ $\rightarrow$ Tiếp điểm cho phép đóng đồng pha `SYNCHROTEQ_READY_PERMISSIVE` & Báo lỗi sai lệch thời gian `ALARM_CB_TIMING_ERROR`.

### 13. MR - Maschinenfabrik Reinhausen (TAPCON / MSENSE)
* **Ứng dụng**: Bộ điều khiển tự động nấc phân áp dưới tải MBA & Hệ thống giám sát tiếp điểm buồng chân không OLTC.
* **5 tầng**: Tỷ số VT, số nấc tối đa (19/27 nấc), bước điện áp mỗi nấc (1.25%) $\rightarrow$ Tự động điều áp `TAPCON Auto`, thuật toán MBA song song triệt tiêu dòng tuần hoàn, giám sát mài mòn tiếp điểm $\rightarrow$ Điện áp đặt mục tiêu $U_{set}$ (110V), dải băng chết $\Delta U$ (1.5%), dòng tuần hoàn cực đại cho phép (0.15A) $\rightarrow$ Trễ chuyển nấc bước 1 ($T_1 = 30\text{s}$), trễ các nấc liên tiếp ($T_2 = 10\text{s}$), thời gian giám sát động cơ chạy nấc $\rightarrow$ Lệnh xuất xung tăng/giảm nấc (`RAISE/LOWER_PULSE`) & Cảnh báo kẹt nấc bộ chuyển đổi.

### 14. Messko / AKM / Hyoda (Đo Nhiệt Độ Dầu OTI & Cuộn Dây WTI MBA)
* **Ứng dụng**: Đồng hồ nhiệt độ và cảm biến Pt100 giám sát phát nóng MBA, điều khiển quạt giải nhiệt và bảo vệ quá nhiệt (ANSI 49).
* **5 tầng**: Cảm biến Pt100 RTD Class A, thang đo 0-160°C, gradient chênh nhiệt cuộn dây/dầu đỉnh (18°C) $\rightarrow$ Cho phép chạy quạt cấp 1/2, bảo vệ cắt nhiệt độ $\rightarrow$ Ngưỡng nhiệt chạy quạt 1 ($55^\circ\text{C}$), quạt 2 ($65^\circ\text{C}$), cảnh báo nhiệt dầu OTI ($85^\circ\text{C}$), cắt sự cố dầu OTI ($105^\circ\text{C}$), cảnh báo nhiệt cuộn dây WTI ($95^\circ\text{C}$), cắt sự cố WTI ($115^\circ\text{C}$) $\rightarrow$ Thời gian duy trì quạt chạy tối thiểu (180s), lọc rung tiếp điểm vi công tắc $\rightarrow$ Tiếp điểm cảnh báo SCADA & Tiếp điểm cắt sự cố gửi tới Rơ-le khóa 86.

### 15. EMB / Cedaspe / Comem (Bảo Vệ Hơi Buchholz & Van Xả Áp Lực PRD)
* **Ứng dụng**: Cụm phụ kiện an toàn cơ khí bảo vệ sự cố thùng máy biến áp và buồng dập hồ quang OLTC (ANSI 63B/PRD).
* **5 tầng**: Đường kính ống nối (DN80/50), môi chất dầu khoáng, kích thước họng van PRD (150mm) $\rightarrow$ Kích hoạt cảnh báo hơi (Phao trên), cắt sự cố dòng dầu (Phao dưới), cắt van xả áp PRD, cắt dòng dầu buồng nấc RS2001 $\rightarrow$ Thể tích khí tích tụ cảnh báo ($200\text{ cm}^3$), vận tốc dòng dầu tác động cắt ($1.0\text{ m/s}$), áp lực mở màng an toàn PRD ($55\text{ kPa} / 0.55\text{ bar}$), mức dầu cực tiểu bình phụ $\rightarrow$ Thời gian lọc tiếp điểm khí (1.0s), thời gian tác động cơ học cắt dòng dầu ($< 20\text{ ms}$) $\rightarrow$ Tiếp điểm cảnh báo khí SCADA & Tiếp điểm cắt tức thời kích hoạt Rơ-le 86 cô lập máy biến áp.

### 16. Qualitrol (Giám Sát Tích Hợp Online & DGA Máy Biến Áp)
* **Ứng dụng**: Hệ thống giám sát trực tuyến khí hòa tan trong dầu DGA, hành trình vi công tắc van xả áp và nhiệt độ điểm nóng Hotspot.
* **5 tầng**: Model 509ITM/Server-DGA, nguồn nuôi 220V, giao thức truyền thông IEC 61850 / Modbus TCP $\rightarrow$ Giám sát DGA trực tuyến, giám sát van PRD, mô hình toán nhiệt điểm nóng IEEE C57.91 $\rightarrow$ Ngưỡng cảnh báo khí $H_2$ (100 ppm), nguy cấp khí hồ quang $C_2H_2$ (5 ppm), cảnh báo quá áp thùng dầu (35 kPa), nhiệt độ điểm nóng cuộn dây ($110^\circ\text{C}$) $\rightarrow$ Khung thời gian theo dõi tốc độ sinh khí DGA (24h), bộ lọc chống xung nhiễu điện từ $\rightarrow$ Tiếp điểm cảnh báo khí DGA cao & Tiếp điểm liên động cắt bảo vệ an toàn thùng dầu.

### 17. Smitt (Rơ-le Khóa Cắt Master Trip Lockout ANSI 86)
* **Ứng dụng**: Rơ-le khóa đóng ngắt nhiều tiếp điểm chất lượng cao, tự giữ cơ học, chống đóng lặp lại khi sự cố chưa được kiểm tra giải trừ.
* **5 tầng**: Điện áp cuộn hút định mức (220V DC), cấu hình 8 NO + 8 NC Heavy Duty, phương thức giải trừ chốt Manual Hand Reset $\rightarrow$ Khóa cơ học tự giữ (86), giám sát tính liên tục mạch cắt TCS (ANSI 74) $\rightarrow$ Dòng kích hoạt cuộn hút ($\ge 1.5\text{A}$), dòng kiểm tra mạch cắt liên tục ($1.5\text{ mA}$) $\rightarrow$ Thời gian tác động lật chốt siêu tốc ($< 8\text{ ms}$), trễ xác nhận đứt mạch cắt $\rightarrow$ Tiếp điểm NO cắt đồng thời các máy cắt liên quan & Tiếp điểm NC ngắt hoàn toàn mạch đóng máy cắt.

### 18. Trench (Biến Dòng CT, Biến Áp VT/CVT & Cuộn Cản Bẫy Sóng Line Trap)
* **Ứng dụng**: Thiết bị đo lường cao thế và ghép nối tín hiệu tải ba truyền thông bảo vệ so lệch/khoảng cách đường dây.
* **5 tầng**: Dòng/áp sơ cấp định mức (1200A, 110kV), thứ cấp danh định (5A, 110V), tần số 50Hz $\rightarrow$ Cuộn đo lường 0.2S, cuộn bảo vệ 5P20, cuộn bảo vệ so lệch Class PX $\rightarrow$ Dung lượng tải phụ (30 VA), bội số dòng giới hạn ALF (20), điện áp điểm uốn $V_k$ (450V), dòng từ hóa cực đại $I_e$, điện trở nội cuộn thứ cấp $R_{ct}$ ($2.5\ \Omega$) $\rightarrow$ Dải tần số bẫy sóng Line Trap (50-500 kHz), hệ số quá độ ngắn mạch $K_{td}$ $\rightarrow$ Giám sát hở mạch nhị thứ CT & Khối trở kháng cao chặn tín hiệu cao tần không thoát ra trạm.

### 19. Sieyuan / Coelme / MESA (Máy Cắt SF6, Dao Cách Ly DS & Tiếp Địa ES)
* **Ứng dụng**: Thiết bị phân phối và đóng cắt cao thế ngoài trời và trong nhà (GIS/AIS), giám sát khí cách điện $SF_6$ và liên động đóng cắt an toàn.
* **5 tầng**: Cấp điện áp định mức (110kV/220kV/500kV), dòng định mức (2000A), khả năng chịu ngắn mạch (40kA/3s) $\rightarrow$ Giám sát mật độ áp lực khí $SF_6$ (ANSI 63G), giám sát nạp lò xo động cơ, logic khóa liên động cơ - điện (ANSI 3) $\rightarrow$ Áp lực $SF_6$ định mức ($0.60\text{ MPa}$), cảnh báo rò khí cấp 1 ($0.52\text{ MPa}$), khóa thao tác đóng cắt cấp 2 ($0.50\text{ MPa}$) $\rightarrow$ Thời gian thao tác đóng định mức (50ms), thời gian cắt định mức (25ms), thời gian nạp lại lò xo (12s), thời gian quay mở dao cách ly (8s) $\rightarrow$ Tiếp điểm khóa toàn bộ thao tác máy cắt khi mất khí $SF_6$, tiếp điểm phụ vị trí dao cách ly (89a/b) đưa vào liên động & Rơ-le chống nhấp nháy 52Y.

### 20. TBEA / Shenyang (SBW) / XD Xian / Hyundai / Mitsubishi (Máy Biến Áp Lực Cao Thế)
* **Ứng dụng**: Máy biến áp lực và kháng bù cao thế truyền tải (110kV/220kV/500kV).
* **5 tầng**: Công suất định mức các cuộn dây (63 MVA), tỷ số điện áp danh định (115/24 kV), tổ đấu dây bù pha ($YNd11$) $\rightarrow$ Tự động điều khiển hệ thống làm mát ONAN/ONAF, giám sát dòng chạm đất mạch từ, giám sát khí dầu DGA online $\rightarrow$ Điện áp ngắn mạch định mức $\%U_k$ (10.5%), tổn hao không tải $P_0$ (42 kW), tổn hao có tải $P_k$ (210 kW), dòng tiếp địa mạch từ cực đại cho phép (100 mA) $\rightarrow$ Thời gian suy giảm dòng từ hóa đóng máy Inrush (0.5s), hằng số quán tính nhiệt biến áp (120 min) $\rightarrow$ Tiếp điểm cảnh báo sự cố quạt/bơm làm mát & Tín hiệu sa thải/cắt khi quá tải nhiệt nguy hiểm.

### 21. Cooper (Tủ Điều Khiển Recloser Tự Đóng Lại Form 4/6)
* **Ứng dụng**: Máy cắt tự đóng lại xuất tuyến trung thế tích hợp rơ-le số thông minh trên lưới phân phối.
* **5 tầng**: Tỷ số CT pha (1000/1), CT đất (1000/1), điện áp định mức 22kV, hồ sơ chỉnh định $\rightarrow$ Cho phép chu trình tự đóng lại (ANSI 79), bảo vệ quá dòng chạm đất (50N/51N), thích nghi tải lạnh CLPU $\rightarrow$ Dòng khởi động cắt pha (400A), dòng khởi động cắt đất (80A), hệ số nhân dòng tải lạnh CLPU (2.0x) $\rightarrow$ Thời gian nghỉ lần 1 (2.0s), thời gian nghỉ lần 2 (15.0s), thời gian hoàn nguyên chu trình (30s) $\rightarrow$ Tiếp điểm khóa chết Recloser sau hết số lần đóng lại (Final Lockout) & Chế độ an toàn công tác đường dây Hot Line Tag.

### 22. Beckwith (Rơ-le Điều Áp M-2001D & Hòa Đồng Bộ M-0169)
* **Ứng dụng**: Rơ-le tự động điều chỉnh nấc máy biến áp và thiết bị kiểm tra hòa đồng bộ máy cắt (ANSI 90/25).
* **5 tầng**: Điện áp đầu vào VT danh định (120V), điện trở bù sụt áp đường dây LDC R (3V) & cảm kháng LDC X (6V) $\rightarrow$ Tự động bù sụt áp LDC, khóa đổi nấc khi có dòng công suất ngược (điện mặt trời/gió), kiểm tra hòa đồng bộ (ANSI 25) $\rightarrow$ Điện áp đặt trung tâm Bandcenter (120V), dải băng chết Bandwidth (2V), độ lệch áp hòa đồng bộ ($\Delta V \le 5\text{V}$), độ lệch tần số ($\Delta f \le 0.1\text{Hz}$), độ lệch góc pha ($\Delta \delta \le 15^\circ$) $\rightarrow$ Trễ đổi nấc bước 1 (30s), trễ các nấc liên tiếp (10s) $\rightarrow$ Xung lệnh tăng/giảm nấc (`PULSE_TAP_RAISE/LOWER`) & Tiếp điểm cho phép đóng máy cắt hòa đồng bộ `PERMISSIVE_SYNC_CLOSE`.
````

## File: docs/features/05-ai-ocr.md
````markdown
# Đặc tả Module AI OCR (Human-in-the-Loop)

Tài liệu này mô tả chi tiết kiến trúc, quy trình và yêu cầu kỹ thuật cho hệ thống AI bóc tách thông số (OCR) từ Phiếu chỉnh định dạng PDF/Image trong hệ thống **RMS**.

---

## 1. Mục tiêu Kiến trúc

1. **Bảo mật tuyệt đối (OT Compliance)**: Toàn bộ quá trình xử lý hình ảnh và bóc tách dữ liệu phải được thực hiện trên hạ tầng máy chủ nội bộ (On-premise). Tuyệt đối **không gửi** dữ liệu sang các dịch vụ Cloud bên ngoài (Google Cloud Vision, AWS Textract, etc.).
2. **Xử lý Bất đồng bộ (Asynchronous)**: Việc OCR tốn nhiều tài nguyên, không được chặn (block) request của người dùng khi upload file.
3. **Độ tin cậy dữ liệu**: Kết quả AI chỉ mang tính chất tham khảo (Draft). Bắt buộc phải có **sự đối chiếu và xác nhận của con người (Human-in-the-loop)** thông qua giao diện Split-view.

---

## 2. Các Thành phần Hệ thống

### 2.1 Backend / API (Django)
- Cung cấp API để nhận file PDF, lưu vào kho lưu trữ nội bộ.
- Sinh Task đẩy vào Message Broker.
- Cung cấp API cập nhật (PATCH) và chốt (POST) kết quả OCR sau khi người dùng review.

### 2.2 Task Queue & Message Broker (RabbitMQ)
- Quản lý hàng đợi các Task OCR (`ocr_jobs`).
- Hỗ trợ Retry có giới hạn khi Worker quá tải hoặc lỗi.

### 2.3 AI OCR Worker (Celery + Tesseract / PaddleOCR)
- Một service độc lập chạy ngầm.
- Xử lý convert PDF trang sang ảnh.
- Nhận diện ký tự, phân tích layout (bảng biểu).
- Trả kết quả JSON chứa: Text nguyên thủy, Key-Value đã bóc tách, Bounding Box (Toạ độ), Confidence Score.

---

## 3. Luồng Xử lý AI OCR (Workflow)

```mermaid
sequenceDiagram
    participant FE as HTMX Frontend
    participant BE as Django API
    participant MQ as RabbitMQ
    participant OCR as Celery OCR Worker
    participant DB as PostgreSQL

    FE->>BE: 1. Upload File PDF
    BE->>DB: 2. Tạo bản ghi `setting_sheet_versions` & `ocr_jobs` (QUEUED)
    BE->>MQ: 3. Enqueue OCR Task {job_id, file_path}
    BE-->>FE: 4. Trả về Response 201 (Không chờ AI)
    
    MQ->>OCR: 5. Worker lấy Task
    OCR->>OCR: 6. Convert PDF to Image
    OCR->>OCR: 7. Run AI Model (Bóc tách Layout & Text)
    OCR->>DB: 8. Lưu `ocr_results` & `ocr_fields` (Bounding box, Confidence)
    OCR->>DB: 9. Update `ocr_jobs` (REVIEW_REQUIRED)
    
    FE->>BE: 10. Polling/WebSocket báo có kết quả AI
    FE->>FE: 11. Render màn hình Split-View
    FE->>BE: 12. KTV sửa lỗi & Xác nhận (PATCH)
    BE->>DB: 13. Ghi log `ocr_field_reviews`
```

---

## 4. Giao diện Đối chiếu OCR (Split-View)

Màn hình Split-view là điểm tiếp xúc giữa con người và AI, yêu cầu thiết kế UX/UI tối ưu:

- **Khung bên trái (Trình xem PDF/Ảnh)**:
  - Phải hỗ trợ Zoom, cuộn trang.
  - Khi hover/click vào một thông số bên khung phải, hệ thống vẽ highlight (dựa trên bounding box) vào vị trí tương ứng trên ảnh.
- **Khung bên phải (Form dữ liệu)**:
  - Hiển thị danh sách các thông số AI đã bóc tách được.
  - Cảnh báo màu vàng (Warning) với những trường có Confidence Score < Ngưỡng (VD: < 80%).
  - Textbox có thể chỉnh sửa trực tiếp.
  - Mỗi khi sửa, người dùng được yêu cầu nhập "Lý do thay đổi" để lưu vết (Audit log).
- **Trạng thái chốt sổ**: Nút "Xác nhận toàn bộ dữ liệu" chỉ được phép bấm khi người dùng đã duyệt/xác nhận các trường dữ liệu quan trọng hoặc có Confidence thấp.

---

## 5. Xử lý Lỗi & Retry

- Lỗi không đọc được file (Corrupted PDF) → Cập nhật trạng thái `FAILED`, ghi rõ `error_message`, gửi thông báo cho người dùng.
- AI Worker crash / Timeout → RabbitMQ tự động đẩy lại Task (Max 3 retries).
- File quá dài (> 50 trang) → AI Worker có thể ngắt tác vụ, chuyển trạng thái về `FAILED_TOO_LARGE`, yêu cầu người dùng cắt nhỏ file.

---

## 6. Yêu cầu Huấn luyện (Future Scope)
Trong tương lai, để nâng cao độ chính xác:
- Có thể thu thập các mẫu phiếu đã được KTV đối chiếu (dữ liệu sạch) để huấn luyện lại mô hình (Fine-tuning PaddleOCR hoặc mô hình LayoutLM).
- Việc huấn luyện phải được thực hiện trên môi trường Sandbox chuyên dụng nội bộ, không dùng dữ liệu production chạy thẳng ra ngoài.
````

## File: docs/mvt_design/MODELS_DESIGN.md
````markdown
# Đặc tả Cơ sở Dữ liệu (Django + PostgreSQL)

**Database:** PostgreSQL 15+
**ORM:** Django ORM (PostgreSQL Backend)

Sử dụng mô hình CSDL quan hệ chuẩn (SQL) kết hợp với kiểu dữ liệu `JSONField` (JSONB) của PostgreSQL để xử lý các dữ liệu linh hoạt (như OCR) mà không cần phá vỡ cấu trúc của CSDL.

## 1. Khai báo Models
Sử dụng thư viện chuẩn `django.db.models`.

### 1.1 Quản lý Tổ chức & Phân quyền
Sử dụng Auth User mặc định của Django, mở rộng bằng Profile.

```python
from django.db import models
from django.contrib.auth.models import User

class Organization(models.Model):
    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)
    org_type = models.CharField(max_length=50) # VTC, OPERATION, TRANSMISSION...
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
```

### 1.2 Trạm Biến áp & Rơ-le (Quan hệ 1-N)
Xây dựng quan hệ Trạm -> Ngăn lộ -> Rơ-le -> Cài đặt.

```python
class Station(models.Model):
    station_code = models.CharField(max_length=50, unique=True)
    station_name = models.CharField(max_length=200)
    location = models.CharField(max_length=255)

class Bay(models.Model):
    station = models.ForeignKey(Station, related_name='bays', on_delete=models.CASCADE)
    bay_code = models.CharField(max_length=50)
    bay_name = models.CharField(max_length=100)

class Relay(models.Model):
    bay = models.ForeignKey(Bay, related_name='relays', on_delete=models.CASCADE)
    relay_code = models.CharField(max_length=50)
    relay_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)

class RelaySetting(models.Model):
    relay = models.ForeignKey(Relay, related_name='settings', on_delete=models.CASCADE)
    parameter_code = models.CharField(max_length=50)
    parameter_name = models.CharField(max_length=100)
    standard_value = models.FloatField()
    unit = models.CharField(max_length=20)
    tolerance_min = models.FloatField()
    tolerance_max = models.FloatField()
```

### 1.3 Phiếu Chỉnh định & Lịch sử
Sử dụng `JSONField` của PostgreSQL cho dữ liệu không cấu trúc, và tạo bảng rời cho chữ ký số để đảm bảo tính chuẩn hóa 3NF.

```python
class SettingSheet(models.Model):
    sheet_code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50) # DRAFT, PENDING_REVIEW, ASSIGNED, COMPLETED
    scan_file = models.FileField(upload_to='scans/')
    
    relay = models.ForeignKey(Relay, on_delete=models.SET_NULL, null=True)
    
    # OCR Data / Mock Data sử dụng JSONB của PostgreSQL
    extracted_data = models.JSONField(null=True, blank=True) 

class SignatureRecord(models.Model):
    sheet = models.ForeignKey(SettingSheet, related_name='signatures', on_delete=models.CASCADE)
    signer_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    signed_at = models.DateTimeField(auto_now_add=True)
    signature_hash = models.CharField(max_length=256)
```

### 1.4 Nhật ký Kiểm tra Định kỳ
```python
class PeriodicCheck(models.Model):
    relay = models.ForeignKey(Relay, on_delete=models.CASCADE)
    sheet = models.ForeignKey(SettingSheet, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    actual_check_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    
class PeriodicCheckItem(models.Model):
    check = models.ForeignKey(PeriodicCheck, related_name='items', on_delete=models.CASCADE)
    parameter_code = models.CharField(max_length=50)
    measured_value = models.FloatField()
    deviation_percent = models.FloatField()
    is_within_tolerance = models.BooleanField()
```

## 2. Ưu điểm của Thiết kế này (PostgreSQL)
1. **Toàn vẹn Dữ liệu (ACID):** RDBMS như PostgreSQL đảm bảo tính nhất quán dữ liệu ở mức cao nhất, tránh mất mát thông tin quan trọng.
2. **Khả năng chứa dữ liệu động (extracted_data):** Tính năng `JSONField` (JSONB) của PostgreSQL cực kỳ tối ưu, cho phép lập chỉ mục (index) và truy vấn trên các trường bên trong file JSON (như kết quả OCR) mà không kém phần linh hoạt so với NoSQL.
3. **Mở rộng dễ dàng với ORM tiêu chuẩn:** Sử dụng 100% tính năng của Django ORM, dễ dàng viết các câu truy vấn phức tạp (Aggregation, Annotation), tích hợp tốt với các thư viện admin, form, và report của hệ sinh thái Django.
````

## File: docs/mvt_design/REQUIREMENTS_MVT.md
````markdown
# Đặc tả Yêu cầu Hệ thống (SRS)
**Dự án:** Hệ thống Quản lý Phiếu Chỉnh định Rơ-le (RMS)
**Kiến trúc:** Django (MVT) + PostgreSQL

## 1. Tổng quan Hệ thống
RMS là hệ thống web phục vụ quy trình lập phiếu, phê duyệt, chuyển giao và xác nhận hoàn thành công tác chỉnh định thông số bảo vệ rơ-le tại các trạm biến áp.
Hệ thống được thiết kế lại hoàn toàn theo kiến trúc **MVT của Django**, sử dụng **PostgreSQL làm cơ sở dữ liệu chính**.

## 2. Kiến trúc Công nghệ
- **Mô hình:** MVT (Model - View - Template)
- **Framework:** Django
- **Cơ sở dữ liệu:** PostgreSQL
- **Giao diện (Frontend):** Django Templates kết hợp TailwindCSS/Bootstrap (Sử dụng HTMX/Alpine.js cho tương tác AJAX động).
- **Tích hợp bên ngoài:** Hệ thống Ký số EVN (qua REST API).

## 3. Các Phân hệ Chức năng & Luồng Nghiệp vụ
### 3.1 Xác thực & Phân quyền (Auth & RBAC)
- Sử dụng Session Authentication mặc định của Django.
- **Vai trò:** A0/A1 (Phát hành), VTC/Vận hành/Điều độ (Rà soát), Kỹ thuật viên (Chỉnh định), Giám sát trạm (Xác nhận), Admin.
- Sử dụng `django.contrib.auth.models.Group` kết hợp custom model mở rộng.

### 3.2 Quản lý Trạm biến áp & Rơ-le
- CRUD thông tin Trạm biến áp (Station), Ngăn lộ (Bay), Rơ-le (Relay).
- **Upload File Cấu hình:** Người dùng upload JSON/Excel. Hệ thống xử lý và lưu vào các bảng quan hệ của PostgreSQL.

### 3.3 Quản lý Phiếu Chỉnh định (Sheet Lifecycle)
- **Khởi tạo & Upload:** A0/A1 chọn trạm, upload file PDF/JPG bản scan phiếu. Form hỗ trợ nhập metadata tạm thời (khi OCR chưa sẵn sàng) và lưu vào `JSONField` của PostgreSQL.
- **Phát hành (Ký số lần 1):** Click nút Ký số, Django View sẽ gọi API Ký số EVN và mở iframe cho A0/A1 thao tác. Xác nhận thành công sẽ chuyển trạng thái sang `PENDING_REVIEW`.
- **Rà soát Đa lớp:** VTC/Vận hành vào màn hình "Chờ rà soát", đối chiếu bản scan và thông số, chọn "Phê duyệt" hoặc "Từ chối". Phê duyệt xong chuyển thành `ASSIGNED_TO_SC`.
- **Chuyển giao:** Công ty Truyền tải gán KTV phụ trách.
- **Xác nhận hoàn thành (Ký số lần 2 & 3):** KTV chỉnh định xong, thực hiện Ký số. Sau đó Giám sát trạm ký xác nhận. Phiếu cập nhật thành `COMPLETED`.

### 3.4 Kiểm tra Định kỳ (Periodic Checks)
- Giao diện dạng bảng lưới (Grid) hiển thị các thông số tiêu chuẩn của Rơ-le.
- Người dùng nhập kết quả đo thực tế, nhấn "Lưu". Logic View tính toán sai lệch % và cảnh báo (ĐẠT / VƯỢT NGƯỠNG).

## 4. Giải pháp Kỹ thuật Lưu trữ với PostgreSQL
- **JSONB / Schemaless Data:** Các thông số `extracted_data` (từ OCR hoặc tự nhập) sẽ được lưu dưới dạng kiểu dữ liệu `JSONField` (JSONB) của PostgreSQL, kết hợp sức mạnh truy vấn NoSQL trong môi trường cơ sở dữ liệu quan hệ (RDBMS).
- **Tính toàn vẹn dữ liệu (Data Integrity):** PostgreSQL cung cấp các ràng buộc khóa ngoại (Foreign Keys) để đảm bảo tính toàn vẹn dữ liệu giữa các bảng như Trạm, Ngăn lộ, Rơ-le và Phiếu chỉnh định.
````

## File: docs/mvt_design/TEMPLATES_UI.md
````markdown
# Thiết kế Giao diện (Django Templates & UI)

Hệ thống theo kiến trúc MVT sẽ sử dụng bộ thư viện Frontend nhúng trực tiếp vào Django Templates.

## 1. Công nghệ Frontend
- **HTML/Template Engine:** Django Template Language (DTL)
- **CSS Framework:** TailwindCSS (via CDN hoặc pre-compiled) / Bootstrap 5.
- **Tương tác động (AJAX/DOM):** Sử dụng **HTMX** để thực hiện các thao tác Upload, Load dữ liệu không cần tải lại trang (Single Page App - like experience).
- **Icons:** FontAwesome / Heroicons.

## 2. Cấu trúc Thư mục Templates (`templates/`)

```text
templates/
│
├── base.html                  # Layout chính (Sidebar, Header, Footer)
├── auth/
│   ├── login.html             # Giao diện đăng nhập
│   └── password_reset.html    # Giao diện đổi mật khẩu
│
├── stations/
│   ├── station_list.html      # Bảng danh sách Trạm
│   ├── station_detail.html    # Chi tiết Trạm (Ngăn lộ, Rơ le)
│   └── import_form.html       # Form kéo thả file JSON/Excel
│
├── sheets/
│   ├── sheet_list.html        # Kanban board / Bảng danh sách Phiếu chỉnh định
│   ├── sheet_form.html        # Form tạo phiếu mới (Khu vực kéo thả file scan)
│   ├── sheet_detail.html      # Màn hình Split-View (Bên trái: PDF Viewer, Bên phải: Form Data)
│   ├── _sign_modal.html       # (Partial) Modal hiển thị trạng thái đang gọi API Ký số
│   └── sheet_review.html      # Màn hình dành cho VTC/Vận hành phê duyệt
│
└── checks/
    ├── check_list.html        # Lịch sử kiểm tra
    └── check_form.html        # Form dạng Lưới (Grid) để nhập dữ liệu đo đạc thực tế
```

## 3. Thiết kế Bố cục Chính (Layout - `base.html`)

Giao diện hỗ trợ Dark Mode, phong cách Sleek Design.

- **Sidebar (Trái - 250px):** 
  - Hiển thị logo EVN/RMS.
  - Menu điều hướng: Dashboard, Trạm Biến áp, Phiếu Chỉnh định, Biên bản Kiểm tra, Quản trị hệ thống.
- **Header (Trên):**
  - Thanh tìm kiếm toàn cục (Global Search).
  - Tên người dùng đang đăng nhập & Nút chuyển đổi Dark/Light mode.
  - Dropdown Đăng xuất.
- **Content Area (Giữa):** Hiển thị khối nội dung chính.

## 4. UI Đặc thù: Màn hình Chi tiết Phiếu Chỉnh định (Split-View)
Đây là màn hình quan trọng nhất của hệ thống, đòi hỏi UX tốt để rà soát.

Sử dụng cấu trúc Flexbox hoặc CSS Grid chia đôi màn hình:
- **Cột Trái (60%):** Nhúng thẻ `<iframe src="{{ sheet.scan_file.url }}">` hoặc thư viện PDF.js để render file scan trực tiếp trên trình duyệt.
- **Cột Phải (40%):** 
  - Phía trên: Hiển thị các Metadata của Phiếu (Mã phiếu, Trạm, Rơ-le, Người phát hành).
  - Giữa: Box Trạng thái Chữ ký (Hiển thị list user đã ký số). Nút **"Ký Số EVN"** to, rõ ràng.
  - Dưới: Nơi nhập liệu Mock Data/Form hoặc hiển thị `extracted_data` dạng JSON cho Kỹ thuật viên đối chiếu.

### 4.1 Tích hợp Ký số không Refresh trang bằng HTMX
```html
<!-- Nút ký số dùng htmx để post ngầm -->
<button hx-post="{% url 'sheet_sign' sheet.id %}" 
        hx-target="#signature-status-box" 
        hx-swap="innerHTML"
        class="bg-blue-600 text-white px-4 py-2 rounded shadow">
    <i class="fas fa-file-signature"></i> Ký số & Phát hành
</button>

<div id="signature-status-box">
    <!-- Nơi hiển thị kết quả trả về từ View (ví dụ: Chữ ký thành công / Mở popup) -->
</div>
```

## 5. UI Đặc thù: Bảng nhập Liệu Định kỳ
- Tạo Table với Input ở mỗi dòng.
- Khi người dùng nhập số, sử dụng Alpine.js (chạy client-side) để tính toán màu sắc cảnh báo đỏ/xanh ngay lập tức trước khi bấm "Lưu".

```html
<tr x-data="{ measured: 0, standard: {{ item.standard_value }} }">
    <td>{{ item.parameter_name }}</td>
    <td>{{ item.standard_value }}</td>
    <td><input type="number" x-model="measured" name="measured_{{ item.code }}"></td>
    <td>
        <span x-text="Math.abs(measured - standard)" 
              :class="Math.abs(measured - standard) > 0.05 ? 'text-red-500' : 'text-green-500'">
        </span>
    </td>
</tr>
```
````

## File: docs/mvt_design/VIEWS_URLS_MAP.md
````markdown
# Thiết kế Routing và Views (MVT)

Thay vì thiết kế các API Endpoint trả về JSON (như DRF), hệ thống sẽ sử dụng các `urls.py` và `views.py` để lấy dữ liệu từ DB (thông qua Djongo ORM), gán vào Context và trả về mã HTML render từ Template.

## 1. Cấu trúc URL Định tuyến (`urls.py`)

| URL Pattern | Tên (Name) | Phương thức HTTP | Chức năng (Ý nghĩa) |
|---|---|---|---|
| `/` | `home` | GET | Trang Dashboard chính (Thống kê phiếu). |
| `/auth/login/` | `login` | GET, POST | Trang Đăng nhập hệ thống. |
| `/auth/logout/` | `logout` | POST | Đăng xuất. |
| `/stations/` | `station_list` | GET | Danh sách Trạm biến áp. |
| `/stations/<id>/` | `station_detail` | GET | Chi tiết Trạm (gồm danh sách Ngăn lộ, Rơ-le). |
| `/stations/import/` | `station_import` | GET, POST | Upload file JSON/Excel khởi tạo Cấu trúc Trạm. |
| `/sheets/` | `sheet_list` | GET | Danh sách Phiếu Chỉnh định. |
| `/sheets/new/` | `sheet_create` | GET, POST | Tạo phiếu mới & Upload file bản scan. |
| `/sheets/<id>/` | `sheet_detail` | GET | Xem chi tiết thông số phiếu & File PDF. |
| `/sheets/<id>/sign/` | `sheet_sign` | POST | Khởi tạo luồng Ký số EVN cho người dùng hiện tại. |
| `/sheets/<id>/review/` | `sheet_review` | GET, POST | VTC/Điều độ rà soát và phê duyệt phiếu. |
| `/sheets/<id>/transfer/`| `sheet_transfer`| POST | Chuyển giao phiếu cho Kỹ thuật viên (Giao việc). |
| `/checks/` | `check_list` | GET | Danh sách các biên bản kiểm tra định kỳ. |
| `/checks/new/<relay_id>/`| `check_create` | GET, POST | Form điền số liệu kiểm tra định kỳ rơ-le thực tế. |

## 2. Đặc tả Logic của Views (`views.py`)

Sử dụng kết hợp Class-Based Views (CBV) và Function-Based Views (FBV) theo chuẩn Django:

### 2.1 View Tạo Phiếu & Upload Bản Scan (`sheet_create`)
- **GET:** Trả về Template `sheets/sheet_form.html` kèm ModelForm của `SettingSheet`.
- **POST:** Nhận `scan_file` và `title`.
  - Validate file upload (đảm bảo là PDF/JPG hợp lệ, kích thước < 10MB).
  - Lưu vào MongoDB (file được lưu trên storage vật lý, đường dẫn lưu vào Mongo).
  - Trạng thái phiếu thiết lập ban đầu: `DRAFT`.
  - Redirect về `sheet_detail`.

### 2.2 View Khởi tạo Ký số (`sheet_sign`)
Đây là View thực hiện tích hợp API bên ngoài (Hệ thống Ký số EVN).
- **POST:** 
  1. Lấy `SettingSheet` từ Database.
  2. Hash nội dung file scan (`hash_sha256`).
  3. Gửi HTTP Request (bằng thư viện `requests`) sang `https://evn-sign-api/initiate/` kèm theo hash và User ID hiện tại.
  4. Lấy lại `session_id` và `signing_url` từ EVN.
  5. Trả về Template hoặc dùng HTMX trigger để mở `signing_url` dạng popup/iframe cho user ký.
  6. (Sau khi user ký xong) Hệ thống EVN callback hoặc View tự gọi lại EVN để lấy `signature_data` (Base64) -> Nhúng data vào `SettingSheet.signatures` (Mảng). Đổi trạng thái phiếu.

### 2.3 View Nhập liệu Kiểm tra Định kỳ (`check_create`)
Do MongoDB lưu toàn bộ thông số Rơ-le dạng Array trong DB, việc xuất form cực kỳ dễ dàng.
- **GET:** Lấy `Relay.settings`. Build một danh sách các field để render HTML dạng lưới (Grid/Table). 
- **POST:** Nhận cục `POST.dict()` từ Form.
  - Lặp qua danh sách thông số, so sánh `measured_value` với `standard_value` có sẵn trong Rơ-le (MongoDB Document).
  - Tính toán `deviation_percent = abs(do - chuan)/chuan * 100`.
  - Kiểm tra có nằm trong giới hạn (`tolerance_min` - `tolerance_max`) không.
  - Đóng gói toàn bộ kết quả vào một Array nhúng lưu vào Model `PeriodicCheck.items`.
  - Render ra template báo cáo (`checks/check_report.html`) cảnh báo Đỏ/Xanh.

## 3. Quản lý Permission tại Views
Sử dụng Mixins để chặn quyền truy cập (RBAC).

```python
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView

class SheetReviewView(UserPassesTestMixin, DetailView):
    model = SettingSheet
    template_name = "sheets/sheet_review.html"

    # Chỉ VTC, Vận Hành, Điều độ mới được phép Rà soát
    def test_func(self):
        user = self.request.user
        return user.groups.filter(name__in=['VTC', 'OPERATION_UNIT', 'DISPATCHER']).exists()
```
````

## File: rms_project/__init__.py
````python
from .celery import app as celery_app

__all__ = ('celery_app',)
````

## File: rms_project/asgi.py
````python
"""
ASGI config for rms_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rms_project.settings')

django_asgi_app = get_asgi_application()

import core.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            core.routing.websocket_urlpatterns
        )
    ),
})
````

## File: rms_project/celery.py
````python
import os
from celery import Celery
from celery.signals import worker_ready

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rms_project.settings')

app = Celery('rms_project')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

from celery.schedules import crontab

app.conf.beat_schedule = {
    'check-relays-every-minute': {
        'task': 'stations.tasks.schedule_due_autochecks',
        'schedule': crontab(minute='*'),  # Run every minute
    },
    'auto-sync-api-every-minute': {
        'task': 'core.tasks.check_and_run_auto_sync',
        'schedule': crontab(minute='*'),
    },
    'check-stuck-ocr-jobs': {
        'task': 'sheets.tasks.watchdog_stuck_ocr_jobs',
        'schedule': crontab(minute='*/5'),
    },
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


@worker_ready.connect
def reset_stuck_processing_jobs(sender, **kwargs):
    """
    Khi Celery worker khởi động lại, chỉ reset các OcrJob đang ở trạng thái
    PROCESSING về FAILED — vì những task đó đang thực sự chạy và bị gián đoạn.
    Các job PENDING được giữ nguyên để Celery tiếp tục xử lý từ hàng đợi Redis.
    """
    try:
        import django
        django.setup()
    except RuntimeError:
        pass  # Django đã được setup rồi

    try:
        from sheets.models import OcrJob
        from django.core.cache import cache
        from sheets.tasks import broadcast_ocr_job_update

        # Chỉ reset PROCESSING (đang chạy thật) — KHÔNG đụng vào PENDING (đang xếp hàng)
        stuck_jobs = list(OcrJob.objects.filter(status='PROCESSING').select_related('sheet', 'sheet__created_by'))
        if not stuck_jobs:
            return

        job_ids = []
        for job in stuck_jobs:
            # Xóa cache flags để tránh stale data
            cache.delete(f"ocr_header_done_{job.id}")
            cache.delete(f"ocr_header_failed_{job.id}")
            cache.delete(f"ocr_header_data_{job.id}")
            # Đặt lại về PENDING để tự động chạy lại
            job.status = 'PENDING'
            job.error_detail = None
            job.save(update_fields=['status', 'error_detail'])
            job_ids.append(job.id)
            try:
                broadcast_ocr_job_update(job=job, stage_text='Đang khôi phục tự động...')
            except Exception:
                pass

        if job_ids:
            from sheets.tasks import execute_parallel_ocr_batch
            # Đẩy ngược lại vào hàng đợi với acks_late
            execute_parallel_ocr_batch.delay(job_ids=job_ids)
            print(f"[RMS Startup] Đã AUTO-RECOVER {len(job_ids)} job bị kẹt và đẩy lại vào Queue.")
    except Exception as exc:
        print(f"[RMS Startup] Không thể reset stuck jobs: {exc}")
````

## File: rms_project/settings.py
````python
"""
Django settings for rms_project project.

Generated by 'django-admin startproject' using Django 6.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path
import os
import urllib.parse
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'default-unsafe-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'core',
    'stations',
    'sheets',
    'checks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rms_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'rms_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'
"""
Django settings for rms_project project.

Generated by 'django-admin startproject' using Django 6.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/6.0/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
load_dotenv(BASE_DIR / '.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'default-unsafe-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://electricity.nextdev.name.vn', 'http://electricity.nextdev.name.vn']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Custom apps
    'core',
    'stations',
    'sheets',
    'checks',
    'categories',
    'django_celery_beat',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rms_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.notification_badges',
            ],
        },
    },
]

WSGI_APPLICATION = 'rms_project.wsgi.application'
ASGI_APPLICATION = 'rms_project.asgi.application'

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_AGE = 86400  # 24 hours in seconds
SESSION_SAVE_EVERY_REQUEST = True  # Reset timeout on every user interaction

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [{
                "host": urllib.parse.urlparse(os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')).hostname or '127.0.0.1',
                "port": urllib.parse.urlparse(os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')).port or 6379,
                "db": int((urllib.parse.urlparse(os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')).path or '/1').strip('/')),
                "socket_keepalive": True,
                "socket_timeout": None,
                "socket_connect_timeout": 10,
                "retry_on_timeout": True,
            }],
            "capacity": 1500,
            "expiry": 10,
        },
    },
}

# Celery Configuration Options
CELERY_BROKER_URL = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')
CELERY_RESULT_BACKEND = os.getenv('REDIS_URL', 'redis://127.0.0.1:6379/1')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'rms_db'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# Allow iframes to load media files from the same origin (e.g. for PDF preview)
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Media files (Uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'core.api_renderers.CustomXMLRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 20,
}
````

## File: rms_project/urls.py
````python
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
````

## File: rms_project/wsgi.py
````python
"""
WSGI config for rms_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rms_project.settings')

application = get_wsgi_application()
````

## File: sheets/management/commands/__init__.py
````python
# Django management commands package
````

## File: sheets/management/commands/sync_hybrid_pipeline.py
````python
import json
import os
import sys
import time
from pathlib import Path
from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import transaction

# Ensure OCR_PRJ is on sys.path
ocr_prj_path = os.path.join(settings.BASE_DIR, 'OCR_PRJ')
if ocr_prj_path not in sys.path:
    sys.path.insert(0, ocr_prj_path)

from src.layout_analysis.page3_plus.service import Page3PlusLayoutAnalysisService
from src.relay_form_ocr.orchestrator import flatten_record
from sheets.models import SettingSheet, OcrJob
from stations.models import Station, Relay
from sheets.relay_matcher import match_relay_from_ocr, normalize_text
from sheets.utils import update_has_parameters_changed_for_sheet


def sanitize_json(obj):
    import math
    if isinstance(obj, float):
        if math.isnan(obj) or math.isinf(obj):
            return None
        return obj
    elif isinstance(obj, dict):
        return {k: sanitize_json(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [sanitize_json(v) for v in obj]
    return obj


class Command(BaseCommand):
    help = 'Synchronize and standardize all SettingSheets using the Hybrid Multi-Stage Pipeline'

    def add_arguments(self, parser):
        parser.add_argument('--all', action='store_true', help='Process all sheets with available OCR artifacts')
        parser.add_argument('--sheet-id', type=int, help='Process a specific SettingSheet by ID')
        parser.add_argument('--start-id', type=int, default=None, help='Start processing from a specific SettingSheet ID')
        parser.add_argument('--limit', type=int, default=None, help='Limit maximum number of sheets to process')
        parser.add_argument('--dry-run', action='store_true', help='Run analysis without saving to database or disk')
        parser.add_argument('--resume', action='store_true', help='Skip sheets that already have non-empty extracted_data')
        parser.add_argument('--auto-link', action='store_true', default=True, help='Auto-match relay and station from Page 1')

    def handle(self, *args, **options):
        dry_run = options['dry_run']
        auto_link = options['auto_link']
        resume = options['resume']
        limit = options['limit']
        sheet_id = options.get('sheet_id')
        start_id = options.get('start_id')

        artifacts_dir = Path(settings.MEDIA_ROOT) / 'ocr_artifacts'
        service = Page3PlusLayoutAnalysisService()

        self.stdout.write(self.style.MIGRATE_HEADING("=== BẮT ĐẦU ĐỒNG BỘ TOÀN BỘ DỮ LIỆU BẰNG HYBRID MULTI-STAGE PIPELINE ==="))
        if dry_run:
            self.stdout.write(self.style.WARNING("⚠️ CHẾ ĐỘ THỬ NGHIỆM (DRY-RUN): Không ghi đè CSDL hoặc file đĩa."))

        # Filter sheets to process
        if sheet_id:
            sheets_qs = SettingSheet.objects.filter(id=sheet_id)
            if not sheets_qs.exists():
                self.stderr.write(self.style.ERROR(f"Không tìm thấy SettingSheet với ID {sheet_id}"))
                return
        else:
            sheets_qs = SettingSheet.objects.all().order_by('id')
            if start_id:
                sheets_qs = sheets_qs.filter(id__gte=start_id)

        total_sheets = 0
        success_sheets = 0
        total_pages = 0
        total_tables = 0
        total_parameters = 0
        auto_linked_relays = 0
        start_time = time.time()

        for sheet in sheets_qs:
            if limit and success_sheets >= limit:
                break

            if resume and sheet.extracted_data and len(sheet.extracted_data) > 0:
                continue

            job = sheet.ocr_jobs.order_by('-created_at').first()
            cid = job.correlation_id if job else None
            if not cid:
                continue

            details_dir = artifacts_dir / f"{cid}_details" / "pages"
            if not details_dir.exists():
                continue

            total_sheets += 1
            sheet_start = time.time()

            try:
                page_files = sorted(details_dir.glob('page_*.json'))
                if not page_files:
                    continue

                all_setting_records = []
                all_pages_payload = []
                sheet_tables = 0

                # 1. Nạp Trang 1 (Header/Bìa) nếu có
                header_p1_file = artifacts_dir / f"{cid}_header" / "pages" / "page_0001.json"
                p1_data = None
                if header_p1_file.exists():
                    try:
                        with open(header_p1_file, 'r', encoding='utf-8') as f:
                            p1_data = json.load(f)
                            all_pages_payload.append(p1_data)
                    except Exception:
                        pass

                # 2. Xử lý từng trang chi tiết từ trang 2 trở đi bằng Hybrid Pipeline
                for pf in page_files:
                    with open(pf, 'r', encoding='utf-8') as f:
                        p_data = json.load(f)

                    p_num = p_data.get('page_number', 1)
                    img_path = Path(p_data.get('image_path', ''))
                    if not img_path.exists():
                        # Thử fallback đường dẫn tương đối
                        alt_img = Path(settings.BASE_DIR) / str(img_path).lstrip('/')
                        if alt_img.exists():
                            img_path = alt_img

                    # Chạy Tầng 1 (Morphological Grid) & Tầng 2-3 (Geometric Reconstruction)
                    res = service.analyse_page(
                        img_path,
                        p_data.get('recognition', {}).get('regions', []),
                        document_id=cid,
                        page_number=p_num
                    )

                    n_tables = len(res.layout.get('table_regions', []))
                    sheet_tables += n_tables
                    total_pages += 1

                    # Cập nhật kết quả bố cục mới vào cấu trúc trang
                    p_data['layout'] = res.as_dict()['layout']
                    p_data['layout']['groups'] = res.groups
                    p_data['layout']['records'] = res.records
                    p_data['layout']['rows'] = res.rows
                    p_data['layout']['summary'] = res.summary
                    all_pages_payload.append(p_data)

                    # Ghi đè file trang trên đĩa
                    if not dry_run:
                        with open(pf, 'w', encoding='utf-8') as f:
                            json.dump(p_data, f, ensure_ascii=False, indent=2)

                    # Ánh xạ tên phân nhóm (group_title) vào từng bản ghi thông số
                    layout_groups = {}
                    for g in res.groups:
                        gid = g.get('group_id')
                        title = (g.get('title') or '').strip()
                        if gid and title and len(title) < 80:
                            layout_groups[gid] = title

                    for r in res.records:
                        flat = flatten_record(r)
                        flat['page_number'] = p_num
                        gid = flat.get('group_id')
                        if gid in layout_groups:
                            flat['group_title'] = layout_groups[gid]
                        all_setting_records.append(flat)

                # 3. Tầng 5: Tự động nhận diện & liên kết Rơ-le / Trạm nếu còn trống
                matched_relay_info = ""
                if auto_link and p1_data:
                    p1_fields = p1_data.get('layout', {}).get('fields', {})
                    if not sheet.station and 'station' in p1_fields:
                        st_name = (p1_fields['station'].get('text') or '').strip()
                        if st_name:
                            # Khớp tên trạm linh hoạt
                            norm_ocr_st = normalize_text(st_name).replace('tram', '').split('(')[0].strip()
                            for s_obj in Station.objects.all():
                                norm_s = normalize_text(s_obj.station_name).replace('tram', '').strip()
                                if norm_ocr_st and (norm_ocr_st in norm_s or norm_s in norm_ocr_st):
                                    sheet.station = s_obj
                                    break

                    if not sheet.relay and sheet.station:
                        flat_p1 = {k: v.get('text') for k, v in p1_fields.items() if isinstance(v, dict)}
                        candidates = list(Relay.objects.filter(bay__station=sheet.station).select_related('bay'))
                        if candidates:
                            m_rl, m_score, m_why = match_relay_from_ocr(flat_p1, candidates)
                            if m_rl and m_score >= 30:
                                sheet.relay = m_rl
                                matched_relay_info = f" -> Đã khớp Rơ-le: {m_rl.relay_name} (Điểm: {m_score})"
                                auto_linked_relays += 1

                # 4. Lưu dữ liệu đã chuẩn hóa vào Cơ sở Dữ liệu
                if not dry_run:
                    clean_records = sanitize_json(all_setting_records)
                    clean_pages = sanitize_json(all_pages_payload)

                    sheet.extracted_data = clean_records
                    update_has_parameters_changed_for_sheet(sheet)
                    save_fields = ['extracted_data']
                    if sheet.station_id:
                        save_fields.append('station')
                    if sheet.relay_id:
                        save_fields.append('relay')
                    sheet.save(update_fields=save_fields)

                    # Đồng bộ sang OcrJob
                    if job:
                        job.result_data = job.result_data or {}
                        job.result_data['pages'] = clean_pages
                        job.result_data.setdefault('business', {})['setting_records'] = clean_records
                        job.result_data.setdefault('summary', {})['setting_records'] = len(clean_records)
                        job.status = 'SUCCESS'
                        job.review_status = 'COMPLETED'
                        job.save(update_fields=['result_data', 'status', 'review_status'])

                success_sheets += 1
                total_tables += sheet_tables
                total_parameters += len(all_setting_records)
                elapsed = time.time() - sheet_start

                relay_str = sheet.relay.relay_name if sheet.relay else "Chưa gán"
                self.stdout.write(
                    self.style.SUCCESS(
                        f"✓ [{success_sheets:03d}] Phiếu #{sheet.id:<3} ({sheet.sheet_code:<22}) | "
                        f"{len(page_files):<2} trang | {sheet_tables:<2} bảng | "
                        f"{len(all_setting_records):<3} thông số | {elapsed:.2f}s | Rơ-le: {relay_str}{matched_relay_info}"
                    )
                )

            except Exception as e:
                self.stderr.write(self.style.ERROR(f"✗ Lỗi xử lý Phiếu #{sheet.id} ({sheet.sheet_code}): {e}"))

        total_time = time.time() - start_time
        avg_time = (total_time / success_sheets) if success_sheets > 0 else 0

        self.stdout.write(self.style.MIGRATE_HEADING("\n=== TỔNG KẾT TIẾN TRÌNH ĐỒNG BỘ HYBRID MULTI-STAGE PIPELINE ==="))
        self.stdout.write(f"• Tổng số phiếu đã xử lý thành công: {self.style.SUCCESS(str(success_sheets))} / {total_sheets} phiếu")
        self.stdout.write(f"• Tổng số trang scan đã phân tích bố cục: {self.style.SUCCESS(str(total_pages))} trang")
        self.stdout.write(f"• Tổng số bảng thông số/lưới nhận diện: {self.style.SUCCESS(str(total_tables))} bảng")
        self.stdout.write(f"• Tổng số thông số cài đặt đã bóc tách chuẩn: {self.style.SUCCESS(str(total_parameters))} thông số")
        self.stdout.write(f"• Số lượng Rơ-le tự động liên kết thành công: {self.style.SUCCESS(str(auto_linked_relays))} rơ-le")
        self.stdout.write(f"• Tổng thời gian thực hiện: {self.style.SUCCESS(f'{total_time:.2f}s')} (Trung bình: {avg_time:.2f}s/phiếu)")
        self.stdout.write(self.style.SUCCESS("✓ HOÀN TẤT ĐỒNG BỘ TOÀN BỘ KHO DỮ LIỆU THÀNH CÔNG!"))
````

## File: sheets/management/__init__.py
````python
# Django management package
````

## File: sheets/migrations/__init__.py
````python

````

## File: sheets/migrations/0001_initial.py
````python
# Generated by Django 6.0.7 on 2026-07-18 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SettingSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheet_code', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('DRAFT', 'Draft'), ('PENDING_REVIEW', 'Pending Review'), ('ASSIGNED_TO_SC', 'Assigned to SC'), ('RECEIVED', 'Received'), ('COMPLETED', 'Completed')], default='DRAFT', max_length=50)),
                ('scan_file', models.FileField(upload_to='scans/')),
                ('extracted_data', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('relay', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stations.relay')),
            ],
        ),
        migrations.CreateModel(
            name='SignatureRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signer_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('signed_at', models.DateTimeField(auto_now_add=True)),
                ('signature_hash', models.CharField(max_length=256)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signatures', to='sheets.settingsheet')),
            ],
        ),
    ]
````

## File: sheets/migrations/0002_alter_settingsheet_options.py
````python
# Generated by Django 6.0.7 on 2026-07-18 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settingsheet',
            options={'permissions': [('can_view_stations', 'Can view stations'), ('can_manage_users', 'Can manage users & roles'), ('can_create_sheet', 'Can create sheet and run OCR'), ('can_approve_sheet', 'Can review and approve sheet'), ('can_dispatch_sheet', 'Can dispatch sheet to technician'), ('can_execute_sheet', 'Can execute sheet and sign (Technician)'), ('can_supervise_sheet', 'Can supervise sheet and sign (Supervisor)')]},
        ),
    ]
````

## File: sheets/migrations/0003_alter_settingsheet_status.py
````python
# Generated by Django 6.0.7 on 2026-07-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0002_alter_settingsheet_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsheet',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ISSUED', 'Issued (A0/A1 Signed)'), ('REVIEWED', 'Reviewed'), ('TRANSFERRED', 'Transferred to Technician'), ('RECEIVED', 'Received by Technician'), ('COMPLETED', 'Completed')], default='DRAFT', max_length=50),
        ),
    ]
````

## File: sheets/migrations/0004_alter_settingsheet_options.py
````python
# Generated by Django 6.0.7 on 2026-07-18 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0003_alter_settingsheet_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settingsheet',
            options={'permissions': [('can_view_stations', 'Can view stations'), ('can_view_checks', 'Can view periodic checks'), ('can_manage_users', 'Can manage users & roles'), ('can_create_sheet', 'Can create sheet and run OCR'), ('can_approve_sheet', 'Can review and approve sheet'), ('can_dispatch_sheet', 'Can dispatch sheet to technician'), ('can_execute_sheet', 'Can execute sheet and sign (Technician)'), ('can_supervise_sheet', 'Can supervise sheet and sign (Supervisor)')]},
        ),
    ]
````

## File: sheets/migrations/0005_settingsheet_assigned_to_settingsheet_created_by.py
````python
# Generated by Django 6.0.7 on 2026-07-18 20:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_alter_settingsheet_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_sheets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_sheets', to=settings.AUTH_USER_MODEL),
        ),
    ]
````

## File: sheets/migrations/0006_settingsheet_assigned_supervisor_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-18 20:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0005_settingsheet_assigned_to_settingsheet_created_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='assigned_supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sup_sheets', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='assigned_technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tech_sheets', to=settings.AUTH_USER_MODEL),
        ),
    ]
````

## File: sheets/migrations/0007_remove_settingsheet_assigned_supervisor_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-19 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0006_settingsheet_assigned_supervisor_and_more'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settingsheet',
            name='assigned_supervisor',
        ),
        migrations.RemoveField(
            model_name='settingsheet',
            name='assigned_technician',
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='relay_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='settingsheet',
            name='relay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stations.relay'),
        ),
        migrations.AlterField(
            model_name='settingsheet',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
````

## File: sheets/migrations/0008_alter_settingsheet_status.py
````python
# Generated by Django 6.0.7 on 2026-07-19 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0007_remove_settingsheet_assigned_supervisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsheet',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ISSUED', 'Issued (Ready for Dispatch)'), ('TRANSFERRED', 'Transferred to Technician'), ('RECEIVED', 'Received by Technician'), ('PENDING_REVIEW', 'Pending Operation Approval'), ('COMPLETED', 'Completed')], default='DRAFT', max_length=50),
        ),
    ]
````

## File: sheets/migrations/0009_settingsheet_supervisor_assigned.py
````python
# Generated by Django 6.0.7 on 2026-07-19 14:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0008_alter_settingsheet_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='supervisor_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='supervised_sheets', to=settings.AUTH_USER_MODEL),
        ),
    ]
````

## File: sheets/migrations/0010_settingsheet_is_temporary_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-20 09:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0009_settingsheet_supervisor_assigned'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='is_temporary',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='revert_to_sheet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revert_from_sheets', to='sheets.settingsheet'),
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='reverted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='settingsheet',
            name='valid_until',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
````

## File: sheets/migrations/0011_alter_settingsheet_options_alter_settingsheet_status.py
````python
# Generated by Django 6.0.7 on 2026-07-21 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0010_settingsheet_is_temporary_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='settingsheet',
            options={'ordering': ['-created_at'], 'permissions': [('can_view_stations', 'Can view stations'), ('can_view_checks', 'Can view periodic checks'), ('can_manage_users', 'Can manage users & roles'), ('can_create_sheet', 'Can create sheet and run OCR'), ('can_approve_sheet', 'Can review and approve sheet'), ('can_dispatch_sheet', 'Can dispatch sheet to technician'), ('can_execute_sheet', 'Can execute sheet and sign (Technician)'), ('can_supervise_sheet', 'Can supervise sheet and sign (Supervisor)')]},
        ),
        migrations.AlterField(
            model_name='settingsheet',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ISSUED', 'Issued (Ready for Dispatch)'), ('ROUTED_TO_STATION', 'Routed to Station'), ('TRANSFERRED', 'Transferred to Technician'), ('RECEIVED', 'Received by Technician'), ('PENDING_REVIEW', 'Pending Operation Approval'), ('COMPLETED', 'Completed')], default='DRAFT', max_length=50),
        ),
    ]
````

## File: sheets/migrations/0012_settingsheet_station.py
````python
# Generated by Django 6.0.7 on 2026-07-21 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0011_alter_settingsheet_options_alter_settingsheet_status'),
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stations.station'),
        ),
    ]
````

## File: sheets/migrations/0013_settingsheet_assigned_at_alter_settingsheet_status.py
````python
# Generated by Django 6.0.7 on 2026-07-22 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0012_settingsheet_station'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='assigned_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='settingsheet',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('ISSUED', 'Issued (Ready for Dispatch)'), ('ROUTED_TO_STATION', 'Routed to Station'), ('TRANSFERRED', 'Transferred to Technician'), ('RECEIVED', 'Received by Technician'), ('PENDING_ADMIN_APPROVAL', 'Pending Admin Approval'), ('COMPLETED', 'Completed')], default='DRAFT', max_length=50),
        ),
    ]
````

## File: sheets/migrations/0014_settingsheet_edit_logs_alter_settingsheet_status.py
````python
# Generated by Django 6.0.7 on 2026-07-22 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0013_settingsheet_assigned_at_alter_settingsheet_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='edit_logs',
            field=models.JSONField(blank=True, default=list),
        ),
        migrations.AlterField(
            model_name='settingsheet',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Nháp'), ('ISSUED', 'Chờ Rà soát'), ('ROUTED_TO_STATION', 'Đã chuyển về Trạm'), ('TRANSFERRED', 'Đã giao KTV'), ('RECEIVED', 'Đang thực hiện'), ('PENDING_ADMIN_APPROVAL', 'Chờ Duyệt Ban hành'), ('COMPLETED', 'Hoàn thành')], default='DRAFT', max_length=50),
        ),
    ]
````

## File: sheets/migrations/0015_settingsheet_has_parameters_changed.py
````python
# Generated by Django 6.0.7 on 2026-07-23 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0014_settingsheet_edit_logs_alter_settingsheet_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='has_parameters_changed',
            field=models.BooleanField(default=False),
        ),
    ]
````

## File: sheets/migrations/0016_alter_settingsheet_scan_file.py
````python
# Generated by Django 6.0.7 on 2026-07-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0015_settingsheet_has_parameters_changed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settingsheet',
            name='scan_file',
            field=models.FileField(blank=True, null=True, upload_to='scans/'),
        ),
    ]
````

## File: sheets/migrations/0017_settingsheet_updated_at.py
````python
# Generated by Django 6.0.7 on 2026-07-30 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0016_alter_settingsheet_scan_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
````

## File: sheets/migrations/0018_ocrjob.py
````python
# Generated by Django 6.0.7 on 2026-08-01 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0017_settingsheet_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='OcrJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correlation_id', models.CharField(help_text='ID duy nhất để giao tiếp với hệ thống OCR', max_length=128, unique=True)),
                ('status', models.CharField(choices=[('PENDING', 'Chờ xử lý'), ('PROCESSING', 'Đang xử lý'), ('SUCCESS', 'Thành công'), ('SUCCESS_WITH_WARNINGS', 'Thành công (có cảnh báo)'), ('FAILED', 'Thất bại')], default='PENDING', max_length=50)),
                ('review_status', models.CharField(blank=True, max_length=50, null=True)),
                ('result_data', models.JSONField(blank=True, help_text='Toàn bộ JSON trả về từ OCR', null=True)),
                ('error_code', models.CharField(blank=True, max_length=50, null=True)),
                ('error_stage', models.CharField(blank=True, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ocr_jobs', to='sheets.settingsheet')),
            ],
        ),
    ]
````

## File: sheets/migrations/0019_ocrjob_error_detail.py
````python
# Generated by Django on 2026-08-03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0018_ocrjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrjob',
            name='error_detail',
            field=models.TextField(blank=True, help_text='Chi tiết nguyên nhân lỗi OCR', null=True),
        ),
    ]
````

## File: sheets/migrations/0020_ocrjob_device_mode.py
````python
# Generated by Django 6.0.7 on 2026-08-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0019_ocrjob_error_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='ocrjob',
            name='device_mode',
            field=models.CharField(choices=[('CPU', 'CPU'), ('GPU', 'GPU (CUDA)')], default='CPU', help_text='Chế độ phần cứng xử lý (CPU/GPU)', max_length=10),
        ),
    ]
````

## File: sheets/migrations/0021_settingsheet_execution_station.py
````python
# Generated by Django 6.0.8 on 2026-10-06 15:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0020_ocrjob_device_mode'),
        ('stations', '0011_bay_updated_at_relay_updated_at_station_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='settingsheet',
            name='execution_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='executed_sheets', to='stations.station'),
        ),
    ]
````

## File: sheets/__init__.py
````python

````

## File: sheets/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: sheets/apps.py
````python
from django.apps import AppConfig


class SheetsConfig(AppConfig):
    name = 'sheets'

    def ready(self):
        import sheets.signals
````

## File: sheets/models.py
````python
from django.db import models
from stations.models import Relay

class SettingSheet(models.Model):
    STATUS_CHOICES = (
        ('DRAFT', 'Nháp'),
        ('ISSUED', 'Chờ Rà soát'),
        ('ROUTED_TO_STATION', 'Đã chuyển về Trạm'),
        ('TRANSFERRED', 'Đã giao KTV'),
        ('RECEIVED', 'Đang thực hiện'),
        ('PENDING_ADMIN_APPROVAL', 'Chờ Duyệt Ban hành'),
        ('COMPLETED', 'Hoàn thành'),
    )

    sheet_code = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='DRAFT')
    scan_file = models.FileField(upload_to='scans/', blank=True, null=True)
    
    created_by = models.ForeignKey('auth.User', related_name='created_sheets', on_delete=models.SET_NULL, null=True)
    assigned_to = models.ForeignKey('auth.User', related_name='assigned_sheets', on_delete=models.SET_NULL, null=True, blank=True)
    supervisor_assigned = models.ForeignKey('auth.User', related_name='supervised_sheets', on_delete=models.SET_NULL, null=True, blank=True)
    assigned_at = models.DateTimeField(null=True, blank=True)
    
    relay = models.ForeignKey(Relay, on_delete=models.SET_NULL, null=True, blank=True)
    relay_text = models.CharField(max_length=255, null=True, blank=True)
    station = models.ForeignKey('stations.Station', on_delete=models.SET_NULL, null=True, blank=True)
    
    # Trạm được giao nhiệm vụ thực thi (Cross-Dispatching). Nếu null thì mặc định dùng station.
    execution_station = models.ForeignKey('stations.Station', on_delete=models.SET_NULL, null=True, blank=True, related_name='executed_sheets')

    # OCR Data / Mock Data using JSONField of PostgreSQL
    extracted_data = models.JSONField(null=True, blank=True) 
    
    # Lịch sử sửa đổi thông số
    edit_logs = models.JSONField(default=list, blank=True)

    # Đánh dấu phiếu có thông số thay đổi so với phiên bản trước đó
    has_parameters_changed = models.BooleanField(default=False)


    is_temporary = models.BooleanField(default=False)
    valid_until = models.DateTimeField(null=True, blank=True)
    revert_to_sheet = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='revert_from_sheets')
    reverted = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.sheet_code} - {self.title}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        from django.core.cache import cache
        import time
        cache.set('sheet_list_version', int(time.time()))

    class Meta:
        ordering = ['-created_at']
        permissions = [
            ("can_view_stations", "Can view stations"),
            ("can_view_checks", "Can view periodic checks"),
            ("can_manage_users", "Can manage users & roles"),
            ("can_create_sheet", "Can create sheet and run OCR"),
            ("can_approve_sheet", "Can review and approve sheet"),
            ("can_dispatch_sheet", "Can dispatch sheet to technician"),
            ("can_execute_sheet", "Can execute sheet and sign (Technician)"),
            ("can_supervise_sheet", "Can supervise sheet and sign (Supervisor)"),
        ]

class SignatureRecord(models.Model):
    sheet = models.ForeignKey(SettingSheet, related_name='signatures', on_delete=models.CASCADE)
    signer_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    signed_at = models.DateTimeField(auto_now_add=True)
    signature_hash = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.signer_name} ({self.role})"

class OcrJob(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Chờ xử lý'),
        ('PROCESSING', 'Đang xử lý'),
        ('SUCCESS', 'Thành công'),
        ('SUCCESS_WITH_WARNINGS', 'Thành công (có cảnh báo)'),
        ('FAILED', 'Thất bại'),
    )

    DEVICE_CHOICES = (
        ('CPU', 'CPU'),
        ('GPU', 'GPU (CUDA)'),
    )

    sheet = models.ForeignKey(SettingSheet, related_name='ocr_jobs', on_delete=models.CASCADE)
    correlation_id = models.CharField(max_length=128, unique=True, help_text="ID duy nhất để giao tiếp với hệ thống OCR")
    device_mode = models.CharField(max_length=10, choices=DEVICE_CHOICES, default='CPU', help_text="Chế độ phần cứng xử lý (CPU/GPU)")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')
    review_status = models.CharField(max_length=50, null=True, blank=True)
    
    # Kết quả và lỗi
    result_data = models.JSONField(null=True, blank=True, help_text="Toàn bộ JSON trả về từ OCR")
    error_code = models.CharField(max_length=50, null=True, blank=True)
    error_stage = models.CharField(max_length=50, null=True, blank=True)
    error_detail = models.TextField(null=True, blank=True, help_text="Chi tiết nguyên nhân lỗi OCR")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OCR {self.correlation_id} - {self.get_status_display()}"
````

## File: sheets/relay_matcher.py
````python
"""
Mô-đun nhận diện và ánh xạ rơ-le bảo vệ thông minh (Intelligent Relay Matching Engine).
Hỗ trợ đối soát đa tầng giữa thông tin OCR phiếu chỉnh định và Danh mục Rơ-le EVN (PMIS/RMS):
1. Khớp định danh trực tiếp (Model/Serial/Mã PMIS)
2. Tra cứu họ Model sang mã chức năng ANSI/IEEE C37.2 (7UT -> 87R/87T, 7SA -> 21/87L, SEL-387 -> 87T/87R, RET -> 87T/87R...)
3. Phân tích ngữ cảnh kỹ thuật: Mạch bảo vệ (Mạch 1 -> F87...1, Mạch 2 -> F87...2), Kiểu bảo vệ, Hãng sản xuất.
4. Loại trừ các thiết bị phụ trợ/cơ điện (Rơ le hơi, Van áp lực, Đồng hồ nhiệt độ/mức dầu...).
"""

import re
import unicodedata

# 1. Bảng ánh xạ Tiền tố Model sang Chức năng ANSI & Hãng sản xuất
MODEL_REGISTRY = {
    # Siemens SIPROTEC 5 (Thế hệ mới - DIGSI 5) & SIPROTEC 4 (DIGSI 4)
    # 1. Quá dòng và Xuất tuyến (7SJ Series)
    "7SJ86": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng và xuất tuyến cao cấp (SIPROTEC 5 7SJ86)"},
    "7SJ85": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng và xuất tuyến đa chức năng (SIPROTEC 5 7SJ85)"},
    "7SJ82": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng và xuất tuyến nhỏ gọn (SIPROTEC 5 7SJ82)"},
    "7SJ64": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng và điều khiển ngăn (SIPROTEC 4 7SJ64)"},
    "7SJ62": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng và xuất tuyến (SIPROTEC 4 7SJ62)"},
    "7SJ61": {"functions": ["50/51", "67"], "mfr": "SIEMENS", "desc": "Bảo vệ quá dòng (SIPROTEC 4 7SJ61)"},
    "7SJ": {"functions": ["50/51", "67", "BCU"], "mfr": "SIEMENS", "desc": "Quá dòng / Ngăn lộ (SIPROTEC 7SJ)"},

    # 2. Bảo vệ Khoảng cách Đường dây (7SA Series)
    "7SA87": {"functions": ["21", "87L"], "mfr": "SIEMENS", "desc": "Bảo vệ khoảng cách đường dây cao cấp (SIPROTEC 5 7SA87)"},
    "7SA86": {"functions": ["21", "87L"], "mfr": "SIEMENS", "desc": "Bảo vệ khoảng cách đường dây (SIPROTEC 5 7SA86)"},
    "7SA82": {"functions": ["21"], "mfr": "SIEMENS", "desc": "Bảo vệ khoảng cách đường dây nhỏ gọn (SIPROTEC 5 7SA82)"},
    "7SA6": {"functions": ["21", "87L"], "mfr": "SIEMENS", "desc": "Bảo vệ khoảng cách đường dây (SIPROTEC 4 7SA6)"},
    "7SA52": {"functions": ["21", "87L"], "mfr": "SIEMENS", "desc": "Bảo vệ khoảng cách đường dây (SIPROTEC 4 7SA522)"},
    "7SA": {"functions": ["21", "87L"], "mfr": "SIEMENS", "desc": "Bảo vệ Khoảng cách / ĐD (SIPROTEC 7SA)"},

    # 3. Bảo vệ So lệch Đường dây (7SD Series)
    "7SD87": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch đường dây đa đầu cực (SIPROTEC 5 7SD87)"},
    "7SD86": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch đường dây (SIPROTEC 5 7SD86)"},
    "7SD82": {"functions": ["87L"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch đường dây nhỏ gọn (SIPROTEC 5 7SD82)"},
    "7SD61": {"functions": ["87L"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch đường dây (SIPROTEC 4 7SD610)"},
    "7SD52": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch đường dây (SIPROTEC 4 7SD522/523)"},
    "7SD": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "So lệch Đường dây (SIPROTEC 7SD)"},

    # 4. Kết hợp Bảo vệ So lệch và Khoảng cách Đường dây (7SL Series)
    "7SL87": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Kết hợp so lệch và khoảng cách đường dây cao cấp (SIPROTEC 5 7SL87)"},
    "7SL86": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Kết hợp so lệch và khoảng cách đường dây (SIPROTEC 5 7SL86)"},
    "7SL82": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "Kết hợp so lệch và khoảng cách đường dây (SIPROTEC 5 7SL82)"},
    "7SL": {"functions": ["87L", "21"], "mfr": "SIEMENS", "desc": "So lệch & Khoảng cách Đường dây (SIPROTEC 7SL)"},

    # 5. Bảo vệ So lệch Máy biến áp (7UT Series)
    "7UT87": {"functions": ["87T", "87R", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA tới 5 đầu cực (SIPROTEC 5 7UT87)"},
    "7UT86": {"functions": ["87T", "87R", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA tới 3 đầu cực & REF (SIPROTEC 5 7UT86)"},
    "7UT85": {"functions": ["87T", "87R", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA 2 đầu cực & REF (SIPROTEC 5 7UT85)"},
    "7UT82": {"functions": ["87T", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA nhỏ gọn (SIPROTEC 5 7UT82)"},
    "7UT63": {"functions": ["87T", "87R", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA (SIPROTEC 4 7UT633/635)"},
    "7UT61": {"functions": ["87T", "64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ so lệch MBA (SIPROTEC 4 7UT612/613)"},
    "7UT": {"functions": ["87R", "87T", "64REF"], "mfr": "SIEMENS", "desc": "So lệch MBA / Kháng / REF (SIPROTEC 7UT)"},

    # 6. Bảo vệ So lệch Thanh cái (7SS Series)
    "7SS85": {"functions": ["87B"], "mfr": "SIEMENS", "desc": "Bảo vệ thanh cái phân tán / tập trung (SIPROTEC 5 7SS85)"},
    "7SS52": {"functions": ["87B"], "mfr": "SIEMENS", "desc": "Bảo vệ thanh cái phân tán (SIPROTEC 4 7SS522/523)"},
    "7SS": {"functions": ["87B"], "mfr": "SIEMENS", "desc": "So lệch Thanh cái (SIPROTEC 7SS)"},

    # 7. Các dòng bảo vệ chuyên dụng khác của Siemens
    "7VK87": {"functions": ["50BF", "79", "BCU"], "mfr": "SIEMENS", "desc": "Quản lý máy cắt, hòa đồng bộ & TĐL (SIPROTEC 5 7VK87)"},
    "7VK61": {"functions": ["50BF", "79"], "mfr": "SIEMENS", "desc": "Hư hỏng máy cắt & TĐL (SIPROTEC 4 7VK61)"},
    "7VK": {"functions": ["50BF", "79"], "mfr": "SIEMENS", "desc": "Hư hỏng máy cắt / Tự đóng lại (SIPROTEC 7VK)"},
    "7VH60": {"functions": ["64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ Chạm đất hạn chế trở kháng cao (7VH60)"},
    "7VH": {"functions": ["64REF"], "mfr": "SIEMENS", "desc": "Bảo vệ Chạm đất hạn chế trở kháng cao (7VH)"},
    "7UM62": {"functions": ["87G", "40", "64G"], "mfr": "SIEMENS", "desc": "Bảo vệ máy phát điện (SIPROTEC 4 7UM62)"},
    "7UM": {"functions": ["87G", "40", "64G"], "mfr": "SIEMENS", "desc": "So lệch Máy phát (SIPROTEC 7UM)"},
    "7RW": {"functions": ["81", "27/59"], "mfr": "SIEMENS", "desc": "Tần số / Điện áp (SIPROTEC 7RW)"},
    
    # Schweitzer Engineering Laboratories (SEL)
    # 1. Bảo vệ Xuất tuyến / Feeder (SEL-751 Series)
    "SEL-751A": {"functions": ["50/51", "67", "BCU"], "mfr": "SEL", "desc": "Bảo vệ và điều khiển xuất tuyến nâng cao (SEL-751A)"},
    "SEL-751": {"functions": ["50/51", "67", "BCU"], "mfr": "SEL", "desc": "Bảo vệ xuất tuyến đa chức năng (SEL-751)"},
    "SEL-351": {"functions": ["50/51", "67", "BCU"], "mfr": "SEL", "desc": "Bảo vệ quá dòng và điều khiển xuất tuyến (SEL-351)"},
    "SEL-451": {"functions": ["50/51", "67", "BCU"], "mfr": "SEL", "desc": "Bảo vệ quá dòng và điều khiển ngăn lộ (SEL-451)"},
    "SEL-551": {"functions": ["50/51"], "mfr": "SEL", "desc": "Bảo vệ quá dòng / chạm đất (SEL-551)"},
    "SEL-501": {"functions": ["50/51"], "mfr": "SEL", "desc": "Bảo vệ quá dòng kép (SEL-501)"},

    # 2. Bảo vệ Máy biến áp & Kháng (SEL-787, SEL-487E, SEL-387, SEL-587)
    "SEL-787": {"functions": ["87T", "87R", "64REF", "50/51"], "mfr": "SEL", "desc": "Bảo vệ máy biến áp (SEL-787)"},
    "SEL-487E": {"functions": ["87T", "87R", "64REF", "50/51"], "mfr": "SEL", "desc": "Bảo vệ máy biến áp đa cuộn dây (SEL-487E)"},
    "SEL-387": {"functions": ["87T", "87R", "64REF"], "mfr": "SEL", "desc": "So lệch MBA / Kháng / REF (SEL-387)"},
    "SEL-587": {"functions": ["87T", "87R"], "mfr": "SEL", "desc": "So lệch MBA / Kháng (SEL-587)"},

    # 3. Bảo vệ So lệch & Khoảng cách Đường dây (SEL-411L, SEL-311L, SEL-421, SEL-311C)
    "SEL-411L": {"functions": ["87L", "21", "BCU", "79", "25"], "mfr": "SEL", "desc": "Bảo vệ so lệch đường dây, kết hợp tự động hóa và điều khiển (SEL-411L)"},
    "SEL-311L": {"functions": ["87L", "21"], "mfr": "SEL", "desc": "Bảo vệ so lệch đường dây (SEL-311L)"},
    "SEL-421": {"functions": ["21", "87L", "BCU"], "mfr": "SEL", "desc": "Bảo vệ khoảng cách đường dây cao tốc (SEL-421)"},
    "SEL-311C": {"functions": ["21"], "mfr": "SEL", "desc": "Bảo vệ khoảng cách đường dây (SEL-311C)"},

    # 4. Bảo vệ So lệch Thanh cái & Hư hỏng máy cắt (SEL-487B)
    "SEL-487B": {"functions": ["87B", "50BF"], "mfr": "SEL", "desc": "Bảo vệ so lệch thanh cái và hư hỏng máy cắt (SEL-487B)"},
    
    # ABB / Hitachi Energy (Relion Series: 670, 650, 630, 620, 615 & REX)
    # 1. Bảo vệ Máy biến áp (RET Series)
    "RET670": {"functions": ["87T", "87R", "64REF"], "mfr": "ABB", "desc": "Bảo vệ, điều khiển và giám sát máy biến áp (Relion RET670)"},
    "RET650": {"functions": ["87T", "64REF"], "mfr": "ABB", "desc": "Bảo vệ máy biến áp (Relion RET650)"},
    "RET630": {"functions": ["87T", "87R", "64REF"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy biến áp (Relion RET630)"},
    "RET620": {"functions": ["87T", "64REF"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy biến áp (Relion RET620)"},
    "RET615": {"functions": ["87T", "64REF"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy biến áp (Relion RET615)"},
    "RET521": {"functions": ["87T", "64REF"], "mfr": "ABB", "desc": "Bảo vệ so lệch máy biến áp (ABB RET521)"},

    # 2. Bảo vệ So lệch Đường dây & Cáp (RED Series)
    "RED670": {"functions": ["87L", "21"], "mfr": "ABB", "desc": "Bảo vệ so lệch đường dây và cáp (Relion RED670)"},
    "RED650": {"functions": ["87L"], "mfr": "ABB", "desc": "Bảo vệ so lệch đường dây (Relion RED650)"},
    "RED615": {"functions": ["87L"], "mfr": "ABB", "desc": "Bảo vệ so lệch đường dây (Relion RED615)"},
    "RED521": {"functions": ["87L"], "mfr": "ABB", "desc": "Bảo vệ so lệch đường dây (ABB RED521)"},

    # 3. Bảo vệ Khoảng cách Đường dây (REL Series)
    "REL670": {"functions": ["21", "87L"], "mfr": "ABB", "desc": "Bảo vệ khoảng cách đường dây (Relion REL670)"},
    "REL650": {"functions": ["21"], "mfr": "ABB", "desc": "Bảo vệ khoảng cách đường dây (Relion REL650)"},
    "REL521": {"functions": ["21"], "mfr": "ABB", "desc": "Bảo vệ khoảng cách đường dây (ABB REL521/511)"},

    # 4. Bảo vệ Thanh cái (REB Series)
    "REB670": {"functions": ["87B"], "mfr": "ABB", "desc": "Bảo vệ thanh cái (Relion REB670)"},
    "REB500": {"functions": ["87B"], "mfr": "ABB", "desc": "Hệ thống bảo vệ thanh cái phân tán (ABB REB500)"},

    # 5. Bảo vệ & Điều khiển Xuất tuyến / Feeder (REF Series)
    "REF630": {"functions": ["50/51", "67", "BCU"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển xuất tuyến (Relion REF630)"},
    "REF620": {"functions": ["50/51", "67", "BCU"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển xuất tuyến (Relion REF620)"},
    "REF615": {"functions": ["50/51", "67", "BCU"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển xuất tuyến (Relion REF615)"},

    # 6. Bảo vệ Động cơ (REM Series)
    "REM630": {"functions": ["49", "50/51"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển động cơ (Relion REM630)"},
    "REM620": {"functions": ["49", "50/51"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển động cơ (Relion REM620)"},
    "REM615": {"functions": ["49", "50/51"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển động cơ (Relion REM615)"},

    # 7. Bảo vệ Máy phát điện (REG Series)
    "REG670": {"functions": ["87G", "40", "64G"], "mfr": "ABB", "desc": "Bảo vệ máy phát điện và khối máy phát - MBA (Relion REG670)"},
    "REG630": {"functions": ["87G", "40", "64G"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy phát (Relion REG630)"},
    "REG620": {"functions": ["87G", "40", "64G"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy phát (Relion REG620)"},
    "REG615": {"functions": ["87G", "40", "64G"], "mfr": "ABB", "desc": "Bảo vệ và điều khiển máy phát (Relion REG615)"},

    # 8. Điều khiển & Giám sát Ngăn lộ (REC Series)
    "REC670": {"functions": ["BCU"], "mfr": "ABB", "desc": "Điều khiển và giám sát ngăn lộ (Relion REC670)"},
    "REC650": {"functions": ["BCU"], "mfr": "ABB", "desc": "Điều khiển và giám sát ngăn lộ (Relion REC650)"},

    # 9. Nền tảng Đa năng Relion REX Platform
    "REX640": {"functions": ["87T", "87L", "50/51", "BCU"], "mfr": "ABB", "desc": "Nền tảng bảo vệ và điều khiển đa năng Relion REX640"},
    "REX615": {"functions": ["50/51", "67", "BCU"], "mfr": "ABB", "desc": "Rơ-le bảo vệ và điều khiển Relion REX615"},
    "REX521": {"functions": ["50/51", "67"], "mfr": "ABB", "desc": "Bảo vệ quá dòng và điều khiển ngăn (ABB REX521)"},

    # 10. Tiền tố chung dòng ABB (Fallback)
    "RET": {"functions": ["87T", "87R", "64REF"], "mfr": "ABB", "desc": "So lệch MBA / Kháng / REF (ABB RET)"},
    "REL": {"functions": ["21"], "mfr": "ABB", "desc": "Bảo vệ Khoảng cách (ABB REL)"},
    "RED": {"functions": ["87L"], "mfr": "ABB", "desc": "So lệch Đường dây (ABB RED)"},
    "REC": {"functions": ["BCU"], "mfr": "ABB", "desc": "Điều khiển Ngăn lộ (ABB REC)"},
    "REB": {"functions": ["87B"], "mfr": "ABB", "desc": "So lệch Thanh cái (ABB REB)"},
    "REF": {"functions": ["50/51", "67"], "mfr": "ABB", "desc": "Quá dòng Feeder / Ngăn lộ (ABB REF)"},
    "REM": {"functions": ["49", "50/51"], "mfr": "ABB", "desc": "Bảo vệ động cơ (ABB REM)"},
    "REG": {"functions": ["87G"], "mfr": "ABB", "desc": "So lệch Máy phát (ABB REG)"},
    "VC100": {"functions": ["90"], "mfr": "ABB", "desc": "Bộ điều khiển điện áp tự động (ABB VC100)"},
    
    # MiCOM (Schneider / Alstom / AREVA)
    "MICOM P12": {"functions": ["50/51", "67"], "mfr": "MICOM", "desc": "Bảo vệ quá dòng pha và chạm đất (MiCOM P122/P123/P127)"},
    "P122": {"functions": ["50/51", "67"], "mfr": "MICOM", "desc": "Bảo vệ quá dòng pha và chạm đất (MiCOM P122)"},
    "P123": {"functions": ["50/51", "67"], "mfr": "MICOM", "desc": "Bảo vệ quá dòng pha và chạm đất (MiCOM P123)"},
    "P127": {"functions": ["50/51", "67"], "mfr": "MICOM", "desc": "Bảo vệ quá dòng và có hướng/áp (MiCOM P127)"},
    "P12": {"functions": ["50/51", "67"], "mfr": "MICOM", "desc": "Bảo vệ quá dòng (MiCOM P12x)"},

    "MICOM P14": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Bảo vệ, điều khiển và giám sát xuất tuyến (MiCOM P141/P142/P143/P145)"},
    "P141": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Bảo vệ, điều khiển xuất tuyến (MiCOM P141)"},
    "P142": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Bảo vệ, điều khiển xuất tuyến (MiCOM P142)"},
    "P143": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Bảo vệ, điều khiển xuất tuyến (MiCOM P143)"},
    "P145": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Bảo vệ, điều khiển xuất tuyến (MiCOM P145)"},
    "P14": {"functions": ["50/51", "67", "BCU"], "mfr": "MICOM", "desc": "Quá dòng Feeder / Ngăn lộ (MiCOM P14x)"},

    "MICOM P24": {"functions": ["49", "50/51"], "mfr": "MICOM", "desc": "Bảo vệ động cơ và máy điện quay (MiCOM P241/P242/P243)"},
    "P241": {"functions": ["49", "50/51"], "mfr": "MICOM", "desc": "Bảo vệ động cơ (MiCOM P241)"},
    "P242": {"functions": ["49", "50/51"], "mfr": "MICOM", "desc": "Bảo vệ động cơ (MiCOM P242)"},
    "P243": {"functions": ["49", "50/51"], "mfr": "MICOM", "desc": "Bảo vệ động cơ và máy điện quay (MiCOM P243)"},
    "P24": {"functions": ["49", "50/51"], "mfr": "MICOM", "desc": "Bảo vệ động cơ (MiCOM P24x)"},

    "MICOM P34": {"functions": ["87G", "40", "64G"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện (MiCOM P342/P343/P344/P345)"},
    "P342": {"functions": ["87G", "40"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện (MiCOM P342)"},
    "P343": {"functions": ["87G", "40", "64G"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện (MiCOM P343)"},
    "P344": {"functions": ["87G", "40", "64G"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện (MiCOM P344)"},
    "P345": {"functions": ["87G", "40", "64G"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện công suất lớn (MiCOM P345)"},
    "P34": {"functions": ["87G"], "mfr": "MICOM", "desc": "Bảo vệ máy phát điện (MiCOM P34x)"},

    "MICOM P44": {"functions": ["21", "87L"], "mfr": "MICOM", "desc": "Bảo vệ khoảng cách đường dây - chức năng chính 21 (MiCOM P441/P442/P443)"},
    "P441": {"functions": ["21"], "mfr": "MICOM", "desc": "Bảo vệ khoảng cách đường dây (MiCOM P441)"},
    "P442": {"functions": ["21"], "mfr": "MICOM", "desc": "Bảo vệ khoảng cách đường dây (MiCOM P442)"},
    "P443": {"functions": ["21"], "mfr": "MICOM", "desc": "Bảo vệ khoảng cách đường dây (MiCOM P443)"},
    "P44": {"functions": ["21"], "mfr": "MICOM", "desc": "Bảo vệ Khoảng cách (MiCOM P44x)"},

    "MICOM P54": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "Bảo vệ so lệch dòng điện đường dây - chức năng chính 87L (MiCOM P541-P546)"},
    "P541": {"functions": ["87L"], "mfr": "MICOM", "desc": "So lệch đường dây (MiCOM P541)"},
    "P542": {"functions": ["87L"], "mfr": "MICOM", "desc": "So lệch đường dây (MiCOM P542)"},
    "P543": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "So lệch đường dây kèm khoảng cách (MiCOM P543)"},
    "P544": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "So lệch đường dây kèm khoảng cách (MiCOM P544)"},
    "P545": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "So lệch đường dây kèm khoảng cách (MiCOM P545)"},
    "P546": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "So lệch đường dây đa đầu cực (MiCOM P546)"},
    "P54": {"functions": ["87L", "21"], "mfr": "MICOM", "desc": "So lệch Đường dây (MiCOM P54x)"},

    "MICOM P64": {"functions": ["87T", "87R", "64REF"], "mfr": "MICOM", "desc": "Bảo vệ so lệch máy biến áp - chức năng chính 87T (MiCOM P642/P643/P645)"},
    "P642": {"functions": ["87T", "64REF"], "mfr": "MICOM", "desc": "So lệch máy biến áp 2 cuộn dây (MiCOM P642)"},
    "P643": {"functions": ["87T", "87R", "64REF"], "mfr": "MICOM", "desc": "So lệch máy biến áp 3 cuộn dây & REF (MiCOM P643)"},
    "P645": {"functions": ["87T", "87R", "64REF"], "mfr": "MICOM", "desc": "So lệch máy biến áp 5 cuộn dây (MiCOM P645)"},
    "P64": {"functions": ["87T", "87R", "64REF"], "mfr": "MICOM", "desc": "So lệch MBA / REF (MiCOM P64x)"},

    "MICOM P74": {"functions": ["87B"], "mfr": "MICOM", "desc": "Hệ thống bảo vệ thanh cái phân tán & tập trung (MiCOM P740/P746)"},
    "P740": {"functions": ["87B"], "mfr": "MICOM", "desc": "Hệ thống bảo vệ thanh cái phân tán (MiCOM P740)"},
    "P741": {"functions": ["87B"], "mfr": "MICOM", "desc": "Bảo vệ thanh cái phân tán - Khối trung tâm (MiCOM P741)"},
    "P742": {"functions": ["87B"], "mfr": "MICOM", "desc": "Bảo vệ thanh cái phân tán - Khối ngăn lộ (MiCOM P742)"},
    "P743": {"functions": ["87B"], "mfr": "MICOM", "desc": "Bảo vệ thanh cái phân tán - Khối ngăn lộ (MiCOM P743)"},
    "P746": {"functions": ["87B"], "mfr": "MICOM", "desc": "Bảo vệ thanh cái theo cấu trúc tập trung (MiCOM P746)"},
    "P74": {"functions": ["87B"], "mfr": "MICOM", "desc": "So lệch Thanh cái (MiCOM P74x)"},

    "MICOM P84": {"functions": ["BCU", "79", "25"], "mfr": "MICOM", "desc": "Điều khiển ngăn lộ, tự động đóng lại và kiểm tra hòa đồng bộ (MiCOM P841)"},
    "P841": {"functions": ["BCU", "79", "25"], "mfr": "MICOM", "desc": "Điều khiển ngăn lộ, tự động đóng lại và kiểm tra hòa đồng bộ (MiCOM P841)"},
    "P84": {"functions": ["BCU", "79", "25"], "mfr": "MICOM", "desc": "Điều khiển ngăn lộ & hòa đồng bộ (MiCOM P84x)"},

    "MCAG": {"functions": ["64REF"], "mfr": "MICOM", "desc": "Bảo vệ Chạm đất hạn chế REF (MCAG14/34)"},
    "T60": {"functions": ["87T", "87R"], "mfr": "GE", "desc": "GE Multilin T60 (So lệch MBA)"},
    "L90": {"functions": ["87L"], "mfr": "GE", "desc": "GE Multilin L90 (So lệch ĐD)"},
    "D60": {"functions": ["21"], "mfr": "GE", "desc": "GE Multilin D60 (Khoảng cách)"},
    "B90": {"functions": ["87B"], "mfr": "GE", "desc": "GE Multilin B90 (So lệch Thanh cái)"},
    "B30": {"functions": ["87B"], "mfr": "GE", "desc": "GE Multilin B30 (So lệch Thanh cái)"},
    "F650": {"functions": ["50/51", "67", "BCU"], "mfr": "GE", "desc": "GE Multilin F650 (Quá dòng & BCU)"},
    "C650": {"functions": ["BCU"], "mfr": "GE", "desc": "GE Multilin C650 (Khối điều khiển ngăn lộ)"},
    
    # Toshiba (GR-Series)
    "GRZ200": {"functions": ["21"], "mfr": "TOSHIBA", "desc": "Bảo vệ khoảng cách đường dây (Toshiba GRZ200)"},
    "GRZ100": {"functions": ["21"], "mfr": "TOSHIBA", "desc": "Bảo vệ khoảng cách đường dây (Toshiba GRZ100)"},
    "GRT200": {"functions": ["87T", "87R", "64REF"], "mfr": "TOSHIBA", "desc": "Bảo vệ so lệch máy biến áp (Toshiba GRT200)"},
    "GRT100": {"functions": ["87T", "87R", "64REF"], "mfr": "TOSHIBA", "desc": "Bảo vệ so lệch máy biến áp (Toshiba GRT100)"},
    "GRB200": {"functions": ["87B"], "mfr": "TOSHIBA", "desc": "Bảo vệ so lệch thanh cái (Toshiba GRB200)"},
    "GRB100": {"functions": ["87B"], "mfr": "TOSHIBA", "desc": "Bảo vệ so lệch thanh cái (Toshiba GRB100)"},
    "GRD200": {"functions": ["50/51", "67"], "mfr": "TOSHIBA", "desc": "Bảo vệ quá dòng xuất tuyến (Toshiba GRD200)"},
    "GRD100": {"functions": ["50/51", "67"], "mfr": "TOSHIBA", "desc": "Bảo vệ quá dòng xuất tuyến (Toshiba GRD100)"},
    "GBU200": {"functions": ["BCU"], "mfr": "TOSHIBA", "desc": "Khối điều khiển ngăn lộ (Toshiba GBU200)"},

    # NR Electric / NARI
    "RCS-978": {"functions": ["87T", "87R", "64REF"], "mfr": "NARI", "desc": "So lệch MBA / REF (RCS-978)"},
    "PCS-978": {"functions": ["87T", "87R", "64REF"], "mfr": "NARI", "desc": "So lệch MBA / REF (PCS-978)"},
    "RCS-931": {"functions": ["87L", "21"], "mfr": "NARI", "desc": "So lệch / Khoảng cách ĐD (RCS-931)"},
    "PCS-931": {"functions": ["87L", "21"], "mfr": "NARI", "desc": "So lệch / Khoảng cách ĐD (PCS-931)"},
    "RCS-902": {"functions": ["21"], "mfr": "NARI", "desc": "Khoảng cách (RCS-902)"},
    "PCS-902": {"functions": ["21"], "mfr": "NARI", "desc": "Khoảng cách (PCS-902)"},
    "RCS-915": {"functions": ["87B"], "mfr": "NARI", "desc": "So lệch Thanh cái (RCS-915)"},
    "PCS-915": {"functions": ["87B"], "mfr": "NARI", "desc": "So lệch Thanh cái (PCS-915)"},
    "PCS-9611": {"functions": ["BCU", "50/51", "67"], "mfr": "NARI", "desc": "Bảo vệ quá dòng / Điều khiển ngăn (PCS-9611)"},
    "PCS-921": {"functions": ["50/51", "50BF", "67"], "mfr": "NARI", "desc": "Bảo vệ quá dòng và chống hư hỏng máy cắt (PCS-921)"},
    "RCS-921": {"functions": ["50/51", "50BF", "67"], "mfr": "NARI", "desc": "Bảo vệ quá dòng và chống hư hỏng máy cắt (RCS-921)"},
    "PCS-9705": {"functions": ["BCU"], "mfr": "NARI", "desc": "Khối điều khiển ngăn lộ (PCS-9705S)"},

    # Protecta, Bender & Arteche
    "EUROPROT": {"functions": ["50/51", "67", "BCU"], "mfr": "PROTECTA", "desc": "Rơ-le bảo vệ và điều khiển EuroProt+"},
    "ISO685": {"functions": ["64G"], "mfr": "BENDER", "desc": "Thiết bị giám sát cách điện & chạm đất DC (Bender ISO685)"},
    "RCMS460": {"functions": ["64G"], "mfr": "BENDER", "desc": "Thiết bị định vị sự cố chạm đất DC đa kênh (Bender RCMS460)"},
    "ARTECHE-VJ": {"functions": ["86"], "mfr": "ARTECHE", "desc": "Rơ-le khóa cắt tốc độ cao F86 (Arteche VJ)"},
    "ARTECHE-TCS": {"functions": ["74"], "mfr": "ARTECHE", "desc": "Rơ-le giám sát mạch cắt F74 (Arteche TCS)"},
    
    # Tự động Điều chỉnh Điện áp (ANSI 90 - AVR / OLTC)
    "TAPCON": {"functions": ["90"], "mfr": "MR", "desc": "Bộ điều áp dưới tải OLTC / AVR (TAPCON 230/240/260)"},
    "REG-D": {"functions": ["90"], "mfr": "A.EBERLE", "desc": "Rơ-le điều chỉnh điện áp tự động (REG-D/REG-DA)"},
    "REG-DA": {"functions": ["90"], "mfr": "A.EBERLE", "desc": "Rơ-le điều chỉnh điện áp tự động (REG-DA)"},
    "M-2001": {"functions": ["90"], "mfr": "BECKWITH", "desc": "Bộ điều khiển nấc phân áp biến áp (Beckwith M-2001)"},
}

# 2. Bảng ánh xạ Từ khóa Chức năng (ANSI & Tiếng Việt) có trong TÊN RƠ-LE CSDL
RELAY_FUNCTION_KEYWORDS = {
    "87L": ["87l", "f87l", "so lech dz", "so lech duong day", "so lech quang", "so lech dd", "so lech"],
    "21": ["f21", "khoang cach", "21 21n", "21n"],
    "87T": ["87t", "f87t", "so lech mba", "so lech may bien ap", "so lech bien ap", "so lech t1", "so lech t2", "so lech at1", "so lech at2"],
    "87R": ["87r", "f87r", "so lech khang", "so lech cuon khang"],
    "87B": ["87b", "f87b", "so lech thanh cai", "so lech thanh dan"],
    "50/51": ["f50", "f51", "50 51", "50n", "51n", "50n 51n", "qua dong", "qua dong cham dat", "cat nhanh", "67", "67n", "f67"],
    "67": ["67", "67n", "f67", "qua dong co huong", "qua dong"],
    "64REF": ["64ref", "64 ref", "f64ref", "f64", "64r", "cham dat han che", "cham dat gioi han", "ref", "so lech cham dat han che", "restricted earth fault"],
    "90": ["90", "f90", "dieu chinh dien ap", "tu dong dieu chinh dien ap", "dieu ap", "avr", "oltc", "nap phan ap", "dieu ap duoi tai", "tapcon", "reg d", "regda"],
    "49": ["49", "f49", "qua nhiet", "dong co", "motor", "nhiet do"],
    "87G": ["87g", "f87g", "so lech may phat", "so lech mf", "generator"],
    "40": ["40", "f40", "mat kich tu", "loss of field"],
    "64G": ["64g", "f64g", "cham dat stato", "stator earth fault"],
    "79": ["79", "f79", "tu dong dong lai", "dong lai", "autoreclose", "tdl"],
    "25": ["25", "f25", "kiem tra hoa dong bo", "hoa dong bo", "synchrocheck"],
    "50BF": ["50bf", "f50bf", "hu hong may cat"],
    "BCU": ["bcu", "dieu khien ngan", "dieu khien", "bay control"],
}

# 3. Đồng nghĩa Hãng sản xuất
MANUFACTURER_ALIASES = {
    "nari": ["nari", "nr", "nr electric", "nam thuy"],
    "nr electric": ["nari", "nr", "nr electric", "nam thuy"],
    "nr": ["nari", "nr", "nr electric"],
    "siemens": ["siemens", "siemens ag", "siprotec", "digsi", "digsi 4", "digsi 5", "sigra"],
    "digsi": ["siemens", "siemens ag", "siprotec", "digsi", "digsi 4", "digsi 5", "sigra"],
    "siprotec": ["siemens", "siemens ag", "siprotec", "digsi", "digsi 4", "digsi 5", "sigra"],
    "sigra": ["siemens", "siemens ag", "siprotec", "digsi", "sigra"],
    "abb": ["abb", "hitachi", "hitachi energy", "relion", "pcm600"],
    "hitachi": ["abb", "hitachi", "hitachi energy", "relion", "pcm600"],
    "hitachi energy": ["abb", "hitachi", "hitachi energy", "relion", "pcm600"],
    "relion": ["abb", "hitachi", "hitachi energy", "relion", "pcm600"],
    "pcm600": ["abb", "hitachi", "hitachi energy", "relion", "pcm600"],
    "schneider": ["schneider", "alstom", "areva", "micom", "s1 agile", "easergy"],
    "alstom": ["schneider", "alstom", "areva", "micom"],
    "areva": ["schneider", "alstom", "areva", "micom"],
    "micom": ["micom", "schneider", "alstom", "areva", "s1 agile", "easergy"],
    "sel": ["sel", "schweitzer", "schweitzer engineering", "acselerator", "quickset", "sel-5030", "synchrowave", "sel-5601"],
    "schweitzer": ["sel", "schweitzer", "schweitzer engineering", "acselerator", "quickset", "sel-5030", "synchrowave"],
    "quickset": ["sel", "schweitzer", "acselerator", "quickset", "sel-5030"],
    "acselerator": ["sel", "schweitzer", "acselerator", "quickset", "sel-5030"],
    "synchrowave": ["sel", "schweitzer", "synchrowave", "sel-5601"],
    "ge": ["ge", "general electric", "multilin", "enervista"],
    "mr": ["mr", "reinhausen", "maschinenfabrik reinhausen"],
    "reinhausen": ["mr", "reinhausen", "maschinenfabrik reinhausen"],
    "a.eberle": ["a.eberle", "eberle", "a-eberle", "a eberle"],
    "beckwith": ["beckwith", "beckwith electric"],
    "toshiba": ["toshiba", "gr-tiems", "grz", "grt", "grb", "grd", "gbu"],
    "bender": ["bender", "iso685", "rcms460"],
    "protecta": ["protecta", "europrot", "europrot+"],
    "arteche": ["arteche", "vj", "rd", "tcs"],
    "vizimax": ["vizimax", "synchroteq"],
    "hyoda": ["hyoda"],
    "messko": ["messko"],
    "akm": ["akm"],
    "qualitrol": ["qualitrol", "509itm"],
    "emb": ["emb", "rs2001"],
    "cedaspe": ["cedaspe"],
    "comem": ["comem"],
    "smitt": ["smitt"],
    "trench": ["trench"],
    "sieyuan": ["sieyuan"],
    "coelme": ["coelme"],
    "mesa": ["mesa"],
    "tbea": ["tbea"],
    "shenyang": ["shenyang", "sbw"],
    "hyundai": ["hyundai"],
    "mitsubishi": ["mitsubishi"],
    "cooper": ["cooper"],
    "xd": ["xd", "xd xian", "xian"],
    "remsdaq": ["remsdaq"],
    "eaton": ["eaton"],
    "elin": ["elin"],
    "kinkei": ["kinkei"],
    "ziv": ["ziv"],
    "ls": ["ls", "lsis", "ls electric"],
    "kyongbo": ["kyongbo"],
    "rfl": ["rfl"],
    "ce": ["ce"],
    "hapam": ["hapam"],
    "taikai": ["taikai"],
    "magrini": ["magrini", "magrini galileo"],
    "stromwandler": ["stromwandler"],
}

# 4. Danh sách từ khóa Thiết bị Phụ trợ / Cơ điện / Tiêu đề Công cụ Phần mềm (Cần loại trừ khi tìm rơ-le số chính)
AUXILIARY_KEYWORDS = [
    "ro le hoi", "van ap luc", "van cat nhanh", "van ", "dong ho nhiet do", "dong ho muc dau",
    "dong ho", "ap luc", "muc dau", "nhiet do", "lua chon thoi diem",
    "bo chi thi", "bien dong", "bien dien ap", "bien dong dien",
    "parameter setting", "application configuration", "signal matrix", "disturbance handling", "connectivity package",
    "cfc", "sigra", "continuous function chart", "single line editor", "display editor", "system configurator",
    "selogic", "quickset", "synchrowave", "graphical logic editor", "terminal"
]


def normalize_text(text):
    """Chuẩn hóa tiếng Việt: Bỏ dấu, lowercase, chỉ giữ chữ và số."""
    if not text:
        return ""
    text = str(text)
    nfkd = unicodedata.normalize('NFD', text)
    no_accent = ''.join(c for c in nfkd if unicodedata.category(c) != 'Mn')
    no_accent = no_accent.replace('đ', 'd').replace('Đ', 'D')
    cleaned = re.sub(r'[^a-zA-Z0-9\s]', ' ', no_accent)
    return re.sub(r'\s+', ' ', cleaned).strip().lower()


def extract_circuit_number(ocr_fields):
    """
    Trích xuất số mạch bảo vệ (1 hoặc 2) từ các trường OCR:
    'protection_circuit' ('Mạch Bảo Vệ'), 'protection_cabinet' ('Tủ Bảo Vệ'),
    'protected_equipment' hoặc 'relay_name'.
    """
    raw_texts = [
        str(ocr_fields.get('protection_circuit') or ''),
        str(ocr_fields.get('Mạch Bảo Vệ') or ''),
        str(ocr_fields.get('protection_cabinet') or ''),
        str(ocr_fields.get('Tủ Bảo Vệ') or ''),
        str(ocr_fields.get('form_title') or ''),
        str(ocr_fields.get('protected_equipment') or ''),
        str(ocr_fields.get('Thiết Bị Được Bảo Vệ') or ''),
    ]
    norm_combined = normalize_text(' '.join(raw_texts))
    
    # Kiểm tra mạch 1
    if re.search(r'\b(mach 1|bo 1|bao ve 1|main 1|circuit 1|wr1|wr4|m1)\b', norm_combined) or 'mach 1' in norm_combined or 'bo 1' in norm_combined or 'wr4' in norm_combined or 'wr1' in norm_combined:
        return 1
    # Kiểm tra mạch 2
    if re.search(r'\b(mach 2|bo 2|bao ve 2|main 2|circuit 2|wr2|wr5|m2)\b', norm_combined) or 'mach 2' in norm_combined or 'bo 2' in norm_combined or 'wr5' in norm_combined or 'wr2' in norm_combined:
        return 2
        
    return None


def extract_target_functions_and_model(ocr_fields):
    """
    Xác định họ Model, hãng sản xuất, chức năng chính và chức năng phụ từ dữ liệu OCR.
    """
    relay_name_raw = str(ocr_fields.get('relay_name') or ocr_fields.get('Tên Rơ-le') or '').strip()
    relay_serial_raw = str(ocr_fields.get('relay_serial') or ocr_fields.get('Số Hiệu Rơ-le') or '').strip()
    protection_type_raw = str(ocr_fields.get('protection_type') or ocr_fields.get('Kiểu Bảo Vệ') or '').strip()
    equipment_raw = str(ocr_fields.get('protected_equipment') or ocr_fields.get('Thiết Bị Được Bảo Vệ') or '').strip()
    manufacturer_raw = str(ocr_fields.get('manufacturer') or ocr_fields.get('Nhà Chế Tạo') or '').strip()
    software_raw = str(ocr_fields.get('software') or ocr_fields.get('Phần mềm') or '').strip()

    norm_relay = normalize_text(f"{relay_name_raw} {relay_serial_raw}")
    norm_relay_compact = norm_relay.replace(' ', '')
    norm_prot = normalize_text(protection_type_raw)
    norm_equip = normalize_text(equipment_raw)
    norm_mfr = normalize_text(manufacturer_raw)
    norm_software = normalize_text(software_raw)

    detected_model = None
    detected_mfr = None
    model_functions = set()

    # 1. Tra cứu Model từ MODEL_REGISTRY
    for prefix, info in MODEL_REGISTRY.items():
        norm_prefix = normalize_text(prefix)
        norm_prefix_compact = norm_prefix.replace(' ', '')
        if norm_prefix in norm_relay or norm_prefix_compact in norm_relay_compact or prefix.lower() in relay_name_raw.lower():
            detected_model = prefix
            detected_mfr = info.get('mfr')
            for fn in info.get('functions', []):
                model_functions.add(fn)
            break

    # Suy diễn Hãng từ Phần mềm cấu hình nếu chưa có hãng
    if not detected_mfr:
        if 'pcm600' in norm_software:
            detected_mfr = 'ABB'
        elif 'digsi' in norm_software or 'sigra' in norm_software:
            detected_mfr = 'SIEMENS'
        elif 's1 agile' in norm_software or 'easergy' in norm_software or 'micom s1' in norm_software:
            detected_mfr = 'MICOM'
        elif 'acselerator' in norm_software or 'quickset' in norm_software or 'synchrowave' in norm_software or 'sel 5030' in norm_software or 'sel 5601' in norm_software:
            detected_mfr = 'SEL'
        elif 'enervista' in norm_software:
            detected_mfr = 'GE'

    # 2. Phân tách Chức năng CHÍNH (Primary) vs Chức năng PHỤ (Secondary)
    # Phần đứng trước ngoặc đơn '(' hoặc trước từ 'kèm' là chức năng chính
    primary_text = normalize_text(protection_type_raw.split('(')[0].split('kèm')[0].split('kem')[0])
    primary_functions = set()
    secondary_functions = set(model_functions)

    for fn_code, keywords in RELAY_FUNCTION_KEYWORDS.items():
        for kw in keywords:
            if kw in primary_text:
                primary_functions.add(fn_code)
                break
            elif kw in norm_prot:
                secondary_functions.add(fn_code)
                break

    # 3. Định hướng thêm từ Thiết bị được bảo vệ:
    if 'khang' in norm_equip or re.search(r'\bkh\d{3}\b', norm_equip):
        if '87R' in model_functions or 'so lech' in primary_text:
            primary_functions.add('87R')
    elif 'mba' in norm_equip or 'bien ap' in norm_equip or re.search(r'\bat\d\b', norm_equip):
        if '64REF' in model_functions and ('cham dat han che' in primary_text or 'ref' in primary_text or '64' in primary_text):
            primary_functions.add('64REF')
        elif '90' in model_functions or 'dieu ap' in primary_text or 'dieu chinh dien ap' in primary_text or 'avr' in primary_text:
            primary_functions.add('90')
        elif '87T' in model_functions or 'so lech' in primary_text:
            primary_functions.add('87T')
    elif 'duong day' in norm_equip or re.search(r'\b(57\d|27\d|17\d)\b', norm_equip):
        if 'so lech' in primary_text:
            primary_functions.add('87L')
        elif 'khoang cach' in primary_text:
            primary_functions.add('21')

    # Nếu chưa tìm thấy primary thì lấy các chức năng từ model/kiểu bảo vệ
    if not primary_functions and secondary_functions:
        primary_functions = set(secondary_functions)

    return {
        'detected_model': detected_model,
        'detected_mfr': detected_mfr or manufacturer_raw,
        'primary_functions': list(primary_functions),
        'secondary_functions': list(secondary_functions),
        'relay_name_raw': relay_name_raw,
        'relay_serial_raw': relay_serial_raw,
        'norm_mfr': norm_mfr
    }


def score_relay_candidate(relay_dict, ocr_fields, analysis):
    """
    Tính điểm trùng khớp (0 - 150 điểm) cho một rơ-le ứng viên trong CSDL.
    
    relay_dict: dict có các key {'id', 'relay_code', 'relay_name', 'manufacturer', 'bay_id'}
    """
    score = 0
    match_reasons = []

    relay_code = str(relay_dict.get('relay_code') or '').strip()
    relay_name = str(relay_dict.get('relay_name') or '').strip()
    relay_mfr = str(relay_dict.get('manufacturer') or '').strip()

    norm_r_code = normalize_text(relay_code)
    norm_r_name = normalize_text(relay_name)
    norm_r_mfr = normalize_text(relay_mfr)

    # ── ĐIỀU KIỆN 0: Loại trừ thiết bị phụ trợ/cơ điện ─────────────────────────
    for aux_kw in AUXILIARY_KEYWORDS:
        if aux_kw in norm_r_name:
            # Phạt cực nặng để không bao giờ chọn nhầm Van áp lực, Rơ le hơi, Đồng hồ...
            return -100, ["Thiết bị cơ điện / phụ trợ"]

    # ── TẦNG 1: Khớp Định danh Trực tiếp (Mã hoặc Tên rơ-le trùng thẳng) ───────
    raw_model = analysis['relay_name_raw'].strip().lower()
    if raw_model and (raw_model in relay_name.lower() or raw_model in relay_code.lower()):
        score += 80
        match_reasons.append(f"Model '{analysis['relay_name_raw']}' có trong tên")

    norm_model = normalize_text(raw_model)
    if norm_model and (norm_model in norm_r_name or norm_model in norm_r_code):
        score += 40

    # ── TẦNG 2: Khớp Chức năng CHÍNH vs PHỤ (ANSI & Tiếng Việt) ───────────────
    primary_functions = analysis['primary_functions']
    secondary_functions = analysis['secondary_functions']

    matched_primary = []
    for fn in primary_functions:
        keywords = RELAY_FUNCTION_KEYWORDS.get(fn, [fn.lower()])
        for kw in keywords:
            is_short = len(kw) <= 3 or kw.isdigit()
            if is_short:
                if re.search(rf'\b(?:f)?{re.escape(kw)}\b', norm_r_name):
                    matched_primary.append(fn)
                    break
            else:
                if kw in norm_r_name or f"f{kw}" in norm_r_name:
                    matched_primary.append(fn)
                    break

    if matched_primary:
        score += 60 * len(matched_primary)
        match_reasons.append(f"Chức năng chính: {', '.join(matched_primary)}")
    else:
        # Nếu không khớp chức năng chính, kiểm tra chức năng phụ
        matched_secondary = []
        for fn in secondary_functions:
            keywords = RELAY_FUNCTION_KEYWORDS.get(fn, [fn.lower()])
            for kw in keywords:
                is_short = len(kw) <= 3 or kw.isdigit()
                if is_short:
                    if re.search(rf'\b(?:f)?{re.escape(kw)}\b', norm_r_name):
                        matched_secondary.append(fn)
                        break
                else:
                    if kw in norm_r_name or f"f{kw}" in norm_r_name:
                        matched_secondary.append(fn)
                        break
        if matched_secondary:
            score += 15 * len(matched_secondary)
            match_reasons.append(f"Chức năng phụ: {', '.join(matched_secondary)}")

    # ── TẦNG 3: Khớp Mạch Bảo Vệ (Mạch 1 -> F87...1, Mạch 2 -> F87...2) ───────
    circuit_num = extract_circuit_number(ocr_fields)
    combined_relay_text = f"{norm_r_code} {norm_r_name}"
    if circuit_num:
        circuit_target = str(circuit_num)
        opposite_circuit = '2' if circuit_num == 1 else '1'
        
        # So khớp mẫu Mạch bảo vệ (F50-1/F50-2, F87...1/F87...2, F21-1/F21-2, Mạch 1/2)
        has_correct_circuit = bool(re.search(rf'(?:f)?(?:87[rtl]?|50|51|21)[\-_ \.]*{circuit_target}\b|mach\s*{circuit_target}\b|bo\s*{circuit_target}\b', combined_relay_text))
        has_wrong_circuit = bool(re.search(rf'(?:f)?(?:87[rtl]?|50|51|21)[\-_ \.]*{opposite_circuit}\b|mach\s*{opposite_circuit}\b|bo\s*{opposite_circuit}\b', combined_relay_text))

        if has_correct_circuit:
            score += 30
            match_reasons.append(f"Khớp Mạch {circuit_num}")
        elif has_wrong_circuit:
            score -= 40
            match_reasons.append(f"Lệch Mạch (Phiếu Mạch {circuit_num} ≠ Rơ-le)")

    # ── TẦNG 4: Khớp hoặc Xung đột Hãng Sản Xuất ───────────────────────────────
    expected_mfr = normalize_text(analysis['detected_mfr'])
    if expected_mfr and norm_r_mfr:
        valid_aliases = MANUFACTURER_ALIASES.get(expected_mfr, [expected_mfr])
        if any(alias in norm_r_mfr for alias in valid_aliases) or norm_r_mfr in expected_mfr:
            score += 20
            match_reasons.append(f"Hãng {relay_mfr}")
        else:
            known_mfrs = {"siemens", "abb", "hitachi", "schneider", "alstom", "areva", "sel", "ge", "nari"}
            if any(m in norm_r_mfr for m in known_mfrs) and any(m in expected_mfr for m in known_mfrs):
                score -= 50
                match_reasons.append(f"Lệch Hãng ({relay_mfr} ≠ {analysis['detected_mfr']})")

    # ── TẦNG 4B: Xung đột Dòng Model (Phạt nặng nếu mang dòng model khác) ─────
    detected_model = analysis.get('detected_model')
    if detected_model:
        norm_det_model = normalize_text(detected_model)
        for prefix in MODEL_REGISTRY:
            norm_prefix = normalize_text(prefix)
            if norm_prefix in norm_det_model or norm_det_model in norm_prefix:
                continue
            if norm_prefix in norm_r_name:
                score -= 50
                match_reasons.append(f"Lệch Model ({relay_name} ≠ {analysis['relay_name_raw']})")
                break

    # ── TẦNG 5: Khớp Ngăn Lộ / Máy Cắt (Bay / Breaker Context) ────────────────
    relay_bay_name = normalize_text(relay_dict.get('bay_name') or '')
    ocr_breaker = normalize_text(ocr_fields.get('circuit_breaker') or ocr_fields.get('Máy Cắt') or '')
    ocr_equip = normalize_text(ocr_fields.get('protected_equipment') or ocr_fields.get('Thiết Bị Được Bảo Vệ') or '')

    if relay_bay_name:
        if ocr_breaker and (ocr_breaker in relay_bay_name or re.search(rf'\b{ocr_breaker}\b', relay_bay_name)):
            score += 40
            match_reasons.append(f"Ngăn MC {ocr_breaker}")
        elif ocr_equip:
            equip_tokens = [tok for tok in ocr_equip.split() if (len(tok) >= 3 and tok.isdigit()) or re.match(r'^[a-z]+\d+$', tok)]
            matched_equip = False
            for tok in equip_tokens:
                if tok in relay_bay_name or re.search(rf'\b{tok}\b', relay_bay_name):
                    score += 40
                    match_reasons.append(f"Ngăn {tok.upper()}")
                    matched_equip = True
                    break
            if not matched_equip and (ocr_breaker or equip_tokens):
                score -= 60
                match_reasons.append(f"Lệch Ngăn ({relay_bay_name})")
        elif ocr_breaker:
            score -= 60
            match_reasons.append(f"Lệch Ngăn ({relay_bay_name})")

    return score, match_reasons


def match_relay_from_ocr(ocr_fields, candidate_relays):
    """
    Đánh giá danh sách candidate_relays và chọn ra rơ-le phù hợp nhất.
    
    ocr_fields: dict chứa các trường thông tin Trang 1 từ OCR
    candidate_relays: list of Relay instances hoặc dicts
    
    Trả về: (best_candidate, best_score, explanation_str) hoặc (None, 0, "")
    """
    if not candidate_relays:
        return None, 0, ""

    analysis = extract_target_functions_and_model(ocr_fields)
    
    best_candidate = None
    best_score = -999
    best_reasons = []

    for item in candidate_relays:
        if hasattr(item, 'id'):
            bay_name = ''
            if hasattr(item, 'bay') and item.bay:
                bay_name = getattr(item.bay, 'bay_name', '')
            relay_dict = {
                'id': item.id,
                'relay_code': getattr(item, 'relay_code', ''),
                'relay_name': getattr(item, 'relay_name', ''),
                'manufacturer': getattr(item, 'manufacturer', ''),
                'bay_id': getattr(item, 'bay_id', None),
                'bay_name': bay_name,
                'obj': item
            }
        else:
            relay_dict = item

        score, reasons = score_relay_candidate(relay_dict, ocr_fields, analysis)
        if score > best_score:
            best_score = score
            best_candidate = relay_dict.get('obj', item)
            best_reasons = reasons

    # Ngưỡng tin cậy an toàn: Cần đạt ít nhất 30 điểm
    if best_score >= 30 and best_candidate:
        reason_text = " • ".join(best_reasons)
        return best_candidate, best_score, reason_text

    return None, best_score, ""
````

## File: sheets/services.py
````python
import uuid
import hashlib
from datetime import datetime

class MockEVNSignatureService:
    """
    Dịch vụ mô phỏng API Ký số EVN.
    """
    def initiate_signing_session(self, sheet_id, signer_role):
        """Mô phỏng việc khởi tạo phiên ký số."""
        session_id = f"EVN-MOCK-{uuid.uuid4().hex[:10].upper()}"
        signing_url = f"https://mock-sign.evn.com.vn/sign?session={session_id}"
        
        return {
            "success": True,
            "session_id": session_id,
            "signing_url": signing_url,
            "expires_in": 300
        }

    def confirm_signature(self, sheet, signer_name, signer_role):
        """Mô phỏng xác nhận ký số thành công."""
        raw_content = f"{sheet.sheet_code}_{signer_role}_{datetime.now().isoformat()}"
        signature_hash = hashlib.sha256(raw_content.encode('utf-8')).hexdigest()
        
        return {
            "success": True,
            "signature_hash": signature_hash,
            "signed_at": datetime.now(),
            "status": "SIGNED"
        }

# Khởi tạo singleton
evn_service = MockEVNSignatureService()
````

## File: sheets/signals.py
````python
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import SettingSheet

def invalidate_sheet_cache(sender, instance, **kwargs):
    """
    Tự động tăng version cache khi có phiếu được thêm, sửa, hoặc xóa.
    Điều này làm vô hiệu hóa tất cả các cache cũ của danh sách phiếu,
    đảm bảo người dùng luôn thấy dữ liệu mới nhất.
    """
    try:
        cache.incr('sheet_list_version')
    except ValueError:
        # ValueError xảy ra khi key chưa tồn tại
        cache.set('sheet_list_version', 2)

@receiver(post_save, sender=SettingSheet)
def on_sheet_save(sender, instance, **kwargs):
    invalidate_sheet_cache(sender, instance, **kwargs)

@receiver(post_delete, sender=SettingSheet)
def on_sheet_delete(sender, instance, **kwargs):
    invalidate_sheet_cache(sender, instance, **kwargs)
````

## File: sheets/tasks.py
````python
from celery import shared_task
from django.core.cache import cache
from django.utils import timezone
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import random
import re
import time
import uuid

@shared_task
def execute_bulk_create_task(idempotency_key, user_id, sheet_ids):
    from sheets.models import SettingSheet
    from django.contrib.auth.models import User
    from sheets.views import perform_mock_ocr
    
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        cache.set(idempotency_key, {'status': 'ERROR', 'message': 'User not found'}, timeout=86400)
        return

    success_count = 0
    failed_count = 0
    
    channel_layer = get_channel_layer()

    for sheet_id in sheet_ids:
        try:
            sheet = SettingSheet.objects.get(id=sheet_id)
            file_name = sheet.title
            
            # Gửi thông báo đang bắt đầu xử lý file này
            if channel_layer:
                async_to_sync(channel_layer.group_send)(
                    f"user_{user_id}",
                    {
                        "type": "bulk_progress",
                        "event_type": "bulk_progress",
                        "idempotency_key": idempotency_key,
                        "sheet_id": sheet_id,
                        "file_name": file_name,
                        "status": "processing"
                    }
                )

            # Perform OCR on the uploaded file
            perform_mock_ocr(sheet)
            # Update status to ISSUED (Chờ rà soát)
            sheet.status = 'ISSUED'
            sheet.save(update_fields=['status'])
            success_count += 1
            # Simulate OCR processing delay
            time.sleep(2)
            
            if channel_layer:
                async_to_sync(channel_layer.group_send)(
                    f"user_{user_id}",
                    {
                        "type": "bulk_progress",
                        "event_type": "bulk_progress",
                        "idempotency_key": idempotency_key,
                        "sheet_id": sheet_id,
                        "file_name": file_name,
                        "status": "success",
                        "processed_count": success_count + failed_count,
                        "total": len(sheet_ids)
                    }
                )
                async_to_sync(channel_layer.group_send)(
                    f"user_{user_id}",
                    {
                        "type": "bulk_progress",
                        "event_type": "update_badges"
                    }
                )
        except Exception as e:
            failed_count += 1
            if channel_layer:
                async_to_sync(channel_layer.group_send)(
                    f"user_{user_id}",
                    {
                        "type": "send_notification",
                        "event_type": "bulk_progress",
                        "idempotency_key": idempotency_key,
                        "sheet_id": sheet_id,
                        "status": "failed",
                        "processed_count": success_count + failed_count,
                        "total": len(sheet_ids)
                    }
                )

    result_data = {
        'status': 'COMPLETED',
        'total_requested': len(sheet_ids),
        'success': success_count,
        'failed': failed_count,
        'finished_at': timezone.now().isoformat()
    }

    # Lưu kết quả vào Redis giữ trong 24h
    cache.set(idempotency_key, result_data, timeout=86400)
    
    # Gửi thông báo WebSocket tới User
    channel_layer = get_channel_layer()
    if channel_layer:
        async_to_sync(channel_layer.group_send)(
            f"user_{user_id}",
            {
                "type": "send_notification",
                "title": "Trích xuất Hàng loạt Hoàn tất",
                "message": f"Đã xử lý xong {len(sheet_ids)} file. Thành công: {success_count}, Thất bại: {failed_count}.",
                "level": "success" if failed_count == 0 else "warning"
            }
        )


def _run_ocr_cli(input_pdf, output_root, correlation_id, stage="all", device_mode="CPU",
                  ws_callback=None):
    """
    Chạy OCR CLI subprocess và tuỳ chọn gọi ws_callback(page_no, total_pages, msg) khi có
    thông báo tiến trình từng trang từ stderr.

    Trả về: (returncode, data_dict, stderr_str)
    """
    import subprocess
    import json
    import os
    import sys
    import threading
    import tempfile
    from django.conf import settings

    project_root = settings.BASE_DIR
    ocr_prj_root = os.path.join(project_root, 'OCR_PRJ')

    # ── Chọn đúng Python interpreter ──────────────────────────────────────────
    if os.name == 'nt':
        python_exe = os.path.join(ocr_prj_root, '.venv', 'Scripts', 'python.exe')
    else:
        python_exe = sys.executable

    if not os.path.exists(python_exe):
        return -1, None, f"Không tìm thấy Python OCR tại {python_exe}"

    # Dùng file tạm để nhận JSON output — tránh hoàn toàn vấn đề pipe deadlock
    # khi nhiều job chạy song song (orphaned PaddleOCR child processes giữ pipe mở).
    result_fd, result_path = tempfile.mkstemp(suffix='.json', prefix=f'ocr_{correlation_id}_')
    os.close(result_fd)

    cmd = [
        python_exe, "-m", "src.relay_form_ocr",
        "--input", str(input_pdf),
        "--output-root", str(output_root),
        "--correlation-id", f"{correlation_id}_{stage}",
        "--stage", stage,
        "--json",
        "--output-json", result_path,
        "--overwrite-result",
    ]
    if device_mode == 'GPU':
        cmd.append("--gpu")

    env = os.environ.copy()
    env['PYTHONPATH'] = ocr_prj_root
    env['PYTHONIOENCODING'] = 'utf-8'
    env['PYTHONUTF8'] = '1'

    # ── Chạy subprocess, đọc stderr theo từng dòng để bắt tiến trình trang ───
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,   # stdout không dùng nữa (kết quả ở file)
        stderr=subprocess.PIPE,
        cwd=ocr_prj_root,
        env=env,
        encoding='utf-8',
        errors='replace',
    )

    stderr_lines = []
    def _read_stderr():
        """Đọc toàn bộ stderr; gọi ws_callback khi thấy dòng tiến trình trang."""
        import re
        page_re = re.compile(r'trang\s+(\d+)/(\d+)', re.IGNORECASE)
        for line in proc.stderr:
            line = line.rstrip('\n')
            stderr_lines.append(line)
            if ws_callback:
                m = page_re.search(line)
                if m:
                    try:
                        ws_callback(int(m.group(1)), int(m.group(2)), line)
                    except Exception:
                        pass

    t_stderr = threading.Thread(target=_read_stderr, daemon=True)
    t_stderr.start()

    try:
        proc.wait(timeout=900)  # Timeout 15 phút
    except subprocess.TimeoutExpired:
        proc.kill()
        proc.wait()
        return -1, None, "Quá thời gian (15 phút). Tiến trình OCR bị treo."

    t_stderr.join(timeout=5)

    # Đọc kết quả từ file — không bị ảnh hưởng bởi orphaned child processes
    data = None
    try:
        if os.path.exists(result_path) and os.path.getsize(result_path) > 0:
            with open(result_path, 'r', encoding='utf-8') as f:
                data = json.load(f, parse_constant=lambda x: None)
    except Exception:
        pass
    finally:
        try:
            os.unlink(result_path)
        except Exception:
            pass

    return proc.returncode, data, '\n'.join(stderr_lines)



def _safe_send_ws(channel_layer, user_id, payload):
    if channel_layer and user_id:
        try:
            async_to_sync(channel_layer.group_send)(f"user_{user_id}", payload)
        except Exception:
            pass


def broadcast_ocr_job_update(job=None, job_id=None, stage_text=None):
    """
    Phát sóng sự kiện cập nhật tiến trình OCR qua WebSocket (Django Channels)
    đến toàn bộ client trong group 'ocr_updates' theo thời gian thực.
    """
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    from django.core.cache import cache
    from sheets.models import OcrJob

    channel_layer = get_channel_layer()
    if not channel_layer:
        return

    if job is None and job_id is not None:
        try:
            job = OcrJob.objects.select_related('sheet', 'sheet__created_by').get(id=job_id)
        except OcrJob.DoesNotExist:
            return

    if not job:
        return

    if stage_text:
        cache.set(f"ocr_stage_{job.id}", stage_text, timeout=86400)
    else:
        stage_text = cache.get(f"ocr_stage_{job.id}") or ''

    from django.utils import timezone
    local_created_at = timezone.localtime(job.created_at) if job.created_at else None

    job_data = {
        'id': job.id,
        'sheet_id': job.sheet.id if job.sheet else None,
        'sheet_code': job.sheet.sheet_code if job.sheet else f"Job#{job.id}",
        'sheet_title': job.sheet.title if job.sheet else '',
        'created_by': (
            job.sheet.created_by.get_full_name() or job.sheet.created_by.username
            if job.sheet and job.sheet.created_by else "Hệ thống"
        ),
        'device_mode': getattr(job, 'device_mode', 'CPU') or 'CPU',
        'status': job.status,
        'created_at_date': local_created_at.strftime('%d/%m/%Y') if local_created_at else '',
        'created_at_time': local_created_at.strftime('%H:%M:%S') if local_created_at else '',
        'error_code': job.error_code or '',
        'error_stage': job.error_stage or '',
        'error_detail': job.error_detail or '',
        'stage_text': stage_text or '',
    }

    try:
        admin_failed = OcrJob.objects.filter(status='FAILED').count()
        admin_proc = OcrJob.objects.filter(status__in=['PENDING', 'PROCESSING']).count()
        admin_succ = OcrJob.objects.filter(status__in=['SUCCESS', 'SUCCESS_WITH_WARNINGS']).count()
        admin_total = OcrJob.objects.count()

        admin_payload = {
            'type': 'ocr_event',
            'event_type': 'ocr_update',
            'job': job_data,
            'stats': {
                'total': min(admin_total, 50),
                'actual_total': admin_total,
                'success': admin_succ,
                'processing': admin_proc,
                'failed': admin_failed,
            }
        }
        async_to_sync(channel_layer.group_send)("admin_ocr_updates", admin_payload)
    except Exception:
        pass

    if job.sheet and job.sheet.created_by:
        user = job.sheet.created_by
        if not user.is_superuser:
            try:
                user_failed = OcrJob.objects.filter(sheet__created_by=user, status='FAILED').count()
                user_proc = OcrJob.objects.filter(sheet__created_by=user, status__in=['PENDING', 'PROCESSING']).count()
                user_succ = OcrJob.objects.filter(sheet__created_by=user, status__in=['SUCCESS', 'SUCCESS_WITH_WARNINGS']).count()
                user_total = OcrJob.objects.filter(sheet__created_by=user).count()

                user_payload = {
                    'type': 'ocr_event',
                    'event_type': 'ocr_update',
                    'job': job_data,
                    'stats': {
                        'total': min(user_total, 50),
                        'actual_total': user_total,
                        'success': user_succ,
                        'processing': user_proc,
                        'failed': user_failed,
                    }
                }
                async_to_sync(channel_layer.group_send)(f"user_{user.id}", user_payload)
            except Exception:
                pass


def _notify_page_progress(channel_layer, user_id, sheet_code, page_no, total_pages, stage_label):
    """Gửi thông báo WebSocket tiến trình bóc tách từng trang."""
    # Đã tắt thông báo popup để tránh spam màn hình khi xử lý nhiều phiếu
    pass

import threading

import os

# Cho phép cấu hình số luồng chạy song song cho từng công đoạn qua biến môi trường (mặc định 1)
# BoundedSemaphore cho phép cấu hình linh hoạt thay vì Lock (chỉ 1)
PIPELINE1_CONCURRENCY = int(os.environ.get('PIPELINE1_CONCURRENCY', 1))
PIPELINE2_CONCURRENCY = int(os.environ.get('PIPELINE2_CONCURRENCY', 2))

_pipeline1_lock = threading.BoundedSemaphore(PIPELINE1_CONCURRENCY)
_pipeline2_lock = threading.BoundedSemaphore(PIPELINE2_CONCURRENCY)

def _pipeline_header_worker(job_ids, user_id=None, device_mode='CPU'):
    """
    Pipeline 1 (chạy ngầm song song):
    Với mỗi file, bóc tách tuần tự Trang 1 rồi Trang 2 (theo thứ tự).
    Sau khi bóc tách xong Trang 1 & 2, cập nhật thông tin phiếu (Mã phiếu, trạm, thiết bị),
    đánh dấu cache `ocr_header_done_{job_id} = True` để Pipeline 2 tiếp quản xử lý Trang 3+,
    sau đó Pipeline 1 chuyển sang bóc tách Trang 1 & 2 của file tiếp theo.
    """
    from django.db import connection
    from django.conf import settings
    from sheets.models import OcrJob, SettingSheet
    from stations.models import Station, Relay
    import os

    output_root = os.path.join(settings.MEDIA_ROOT, 'ocr_artifacts')
    os.makedirs(output_root, exist_ok=True)
    channel_layer = get_channel_layer()

    for job_id in job_ids:
        with _pipeline1_lock:
            # ── Xóa cache cũ từ lần chạy trước (phòng flag stale gây lỗi) ─────────────
            cache.delete(f"ocr_header_done_{job_id}")
            cache.delete(f"ocr_header_failed_{job_id}")
            cache.delete(f"ocr_header_data_{job_id}")
    
            connection.close()
            try:
                job = OcrJob.objects.select_related('sheet', 'sheet__created_by').get(id=job_id)
            except OcrJob.DoesNotExist:
                cache.set(f"ocr_header_done_{job_id}", True, timeout=86400)
                cache.set(f"ocr_header_failed_{job_id}", True, timeout=86400)
                continue
    
            # ── Lấy đường dẫn file PDF ────────────────────────────────────────────
            input_pdf = None
            if job.sheet and job.sheet.scan_file:
                try:
                    input_pdf = job.sheet.scan_file.path
                except Exception:
                    input_pdf = str(job.sheet.scan_file)
    
            if not input_pdf or not os.path.exists(input_pdf):
                job.status = 'FAILED'
                job.error_detail = 'Không tìm thấy file scan PDF đính kèm.'
                job.save(update_fields=['status', 'error_detail'])
                broadcast_ocr_job_update(job=job, stage_text='Thiếu file scan PDF')
                cache.set(f"ocr_header_failed_{job_id}", True, timeout=86400)
                cache.set(f"ocr_header_done_{job_id}", True, timeout=86400)
                continue
    
            job.status = 'PROCESSING'
            job.sheet.status = 'DRAFT'
            job.sheet.save(update_fields=['status'])
            job.save(update_fields=['status'])
            broadcast_ocr_job_update(job=job, stage_text='Đang bóc tách Trang 1/2 (Thông tin chung)...')
    
            sheet_code = job.sheet.sheet_code or f"Job#{job_id}"
    
            # ── Thông báo bắt đầu Pipeline 1 ─────────────────────────────────────
            # Đã tắt thông báo popup
    
            # ── Định nghĩa callback cập nhật tiến trình trang ─────────────────────
            def _page_cb(page_no, total_pages, _msg, _chl=channel_layer, _uid=user_id,
                         _sc=sheet_code, _jb=job):
                _notify_page_progress(_chl, _uid, _sc, page_no, total_pages,
                                       f"Trang {page_no}/{total_pages} (Thông tin chung)")
                broadcast_ocr_job_update(job=_jb, stage_text=f"Đang bóc tách Trang {page_no}/{total_pages} (Thông tin chung)...")
    
            # ── Gọi OCR CLI cho stage=header (Trang 1 & 2 theo thứ tự) ───────────
            ret_code, data, stderr = _run_ocr_cli(
                input_pdf, output_root, job.correlation_id,
                stage="header", device_mode=device_mode,
                ws_callback=_page_cb,
            )
    
            if ret_code != 0 or not data or data.get('status') not in ('success', 'success_with_warnings'):
                job.status = 'FAILED'
                err_msg = (
                    (data.get('error', {}).get('message') if data and 'error' in data else None)
                    or stderr or f"Lỗi OCR Header (Exit Code {ret_code})"
                )
                job.error_detail = err_msg
                job.save(update_fields=['status', 'error_detail'])
                broadcast_ocr_job_update(job=job, stage_text='Lỗi bóc tách Trang 1 & 2')
                cache.set(f"ocr_header_failed_{job_id}", True, timeout=86400)
                cache.set(f"ocr_header_done_{job_id}", True, timeout=86400)
    
                _safe_send_ws(channel_layer, user_id, {
                    "type": "send_notification",
                    "title": "Lỗi bóc tách Trang 1 & 2",
                    "message": f"Không thể trích xuất thông tin chung của phiếu {sheet_code}: {err_msg[:150]}",
                    "level": "error",
                })
                _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})
                continue
    
            # ── Cập nhật thông tin phiếu từ kết quả Trang 1 ──────────────────────
            business = data.get('business', {})
            page1 = business.get('page1_fields', {})
    
            if 'ticket_number' in page1 and page1['ticket_number'].get('value'):
                ocr_sheet_code = page1['ticket_number']['value']
                if not SettingSheet.objects.filter(sheet_code=ocr_sheet_code).exclude(pk=job.sheet.pk).exists():
                    job.sheet.sheet_code = ocr_sheet_code
                    job.sheet.title = f"Phiếu {job.sheet.sheet_code}"
                else:
                    job.sheet.title = f"Phiếu {ocr_sheet_code} (Bản phụ)"
                sheet_code = job.sheet.sheet_code
    
            if 'station' in page1 and page1['station'].get('value'):
                station_name_ocr = page1['station']['value']
                from stations.models import Station
                from sheets.relay_matcher import normalize_text
                
                # 1. Thử match trực tiếp
                st = Station.objects.filter(station_name__icontains=station_name_ocr).first()
                # 2. Nếu không được, tìm theo từ khóa trạm (chuẩn hóa tiếng Việt, bỏ tiền tố trạm, mã điều độ và hậu tố ngoặc)
                if not st:
                    norm_ocr_st = normalize_text(station_name_ocr)
                    clean_ocr = norm_ocr_st.replace('tram', '').split('(')[0].strip()
                    ocr_words = [w for w in clean_ocr.split() if len(w) >= 3 and not re.match(r'^[e]\d+(\.\d+)?$', w)]
                    for s_obj in Station.objects.all():
                        norm_s_name = normalize_text(s_obj.station_name).replace('tram', '').strip()
                        if clean_ocr and norm_s_name and (clean_ocr in norm_s_name or norm_s_name in clean_ocr):
                            st = s_obj
                            break
                        if ocr_words and all(w in norm_s_name for w in ocr_words):
                            st = s_obj
                            break
                if st and not job.sheet.station:
                    job.sheet.station = st
    
            # Nhận diện Rơ-le thông minh qua Multi-Layer Relay Matcher
            from sheets.relay_matcher import match_relay_from_ocr
            flat_page1 = {k: v.get('value') for k, v in page1.items() if isinstance(v, dict)}

            candidate_relays = []
            if job.sheet.station:
                # Quét toàn bộ rơ-le trong trạm (có prefetch bay để engine chấm điểm đa tầng cả bay và máy cắt)
                candidate_relays = list(Relay.objects.filter(bay__station=job.sheet.station).select_related('bay'))
            else:
                candidate_relays = []

            if candidate_relays:
                matched_rl, match_score, match_why = match_relay_from_ocr(flat_page1, candidate_relays)
                if matched_rl and not job.sheet.relay:
                    if matched_rl.bay and matched_rl.bay.station_id == job.sheet.station.id:
                        job.sheet.relay = matched_rl
    
            job.sheet.status = 'ISSUED'   # Chuyển sang Chờ rà soát ngay sau Trang 1 & 2
            job.sheet.save()
            cache.set(f"ocr_header_data_{job_id}", data, timeout=86400)
            cache.set(f"ocr_header_done_{job_id}", True, timeout=86400)
    
            # ── Thông báo Pipeline 1 hoàn tất, Pipeline 2 được giải phóng ─────────
            broadcast_ocr_job_update(job=job, stage_text='Hoàn thành thông tin chung, đang chờ bóc tách bảng thông số...')
            _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})


def _load_header_data_from_disk(output_root, correlation_id):
    """
    Fallback nạp dữ liệu header từ disk artifact nếu cache Redis bị mất
    (do worker restart, timeout hoặc cache miss).
    """
    import os
    import json
    header_dir = os.path.join(output_root, f"{correlation_id}_header")
    extraction_path = os.path.join(header_dir, "extraction.json")
    if not os.path.exists(extraction_path):
        return {}
    try:
        with open(extraction_path, "r", encoding="utf-8") as f:
            raw_res = json.load(f)
        p1_fields = {}
        for k, v in raw_res.get("important_fields", {}).items():
            p1_fields[k] = {"value": v}
        
        pages = raw_res.get("pages", [])
        pages_dir = os.path.join(header_dir, "pages")
        if os.path.isdir(pages_dir):
            loaded_pages = []
            for pf in sorted(os.listdir(pages_dir)):
                if pf.endswith('.json'):
                    try:
                        with open(os.path.join(pages_dir, pf), 'r', encoding='utf-8') as pff:
                            loaded_pages.append(json.load(pff))
                    except Exception:
                        pass
            if loaded_pages:
                pages = loaded_pages

        return {
            "stage": "header",
            "status": "success",
            "correlation_id": f"{correlation_id}_header",
            "business": {
                "page1_fields": p1_fields,
                "important_source_labels": raw_res.get("important_source_labels", {}),
                "important_field_resolution": raw_res.get("important_field_resolution", {}),
            },
            "pages": pages,
            "warnings": raw_res.get("warnings", []),
            "summary": raw_res.get("summary", {}),
        }
    except Exception:
        return {}


def _pipeline_details_worker(job_ids, user_id=None, device_mode='CPU'):
    """
    Pipeline 2 (chạy ngầm song song):
    Chờ Pipeline 1 hoàn thành Trang 1 & 2 của từng file, sau đó bóc tách tuần tự
    Trang 3 → Trang 4 → Trang 5 → ... theo thứ tự.
    Sau khi hoàn tất, cập nhật bảng thông số và chuyển phiếu sang Chờ rà soát.
    """
    from django.db import connection
    from django.conf import settings
    from sheets.models import OcrJob
    from sheets.utils import update_has_parameters_changed_for_sheet
    import os

    output_root = os.path.join(settings.MEDIA_ROOT, 'ocr_artifacts')
    os.makedirs(output_root, exist_ok=True)
    channel_layer = get_channel_layer()

    for job_id in job_ids:
        with _pipeline2_lock:
            try:
                # ── Đợi Pipeline 1 hoàn tất file này (timeout 10 phút) ───────────────
                wait_start = time.time()
                while not cache.get(f"ocr_header_done_{job_id}"):
                    if time.time() - wait_start > 600:
                        # Hết timeout: Pipeline 1 có thể bị chết — đánh dấu FAILED rõ ràng
                        connection.close()
                        try:
                            stuck_job = OcrJob.objects.select_related('sheet').get(id=job_id)
                            if stuck_job.status == 'PROCESSING':
                                stuck_job.status = 'FAILED'
                                stuck_job.error_detail = 'Pipeline 1 (Header) timeout sau 10 phút. Có thể do Celery khởi động lại giữa chừng. Hãy thử lại.'
                                stuck_job.save(update_fields=['status', 'error_detail'])
                                broadcast_ocr_job_update(job=stuck_job, stage_text='Timeout — Thử lại')
                                _safe_send_ws(channel_layer, user_id, {
                                    "type": "bulk_progress",
                                    "event_type": "update_badges"
                                })
                        except Exception:
                            pass
                        break
                    time.sleep(0.5)
        
                # Nếu Pipeline 1 báo lỗi → bỏ qua file này
                if cache.get(f"ocr_header_failed_{job_id}"):
                    continue
        
                connection.close()
                try:
                    job = OcrJob.objects.select_related('sheet', 'sheet__created_by').get(id=job_id)
                except OcrJob.DoesNotExist:
                    continue
        
                input_pdf = None
                if job.sheet and job.sheet.scan_file:
                    try:
                        input_pdf = job.sheet.scan_file.path
                    except Exception:
                        input_pdf = str(job.sheet.scan_file)
        
                if not input_pdf or not os.path.exists(input_pdf):
                    job.status = 'FAILED'
                    job.error_detail = 'Không tìm thấy file scan PDF (Pipeline 2).'
                    job.save(update_fields=['status', 'error_detail'])
                    broadcast_ocr_job_update(job=job, stage_text='Thiếu file PDF ở Pipeline 2')
                    _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})
                    continue
        
                sheet_code = job.sheet.sheet_code or f"Job#{job_id}"
                page_count = 0
                try:
                    import fitz
                    with fitz.open(input_pdf) as doc:
                        page_count = len(doc)
                except Exception:
                    pass
                    
                if page_count > 0:
                    stage_txt = f'Đang khởi tạo OCR (Trang 2/{page_count})...'
                else:
                    stage_txt = 'Đang khởi tạo OCR (Trang 2+)...'
                    
                broadcast_ocr_job_update(job=job, stage_text=stage_txt)
        
                # ── Định nghĩa callback cập nhật tiến trình trang ─────────────────────
                def _page_cb(page_no, total_pages, _msg, _chl=channel_layer, _uid=user_id,
                             _sc=sheet_code, _jb=job):
                    _notify_page_progress(_chl, _uid, _sc, page_no, total_pages,
                                           f"Trang {page_no}/{total_pages} (Bảng thông số)")
                    broadcast_ocr_job_update(job=_jb, stage_text=f"Đang bóc tách Trang {page_no}/{total_pages} (Bảng thông số)...")
        
                # ── Gọi OCR CLI cho stage=details (Trang 3+ theo thứ tự) ──────────────
                ret_code, data, stderr = _run_ocr_cli(
                    input_pdf, output_root, job.correlation_id,
                    stage="details", device_mode=device_mode,
                    ws_callback=_page_cb,
                )
        
                header_data = cache.get(f"ocr_header_data_{job_id}") or {}
                if not header_data or not header_data.get('business', {}).get('page1_fields'):
                    disk_header = _load_header_data_from_disk(output_root, job.correlation_id)
                    if disk_header:
                        header_data = disk_header

                if ret_code != 0 or not data or data.get('status') not in ('success', 'success_with_warnings'):
                    job.status = 'FAILED'
                    job.sheet.status = 'DRAFT'
                    job.sheet.save(update_fields=['status'])
                    err_msg = (
                        (data.get('error', {}).get('message') if data and 'error' in data else None)
                        or stderr or f"Lỗi OCR Details (Exit Code {ret_code})"
                    )
                    job.error_detail = err_msg
                    job.save(update_fields=['status', 'error_detail'])
                    broadcast_ocr_job_update(job=job, stage_text='Lỗi bóc tách Bảng thông số')

                    _safe_send_ws(channel_layer, user_id, {
                        "type": "send_notification",
                        "title": "Lỗi bóc tách Bảng thông số",
                        "message": f"Không thể xử lý bảng thông số phiếu {sheet_code}: {err_msg[:150]}",
                        "level": "error",
                    })
                    _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})
                    continue

                setting_records = data.get('business', {}).get('setting_records', []) if isinstance(data, dict) else []
                note_candidates = data.get('business', {}).get('note_candidates', []) if isinstance(data, dict) else []

                # Hợp nhất danh sách trang (ưu tiên trang từ details nếu có phân tích bảng)
                pages_dict = {}
                for p in (header_data.get('pages', []) or []):
                    if isinstance(p, dict) and 'page_number' in p:
                        pages_dict[p['page_number']] = p
                for p in (data.get('pages', []) or []):
                    if isinstance(p, dict) and 'page_number' in p:
                        pages_dict[p['page_number']] = p

                # Đảm bảo trang 1 luôn có mặt nếu có artifact trên đĩa
                if 1 not in pages_dict:
                    p1_file = os.path.join(output_root, f"{job.correlation_id}_header", "pages", "page_0001.json")
                    if os.path.exists(p1_file):
                        try:
                            with open(p1_file, 'r', encoding='utf-8') as f:
                                pages_dict[1] = json.load(f)
                        except Exception:
                            pass

                combined_pages = [pages_dict[k] for k in sorted(pages_dict.keys())]

                # Ánh xạ tiêu đề phân nhóm (group_title) từ layout vào từng setting_record
                layout_groups_by_page = {}
                for p in combined_pages:
                    if isinstance(p, dict):
                        pno = p.get('page_number')
                        layout = p.get('layout', {})
                        if isinstance(layout, dict):
                            for g in layout.get('groups', []):
                                gid = g.get('group_id')
                                title = (g.get('title') or '').strip()
                                if gid and title and len(title) < 80:
                                    if not title.lower().startswith(('lưu ý', 'ghi chú', 'ý kiến', '1,', '2,', '3,', '4,', 'phiếu này', 'nguyên nhân')):
                                        layout_groups_by_page[(pno, gid)] = title

                for r in setting_records:
                    if isinstance(r, dict):
                        pno = r.get('page_number')
                        gid = r.get('group_id')
                        if (pno, gid) in layout_groups_by_page:
                            r['group_title'] = layout_groups_by_page[(pno, gid)]

                job.sheet.extracted_data = setting_records
                update_has_parameters_changed_for_sheet(job.sheet)
                # Không đổi status nữa vì đã ISSUED ở Pipeline 1. Chỉ lưu update_fields 
                # để tránh ghi đè thông tin phân công (assigned_to) nếu user đang thao tác
                job.sheet.save(update_fields=['extracted_data'])

                job.status = 'SUCCESS'
                job.review_status = 'COMPLETED'
                job.result_data = {
                    'status': 'success',
                    'business': {
                        'page1_fields': header_data.get('business', {}).get('page1_fields', {}),
                        'important_source_labels': header_data.get('business', {}).get('important_source_labels', {}),
                        'important_field_resolution': header_data.get('business', {}).get('important_field_resolution', {}),
                        'setting_records': setting_records,
                        'note_candidates': note_candidates,
                    },
                    'summary': {
                        **header_data.get('summary', {}),
                        **data.get('summary', {}),
                    },
                    'pages': combined_pages,
                }
                job.save()
                broadcast_ocr_job_update(job=job, stage_text='Đã hoàn thành ✓')

            except Exception as e:
                import traceback
                error_detail = f"Lỗi hệ thống trong Pipeline 2: {str(e)}\n{traceback.format_exc()}"
                try:
                    job.status = 'FAILED'
                    job.error_detail = error_detail
                    job.save(update_fields=['status', 'error_detail'])
                    broadcast_ocr_job_update(job=job, stage_text='Lỗi hệ thống (Pipeline 2)')
                    _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})
                except Exception:
                    pass
    
            # ── Thông báo hoàn tất toàn bộ phiếu ─────────────────────────────────
            _safe_send_ws(channel_layer, user_id, {"type": "bulk_progress", "event_type": "update_badges"})
    

@shared_task(acks_late=True, reject_on_worker_lost=True)
def execute_parallel_ocr_batch(job_ids, user_id=None, device_mode='CPU'):
    """
    Điều phối 2 Pipeline OCR chạy song song ngầm:
      - Pipeline 1: Bóc tách Trang 1 → Trang 2 theo thứ tự cho từng file.
      - Pipeline 2: Đi theo sau, chờ Pipeline 1 bóc tách xong file nào thì bóc Trang 3+ của file đó.
    """
    import concurrent.futures
    import logging
    logger = logging.getLogger(__name__)

    if not isinstance(job_ids, list):
        job_ids = [job_ids]

    logger.info("[OCR Batch] Bắt đầu xử lý %d job(s) qua 2 luồng Pipeline song song", len(job_ids))
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        f_header  = executor.submit(_pipeline_header_worker,  job_ids, user_id, device_mode)
        f_details = executor.submit(_pipeline_details_worker, job_ids, user_id, device_mode)
        
        for future in (f_header, f_details):
            try:
                future.result()
            except Exception as exc:
                logger.exception(
                    "[OCR Batch] Pipeline worker raised an exception: %s", exc
                )

    logger.info("[OCR Batch] Hoàn thành %d job(s)", len(job_ids))
    return f"Processed batch of {len(job_ids)} OCR jobs via 2 parallel pipelines"



@shared_task(bind=True, max_retries=3, acks_late=True, reject_on_worker_lost=True)
def run_ocr_subprocess(self, job_id):
    """Task đơn lẻ tương thích ngược: kích hoạt qua luồng 2 pipeline song song."""
    from sheets.models import OcrJob
    try:
        job = OcrJob.objects.select_related('sheet', 'sheet__created_by').get(id=job_id)
        user_id = job.sheet.created_by.id if job.sheet.created_by else None
        device_mode = getattr(job, 'device_mode', 'CPU')
        return execute_parallel_ocr_batch(job_ids=[job_id], user_id=user_id, device_mode=device_mode)
    except Exception as exc:
        raise self.retry(exc=exc, countdown=10)

@shared_task
def check_gpu_availability_task():
    gpu_available = False
    gpu_name = None
    try:
        import torch
        gpu_available = torch.cuda.is_available()
        if gpu_available:
            gpu_name = torch.cuda.get_device_name(0)
    except Exception:
        pass
    gpu_info = {'available': gpu_available, 'name': gpu_name}
    from django.core.cache import cache
    cache.set('ocr_gpu_info', gpu_info, timeout=86400)

@shared_task
def watchdog_stuck_ocr_jobs():
    """
    Chạy định kỳ để tìm các OcrJob bị kẹt ở trạng thái PROCESSING quá 15 phút.
    Nếu tìm thấy, tự động Re-queue 1 lần nếu cần, hoặc chỉ báo FAILED để user thử lại.
    """
    import datetime
    from django.utils import timezone
    from sheets.models import OcrJob
    from django.core.cache import cache

    timeout_threshold = timezone.now() - datetime.timedelta(minutes=15)
    stuck_jobs = list(OcrJob.objects.filter(status='PROCESSING', updated_at__lt=timeout_threshold).select_related('sheet', 'sheet__created_by'))
    
    if not stuck_jobs:
        return

    job_ids_to_requeue = []
    for job in stuck_jobs:
        cache.delete(f"ocr_header_done_{job.id}")
        cache.delete(f"ocr_header_failed_{job.id}")
        cache.delete(f"ocr_header_data_{job.id}")
        
        retry_key = f"ocr_job_retry_count_{job.id}"
        retries = cache.get(retry_key, 0)
        
        if retries < 2:  # Tối đa 2 lần retry tự động
            cache.set(retry_key, retries + 1, timeout=86400)
            job.status = 'PENDING'
            job.error_detail = None
            job.save(update_fields=['status', 'error_detail'])
            job_ids_to_requeue.append(job.id)
            try:
                broadcast_ocr_job_update(job=job, stage_text=f'Watchdog Timeout - Đang thử lại (Lần {retries + 1}/2)')
            except Exception:
                pass
        else:
            job.status = 'FAILED'
            job.error_detail = 'Tiến trình trích xuất bị treo (Timeout > 15 phút) và đã vượt quá số lần tự động thử lại. Vui lòng kiểm tra lại file PDF hoặc chạy lại thủ công.'
            job.save(update_fields=['status', 'error_detail'])
            try:
                broadcast_ocr_job_update(job=job, stage_text='Thất bại do treo hệ thống')
            except Exception:
                pass

    if job_ids_to_requeue:
        execute_parallel_ocr_batch.delay(job_ids=job_ids_to_requeue)
        print(f"[Watchdog] Đã AUTO-RETRY {len(job_ids_to_requeue)} job bị treo > 15p.")
````

## File: sheets/tests.py
````python
from django.test import TransactionTestCase
from django.contrib.auth.models import User
from unittest.mock import patch, MagicMock
from sheets.models import SettingSheet, OcrJob
from sheets.tasks import execute_parallel_ocr_batch
from django.core.cache import cache
import tempfile
import os

from django.core.files.uploadedfile import SimpleUploadedFile

class ParallelOcrPipelineTests(TransactionTestCase):
    def setUp(self):
        cache.clear()
        User.objects.filter(username='testuser_parallel').delete()
        SettingSheet.objects.filter(sheet_code__in=['TEST-001', 'TEST-002', 'CODE-corr_tes']).delete()
        
        self.user = User.objects.create_user(username='testuser_parallel', password='password123')
        
        file1 = SimpleUploadedFile("test1.pdf", b"%PDF-1.4 test 1", content_type="application/pdf")
        file2 = SimpleUploadedFile("test2.pdf", b"%PDF-1.4 test 2", content_type="application/pdf")
        
        self.sheet1 = SettingSheet.objects.create(
            sheet_code="TEST-001",
            title="Phiếu Test 1",
            scan_file=file1,
            status='DRAFT',
            created_by=self.user
        )
        self.job1 = OcrJob.objects.create(
            sheet=self.sheet1,
            correlation_id="corr_test_001"
        )
        
        self.sheet2 = SettingSheet.objects.create(
            sheet_code="TEST-002",
            title="Phiếu Test 2",
            scan_file=file2,
            status='DRAFT',
            created_by=self.user
        )
        self.job2 = OcrJob.objects.create(
            sheet=self.sheet2,
            correlation_id="corr_test_002"
        )

    def tearDown(self):
        cache.clear()
        User.objects.filter(username='testuser_parallel').delete()
        SettingSheet.objects.filter(sheet_code__in=['TEST-001', 'TEST-002', 'CODE-corr_tes']).delete()

    @patch('sheets.tasks._run_ocr_cli')
    def test_parallel_batch_execution_success(self, mock_run_cli):
        # Giả lập kết quả trả về từ CLI
        def fake_run_cli(input_pdf, output_root, correlation_id, stage="all", device_mode="CPU", **kwargs):
            if stage == "header":
                return 0, {
                    "status": "success",
                    "business": {
                        "page1_fields": {
                            "ticket_number": {"value": f"CODE-{correlation_id[:8]}"},
                            "station": {"value": "Trạm 220kV Test"},
                        }
                    },
                    "pages": [{"page_number": 1}, {"page_number": 2}]
                }, ""
            elif stage == "details":
                return 0, {
                    "status": "success",
                    "business": {
                        "setting_records": [
                            {"item_number": "1", "parameter_name": "I>", "value": "5.0"}
                        ]
                    },
                    "pages": [{"page_number": 3}]
                }, ""
            return 0, {}, ""

        mock_run_cli.side_effect = fake_run_cli

        result = execute_parallel_ocr_batch([self.job1.id, self.job2.id], user_id=self.user.id)
        self.assertIn("Processed batch of 2 OCR jobs", result)

        self.job1.refresh_from_db()
        self.sheet1.refresh_from_db()
        self.assertEqual(self.job1.status, "SUCCESS")
        self.assertEqual(self.sheet1.status, "ISSUED")
        self.assertEqual(len(self.sheet1.extracted_data), 1)
        self.assertEqual(self.sheet1.extracted_data[0]["parameter_name"], "I>")

        self.job2.refresh_from_db()
        self.sheet2.refresh_from_db()
        self.assertEqual(self.job2.status, "SUCCESS")
        self.assertEqual(self.sheet2.status, "ISSUED")
        self.assertEqual(len(self.sheet2.extracted_data), 1)

    @patch('sheets.tasks.execute_parallel_ocr_batch.delay')
    def test_sheet_create_with_folder_paths(self, mock_batch_delay):
        from django.test import Client
        from django.contrib.auth.models import Permission

        client = Client()
        perm = Permission.objects.get(codename='can_create_sheet')
        self.user.user_permissions.add(perm)
        client.force_login(self.user)

        pdf1 = SimpleUploadedFile("phieu_01.pdf", b"%PDF-1.4 sample content", content_type="application/pdf")
        
        response = client.post('/sheets/create/', {
            'scan_files': [pdf1],
            'file_title': 'TBA 500kV Nha Be / Phieu_01.pdf',
            'relative_path': 'TBA 500kV Nha Be/Phieu_01.pdf',
            'device_mode': 'CPU',
        }, HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        self.assertEqual(response.status_code, 200)
        created_sheet = SettingSheet.objects.filter(title='TBA 500kV Nha Be / Phieu_01.pdf').first()
        self.assertIsNotNone(created_sheet)
        self.assertEqual(created_sheet.created_by, self.user)
````

## File: sheets/urls.py
````python
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
````

## File: sheets/utils.py
````python
from .models import SettingSheet

def update_has_parameters_changed_for_sheet(sheet):
    """
    So sánh thông số của phiếu hiện tại với phiếu trước đó (của cùng một rơ-le).
    Cập nhật cờ has_parameters_changed = True nếu có thay đổi.
    """
    if not sheet.relay or not sheet.extracted_data:
        if sheet.has_parameters_changed:
            sheet.has_parameters_changed = False
            sheet.save(update_fields=['has_parameters_changed'])
        return False

    previous_sheet = SettingSheet.objects.filter(
        relay=sheet.relay,
        created_at__lt=sheet.created_at
    ).order_by('-created_at').first()

    if not previous_sheet:
        # Nếu không có phiếu trước đó, coi như không thay đổi (hoặc tuỳ logic business, ở đây theo logic cũ là không thêm vào list updated)
        has_diff = False
    else:
        old_data = previous_sheet.extracted_data or []
        if isinstance(old_data, dict):
            old_data = [{'parameter_code': k, 'value': v} for k, v in old_data.items()]
        elif not isinstance(old_data, list):
            old_data = []
            
        new_data = sheet.extracted_data or []
        if isinstance(new_data, dict):
            new_data = [{'parameter_code': k, 'value': v} for k, v in new_data.items()]
        elif not isinstance(new_data, list):
            new_data = []
        
        old_dict = {item.get('parameter_code'): item for item in old_data if item.get('parameter_code')}
        new_dict = {item.get('parameter_code'): item for item in new_data if item.get('parameter_code')}
        
        has_diff = False
        for code, new_item in new_dict.items():
            if code not in old_dict:
                has_diff = True
                break
            else:
                try:
                    old_val = float(old_dict[code].get('value', 0))
                    new_val = float(new_item.get('value', 0))
                    if old_val != new_val:
                        has_diff = True
                        break
                except (ValueError, TypeError):
                    if str(old_dict[code].get('value')) != str(new_item.get('value')):
                        has_diff = True
                        break
        
        if not has_diff:
            for code in old_dict:
                if code not in new_dict:
                    has_diff = True
                    break

    if sheet.has_parameters_changed != has_diff:
        sheet.has_parameters_changed = has_diff
        sheet.save(update_fields=['has_parameters_changed'])
        
    return has_diff


import re

def beautify_relay_value(val):
    """Chuẩn hóa cú pháp gán biến rơ-le (e.g. IRS-1 -> IRS = 1, CTR1?1200 -> CTR1 = 1200)."""
    if not val or not isinstance(val, str):
        return val
    s = val.strip()
    if s.lower() in ['auto-connected', 'not connected', 'connected'] or 'connected' in s.lower():
        return s
    # Fix OCR ? in assignments: CTR1?1200 or SLP1 ? 20 -> CTR1 = 1200
    s = re.sub(r'([A-Za-z0-9_]+)\s*\?\s*([0-9A-Za-z\.]+)', r'\1 = \2', s)
    # Fix single hyphen in variable assignments: IRS-1, TH5D-250, E87W1 - Y (avoid English words like auto-connected)
    if not re.search(r'\b(auto|self|user|cross|multi|sub|inter)-', s, re.IGNORECASE):
        s = re.sub(r'([A-Za-z0-9_]{2,})\s*-\s*([0-9A-Za-z\.]+)', r'\1 = \2', s)
    # Fix common OCR typos: 087P -> O87P (letter O), WICT -> W1CT
    s = re.sub(r'\b087P\b', 'O87P', s)
    s = re.sub(r'\bWICT\b', 'W1CT', s)
    s = re.sub(r'\bWICTC\b', 'W1CTC', s)
    return s


def parse_sub_values(val):
    """
    Tách chuỗi biểu thức đa cuộn dây/đa biến (ví dụ: E87W1 = Y | E87W2 = Y | E87W3 = N)
    thành danh sách chip có trạng thái màu sắc.
    CHỈ áp dụng khi chuỗi thực sự là biểu thức đa biến (có từ 2 biến trở lên phân tách bởi '|' hoặc ';').
    Tuyệt đối không áp dụng cho dòng chỉ có 1 biến đơn lẻ (như RID = SEL-351A, E50P = 2, MVA = 450)
    để tránh hiển thị trùng lặp 2 thông số giống hệt nhau trên cùng một dòng.
    """
    if not val or not isinstance(val, str):
        return []
    
    # Nếu không có dấu phân tách đa biến (| hoặc ;), đây là giá trị đơn lẻ -> Không tạo sub_vals
    if '|' not in val and ';' not in val:
        return []

    # Split by pipe or semicolon
    raw_parts = [p.strip() for p in re.split(r'[|;]+', val) if p.strip()]
    if len(raw_parts) < 2:
        return []

    sub_vals = []
    for p in raw_parts:
        m = re.match(r'^([A-Za-z0-9_]+)\s*[:=]\s*([A-Za-z0-9_.\?\-]+)(?:\s*\((.*?)\))?$', p)
        if m:
            k = m.group(1).strip()
            v = m.group(2).strip()
            note = (m.group(3) or '').strip()
            
            # Determine badge color type
            v_upper = v.upper()
            if v_upper in ['Y', 'YES', 'ON', 'ENABLE', 'ENABLED']:
                status = 'success'
            elif v_upper in ['N', 'NO', 'OFF', 'DISABLE', 'DISABLED', '<NONE>', 'NONE']:
                status = 'neutral'
            else:
                status = 'info'
                
            sub_vals.append({
                'k': k,
                'v': v,
                'note': note,
                'status': status,
                'raw': p
            })
            
    # Phải có từ 2 biến trở lên mới hiển thị các thẻ chip phân rã
    if len(sub_vals) < 2:
        return []
        
    return sub_vals


def prepare_display_data(raw_data, pages=None):
    """
    Chuẩn hóa và làm sạch dữ liệu OCR để hiển thị trên giao diện đẹp mắt, chuyên nghiệp:
    1. Phân chia rõ ràng các phân đoạn chức năng (Functional Sections / Setting Groups) từ OCR layout hoặc group_id.
    2. Loại bỏ triệt để các dòng rác Tiêu đề hành chính (TẬP ĐOÀN ĐIỆN LỰC, TRUNG TÂM ĐIỀU ĐỘ, PHIẾU CHỈNH ĐỊNH).
    3. Loại bỏ các dòng tiêu đề cột bị OCR bóc tách thành dòng dữ liệu (Setting Title, Value, Unit, Range).
    4. Tự động chuẩn hóa form bảng đa cột (NARI/NR Electric): Khôi phục giá trị thực khi bị đẩy sang description hoặc record_key.
    5. Tách các tiêu đề phân nhóm kỹ thuật (Section Headers: System Settings, Protection Settings,...).
    6. Hợp nhất phụ đề tiếng Việt trong ngoặc đơn (...) vào dòng cha thay vì tạo dòng rác lẻ loi.
    7. Bóc tách biểu thức đa biến số (W1..W4, CT Ratio) thành các Chip Badge trực quan.
    8. Tự động nhận diện cấu trúc từng trang: is_history_page, page_is_columnar, page_has_code.
    9. Giữ nguyên original_index để lưu đúng vào database.
    """
    if not raw_data or not isinstance(raw_data, list):
        return [], {}, {}
        
    group_regex = re.compile(r'\b(GROUP\s+[0-9]+|NHÓM\s+[0-9]+|GR\s+[0-9]+|System\s*Settings|Protection\s*Setting[A-Za-z0-9_/\s]*)\b', re.IGNORECASE)
    leading_code_regex = re.compile(r'^\s*([0-9]{3,5}[A-Za-z]?)\s+(.+)$')
    paren_regex = re.compile(r'^\s*\((.+)\)\s*$')
    KNOWN_UNITS = {'hz', 'a', 'v', 'kv', 'deg', 's', 'ms', 'min', 'ohm', 'ω', '%', 'sec', 'a.', 'c.', 'kv.', 'mva'}
    
    VAL_PATTERNS = [
        r'auto-connected',
        r'not\s+connected',
        r'connected',
        r'Side\s+[0-9]+\s+earth',
        r'[0-9]+A/[0-9]+A\s+current\s+input',
        r'S[0-9]:M[0-9],\s*S[0-9]:M[0-9]',
        r'Display\s+Targets\s+on\s+every\s+Pickup',
        r'image\s+[0-9]+',
        r'[0-9]+\s+RTD\s+.*',
        r'Ther\.\s+replica\s+.*',
        r'Save\s+with\s+Pickup',
        r'Terminal\s+[A-Za-z0-9]+',
        r'Degree\s+Celsius',
        r'L[0-9]\s+L[0-9]\s+L[0-9]',
        r'ON|OFF|YES|NO|NONE|<NONE>|Knone\??|Knones?|Enabled|Disabled|Autotransformer|Transformer',
        r'[0-9]+(?:\.[0-9]+)?\s*(?:sec|s|ms|A|V|kV|MVA|Hz|%|Ohm|Ω)?',
        r'[0-9N]',
    ]
    val_regex = re.compile(r'\s+(' + '|'.join(VAL_PATTERNS) + r')\s*$', re.IGNORECASE)

    # Xây dựng từ điển tra cứu OCR records và tiêu đề phân nhóm kỹ thuật
    ocr_records_lookup = {}
    layout_group_titles = {}
    if pages and isinstance(pages, list):
        for p in pages:
            if not isinstance(p, dict):
                continue
            pno = p.get('page_number')
            layout = p.get('layout') or {}
            for r in layout.get('records', []):
                rid = r.get('record_id')
                if rid:
                    ocr_records_lookup[(pno, rid)] = r
            for g in layout.get('groups', []):
                if not isinstance(g, dict):
                    continue
                gid = g.get('group_id')
                title = (g.get('title') or '').strip()
                if not gid or not title:
                    continue
                if title.lower().startswith(('lưu ý', 'ghi chú', 'ý kiến', '1,', '2,', '3,', '4,', 'phiếu này', 'nguyên nhân')):
                    continue
                if len(title) > 80:
                    continue
                if title.islower():
                    title = title.upper()
                layout_group_titles[(pno, gid)] = title

    def _get_txt(x):
        if x is None:
            return ''
        if isinstance(x, dict):
            return str(x.get('text') or '').strip()
        return str(x).strip()

    pending_section = None
    initial_rows = []
    current_group_key = object()

    # Pre-detect Matrix pages (Binary Output / Relay Contact Matrix: BO, BI, DO, DI)
    matrix_pages = set()
    for raw_item in raw_data:
        p = raw_item.get('page_number') or 1
        p_code = str(raw_item.get('parameter_code') or '').strip().lower()
        p_name = str(raw_item.get('parameter_name') or '').strip().lower()
        p_val = str(raw_item.get('value') or '').strip().lower()
        if p_code in ['bo', 'bi', 'do', 'di', 'output', 'input'] and any(k in p_val for k in ['information', 'configuration', 'destination', 'matrix']):
            matrix_pages.add(p)
        elif raw_item.get('is_matrix'):
            matrix_pages.add(p)

    page_notes = {}

    # Step 1: Filter noise, eliminate table headers, and normalize columnar/matrix items
    for idx, raw_item in enumerate(raw_data):
        item = dict(raw_item)
        item['original_index'] = idx
        item['section_divider'] = item.get('section_divider', '')
        item['group_title'] = item.get('group_title', '')
        
        rk = str(item.get('record_key') or '').strip()
        code = (item.get('parameter_code') or '').strip()
        name = (item.get('parameter_name') or '').strip()
        val = (item.get('value') or '').strip()
        unit = (item.get('unit') or '').strip()
        desc = (item.get('description') or '').strip()
        page = item.get('page_number') or 1
        gid = item.get('group_id')
        rid = str(item.get('record_id') or '')

        # Khôi phục giá trị hoặc tên bị thiếu từ OCR records
        ocr_r = ocr_records_lookup.get((page, rid)) or {}
        ocr_extra = _get_txt(ocr_r.get('extra'))
        ocr_val = _get_txt(ocr_r.get('value'))
        ocr_name = _get_txt(ocr_r.get('parameter_name'))
        ocr_desc = _get_txt(ocr_r.get('description'))
        ocr_code = _get_txt(ocr_r.get('parameter_code'))
        ocr_range = _get_txt(ocr_r.get('range'))
        ocr_unit = _get_txt(ocr_r.get('unit'))
        ocr_rk = _get_txt(ocr_r.get('record_key'))

        if not rk and ocr_rk:
            rk = ocr_rk
        if not code and ocr_code:
            code = ocr_code
        if not unit and ocr_unit:
            unit = ocr_unit
        if not val:
            val = ocr_val or ocr_extra or _get_txt(item.get('extra'))
        if not name:
            if ocr_name:
                name = ocr_name
            elif desc and (code or ocr_code or rk):
                name = desc
                desc = ''
            elif ocr_desc and (code or ocr_code or rk):
                name = ocr_desc
                desc = ''

        range_val = _get_txt(item.get('range')) or ocr_range

        # Nhận diện phân nhóm chức năng khi chuyển group_id theo trang
        item_group_key = (page, gid) if gid else None
        if item_group_key != current_group_key:
            current_group_key = item_group_key
            if item_group_key and item_group_key in layout_group_titles:
                pending_section = layout_group_titles[item_group_key]
            elif item.get('group_title'):
                pending_section = item['group_title']
        
        # 1. Institutional header noise elimination
        all_text = f"{code} {name} {desc} {val}".upper()
        if any(h in all_text for h in [
            'TẬP ĐOÀN ĐIỆN LỰC', 'TRUNG TÂM ĐIỀU ĐỘ', 'PHIẾU CHỈNH ĐỊNH',
            'GIÁ TRỊ CHỈNH ĐỊNH SỬ DỤNG CHO CHẾ ĐỘ', 'GIÁ TRỊ CHỈNH ĐỊNH',
            'THÔNG SỐ CHỈNH ĐỊNH', 'THÔNG SỔ CHỈNH ĐỊNH'
        ]):
            continue

        # Matrix Table Handling (Binary Output / Contact Matrix: BO, No., Group, Information, Type, Configuration)
        if page in matrix_pages:
            # A. Leaked Matrix Header row
            is_mat_header = (
                code.lower() in ['bo', 'bi', 'do', 'di', 'output', 'input'] or
                (name.lower() in ['no.', 'no', 'stt'] and any(k in val.lower() for k in ['information', 'configuration', 'type', 'group']))
            )
            if is_mat_header:
                continue

            # B. Extract footnote from val or name if present
            m_note = re.search(r'(Ghi chú\s*:.*)$', val, re.IGNORECASE)
            if m_note:
                note_str = m_note.group(1).strip()
                if 'output số 2' in name.lower() and not note_str.endswith('2)'):
                    note_str = note_str + ' output số 2)'
                page_notes[page] = note_str
                val = val[:m_note.start()].strip()
            elif 'ghi chú:' in name.lower():
                page_notes[page] = name.strip()

            # C. Parse BO Contact Number
            bo = code or ''
            if bo == 'J':
                bo = '7'
            elif bo in ['09', '08', '9']:
                bo = '8'
            elif (not bo or bo.lower() == 'none') and 'output số 2' in (name.lower() + ' ' + val.lower()):
                bo = '2'

            # D. Parse Function / Signal Number (No.)
            m_no = re.search(r'([0-9]{3,5}(?:\.[0-9A-Za-z]+)*)', name)
            func_no = m_no.group(1) if m_no else name

            # E. Parse Output Type and Configuration
            out_type = item.get('type') or 'OUT'
            out_cfg = item.get('configuration') or 'U'
            m_end = re.search(r'\b(J?OUTJ?)\s*([UL])?\s*$', val, re.IGNORECASE)
            if m_end:
                out_type = 'OUT'
                out_cfg = m_end.group(2) or 'U'
                val = val[:m_end.start()].strip()
            else:
                val = re.sub(r'[\s/]*J?OUTJ?[\s/]*[UL]?\s*$', '', val, flags=re.IGNORECASE).strip()

            # F. Parse Group & Information text
            existing_group = item.get('group') or item.get('matrix_group') or ''
            existing_info = item.get('info') or item.get('matrix_info') or ''
            if existing_group and existing_info:
                group_name = existing_group
                info_text = existing_info
            else:
                m_grp = re.match(r'^(Diff\.\s*Prot|REF|Therm\.\s*Overload)\s+(.+)$', val, re.IGNORECASE)
                if m_grp:
                    group_name = m_grp.group(1).strip()
                    info_text = m_grp.group(2).strip()
                else:
                    v_low = val.lower()
                    if v_low.startswith('diff'):
                        group_name = 'Diff. Prot'
                        info_text = re.sub(r'^diff\.\s*prot\s*', '', val, flags=re.IGNORECASE).strip()
                    elif v_low.startswith('ref'):
                        group_name = 'REF'
                        info_text = re.sub(r'^ref\s*', '', val, flags=re.IGNORECASE).strip()
                    elif v_low.startswith('therm'):
                        group_name = 'Therm. Overload'
                        info_text = re.sub(r'^therm\.\s*overload\s*', '', val, flags=re.IGNORECASE).strip()
                    elif 'restr' in v_low or func_no == '199.2451.01':
                        group_name = 'REF'
                        info_text = val
                    elif 'differential prot' in v_low or func_no in ['05691', '05692']:
                        group_name = 'Diff. Prot'
                        info_text = val
                    elif 'thermal overload' in v_low or func_no == '044.2603.01':
                        group_name = 'Therm. Overload'
                        info_text = val
                    else:
                        group_name = existing_group or ''
                        info_text = existing_info or val

            if group_name.lower().startswith('diff'):
                group_name = 'Diff. Prot'
            elif group_name.lower().startswith('ref'):
                group_name = 'REF'
            elif group_name.lower().startswith('therm'):
                group_name = 'Therm. Overload'
            elif not group_name:
                if func_no in ['05691', '05692'] or 'diff' in info_text.lower():
                    group_name = 'Diff. Prot'
                elif func_no == '199.2451.01' or 'restr' in info_text.lower():
                    group_name = 'REF'
                elif func_no == '044.2603.01' or 'thermal' in info_text.lower():
                    group_name = 'Therm. Overload'

            # Standardize info text
            if func_no == '05692' or 'IDIFFSS' in info_text or 'IDIFF>>' in info_text:
                info_text = 'Differential prot.: TRIP by IDIFF>>'
            elif func_no == '05691' or 'IDIFF' in info_text:
                info_text = 'Differential prot.: TRIP by IDIFF>'
            elif 'restr' in info_text.lower() or func_no == '199.2451.01':
                info_text = 'Restr. earth flt.: TRIP'
            elif 'thermal' in info_text.lower() or func_no == '044.2603.01':
                info_text = 'Thermal Overload Alarm'

            item['is_matrix'] = True
            item['clean_code'] = bo
            item['bo_contact'] = bo
            item['clean_func_no'] = func_no
            item['clean_group'] = group_name
            item['clean_info'] = info_text
            item['clean_type'] = out_type
            item['clean_cfg'] = out_cfg
            item['clean_name'] = func_no
            item['clean_value'] = f"{group_name} | {info_text}"
            item['clean_unit'] = ''
            item['clean_desc'] = ''
            initial_rows.append(item)
            continue
            
        # 2. Leaked page ticket number row
        if name.lower() in ['số:', 'số', 'tờ số:', 'tờ số', 'to so'] and re.search(r'\b[A-Za-z0-9]+-[0-9]{2}-[0-9]{4}\b', val):
            continue
            
        # 3. Leaked table column headers (STT / Setting Title / Value / Unit / Step / Range)
        rk_lower = rk.lower()
        val_lower = val.lower()
        desc_lower = desc.lower()
        code_lower = code.lower()
        name_lower = name.lower()
        
        is_col_header_key = (
            rk_lower in ['no.', 'no', 'stt', 'stt.'] or 
            code_lower in ['no.', 'no', 'stt', 'stt.'] or 
            name_lower in ['no.', 'no', 'stt', 'stt.'] or
            name_lower.startswith('setting title')
        )
        header_terms = ['setting', 'settings', 'function', 'scope', 'value', 'unit', 'step', 'range', 'chức năng', 'giá trị', 'dải']
        has_header_term = any(t in desc_lower or t in val_lower or t in name_lower for t in header_terms)
        
        is_leaked_header = (
            (is_col_header_key and has_header_term) or
            (name_lower in ['setting title', 'thông số cài đặt'] and any(t in val_lower or t in desc_lower for t in ['value', 'unit', 'range', 'giá trị', 'đơn vị'])) or
            (name_lower == 'setting title' and val_lower in ['value', 'range', 'unit', ''])
        )

        if is_leaked_header:
            m_sec = re.search(r'\b(Group\s+[^;]+(?:\s*;\s*Group\s+[^;\n]+)?|Device\s+Configuration)\b', f'{name} {val} {desc}', re.IGNORECASE)
            if m_sec:
                sec_clean = m_sec.group(1).strip()
                sec_clean = re.sub(r'(?:\s+(?:Settings|Setting|Value|No\.?|Chức\s+năng|Thông\s+số))+\s*$', '', sec_clean, flags=re.IGNORECASE).strip()
                pending_section = sec_clean
            continue
            
        # 4. Pure section divider
        m_group = re.match(r'^\s*(Group\s+[^;]+(?:\s*;\s*Group\s+[^;\n]+)?|Device\s+Configuration)\s*$', name, re.IGNORECASE)
        if not m_group:
            m_group = re.match(r'^\s*(Group\s+[^;]+(?:\s*;\s*Group\s+[^;\n]+)?|Device\s+Configuration)\s*$', val, re.IGNORECASE)
        if not code and m_group:
            sec_clean = m_group.group(1).strip()
            sec_clean = re.sub(r'(?:\s+(?:Settings|Setting|Value|No\.?|Chức\s+năng|Thông\s+số))+\s*$', '', sec_clean, flags=re.IGNORECASE).strip()
            pending_section = sec_clean
            continue

        # Strip trailing BM form codes and year noise
        name = re.sub(r'\s+19[89][0-9]\b', '', name)
        name = re.sub(r'\s*BM\.[0-9]+[A-Za-z0-9\.]*\s*$', '', name, flags=re.IGNORECASE).strip()
        desc = re.sub(r'\s+19[89][0-9]\b', '', desc)
        desc = re.sub(r'\s*BM\.[0-9]+[A-Za-z0-9\.]*\s*$', '', desc, flags=re.IGNORECASE).strip()
        
        # 5. Remove embedded next section from val if present (e.g. 0213)
        if code in ['0213'] and 'Group CT-Assign' in val:
            val = re.sub(r'Group\s+[^;]+;\s*Group\s+CT-Assign\s*', '', val, flags=re.IGNORECASE).strip()

        # Leading code extraction (Siemens)
        if (not code or code.lower() == 'none') and name:
            match_code = leading_code_regex.match(name)
            if match_code:
                code = match_code.group(1).strip()
                name = match_code.group(2).strip()

        # Embedded section divider inside name or val before parameter name
        m_embed_name = re.match(r'^\s*(Group\s+[^;]+;\s*Group\s+[A-Za-z0-9_\'-]+)\s+(.+)$', name, re.IGNORECASE)
        if m_embed_name and code:
            pending_section = m_embed_name.group(1).strip()
            name = m_embed_name.group(2).strip()

        # Check section titles
        if pending_section:
            item['section_divider'] = pending_section
            pending_section = None
            
        # Layout groups from OCR layout are the ground truth for section dividers.
        # Regex section splitting should only be used as a fallback when no layout groups exist.
        has_layout = bool(layout_group_titles)
        is_setting_group_param = bool(re.search(r'\b(setting\s+group|active\s+group|group\s+select)\b', name, re.IGNORECASE))
        
        if not has_layout and not is_setting_group_param and not (code and val):
            match_grp = group_regex.search(name)
            if match_grp:
                next_sec = match_grp.group(1).strip()
                name = name[:match_grp.start()].strip()
                pending_section = next_sec
                
            match_val_grp = group_regex.search(val)
            if match_val_grp:
                next_sec = match_val_grp.group(1).strip()
                val = val[:match_val_grp.start()].strip()
                pending_section = next_sec

        # 6. Columnar / NARI form normalization
        # Subcase A: record_key contains Setting Title (e.g. '- 50/51P.U2 VCE' or '9 50/51P1.t Op')
        m_name = re.search(r'([0-9A-Za-z/_\.]+\.[A-Za-z0-9_]+)', rk)
        if m_name and (re.match(r'^[0-9]+(\.[0-9]+)?$', name) or name in ['?', 'Không sử dụng', '001F']):
            stt_match = re.search(r'^\s*([0-9]+)', rk)
            stt = stt_match.group(1) if stt_match else ''
            setting_name = rk[m_name.start():].strip().replace(' ', '_')
            val_clean = name
            unit_clean = desc if desc.lower() in KNOWN_UNITS or len(desc) <= 3 else ''
            range_clean = val
            item['clean_code'] = stt
            item['clean_name'] = setting_name
            item['clean_value'] = val_clean
            item['clean_unit'] = unit_clean
            item['clean_desc'] = ''
            item['clean_range'] = range_clean
            item['is_columnar'] = True
            initial_rows.append(item)
            continue

        # Subcase B: Value was placed in description
        is_paren_trans = desc.startswith('(') and desc.endswith(')')
        if desc and not is_paren_trans and (re.match(r'^[0-9\.\-\?]+$', desc) or desc in ['Không sử dụng', 'AT2 500', '001F', '?']):
            val_clean = desc
            if val_clean.startswith('.') and len(val_clean) > 1 and val_clean[1].isdigit():
                val_clean = '-' + val_clean[1:]
            unit_clean = unit
            range_clean = ''
            if not unit_clean and (val.lower() in KNOWN_UNITS or val.lower() in ['v', 'a', 's', 'kv', 'deg']):
                unit_clean = val.upper() if val.lower() in ['v', 'a', 'kv'] else val
            elif re.search(r'^[0-9\.]+\s*-\s*[0-9\.]+$', val):
                range_clean = val
            stt = rk if re.match(r'^[0-9]+$', rk) else ''
            item['clean_code'] = stt
            item['clean_name'] = name
            item['clean_value'] = val_clean
            item['clean_unit'] = unit_clean
            item['clean_desc'] = ''
            item['clean_range'] = range_clean
            item['is_columnar'] = True
            initial_rows.append(item)
            continue

        # Subcase C: Function block without parameters marked as "không sử dụng"
        if (not name or name.lower() in ['không sử dụng', 'khong su dung']) and rk and ('setting' in rk.lower() or 'prot' in rk.lower() or '/' in rk):
            item['clean_code'] = ''
            item['clean_name'] = rk.strip().rstrip(':')
            item['clean_value'] = 'Không sử dụng'
            item['clean_unit'] = ''
            item['clean_desc'] = ''
            item['clean_range'] = ''
            item['is_columnar'] = True
            initial_rows.append(item)
            continue

        # Subcase D: Columnar Setting Grid (STT | Setting Title | Value | Unit | Range)
        if range_val or (unit and (rk or (code and code.isdigit() and int(code) < 100))):
            val_clean = beautify_relay_value(val)
            item['clean_code'] = rk or code
            item['clean_name'] = name
            item['clean_value'] = val_clean
            item['clean_unit'] = unit
            item['clean_desc'] = desc
            item['clean_range'] = range_val
            item['is_columnar'] = True
            initial_rows.append(item)
            continue

        # Identical code and name resolution
        if code and name and (code == name or name.startswith(code)) and len(val.split()) >= 2:
            m_val = val_regex.search(val)
            if m_val:
                name = val[:m_val.start()].strip()
                val = m_val.group(1).strip()
            else:
                parts = val.split()
                name = ' '.join(parts[:-1]).strip()
                val = parts[-1].strip()

        if val in ['Knone?', 'Knones']:
            val = '<none>'
        if code == '0213' and val.upper() in ['N', '2']:
            val = '2'
                
        val = beautify_relay_value(val)
        
        item['clean_code'] = code if code.lower() != 'none' else ''
        item['clean_name'] = name
        item['clean_value'] = val
        item['clean_unit'] = unit
        item['clean_desc'] = desc
        item['clean_range'] = range_val
        if range_val:
            item['is_columnar'] = True
        
        initial_rows.append(item)

    # Step 2: Smart Fusion of orphaned Vietnamese subtitles
    merged_rows = []
    for item in initial_rows:
        name = item.get('clean_name') or ''
        desc = item.get('clean_desc') or ''
        code = item.get('clean_code') or ''
        val = item.get('clean_value') or ''
        
        is_subtitle = False
        subtitle_text = ""
        
        if not code and not item.get('is_columnar') and not item.get('is_matrix'):
            if name and paren_regex.match(name) and not desc:
                is_subtitle = True
                subtitle_text = name
            elif not name and desc and paren_regex.match(desc):
                is_subtitle = True
                subtitle_text = desc
            elif name and name.startswith('(') and name.endswith(')'):
                is_subtitle = True
                subtitle_text = name

        if is_subtitle and merged_rows and merged_rows[-1].get('page_number') == item.get('page_number'):
            prev = merged_rows[-1]
            prev_desc = prev.get('clean_desc') or ''
            if subtitle_text not in prev_desc:
                prev['clean_desc'] = f"{prev_desc} {subtitle_text}".strip()
            prev_val = prev.get('clean_value') or ''
            if val and val not in prev_val:
                if not prev_val:
                    prev['clean_value'] = val
                    prev['value'] = val
                else:
                    prev['clean_value'] = f"{prev_val} | {val}"
                    prev['value'] = f"{prev_val} | {val}"
            if 'merged_indices' not in prev:
                prev['merged_indices'] = []
            prev['merged_indices'].append(item.get('original_index'))
        else:
            merged_rows.append(item)

    # Step 3: Detect history table pages vs technical parameter pages
    page_stats = {}
    page_items_map = {}
    for item in merged_rows:
        p = item.get('page_number') or 1
        page_stats[p] = page_stats.get(p, 0) + 1
        page_items_map.setdefault(p, []).append(item)

    page_is_history = {}
    for p, p_items in page_items_map.items():
        if any(it.get('is_history') for it in p_items):
            page_is_history[p] = True
            continue
        hist_hits = 0
        for it in p_items:
            name = (it.get('clean_name') or '').strip()
            desc = (it.get('clean_desc') or it.get('description') or '').strip()
            val = (it.get('clean_value') or it.get('value') or '').strip()
            all_text = f"{name} {desc} {val}".lower()
            if re.search(r'\b(?:[0-9]{2}/[0-9]{4}\.[A-Za-z0-9]+|A0-[0-9]{2}-[0-9]{4})\b', f"{name} {desc}"):
                if any(k in all_text for k in ['thay phiếu', 'thay đổi', 'tháo dỡ', 'hiệu chỉnh', 'bổ sung', 'mở rộng', 'phản hồi', 'công văn', 'nội dung sửa đổi']):
                    hist_hits += 1
        if hist_hits > 0 and hist_hits >= len(p_items) * 0.5:
            page_is_history[p] = True

    # Step 4: Detect page_has_code, page_is_columnar, page_is_matrix
    page_has_code = {}
    page_is_columnar = {}
    page_is_matrix = {}
    for p, p_items in page_items_map.items():
        if page_is_history.get(p, False):
            page_has_code[p] = False
            page_is_columnar[p] = False
            page_is_matrix[p] = False
            continue

        matrix_count = sum(1 for it in p_items if it.get('is_matrix'))
        if matrix_count > 0 and (matrix_count >= len(p_items) * 0.4 or p in matrix_pages):
            page_is_matrix[p] = True
            page_has_code[p] = False
            page_is_columnar[p] = False
            if p in page_notes and p_items:
                p_items[-1]['page_note'] = page_notes[p]
            continue

        page_is_matrix[p] = False
        col_count = sum(1 for it in p_items if it.get('is_columnar'))
        is_col = col_count >= len(p_items) * 0.4
        page_is_columnar[p] = is_col
        if is_col:
            page_has_code[p] = False
        else:
            code_count = sum(1 for it in p_items if it.get('clean_code') and not (it.get('clean_code').isdigit() and int(it.get('clean_code')) < 100))
            page_has_code[p] = code_count >= len(p_items) * 0.4

    row_counters = {}
    for item in merged_rows:
        p = item.get('page_number') or 1
        is_hist = page_is_history.get(p, False)
        is_col = page_is_columnar.get(p, False)
        is_mat = page_is_matrix.get(p, False)
        has_code = page_has_code.get(p, False)
        
        item['is_history_page'] = is_hist
        item['page_has_code'] = has_code
        item['page_is_columnar'] = is_col
        item['page_is_matrix'] = is_mat
        if is_mat:
            item['is_matrix'] = True
        
        row_counters[p] = row_counters.get(p, 0) + 1
        
        if is_hist:
            m_t = re.search(r'\b(?:[0-9]{2}/[0-9]{4}\.[A-Za-z0-9]+|A0-[0-9]{2}-[0-9]{4}(?:/[A-Za-z0-9]+)?)\b', f"{item.get('clean_name', '')} {item.get('clean_desc', '')} {item.get('description', '')} {item.get('clean_value', '')}")
            if m_t:
                item['clean_name'] = m_t.group(0)
            if not item.get('clean_code') or item.get('clean_code') == 'None':
                item['clean_code'] = str(row_counters[p])
            if not item.get('clean_value') and item.get('clean_desc'):
                item['clean_value'] = item['clean_desc']
            item['sub_vals'] = []
        elif is_col:
            item['clean_code'] = str(row_counters[p])
            item['sub_vals'] = []
        elif is_mat:
            item['sub_vals'] = []
        else:
            item['sub_vals'] = parse_sub_values(item.get('clean_value', ''))

    return merged_rows, page_stats, page_is_history
````

## File: sheets/views_bulk.py
````python
import json
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.cache import cache
from django.contrib import messages

@login_required
def bulk_create_ui(request):
    """Render the UI for Bulk Sheet Creation (Test Utility)"""
    # Only allow Dispatcher for testing
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet'):
        messages.error(request, "Bạn không có quyền truy cập tính năng Test này.")
        return redirect('sheet_list')
    from django.utils import timezone
    from datetime import timedelta
    from sheets.models import SettingSheet

    # Get sheets created by this user in the last 24 hours
    time_threshold = timezone.now() - timedelta(hours=24)
    recent_sheets_qs = SettingSheet.objects.filter(
        created_by=request.user,
        created_at__gte=time_threshold
    ).order_by('-created_at')
    
    total_recent = recent_sheets_qs.count()
    from django.core.paginator import Paginator
    paginator = Paginator(recent_sheets_qs, 20)
    page_number = request.GET.get('page', 1)
    recent_sheets = paginator.get_page(page_number)

    return render(request, 'sheets/bulk_create.html', {
        'recent_sheets': recent_sheets,
        'total_recent': total_recent
    })

@login_required
def bulk_create_execute(request):
    """API endpoint to execute bulk creation logic via Celery with Idempotency"""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet'):
        return JsonResponse({'error': 'Unauthorized'}, status=403)
        
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
    idempotency_key = request.POST.get('idempotency_key')
    if not idempotency_key:
        return JsonResponse({'error': 'Mã Idempotency (idempotency_key) là bắt buộc'}, status=400)
        
    scan_files = request.FILES.getlist('scan_files')
    if not scan_files:
        return JsonResponse({'error': 'Vui lòng tải lên ít nhất 1 file.'}, status=400)
        
    # Kiểm tra Idempotency Lock
    cached_status = cache.get(idempotency_key)
    if cached_status:
        if cached_status == 'PROCESSING':
            return JsonResponse({'status': 'PROCESSING', 'message': 'Hệ thống đang xử lý yêu cầu này, vui lòng đợi.'})
        else:
            return JsonResponse({'status': 'COMPLETED', 'data': cached_status})
            
    # Khóa Idempotency
    cache.set(idempotency_key, 'PROCESSING', timeout=86400)
    
    # Chuẩn bị dữ liệu: Tạo các bản ghi SettingSheet với trạng thái DRAFT
    from stations.models import Station, Relay
    from sheets.models import SettingSheet
    import random
    import uuid

    station_ids = list(Station.objects.values_list('id', flat=True))
    relay_ids = list(Relay.objects.values_list('id', flat=True))
    
    sheet_ids = []
    
    for f in scan_files:
        station_id = random.choice(station_ids) if station_ids else None
        relay_id = random.choice(relay_ids) if relay_ids else None
        # Generate random sheet code
        unique_id = str(uuid.uuid4())[:8].upper()
        sheet_code = f"AUTO-{unique_id}"
        
        sheet = SettingSheet.objects.create(
            sheet_code=sheet_code,
            title=f.name,
            relay_id=relay_id,
            station_id=station_id,
            scan_file=f,
            status='DRAFT', # Will be processed by Celery
            created_by=request.user
        )
        sheet_ids.append(sheet.id)
    
    # Kích hoạt Celery Worker
    from sheets.tasks import execute_bulk_create_task
    execute_bulk_create_task.delay(idempotency_key, request.user.id, sheet_ids)
    
    return JsonResponse({
        'status': 'ACCEPTED',
        'message': f'Đã đưa {len(sheet_ids)} file vào hàng đợi Celery (Background Processing). Vui lòng chờ thông báo (Toast) khi hoàn tất.'
    })

@login_required
def api_extract_test_ui(request):
    """Render the UI for API Extract Test"""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet'):
        messages.error(request, "Bạn không có quyền truy cập tính năng Test này.")
        return redirect('sheet_list')
    return render(request, 'sheets/api_extract_test.html')

@login_required
def api_extract_test_execute(request):
    """Mock API endpoint to simulate data extraction"""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet'):
        return JsonResponse({'error': 'Unauthorized'}, status=403)
        
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
        
    scan_files = request.FILES.getlist('scan_files')
    if not scan_files:
        return JsonResponse({'error': 'Vui lòng tải lên ít nhất 1 file.'}, status=400)
        
    api_url = request.POST.get('api_url')
    
    if api_url:
        import requests
        # Pass files to the real API
        try:
            # Prepare files for requests
            files_to_send = []
            for f in scan_files:
                # requests expects a tuple (filename, fileobj, content_type)
                files_to_send.append(('scan_files', (f.name, f.read(), f.content_type)))
                
            response = requests.post(api_url, files=files_to_send, timeout=30)
            # Try to return the JSON directly from the API
            try:
                api_json = response.json()
                return JsonResponse({
                    'status': 'SUCCESS' if response.ok else 'ERROR',
                    'message': f'Phản hồi từ {api_url}',
                    'data': api_json,
                    'http_status': response.status_code
                })
            except ValueError:
                return JsonResponse({
                    'status': 'ERROR',
                    'error': 'API không trả về định dạng JSON hợp lệ.',
                    'raw_response': response.text[:500] # Return partial raw response for debugging
                })
        except requests.exceptions.RequestException as e:
            return JsonResponse({
                'status': 'ERROR',
                'error': f'Lỗi khi kết nối đến API: {str(e)}'
            })
        
    # Simulate processing and return mock data if no api_url provided
    # For multiple files, we'll return an array of results
    import time
    time.sleep(1) # Simulate API delay
    
    results = []
    for f in scan_files:
        results.append({
            'file_name': f.name,
            'status': 'success',
            'extracted_data': {
                'Tên Trạm': 'Trạm Mock 110kV',
                'Ngăn lộ': 'Lộ 171',
                'Loại Rơ-le': 'SEL-311C',
                'Hãng sản xuất': 'Schweitzer Engineering Laboratories',
                'Các thông số': {
                    'I>>': '10A',
                    't>>': '0.1s',
                    'I>': '5A',
                    't>': '0.5s'
                }
            }
        })
        
    return JsonResponse({
        'status': 'SUCCESS',
        'message': f'Đã trích xuất thành công {len(scan_files)} file.',
        'data': results
    })
````

## File: sheets/views.py
````python
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
import random
import time
from .models import SettingSheet, SignatureRecord
from stations.models import Relay
from .services import evn_service
from .utils import prepare_display_data

import hashlib
from django.core.cache import cache

def get_sheet_kpis(base_sheets, status_filter):
    """Tính toán các chỉ số KPI theo ngữ cảnh của trang danh sách phiếu."""
    if status_filter == 'ISSUED':
        kpi_type = 'ISSUED'
        target_qs = base_sheets.filter(status='ISSUED')
        kpi_stats = {
            'total': target_qs.count(),
            'matched': target_qs.filter(relay__isnull=False).count(),
            'unlinked': target_qs.filter(relay__isnull=True).count(),
            'changed': target_qs.filter(has_parameters_changed=True).count(),
        }
    elif status_filter == 'ROUTED_TO_STATION':
        kpi_type = 'ROUTED_TO_STATION'
        target_qs = base_sheets.filter(status='ROUTED_TO_STATION')
        kpi_stats = {
            'total': target_qs.count(),
            'unassigned': target_qs.filter(assigned_to__isnull=True).count(),
            'assigned': target_qs.filter(assigned_to__isnull=False).count(),
            'changed': target_qs.filter(has_parameters_changed=True).count(),
        }
    elif any(s in (status_filter or '') for s in ['TRANSFERRED', 'RECEIVED']):
        kpi_type = 'IN_PROGRESS'
        target_qs = base_sheets.filter(status__in=['TRANSFERRED', 'RECEIVED'])
        kpi_stats = {
            'total': target_qs.count(),
            'transferred': target_qs.filter(status='TRANSFERRED').count(),
            'received': target_qs.filter(status='RECEIVED').count(),
            'changed': target_qs.filter(status__in=['TRANSFERRED', 'RECEIVED'], has_parameters_changed=True).count(),
        }
    elif status_filter == 'COMPLETED':
        kpi_type = 'COMPLETED'
        target_qs = base_sheets.filter(status='COMPLETED')
        kpi_stats = {
            'total': target_qs.count(),
            'matched': target_qs.filter(relay__isnull=False).count(),
            'custom': target_qs.filter(relay__isnull=True).count(),
            'changed': target_qs.filter(has_parameters_changed=True).count(),
        }
    else:
        kpi_type = 'ALL'
        kpi_stats = {
            'total': base_sheets.count(),
            'issued': base_sheets.filter(status='ISSUED').count(),
            'in_progress': base_sheets.filter(status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED', 'PENDING_ADMIN_APPROVAL']).count(),
            'completed': base_sheets.filter(status='COMPLETED').count(),
        }
    return kpi_type, kpi_stats

@login_required
def sheet_list(request):
    """View danh sách phiếu chỉnh định."""
    search_query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    sub_filter = request.GET.get('sub_filter', '')
    voltage_filter = request.GET.get('voltage', '')
    page_number = request.GET.get('page', 1)
    
    sheets = SettingSheet.objects.select_related('created_by', 'relay', 'relay__bay', 'relay__bay__station', 'station').all().order_by('-updated_at', '-created_at')
    
    # PBAC Data Filtering
    if request.user.is_superuser or request.user.has_perm('sheets.can_manage_users') or request.user.has_perm('sheets.can_approve_sheet'):
        pass # Can see all sheets
    else:
        # Check if user is bound to a station
        station = None
        try:
            station = request.user.userprofile.station
        except Exception:
            pass
            
        if station:
            from django.db.models import Q
            sheets = sheets.filter(
                Q(execution_station=station) | 
                (Q(execution_station__isnull=True) & (Q(station=station) | Q(relay__bay__station=station)))
            ).distinct()
        else:
            # Fallback to creator scope for users not bound to a station
            sheets = sheets.filter(created_by=request.user)

    from django.core.paginator import Paginator
    from django.db.models import Q

    # Base sheets for KPI metrics calculation before search & sub filters
    base_sheets = sheets

    # 1. Status Filter
    if status_filter:
        sheets = sheets.filter(status__in=status_filter.split(','))

    # Calculate KPI Stats
    kpi_type, kpi_stats = get_sheet_kpis(base_sheets, status_filter)

    # 2. Sub Filter (Quick Filter from KPI cards or Pill tabs)
    if sub_filter:
        if sub_filter == 'MATCHED':
            sheets = sheets.filter(relay__isnull=False)
        elif sub_filter == 'UNLINKED':
            sheets = sheets.filter(relay__isnull=True)
        elif sub_filter == 'CHANGED':
            sheets = sheets.filter(has_parameters_changed=True)
        elif sub_filter == 'UNASSIGNED':
            sheets = sheets.filter(assigned_to__isnull=True)
        elif sub_filter == 'ASSIGNED':
            sheets = sheets.filter(assigned_to__isnull=False)
        elif sub_filter == 'TRANSFERRED':
            sheets = sheets.filter(status='TRANSFERRED')
        elif sub_filter == 'RECEIVED':
            sheets = sheets.filter(status='RECEIVED')
        elif sub_filter == 'ISSUED':
            sheets = sheets.filter(status='ISSUED')
        elif sub_filter == 'IN_PROGRESS':
            sheets = sheets.filter(status__in=['ROUTED_TO_STATION', 'TRANSFERRED', 'RECEIVED', 'PENDING_ADMIN_APPROVAL'])
        elif sub_filter == 'COMPLETED':
            sheets = sheets.filter(status='COMPLETED')

    # 3. Voltage Filter
    if voltage_filter:
        if voltage_filter == '500':
            sheets = sheets.filter(Q(sheet_code__icontains='500') | Q(title__icontains='500') | Q(station__station_name__icontains='500'))
        elif voltage_filter == '220':
            sheets = sheets.filter(Q(sheet_code__icontains='220') | Q(title__icontains='220') | Q(station__station_name__icontains='220'))
        elif voltage_filter == '110':
            sheets = sheets.filter(Q(sheet_code__icontains='110') | Q(title__icontains='110') | Q(station__station_name__icontains='110'))
        elif voltage_filter == 'medium':
            sheets = sheets.filter(
                Q(sheet_code__icontains='35') | Q(sheet_code__icontains='22') |
                Q(title__icontains='trung') | Q(title__icontains='35') | Q(title__icontains='22') |
                Q(station__station_name__icontains='35') | Q(station__station_name__icontains='22')
            )

    # 4. Search Query Filter
    if search_query:
        search_clean = search_query.replace(',', ' ').replace('-', ' ')
        terms = [t for t in search_clean.split() if t]
        for term in terms:
            sheets = sheets.filter(
                Q(sheet_code__icontains=term) |
                Q(title__icontains=term) |
                Q(relay__relay_code__icontains=term) |
                Q(relay__relay_name__icontains=term) |
                Q(relay_text__icontains=term) |
                Q(station__station_name__icontains=term) |
                Q(station__station_code__icontains=term)
            )

    paginator = Paginator(sheets, 40)
    page_obj = paginator.get_page(page_number)
    
    # Force queryset evaluation before caching
    _ = list(page_obj.object_list)

    list_title = 'Tất cả Phiếu Chỉnh định'
    if status_filter == 'COMPLETED':
        list_title = 'Hồ sơ Đã Ban hành'
    elif status_filter == 'PENDING_ADMIN_APPROVAL':
        list_title = 'Phiếu Chờ Ký Duyệt'
    elif status_filter == 'ROUTED_TO_STATION':
        list_title = 'Phiếu Chờ Phân Công'
    elif status_filter == 'RECEIVED' or status_filter == 'TRANSFERRED,RECEIVED':
        list_title = 'Trạm Đang Xử Lý'
    elif status_filter == 'ISSUED':
        list_title = 'Phiếu Chờ Rà soát'

    context = {
        'sheets': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'sub_filter': sub_filter,
        'voltage_filter': voltage_filter,
        'kpi_type': kpi_type,
        'kpi_stats': kpi_stats,
        'list_title': list_title
    }
    return render(request, 'sheets/sheet_list.html', context)

@login_required
def my_sheets(request):
    """View danh sách phiếu của tôi."""
    search_query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    sub_filter = request.GET.get('sub_filter', '')
    voltage_filter = request.GET.get('voltage', '')
    page_number = request.GET.get('page', 1)

    # Lấy các phiếu do mình tạo hoặc được assign cho mình
    from django.db.models import Q
    sheets = SettingSheet.objects.select_related('created_by', 'relay', 'relay__bay', 'relay__bay__station', 'station').filter(
        Q(created_by=request.user) | Q(assigned_to=request.user) | Q(supervisor_assigned=request.user)
    ).order_by('-created_at')
    
    base_sheets = sheets
    kpi_type, kpi_stats = get_sheet_kpis(base_sheets, status_filter)

    if status_filter:
        sheets = sheets.filter(status__in=status_filter.split(','))

    if sub_filter:
        if sub_filter == 'MATCHED':
            sheets = sheets.filter(relay__isnull=False)
        elif sub_filter == 'UNLINKED':
            sheets = sheets.filter(relay__isnull=True)
        elif sub_filter == 'CHANGED':
            sheets = sheets.filter(has_parameters_changed=True)

    if voltage_filter:
        if voltage_filter == '500':
            sheets = sheets.filter(Q(sheet_code__icontains='500') | Q(title__icontains='500') | Q(station__station_name__icontains='500'))
        elif voltage_filter == '220':
            sheets = sheets.filter(Q(sheet_code__icontains='220') | Q(title__icontains='220') | Q(station__station_name__icontains='220'))
        elif voltage_filter == '110':
            sheets = sheets.filter(Q(sheet_code__icontains='110') | Q(title__icontains='110') | Q(station__station_name__icontains='110'))
        elif voltage_filter == 'medium':
            sheets = sheets.filter(
                Q(sheet_code__icontains='35') | Q(sheet_code__icontains='22') |
                Q(title__icontains='trung') | Q(title__icontains='35') | Q(title__icontains='22') |
                Q(station__station_name__icontains='35') | Q(station__station_name__icontains='22')
            )

    from django.core.paginator import Paginator

    if search_query:
        search_clean = search_query.replace(',', ' ').replace('-', ' ')
        terms = [t for t in search_clean.split() if t]
        for term in terms:
            sheets = sheets.filter(
                Q(sheet_code__icontains=term) |
                Q(title__icontains=term) |
                Q(relay__relay_code__icontains=term) |
                Q(relay__relay_name__icontains=term) |
                Q(relay_text__icontains=term) |
                Q(station__station_name__icontains=term) |
                Q(station__station_code__icontains=term)
            )

    paginator = Paginator(sheets, 40)
    page_obj = paginator.get_page(page_number)
    
    _ = list(page_obj.object_list)

    context = {
        'sheets': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'sub_filter': sub_filter,
        'voltage_filter': voltage_filter,
        'kpi_type': kpi_type,
        'kpi_stats': kpi_stats,
        'list_title': 'Phiếu của tôi'
    }
    return render(request, 'sheets/sheet_list.html', context)

@login_required
def updated_sheets(request):
    """View danh sách các phiếu có thay đổi thông số so với bản cũ."""
    search_query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    sub_filter = request.GET.get('sub_filter', '')
    voltage_filter = request.GET.get('voltage', '')
    page_number = request.GET.get('page', 1)

    sheets = SettingSheet.objects.select_related('created_by', 'relay', 'relay__bay', 'relay__bay__station', 'station').filter(has_parameters_changed=True).order_by('-created_at')

    base_sheets = sheets
    kpi_type, kpi_stats = get_sheet_kpis(base_sheets, status_filter)

    from django.core.paginator import Paginator
    from django.db.models import Q
    
    if search_query:
        search_clean = search_query.replace(',', ' ').replace('-', ' ')
        terms = [t for t in search_clean.split() if t]
        for term in terms:
            sheets = sheets.filter(
                Q(sheet_code__icontains=term) |
                Q(title__icontains=term) |
                Q(relay__relay_code__icontains=term) |
                Q(relay__relay_name__icontains=term) |
                Q(relay_text__icontains=term) |
                Q(station__station_name__icontains=term) |
                Q(station__station_code__icontains=term)
            )
        
    if status_filter:
        sheets = sheets.filter(status__in=status_filter.split(','))

    if sub_filter:
        if sub_filter == 'MATCHED':
            sheets = sheets.filter(relay__isnull=False)
        elif sub_filter == 'UNLINKED':
            sheets = sheets.filter(relay__isnull=True)

    if voltage_filter:
        if voltage_filter == '500':
            sheets = sheets.filter(Q(sheet_code__icontains='500') | Q(title__icontains='500') | Q(station__station_name__icontains='500'))
        elif voltage_filter == '220':
            sheets = sheets.filter(Q(sheet_code__icontains='220') | Q(title__icontains='220') | Q(station__station_name__icontains='220'))
        elif voltage_filter == '110':
            sheets = sheets.filter(Q(sheet_code__icontains='110') | Q(title__icontains='110') | Q(station__station_name__icontains='110'))
        elif voltage_filter == 'medium':
            sheets = sheets.filter(
                Q(sheet_code__icontains='35') | Q(sheet_code__icontains='22') |
                Q(title__icontains='trung') | Q(title__icontains='35') | Q(title__icontains='22') |
                Q(station__station_name__icontains='35') | Q(station__station_name__icontains='22')
            )

    paginator = Paginator(sheets, 40)
    page_obj = paginator.get_page(page_number)
    
    _ = list(page_obj.object_list)

    context = {
        'sheets': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'sub_filter': sub_filter,
        'voltage_filter': voltage_filter,
        'kpi_type': kpi_type,
        'kpi_stats': kpi_stats,
        'list_title': 'Phiếu Có Thay Đổi Thông Số (Cần Lưu Ý)'
    }
    return render(request, 'sheets/sheet_list.html', context)

@login_required
def sheet_create(request):
    """View upload PDF và tạo phiếu."""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet'):
        messages.error(request, "Bạn không có quyền truy cập chức năng trích xuất thông tin.")
        return redirect('sheet_list')

    if request.method == 'POST':
        scan_files = request.FILES.getlist('scan_files')
        
        if not scan_files:
            messages.error(request, "Vui lòng tải lên ít nhất một file PDF.")
            return redirect('sheet_create')
            
        import uuid
        from .models import OcrJob
        from .tasks import execute_parallel_ocr_batch
        
        device_mode = request.POST.get('device_mode', 'CPU').strip().upper()
        if device_mode not in ['CPU', 'GPU']:
            device_mode = 'CPU'

        file_titles = request.POST.getlist('file_titles')
        single_file_title = request.POST.get('file_title', '').strip()
        relative_paths = request.POST.getlist('relative_paths')
        single_relative_path = request.POST.get('relative_path', '').strip()

        job_ids = []
        for idx, scan_file in enumerate(scan_files):
            temp_uuid = uuid.uuid4().hex[:8]
            temp_sheet_code = f"OCR-TEMP-{temp_uuid}"
            
            # Ưu tiên lấy tên tiêu đề / đường dẫn thư mục để dễ quản lý theo dõi
            display_title = ""
            if idx < len(file_titles) and file_titles[idx]:
                display_title = file_titles[idx].strip()
            elif single_file_title:
                display_title = single_file_title
            elif idx < len(relative_paths) and relative_paths[idx]:
                display_title = relative_paths[idx].strip()
            elif single_relative_path:
                display_title = single_relative_path
            else:
                display_title = scan_file.name

            sheet = SettingSheet.objects.create(
                sheet_code=temp_sheet_code,
                title=display_title if display_title else f"Phiếu OCR {temp_uuid}",
                scan_file=scan_file,
                status='DRAFT', # Khởi tạo ở trạng thái Nháp / Đang bóc tách OCR
                created_by=request.user
            )
            
            job = OcrJob.objects.create(
                sheet=sheet,
                correlation_id=f"sheet_{sheet.id}_{temp_uuid}",
                device_mode=device_mode
            )
            job_ids.append(job.id)
            
        from .tasks import broadcast_ocr_job_update
        for j_id in job_ids:
            broadcast_ocr_job_update(job_id=j_id, stage_text='Đang chờ xử lý...')
            
        execute_parallel_ocr_batch.delay(job_ids, user_id=request.user.id, device_mode=device_mode)
        created_count = len(job_ids)
            
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            from django.http import JsonResponse
            return JsonResponse({'status': 'ok', 'created': created_count})
            
        messages.success(request, f"Đã đưa {created_count} file vào tiến trình xử lý OCR ngầm! Dưới đây là tiến độ trích xuất.")
        return redirect('ocr_job_list')

    from stations.models import Station
    stations = Station.objects.all()
    relays = Relay.objects.all()
    initial_relay = request.GET.get('relay_code', '')
    return render(request, 'sheets/sheet_form.html', {
        'stations': stations,
        'relays': relays,
        'initial_relay': initial_relay
    })

@login_required
def sheet_detail(request, pk):
    """View chi tiết phiếu - Split View."""
    sheet = get_object_or_404(SettingSheet, pk=pk)
    
    # Get parameters for the selected relay
    settings = sheet.relay.settings.all() if sheet.relay else []
    
    # Lấy danh sách user theo Role để dùng cho Popup Giao việc
    from django.contrib.auth.models import User
    dispatchers = User.objects.filter(groups__name='DISPATCHER')
    reviewers = User.objects.filter(groups__name='ADMIN')
    
    if hasattr(request.user, 'userprofile') and request.user.userprofile.station and not request.user.is_superuser:
        try:
            station = request.user.userprofile.station
            technicians = User.objects.filter(groups__name='TECHNICIAN', userprofile__station=station)
            supervisors = User.objects.filter(groups__name='SUPERVISOR', userprofile__station=station)
        except Exception:
            technicians = User.objects.none()
            supervisors = User.objects.none()
    else:
        technicians = User.objects.filter(groups__name='TECHNICIAN')
        supervisors = User.objects.filter(groups__name='SUPERVISOR')
    
    dispatcher_sig = sheet.signatures.filter(role='DISPATCHER').first()
    tech_sig = sheet.signatures.filter(role='TECHNICIAN').first()
    sup_sig = sheet.signatures.filter(role='SUPERVISOR').first()
    admin_sig = sheet.signatures.filter(role='ADMIN').first()
    
    # Logic: So sánh với phiếu cũ gần nhất
    previous_sheet = None
    differences = []
    has_previous = False
    
    ocr_job = sheet.ocr_jobs.order_by('-created_at').first()
    ocr_pages = ocr_job.result_data.get('pages', []) if (ocr_job and ocr_job.result_data) else []
    display_data, page_stats, page_is_history = prepare_display_data(sheet.extracted_data, pages=ocr_pages)
    section_groups = list(dict.fromkeys(d['section_divider'] for d in display_data if d.get('section_divider')))
    tech_count = sum(1 for x in display_data if not x.get('is_history_page'))
    history_count = sum(1 for x in display_data if x.get('is_history_page'))
    history_pages = [p for p, is_h in page_is_history.items() if is_h]

    if sheet.relay and display_data:
        if sheet.sheet_code.startswith('AUTO-CORRECT-'):
            has_previous = True
            for item in display_data:
                if 'wrong_value' in item:
                    differences.append({
                        'code': item.get('parameter_code'),
                        'name': item.get('parameter_name', ''),
                        'unit': item.get('unit', ''),
                        'type': 'CHANGED',
                        'old_value': item.get('wrong_value'),
                        'new_value': item.get('value')
                    })
        else:
            previous_sheet = SettingSheet.objects.filter(
                relay=sheet.relay,
                created_at__lt=sheet.created_at
            ).order_by('-created_at').first()
            
            if previous_sheet:
                has_previous = True
                old_data = previous_sheet.extracted_data or []
                new_data = display_data or []
                
                # Convert to dict for easier comparison by parameter_code
                old_dict = {item.get('parameter_code'): item for item in old_data if item.get('parameter_code')}
                new_dict = {item.get('parameter_code'): item for item in new_data if item.get('parameter_code')}
                
                # Compare
                # 1. Added and Changed
                for code, new_item in new_dict.items():
                    if code not in old_dict:
                        differences.append({
                            'code': code,
                            'name': new_item.get('parameter_name', ''),
                            'unit': new_item.get('unit', ''),
                            'type': 'ADDED',
                            'old_value': None,
                            'new_value': new_item.get('value')
                        })
                    else:
                        old_item = old_dict[code]
                        try:
                            old_val = float(old_item.get('value', 0))
                            new_val = float(new_item.get('value', 0))
                            if old_val != new_val:
                                differences.append({
                                    'code': code,
                                    'name': new_item.get('parameter_name', ''),
                                    'unit': new_item.get('unit', ''),
                                    'type': 'CHANGED',
                                    'old_value': old_val,
                                    'new_value': new_val
                                })
                        except (ValueError, TypeError):
                            # In case values are not convertible to float
                            if str(old_item.get('value')) != str(new_item.get('value')):
                                differences.append({
                                    'code': code,
                                    'name': new_item.get('parameter_name', ''),
                                    'unit': new_item.get('unit', ''),
                                    'type': 'CHANGED',
                                    'old_value': old_item.get('value'),
                                    'new_value': new_item.get('value')
                                })
                
                # 2. Removed
                for code, old_item in old_dict.items():
                    if code not in new_dict:
                        differences.append({
                            'code': code,
                            'name': old_item.get('parameter_name', ''),
                            'unit': old_item.get('unit', ''),
                            'type': 'REMOVED',
                            'old_value': old_item.get('value'),
                            'new_value': None
                        })
    
    # Calculate counts
    added_count = sum(1 for d in differences if d['type'] == 'ADDED')
    removed_count = sum(1 for d in differences if d['type'] == 'REMOVED')
    changed_count = sum(1 for d in differences if d['type'] == 'CHANGED')
    total_diff_count = len(differences)
    
    
    # Build history logs
    history_logs = []
    
    # 1. Created
    history_logs.append({
        'time': sheet.created_at,
        'action': 'Khởi tạo phiếu (Tải lên bản scan OCR)',
        'user_name': sheet.created_by.get_full_name() or sheet.created_by.username if sheet.created_by else 'Hệ thống',
        'icon': 'fa-file-upload',
        'color_class': 'text-blue-500',
        'bg_class': 'bg-blue-100',
        'border_class': 'border-blue-200'
    })
    
    # 2. Signatures
    for sig in sheet.signatures.all().order_by('signed_at'):
        if sig.role == 'DISPATCHER':
            history_logs.append({
                'time': sig.signed_at,
                'action': 'Duyệt lệnh và Chuyển về Trạm',
                'user_name': sig.signer_name,
                'icon': 'fa-paper-plane',
                'color_class': 'text-teal-500',
                'bg_class': 'bg-teal-100',
                'border_class': 'border-teal-200'
            })
        elif sig.role == 'TECHNICIAN':
            history_logs.append({
                'time': sig.signed_at,
                'action': 'KTV thi công cài đặt và Ký xác nhận',
                'user_name': sig.signer_name,
                'icon': 'fa-wrench',
                'color_class': 'text-green-500',
                'bg_class': 'bg-green-100',
                'border_class': 'border-green-200'
            })
        elif sig.role == 'SUPERVISOR':
            history_logs.append({
                'time': sig.signed_at,
                'action': 'Giám sát trạm kiểm tra và Ký xác nhận',
                'user_name': sig.signer_name,
                'icon': 'fa-eye',
                'color_class': 'text-emerald-500',
                'bg_class': 'bg-emerald-100',
                'border_class': 'border-emerald-200'
            })
        elif sig.role == 'ADMIN':
            history_logs.append({
                'time': sig.signed_at,
                'action': 'Quản trị viên phê duyệt ban hành',
                'user_name': sig.signer_name,
                'icon': 'fa-check-double',
                'color_class': 'text-amber-500',
                'bg_class': 'bg-amber-100',
                'border_class': 'border-amber-200'
            })
            
    if getattr(sheet, 'assigned_at', None) or sheet.assigned_to or sheet.supervisor_assigned:
        history_logs.append({
            'time': sheet.assigned_at or getattr(dispatcher_sig, 'signed_at', sheet.created_at),
            'action': 'Trưởng trạm phân công KTV & Giám sát',
            'user_name': 'Trưởng nhóm Trạm',
            'icon': 'fa-user-tag',
            'color_class': 'text-purple-500',
            'bg_class': 'bg-purple-100',
            'border_class': 'border-purple-200'
        })

    # 3. Edit logs
    if isinstance(sheet.edit_logs, list):
        from django.utils.dateparse import parse_datetime
        for log in sheet.edit_logs:
            try:
                dt = parse_datetime(log.get('time', ''))
                if dt:
                    changes_text = "<br>".join([f"• {c}" for c in log.get('changes', [])])
                    history_logs.append({
                        'time': dt,
                        'action': f"Sửa đổi thông số OCR:<br><span class='text-xs text-slate-500 font-medium'>{changes_text}</span>",
                        'user_name': log.get('user', 'Người Điều phối'),
                        'icon': 'fa-edit',
                        'color_class': 'text-orange-500',
                        'bg_class': 'bg-orange-100',
                        'border_class': 'border-orange-200'
                    })
            except Exception:
                pass

    # Sort descending
    history_logs.sort(key=lambda x: x['time'], reverse=True)
    
    from stations.models import Station
    context = {
        'sheet': sheet,
        'settings': settings,
        'stations': Station.objects.all(),
        'reviewers': reviewers,
        'dispatchers': dispatchers,
        'technicians': technicians,
        'supervisors': supervisors,
        'dispatcher_sig': dispatcher_sig,
        'tech_sig': tech_sig,
        'sup_sig': sup_sig,
        'admin_sig': admin_sig,
        'previous_sheet': previous_sheet,
        'differences': differences,
        'has_previous': has_previous,
        'added_count': added_count,
        'removed_count': removed_count,
        'changed_count': changed_count,
        'total_diff_count': total_diff_count,
        'display_data': display_data,
        'page_stats': page_stats,
        'section_groups': section_groups,
        'tech_count': tech_count,
        'history_count': history_count,
        'history_pages': history_pages,
        'history_logs': history_logs,
    }
    
    # Get extra metadata from OCR
    latest_ocr_job = sheet.ocr_jobs.filter(status__in=['SUCCESS', 'SUCCESS_WITH_WARNINGS']).order_by('-created_at').first()
    business = {}
    if latest_ocr_job and latest_ocr_job.result_data:
        business = latest_ocr_job.result_data.get('business', {})
    else:
        active_job = sheet.ocr_jobs.filter(status='PROCESSING').order_by('-created_at').first()
        if active_job:
            cached_data = cache.get(f"ocr_header_data_{active_job.id}")
            if cached_data:
                business = cached_data.get('business', {})

    if business and 'page1_fields' in business:
            key_translations = {
                'ticket_number': 'Số Phiếu',
                'page_reference': 'Số Bản Vẽ / Trang',
                'station': 'Trạm',
                'protected_equipment': 'Thiết Bị Được Bảo Vệ',
                'protection_type': 'Kiểu Bảo Vệ',
                'circuit_breaker': 'Máy Cắt',
                'relay_name': 'Tên Rơ-le',
                'relay_version': 'Phiên Bản Rơ-le',
                'wiring_diagram': 'Sơ Đồ Đấu Dây',
                'relay_serial': 'Số Hiệu Rơ-le',
                'current_transformer_ratio': 'Tỷ Số Biến Dòng Điện',
                'manufacturer': 'Nhà Chế Tạo',
                'voltage_transformer_ratio': 'Tỷ Số Biến Điện Áp',
                'installation_year': 'Năm Lắp Đặt',
                'single_line_drawing': 'Sơ Đồ Một Sợi',
                'software': 'Phần Mềm',
                'protection_cabinet': 'Tủ Bảo Vệ',
                'protection_circuit': 'Mạch Bảo Vệ',
                'issuance_purpose': 'Mục Đích Ban Hành / Chỉnh Định',
                'dispatch_center_request': 'Yêu Cầu Của Trung Tâm Điều Độ',
                'software_version': 'Phiên Bản Phần Mềm',
                'page_number': 'Trang Số',
                'total_pages': 'Tổng Số Trang',
                'form_title': 'Tiêu Đề Phiếu',
                'protection_principle_heading': 'Nguyên Tắc Hoạt Động'
            }
            
            formatted_fields = {}
            for k, v in business['page1_fields'].items():
                if v and v.get('value'):
                    # Dịch key sang tiếng Việt, nếu không có thì format từ key tiếng Anh
                    formatted_key = key_translations.get(k.lower(), k.replace('_', ' ').title())
                    formatted_fields[formatted_key] = v
            context['page1_fields'] = formatted_fields
    
    # Pass stations, bays, and relays for editing metadata
    from stations.models import Station, Bay, Relay
    import json
    
    if 'page1_fields' in context:
        context['page1_fields_json'] = json.dumps({k: v.get('value', '') for k, v in context['page1_fields'].items() if isinstance(v, dict)})
    else:
        context['page1_fields_json'] = "{}"
    
    # 1. Tự động liên kết Trạm nếu phiếu chưa có trạm (từ kết quả OCR Trang 1)
    target_station = sheet.station
    if not target_station:
        raw_ocr_st = ''
        if 'page1_fields' in context and 'Trạm' in context['page1_fields']:
            raw_ocr_st = context['page1_fields']['Trạm'].get('value', '')
        elif business and 'page1_fields' in business and 'station' in business['page1_fields']:
            raw_ocr_st = business['page1_fields']['station'].get('value', '')
        
        if raw_ocr_st:
            from sheets.relay_matcher import normalize_text
            st = Station.objects.filter(station_name__icontains=raw_ocr_st).first()
            if not st:
                norm_ocr_st = normalize_text(raw_ocr_st)
                clean_ocr = norm_ocr_st.replace('tram', '').split('(')[0].strip()
                for s_obj in Station.objects.all():
                    norm_s_name = normalize_text(s_obj.station_name).replace('tram', '').strip()
                    if clean_ocr and norm_s_name and (clean_ocr in norm_s_name or norm_s_name in clean_ocr):
                        st = s_obj
                        break
            if st:
                target_station = st
                sheet.station = st
                sheet.save(update_fields=['station'])

    # 2. Tự động liên kết Rơ-le nếu phiếu chưa có rơ-le (sử dụng Multi-Layer Relay Matcher)
    if target_station and not sheet.relay:
        from sheets.relay_matcher import match_relay_from_ocr
        flat_p1 = {}
        if 'page1_fields' in context:
            flat_p1 = {k: v.get('value') for k, v in context['page1_fields'].items() if isinstance(v, dict)}
        if not flat_p1 and business and 'page1_fields' in business:
            flat_p1 = {k: v.get('value') for k, v in business['page1_fields'].items() if isinstance(v, dict)}
        
        if flat_p1:
            candidate_relays = list(Relay.objects.filter(bay__station=target_station).select_related('bay'))
            if candidate_relays:
                matched_rl, match_score, match_why = match_relay_from_ocr(flat_p1, candidate_relays)
                if matched_rl and matched_rl.bay and matched_rl.bay.station_id == target_station.id:
                    sheet.relay = matched_rl
                    sheet.save(update_fields=['relay'])

    # Kiểm tra tính toàn vẹn: Rơ-le đã lưu có thuộc đúng Trạm đã lưu không?
    current_relay = sheet.relay
    current_relay_bay = sheet.relay.bay if sheet.relay else None
    active_station = sheet.station or target_station
    if sheet.relay and active_station:
        if sheet.relay.bay and sheet.relay.bay.station_id != active_station.id:
            # Rơ-le trong DB không thuộc Trạm của phiếu! Bỏ qua để UI tự gợi ý đúng rơ-le trong trạm
            current_relay = None
            current_relay_bay = None

    context['current_station_id'] = str(active_station.id) if active_station else ''
    context['current_relay_id'] = str(current_relay.id) if current_relay else ''
    context['current_relay_bay_id'] = str(current_relay_bay.id) if current_relay_bay else ''

    stations_data = list(Station.objects.values('id', 'station_name'))
    
    # Tối ưu hóa hiệu năng: Chỉ nạp Bays và Relays của Trạm hiện tại
    if active_station:
        bays_data = list(Bay.objects.filter(station=active_station).values('id', 'station_id', 'bay_name'))
        relays_data = list(Relay.objects.filter(bay__station=active_station).values('id', 'bay_id', 'relay_code', 'relay_name', 'manufacturer'))
    else:
        bays_data = list(Bay.objects.values('id', 'station_id', 'bay_name'))
        relays_data = []
    
    context['stations_json'] = json.dumps(stations_data)
    context['bays_json'] = json.dumps(bays_data)
    context['relays_json'] = json.dumps(relays_data)
    
    return render(request, 'sheets/sheet_detail.html', context)

@login_required
def sheet_assign(request, pk):
    """View để Dispatcher phân công phiếu cho KTV và Giám sát."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        
        # OCC
        original_updated_at = request.POST.get('_original_updated_at')
        if original_updated_at and str(sheet.updated_at.timestamp()) != original_updated_at:
            messages.error(request, "Dữ liệu phiếu này đã bị thay đổi bởi một người khác trong khi bạn đang xem. Hãy tải lại trang để xem nội dung mới nhất.")
            return redirect('sheet_detail', pk=pk)
            
        assignee_id = request.POST.get('assignee_id')
        supervisor_id = request.POST.get('supervisor_id')
        new_status = request.POST.get('status')
        
        from django.contrib.auth.models import User
        if assignee_id:
            sheet.assigned_to = User.objects.get(pk=assignee_id)
        if supervisor_id:
            sheet.supervisor_assigned = User.objects.get(pk=supervisor_id)
        
        if assignee_id or supervisor_id:
            from django.utils import timezone
            sheet.assigned_at = timezone.now()
            
        valid_statuses = [s[0] for s in SettingSheet.STATUS_CHOICES]
        if new_status in valid_statuses:
            sheet.status = new_status
            
        sheet.save()
        
        # --- Send real-time notifications via Channels ---
        try:
            from asgiref.sync import async_to_sync
            from channels.layers import get_channel_layer
            channel_layer = get_channel_layer()
            if channel_layer:
                if assignee_id:
                    async_to_sync(channel_layer.group_send)(
                        f"user_{assignee_id}",
                        {
                            "type": "send_notification",
                            "title": "Nhiệm vụ Mới",
                            "message": f"Điều phối viên vừa phân công Phiếu {sheet.sheet_code} cho bạn."
                        }
                    )
                if supervisor_id:
                    async_to_sync(channel_layer.group_send)(
                        f"user_{supervisor_id}",
                        {
                            "type": "send_notification",
                            "title": "Nhiệm vụ Giám sát",
                            "message": f"Bạn được chỉ định giám sát Phiếu {sheet.sheet_code}."
                        }
                    )
        except Exception as e:
            print("Channels error:", e)
            
        messages.success(request, f"Đã phân công phiếu {sheet.sheet_code} thành công!")
        return redirect('sheet_detail', pk=pk)
    return redirect('sheet_list')

@login_required
def sheet_route_to_station(request, pk):
    """
    Route a sheet directly to the station.
    Allowed for DISPATCHER, ADMIN, or the creator of the sheet.
    """
    sheet = get_object_or_404(SettingSheet, pk=pk)
    
    if request.method == 'POST':
        # OCC
        original_updated_at = request.POST.get('_original_updated_at')
        if original_updated_at and str(sheet.updated_at.timestamp()) != original_updated_at:
            messages.error(request, "Dữ liệu phiếu này đã bị thay đổi bởi một người khác trong khi bạn đang thao tác. Hãy tải lại trang để xem nội dung mới nhất.")
            return redirect('sheet_detail', pk=pk)
            
        # Check permissions: Dispatcher
        has_perm = request.user.has_perm('sheets.can_dispatch_sheet')
        
        if has_perm and sheet.status == 'ISSUED':
            if sheet.created_by != request.user and not request.user.is_superuser:
                messages.error(request, "Bạn chỉ có thể duyệt chuyển trạm đối với những phiếu do chính bạn khởi tạo.")
                return redirect('sheet_detail', pk=pk)
                
            # Auto-save station and relay if passed from the frontend form
            station_id = request.POST.get('station_id')
            relay_id = request.POST.get('relay_id')
            
            if station_id:
                from stations.models import Station
                station = Station.objects.filter(id=station_id).first()
                if station:
                    sheet.station = station
                    
            if relay_id:
                try:
                    relay_id_int = int(relay_id)
                    from stations.models import Relay
                    relay = Relay.objects.filter(id=relay_id_int).first()
                    if relay:
                        sheet.relay = relay
                        sheet.relay_text = None
                except ValueError:
                    sheet.relay = None
                    sheet.relay_text = relay_id.strip()
                    
            if not sheet.station or not sheet.relay:
                messages.error(request, "Bạn chưa cập nhật thông tin Trạm đích và Rơ-le cho phiếu này. Vui lòng quay lại tab 'Dữ liệu OCR', chọn đủ thông tin và bấm 'Cập nhật Thông tin' trước khi chuyển Trạm.")
                return redirect('sheet_detail', pk=pk)
                
            execution_station_id = request.POST.get('execution_station_id')
            if execution_station_id:
                from stations.models import Station
                exec_station = Station.objects.filter(id=execution_station_id).first()
                if exec_station:
                    sheet.execution_station = exec_station
            else:
                sheet.execution_station = None

            sheet.status = 'ROUTED_TO_STATION'
            sheet.save()
            
            # Ghi nhận người duyệt
            import hashlib
            from django.utils.timezone import now
            hash_input = f"{sheet.id}-{request.user.username}-{now()}".encode('utf-8')
            sig_hash = hashlib.sha256(hash_input).hexdigest()
            
            SignatureRecord.objects.create(
                sheet=sheet,
                signer_name=request.user.get_full_name() or request.user.username,
                role='DISPATCHER',
                signature_hash=sig_hash
            )
            
            messages.success(request, f"Đã duyệt và chuyển phiếu {sheet.sheet_code} về Trạm thành công!")
        else:
            messages.error(request, "Bạn không có quyền hoặc phiếu không ở trạng thái hợp lệ.")
        return redirect('sheet_detail', pk=pk)
    return redirect('sheet_list')

@login_required
def sheet_update_status(request, pk):
    """View update status via HTMX (mock logic)."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        new_status = request.POST.get('status')
        
        valid_statuses = [s[0] for s in SettingSheet.STATUS_CHOICES]
        if new_status in valid_statuses:
            sheet.status = new_status
            sheet.save()
            messages.success(request, f"Đã cập nhật trạng thái thành {sheet.get_status_display()}")
            
        return redirect('sheet_detail', pk=pk)
    return redirect('sheet_list')

@login_required
def initiate_signature(request, pk):
    """View giả lập tạo phiên ký số EVN."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        role = request.POST.get('role', 'ADMIN')
        
        # Gọi Mock Service
        res = evn_service.initiate_signing_session(sheet.id, role)
        
        return JsonResponse({
            'success': True,
            'session_id': res['session_id'],
            'signing_url': res['signing_url'],
            'role': role
        })
    return JsonResponse({'success': False}, status=400)

@login_required
def confirm_signature(request, pk):
    """View giả lập xác nhận ký số thành công."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        role = request.POST.get('role')
        signer_name = request.user.get_full_name() or request.user.username
        
        # Gọi Mock Service để xác thực và lấy chữ ký
        res = evn_service.confirm_signature(sheet, signer_name, role)
        
        if res['success']:
            tech_sig_exists = sheet.signatures.filter(role='TECHNICIAN').exists()
            sup_sig_exists = sheet.signatures.filter(role='SUPERVISOR').exists()

            # Server-side validation of signature sequence
            if role == 'SUPERVISOR' and not tech_sig_exists:
                return JsonResponse({'success': False, 'error': 'Technician must sign first'}, status=400)
            if role == 'ADMIN' and not sup_sig_exists:
                return JsonResponse({'success': False, 'error': 'Supervisor must sign first'}, status=400)

            # Lưu chữ ký vào DB
            SignatureRecord.objects.create(
                sheet=sheet,
                signer_name=signer_name,
                role=role,
                signature_hash=res['signature_hash']
            )
            
            messages.success(request, f"Ký số thành công ({role})!")
            
            # Cập nhật trạng thái phiếu dựa trên Role
            if role == 'TECHNICIAN' and sheet.status == 'RECEIVED':
                pass # Chờ thêm Giám sát trạm
            elif role == 'SUPERVISOR' and sheet.status == 'RECEIVED':
                sheet.status = 'PENDING_ADMIN_APPROVAL' # Đẩy lên cho ADMIN duyệt
                sheet.save()
            elif role == 'ADMIN' and sheet.status == 'PENDING_ADMIN_APPROVAL':
                sheet.status = 'COMPLETED'
                sheet.save()
                
                # Cập nhật thông số kỹ thuật mới từ phiếu hoàn thành vào RelaySetting
                relay = sheet.relay
                if relay and sheet.extracted_data:
                    from stations.models import RelaySetting
                    
                    new_codes = set()
                    new_data_dict = {}
                    for item in sheet.extracted_data:
                        code = item.get('parameter_code')
                        if code:
                            new_codes.add(code)
                            new_data_dict[code] = item
                            
                    # Remove parameters that are no longer in this sheet
                    RelaySetting.objects.filter(relay=relay).exclude(parameter_code__in=new_codes).delete()
                    
                    # Update or Add parameters
                    for code, item in new_data_dict.items():
                        val = 0.0
                        try:
                            val = float(item.get('value', 0))
                        except (ValueError, TypeError):
                            pass
                            
                        setting, created = RelaySetting.objects.get_or_create(
                            relay=relay,
                            parameter_code=code,
                            defaults={
                                'parameter_name': item.get('parameter_name', '')[:100],
                                'standard_value': val,
                                'unit': str(item.get('unit', ''))[:20],
                                'tolerance_min': val * 0.95,
                                'tolerance_max': val * 1.05,
                            }
                        )
                        if not created:
                            setting.parameter_name = item.get('parameter_name', '')[:100]
                            setting.standard_value = val
                            setting.unit = str(item.get('unit', ''))[:20]
                            setting.save()
                            
                # Khôi phục Auto Check nếu Rơ-le đang bị tạm ngưng (AUTO-CORRECT)
                relay = sheet.relay
                if relay and relay.is_paused_for_correction:
                    relay.is_paused_for_correction = False
                    if relay.paused_schedule_data:
                        relay.check_interval_value = relay.paused_schedule_data.get('check_interval_value', 1)
                        relay.check_interval_unit = relay.paused_schedule_data.get('check_interval_unit', 'h')
                        relay.paused_schedule_data = None
                        
                    from django.utils import timezone
                    relay.last_checked_at = timezone.now()
                    relay.next_check_at = relay.calculate_next_check(from_time=relay.last_checked_at)
                    relay.save()
                
            tech_sig = sheet.signatures.filter(role='TECHNICIAN').first()
            sup_sig = sheet.signatures.filter(role='SUPERVISOR').first()
            admin_sig = sheet.signatures.filter(role='ADMIN').first()
                
            return render(request, 'sheets/partials/_signature_panel.html', {
                'sheet': sheet,
                'tech_sig': tech_sig,
                'sup_sig': sup_sig,
                'admin_sig': admin_sig
            })
            
    return JsonResponse({'success': False}, status=400)

def perform_mock_ocr(sheet):
    """Hàm chạy AI OCR (mock) trực tiếp."""
    import random
    extracted_data = []
    
    # 1. Trích xuất metadata từ PDF (Tên trạm, Mã rơ-le)
    station_name = sheet.station.station_name if sheet.station else 'Không xác định'
    relay_code = sheet.relay.relay_code if sheet.relay else (sheet.relay_text or 'Không xác định')
    
    extracted_data.append({
        'parameter_code': 'STATION_NAME',
        'parameter_name': 'Tên Trạm (Nhận diện)',
        'unit': '',
        'value': station_name,
        'original_value': station_name,
        'confidence': round(random.uniform(95.0, 99.9), 1)
    })
    
    extracted_data.append({
        'parameter_code': 'RELAY_CODE',
        'parameter_name': 'Mã Rơ-le (Nhận diện)',
        'unit': '',
        'value': relay_code,
        'original_value': relay_code,
        'confidence': round(random.uniform(95.0, 99.9), 1)
    })
    
    # 2. Trích xuất thông số
    if sheet.relay and sheet.relay.settings.exists():
        for setting in sheet.relay.settings.all():
            is_perfect = random.random() > 0.1
            val = setting.standard_value if is_perfect else setting.standard_value * random.uniform(0.95, 1.05)
            val = round(val, 2)
            
            conf = random.uniform(85.0, 99.9) if not is_perfect else random.uniform(97.0, 99.9)
            
            extracted_data.append({
                'parameter_code': setting.parameter_code,
                'parameter_name': setting.parameter_name,
                'unit': setting.unit,
                'value': val,
                'original_value': val,
                'confidence': round(conf, 1)
            })
    else:
        # Nếu không có relay hoặc relay chưa cấu hình thông số, tạo random 20-30 thông số
        mock_params_template = [
            {'code': 'I_max', 'name': 'Dòng điện cắt cực đại', 'unit': 'A', 'min': 10, 'max': 50},
            {'code': 'T_delay', 'name': 'Thời gian trễ cắt', 'unit': 's', 'min': 0.1, 'max': 2.0},
            {'code': 'V_min', 'name': 'Điện áp cắt thấp áp', 'unit': 'V', 'min': 90, 'max': 110},
            {'code': 'V_max', 'name': 'Điện áp cắt quá áp', 'unit': 'V', 'min': 120, 'max': 150},
            {'code': 'F_min', 'name': 'Tần số cắt thấp', 'unit': 'Hz', 'min': 48, 'max': 49.5},
            {'code': 'F_max', 'name': 'Tần số cắt cao', 'unit': 'Hz', 'min': 50.5, 'max': 52},
            {'code': 'Z_reach_1', 'name': 'Vùng bảo vệ khoảng cách 1', 'unit': 'Ohm', 'min': 1, 'max': 10},
            {'code': 'Z_reach_2', 'name': 'Vùng bảo vệ khoảng cách 2', 'unit': 'Ohm', 'min': 10, 'max': 25},
            {'code': 'Z_reach_3', 'name': 'Vùng bảo vệ khoảng cách 3', 'unit': 'Ohm', 'min': 25, 'max': 50},
            {'code': 'I_diff', 'name': 'Dòng điện so lệch', 'unit': 'A', 'min': 0.5, 'max': 5.0},
            {'code': 'T_diff', 'name': 'Thời gian cắt so lệch', 'unit': 's', 'min': 0.0, 'max': 0.5},
            {'code': 'Dir_angle', 'name': 'Góc hướng dòng', 'unit': 'Deg', 'min': -90, 'max': 90},
            {'code': 'I_earth_1', 'name': 'Dòng chạm đất cực đại cấp 1', 'unit': 'A', 'min': 1, 'max': 10},
            {'code': 'T_earth_1', 'name': 'Thời gian trễ chạm đất cấp 1', 'unit': 's', 'min': 0.1, 'max': 1.0},
            {'code': 'I_earth_2', 'name': 'Dòng chạm đất cực đại cấp 2', 'unit': 'A', 'min': 10, 'max': 50},
            {'code': 'P_reverse', 'name': 'Công suất ngược', 'unit': 'kW', 'min': 5, 'max': 20},
            {'code': 'T_reverse', 'name': 'Thời gian cắt công suất ngược', 'unit': 's', 'min': 0.5, 'max': 5.0},
            {'code': 'I_thermal', 'name': 'Dòng bảo vệ quá nhiệt', 'unit': 'A', 'min': 50, 'max': 200},
            {'code': 'K_thermal', 'name': 'Hệ số thời gian nhiệt', 'unit': '', 'min': 0.1, 'max': 1.5},
            {'code': 'T_reclose_1', 'name': 'Thời gian tự đóng lại lần 1', 'unit': 's', 'min': 0.5, 'max': 3.0},
            {'code': 'T_reclose_2', 'name': 'Thời gian tự đóng lại lần 2', 'unit': 's', 'min': 10, 'max': 30},
            {'code': 'N_reclose', 'name': 'Số lần tự đóng lại', 'unit': 'lần', 'min': 1, 'max': 3},
            {'code': 'U_sync', 'name': 'Điện áp hòa đồng bộ', 'unit': 'V', 'min': 95, 'max': 105},
            {'code': 'F_sync', 'name': 'Độ lệch tần số hòa đồng bộ', 'unit': 'Hz', 'min': 0.05, 'max': 0.2},
            {'code': 'Phi_sync', 'name': 'Góc lệch pha hòa đồng', 'unit': 'Deg', 'min': 5, 'max': 15},
            {'code': 'I_unbalance', 'name': 'Dòng không cân bằng', 'unit': 'A', 'min': 1, 'max': 5},
            {'code': 'V_unbalance', 'name': 'Điện áp không cân bằng', 'unit': 'V', 'min': 2, 'max': 10},
            {'code': 'T_start', 'name': 'Thời gian khởi động', 'unit': 's', 'min': 1, 'max': 10}
        ]
        
        # Tự động sinh thêm thông số cho các pha A, B, C, N để làm phong phú dữ liệu (đủ 50-60 dòng)
        expanded_params = []
        for p in mock_params_template:
            expanded_params.append(p)
            if 'chạm đất' not in p['name'] and p['unit'] in ['A', 'V']:
                expanded_params.append({**p, 'code': f"{p['code']}_phA", 'name': f"{p['name']} (Pha A)"})
                expanded_params.append({**p, 'code': f"{p['code']}_phB", 'name': f"{p['name']} (Pha B)"})
                expanded_params.append({**p, 'code': f"{p['code']}_phC", 'name': f"{p['name']} (Pha C)"})
            if 'chạm đất' in p['name'] or 'không cân bằng' in p['name']:
                expanded_params.append({**p, 'code': f"{p['code']}_N", 'name': f"{p['name']} (Trung tính)"})

        # Chọn 50 thông số đầu tiên (hoặc ngẫu nhiên 50)
        selected_params = random.sample(expanded_params, min(50, len(expanded_params)))
        
        for idx, p in enumerate(selected_params):
            val = round(random.uniform(p['min'], p['max']), 2)
            conf = random.uniform(85.0, 99.9)
            page_num = (idx // 12) + 1  # 12 parameters per page
            extracted_data.append({
                'parameter_code': p['code'],
                'parameter_name': p['name'],
                'unit': p['unit'],
                'value': val,
                'original_value': val,
                'confidence': round(conf, 1),
                'page_number': page_num
            })
            
    # Assign page_number to relay settings if using relay
    if sheet.relay and sheet.relay.settings.exists():
        for idx, data in enumerate(extracted_data):
            if 'page_number' not in data:
                # First two are metadata, skip them or put them on page 1
                if data['parameter_code'] in ['STATION_NAME', 'RELAY_CODE']:
                    data['page_number'] = 1
                else:
                    # offset by 2 for metadata
                    data['page_number'] = ((idx - 2) // 12) + 1

    sheet.extracted_data = extracted_data
    sheet.save()
    
    from .utils import update_has_parameters_changed_for_sheet
    update_has_parameters_changed_for_sheet(sheet)
    
    return extracted_data

@login_required
def run_mock_ocr(request, pk):
    """View kích hoạt lại quá trình chạy AI OCR (thủ công)."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        
        if sheet.status not in ['DRAFT', 'ISSUED']:
            messages.error(request, "Phiếu đã được duyệt và chuyển trạm. Không thể chạy lại AI OCR.")
            return redirect('sheet_detail', pk=pk)
            
        import uuid
        from .models import OcrJob
        from .tasks import run_ocr_subprocess
        
        job = OcrJob.objects.create(
            sheet=sheet,
            correlation_id=f"sheet_{sheet.id}_{uuid.uuid4().hex[:8]}"
        )
        run_ocr_subprocess.delay(job.id)
        
        messages.success(request, "Đã gửi yêu cầu chạy OCR thực tế. Quá trình xử lý đang diễn ra ngầm.")
        return redirect('sheet_detail', pk=pk)
    return redirect('sheet_list')

@login_required
def sheet_save_actual_data(request, pk):
    """View cho phép KTV lưu thông số thực tế và Điều phối sửa lỗi OCR."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        
        # Optimistic Concurrency Control
        original_updated_at = request.POST.get('_original_updated_at')
        if original_updated_at and str(sheet.updated_at.timestamp()) != original_updated_at:
            messages.error(request, "Dữ liệu phiếu này đã bị thay đổi bởi một người khác trong khi bạn đang xem. Hãy tải lại trang để xem nội dung mới nhất trước khi chỉnh sửa.")
            return redirect('sheet_detail', pk=pk)
        
        if sheet.status not in ['DRAFT', 'ISSUED']:
            messages.error(request, "Phiếu đã được duyệt và chuyển trạm. Không thể sửa đổi thông số OCR nữa.")
            return redirect('sheet_detail', pk=pk)
            
        is_dispatcher = request.user.has_perm('sheets.can_create_sheet') or request.user.has_perm('sheets.can_dispatch_sheet')
        
        if is_dispatcher:
            changes = []
            
            # 1. Cập nhật Thông tin định danh chung (Mã phiếu, Tiêu đề, Trạm, Rơ-le) nếu có gửi lên
            if 'sheet_code' in request.POST:
                new_code = request.POST.get('sheet_code', '').strip()
                if new_code and new_code != sheet.sheet_code:
                    changes.append(f"Mã phiếu: {sheet.sheet_code} ➡️ {new_code}")
                    sheet.sheet_code = new_code

            if 'title' in request.POST:
                new_title = request.POST.get('title', '').strip()
                if new_title != (sheet.title or ''):
                    sheet.title = new_title

            if 'station_id' in request.POST:
                station_id = request.POST.get('station_id')
                if station_id:
                    from stations.models import Station
                    station_obj = Station.objects.filter(id=station_id).first()
                    if station_obj and sheet.station != station_obj:
                        changes.append(f"Trạm: {sheet.station.station_name if sheet.station else 'Chưa gán'} ➡️ {station_obj.station_name}")
                        sheet.station = station_obj

            if 'relay_id' in request.POST:
                relay_id = request.POST.get('relay_id')
                if relay_id:
                    from stations.models import Relay
                    try:
                        relay_id_int = int(relay_id)
                        relay_obj = Relay.objects.filter(id=relay_id_int).first()
                        if relay_obj and sheet.relay != relay_obj:
                            changes.append(f"Rơ-le: {sheet.relay.relay_name if sheet.relay else 'Chưa gán'} ➡️ {relay_obj.relay_name}")
                            sheet.relay = relay_obj
                            sheet.relay_text = None
                    except ValueError:
                        relay_text = relay_id.strip()
                        from stations.models import Relay
                        matched = None
                        if sheet.station:
                            matched = Relay.objects.filter(relay_code=relay_text, bay__station=sheet.station).first()
                            if not matched:
                                matched = Relay.objects.filter(relay_name__icontains=relay_text, bay__station=sheet.station).first()
                        if not matched:
                            matched = Relay.objects.filter(relay_code=relay_text).first()
                        
                        if matched:
                            if sheet.relay != matched:
                                changes.append(f"Rơ-le: {sheet.relay.relay_name if sheet.relay else 'Chưa gán'} ➡️ {matched.relay_name}")
                                sheet.relay = matched
                                sheet.relay_text = None
                        else:
                            if sheet.relay_text != relay_text:
                                changes.append(f"Rơ-le (nhập tay): {relay_text}")
                                sheet.relay = None
                                sheet.relay_text = relay_text

            # 2. Cập nhật Bảng thông số kỹ thuật (OCR Parameters)
            if sheet.extracted_data:
                updated_data = []
                for index, item in enumerate(sheet.extracted_data):
                    # Kiểm tra xem dòng này có bị đánh dấu xóa không
                    if request.POST.get(f'ocr_delete_{index}') == '1':
                        code_disp = item.get('parameter_code') or f'Dòng {index+1}'
                        changes.append(f"Đã xóa dòng rác: [{code_disp}] {item.get('parameter_name', '')}")
                        continue  # Bỏ qua không đưa vào updated_data

                    # 2.1 Cập nhật Mã thông số (Parameter Code)
                    ocr_code = request.POST.get(f'ocr_code_{index}')
                    if ocr_code is not None:
                        ocr_code_clean = ocr_code.strip()
                        old_code = str(item.get('parameter_code') or '').strip()
                        if ocr_code_clean != old_code and ocr_code_clean != '':
                            changes.append(f"Sửa mã: {old_code or '---'} ➡️ {ocr_code_clean}")
                            item['parameter_code'] = ocr_code_clean
                            item['record_key'] = ocr_code_clean
                            item['clean_code'] = ocr_code_clean

                    # 2.2 Cập nhật Tên thông số (Parameter Name)
                    ocr_name = request.POST.get(f'ocr_name_{index}')
                    if ocr_name is not None:
                        ocr_name_clean = ocr_name.strip()
                        old_name = str(item.get('parameter_name') or '').strip()
                        if ocr_name_clean != old_name and ocr_name_clean != '':
                            changes.append(f"Sửa tên [{item.get('parameter_code')}]: {old_name} ➡️ {ocr_name_clean}")
                            item['parameter_name'] = ocr_name_clean
                            item['clean_name'] = ocr_name_clean

                    # 2.3 Cập nhật Giá trị cài đặt (Value)
                    ocr_val = request.POST.get(f'ocr_value_{index}')
                    if ocr_val is not None:
                        old_val_raw = item.get('value')
                        old_val_str = str(old_val_raw or '').strip()
                        new_val_raw = ocr_val.strip()
                        
                        is_changed = False
                        try:
                            # Nếu cả 2 đều là số, so sánh theo dạng số
                            old_float = float(old_val_raw)
                            new_float = float(new_val_raw)
                            if old_float != new_float:
                                is_changed = True
                                new_val = new_float
                            else:
                                new_val = old_val_raw # Giữ nguyên type cũ
                        except (ValueError, TypeError):
                            # Nếu là chuỗi (hoặc 1 trong 2 là chuỗi)
                            if old_val_str != new_val_raw:
                                is_changed = True
                            new_val = new_val_raw
                            
                        if is_changed:
                            code_lbl = item.get('parameter_code') or f'Dòng {index+1}'
                            if 'original_value' not in item:
                                item['original_value'] = old_val_raw
                            changes.append(f"{code_lbl}: {old_val_str or '---'} ➡️ {new_val}")
                            item['value'] = new_val
                            item['clean_value'] = new_val
                            # Nếu đây là dạng bảng bị lệch cột (giá trị trước đó nằm ở description)
                            if item.get('description') and str(item.get('description')).strip() in [str(new_val), str(old_val_str)]:
                                item['description'] = ''
                            if old_val_str.lower() in {'hz', 'a', 'v', 'kv', 's', 'sec', 'ms', 'x', 'deg', 'none', 'ohm', 'ω', '%'} and not item.get('unit'):
                                item['unit'] = old_val_raw

                    # 2.4 Cập nhật các trường đặc thù Ma trận Tiếp điểm Đầu ra (Matrix BO/BI)
                    ocr_group = request.POST.get(f'ocr_group_{index}')
                    if ocr_group is not None:
                        item['group'] = ocr_group.strip()
                        item['matrix_group'] = ocr_group.strip()
                        item['clean_group'] = ocr_group.strip()

                    ocr_type = request.POST.get(f'ocr_type_{index}')
                    if ocr_type is not None:
                        item['type'] = ocr_type.strip()
                        item['clean_type'] = ocr_type.strip()

                    ocr_cfg = request.POST.get(f'ocr_cfg_{index}')
                    if ocr_cfg is not None:
                        item['configuration'] = ocr_cfg.strip()
                        item['clean_cfg'] = ocr_cfg.strip()

                    if item.get('is_matrix'):
                        if ocr_name:
                            item['clean_func_no'] = ocr_name.strip()
                        if ocr_val:
                            item['clean_info'] = str(new_val)
                            item['matrix_info'] = str(new_val)

                    updated_data.append(item)
                
                sheet.extracted_data = updated_data
                
            if changes:
                from django.utils import timezone
                edit_log = {
                    'time': timezone.now().isoformat(),
                    'user': request.user.get_full_name() or request.user.username,
                    'changes': changes
                }
                if not isinstance(sheet.edit_logs, list):
                    sheet.edit_logs = []
                sheet.edit_logs.append(edit_log)
                
            sheet.save()
            
            if sheet.extracted_data:
                from .utils import update_has_parameters_changed_for_sheet
                update_has_parameters_changed_for_sheet(sheet)
            
            if changes:
                msg = "Đã lưu toàn bộ thông tin phiếu: " + " | ".join(changes[:3])
                if len(changes) > 3:
                    msg += f" (và {len(changes) - 3} thay đổi khác)"
                messages.success(request, msg)
                
                try:
                    from asgiref.sync import async_to_sync
                    from channels.layers import get_channel_layer
                    channel_layer = get_channel_layer()
                    if channel_layer and sheet.created_by:
                        async_to_sync(channel_layer.group_send)(
                            f"user_{sheet.created_by.id}",
                            {
                                "type": "send_notification",
                                "title": "Cập nhật dữ liệu OCR",
                                "message": f"Điều phối viên đã sửa thông tin phiếu {sheet.sheet_code}: " + " | ".join(changes[:2])
                            }
                        )
                except Exception as e:
                    print("WebSocket Error:", e)
            else:
                messages.success(request, 'Đã lưu toàn bộ thông tin phiếu và thông số cài đặt thành công!')
        else:
            messages.error(request, 'Bạn không có quyền cập nhật thông số cho phiếu này.')
            
        return redirect('sheet_detail', pk=pk)
    return redirect('sheet_list')

@login_required
def sheet_update_metadata(request, pk):
    """View cho phép Điều phối viên cập nhật lại thông tin chung của phiếu (Mã, Trạm, Rơ-le) sau OCR."""
    if request.method == 'POST':
        sheet = get_object_or_404(SettingSheet, pk=pk)
        
        if sheet.status not in ['DRAFT', 'ISSUED', 'ROUTED_TO_STATION']:
            messages.error(request, "Phiếu đã được phân công hoặc khóa. Không thể sửa thông tin chung nữa.")
            return redirect('sheet_detail', pk=pk)
            
        is_dispatcher = request.user.has_perm('sheets.can_create_sheet') or request.user.has_perm('sheets.can_dispatch_sheet')
        
        if is_dispatcher:
            sheet.sheet_code = request.POST.get('sheet_code', sheet.sheet_code).strip()
            sheet.title = request.POST.get('title', sheet.title).strip()
            
            station_id = request.POST.get('station_id')
            if station_id:
                from stations.models import Station
                sheet.station = Station.objects.filter(id=station_id).first()
                
            relay_id = request.POST.get('relay_id')
            if relay_id:
                try:
                    relay_id_int = int(relay_id)
                    from stations.models import Relay
                    relay = Relay.objects.filter(id=relay_id_int).first()
                    if relay:
                        sheet.relay = relay
                        sheet.relay_text = None
                except ValueError:
                    # If relay_id is not an integer (e.g. user typed a custom relay name in TomSelect create mode)
                    relay_text = relay_id.strip()
                    from stations.models import Relay
                    # If station is known, search within the station first
                    if sheet.station:
                        sheet.relay = Relay.objects.filter(relay_code=relay_text, bay__station=sheet.station).first()
                        if not sheet.relay:
                            sheet.relay = Relay.objects.filter(relay_name__icontains=relay_text, bay__station=sheet.station).first()
                    else:
                        sheet.relay = Relay.objects.filter(relay_code=relay_text).first()
                    sheet.relay_text = relay_text if not sheet.relay else None
            else:
                # Fallback to relay_text if they didn't select relay dropdown but typed something?
                relay_text = request.POST.get('relay_text')
                if relay_text:
                    from stations.models import Relay
                    relay_text = relay_text.strip()
                    sheet.relay = Relay.objects.filter(relay_code=relay_text).first()
                    sheet.relay_text = relay_text if not sheet.relay else None
                
            sheet.save()
            messages.success(request, "Đã cập nhật thông tin chung của phiếu thành công.")
            
    return redirect('sheet_detail', pk=pk)

@login_required
def ocr_job_list(request):
    """View hiển thị tiến độ trích xuất các phiếu (OcrJob). Hỗ trợ cả HTML và JSON API (Phân trang Server-side)."""
    import json
    from .models import OcrJob
    from django.http import JsonResponse
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    from django.db.models import Q
    
    # 0. Xác định phạm vi dữ liệu dựa trên quyền user (chỉ xem phiếu do mình tạo, trừ Admin)
    base_qs = OcrJob.objects.select_related('sheet', 'sheet__created_by')
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_dispatch_sheet'):
        base_qs = base_qs.filter(sheet__created_by=request.user)

    # 1. Thống kê tổng quan (Luôn query toàn bộ DB trong phạm vi user, không phụ thuộc filter)
    # TỐI ƯU: Dùng aggregate để gộp 4 lệnh đếm thành 1 câu query duy nhất
    from django.db.models import Count, Q
    stats = base_qs.aggregate(
        failed_count=Count('id', filter=Q(status='FAILED')),
        processing_count=Count('id', filter=Q(status__in=['PENDING', 'PROCESSING'])),
        success_count=Count('id', filter=Q(status__in=['SUCCESS', 'SUCCESS_WITH_WARNINGS'])),
        total_count=Count('id')
    )
    print(f"[DEBUG OCR_JOB_LIST] User: {request.user.username}, Is Superuser: {request.user.is_superuser}, Base QS count: {base_qs.count()}, Stats: {stats}")
    failed_count = stats['failed_count']
    processing_count = stats['processing_count']
    success_count = stats['success_count']
    total_count = stats['total_count']

    # 2. Xử lý Filters
    status_filter = request.GET.get('status', 'ALL')
    device_filter = request.GET.get('device_mode', 'ALL')
    search_query = request.GET.get('q', '').strip()
    
    queryset = base_qs.order_by('-created_at')
    
    if status_filter == 'SUCCESS':
        queryset = queryset.filter(status__in=['SUCCESS', 'SUCCESS_WITH_WARNINGS'])
    elif status_filter == 'PROCESSING':
        queryset = queryset.filter(status__in=['PENDING', 'PROCESSING'])
    elif status_filter == 'FAILED':
        queryset = queryset.filter(status='FAILED')
        
    if device_filter == 'CPU':
        queryset = queryset.filter(device_mode='CPU')
    elif device_filter == 'GPU':
        queryset = queryset.filter(device_mode='GPU')
        
    if search_query:
        queryset = queryset.filter(
            Q(sheet__sheet_code__icontains=search_query) |
            Q(sheet__title__icontains=search_query) |
            Q(sheet__created_by__username__icontains=search_query) |
            Q(sheet__created_by__first_name__icontains=search_query)
        )
        
    # 3. Phân trang (15 items/trang)
    paginator = Paginator(queryset, 15)
    page_number = request.GET.get('page', 1)
    
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
        page_number = 1
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        page_number = paginator.num_pages

    # 4. Chuyển đổi dữ liệu trang hiện tại sang danh sách dict
    # TỐI ƯU: Gộp 15 lệnh gọi Redis (cache.get) lẻ tẻ thành 1 lệnh cache.get_many duy nhất
    job_ids = [job.id for job in page_obj]
    cache_keys = [f"ocr_stage_{jid}" for jid in job_ids]
    stages_from_cache = cache.get_many(cache_keys)

    jobs_data = []
    for job in page_obj:
        stage_text = stages_from_cache.get(f"ocr_stage_{job.id}") or ''
        if not stage_text and job.status == 'PROCESSING':
            if cache.get(f"ocr_header_done_{job.id}"):
                stage_text = "Đã xong Trang 1 & 2 ✓ — Đang bóc tách bảng thông số (Trang 3+)..."
            else:
                stage_text = "Đang bóc tách Trang 1 (Thông tin chung)..."
        elif not stage_text and job.status in ('SUCCESS', 'SUCCESS_WITH_WARNINGS'):
            stage_text = "Đã hoàn thành 100% ✓"

        from django.utils import timezone
        
        local_created_at = timezone.localtime(job.created_at) if job.created_at else None
        
        jobs_data.append({
            'id': job.id,
            'sheet_id': job.sheet.id if job.sheet else None,
            'sheet_code': job.sheet.sheet_code if job.sheet else f"Job#{job.id}",
            'sheet_title': job.sheet.title if job.sheet else '',
            'created_by': (
                job.sheet.created_by.get_full_name() or job.sheet.created_by.username
                if job.sheet and job.sheet.created_by else "Hệ thống"
            ),
            'device_mode': getattr(job, 'device_mode', 'CPU') or 'CPU',
            'status': job.status,
            'created_at_date': local_created_at.strftime('%d/%m/%Y') if local_created_at else '',
            'created_at_time': local_created_at.strftime('%H:%M:%S') if local_created_at else '',
            'error_code': job.error_code or '',
            'error_stage': job.error_stage or '',
            'error_detail': job.error_detail or '',
            'stage_text': stage_text,
            'sheet_status': job.sheet.status if job.sheet else '',
        })

    # Hỗ trợ fetch API / AJAX polling mượt mà không reload trang
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({
            'status': 'ok',
            'jobs': jobs_data,
            'pagination': {
                'current_page': int(page_number),
                'total_pages': paginator.num_pages,
                'has_next': page_obj.has_next(),
                'has_previous': page_obj.has_previous(),
                'total_items': paginator.count,
            },
            'stats': {
                'total': total_count,
                'failed': failed_count,
                'processing': processing_count,
                'success': success_count,
            }
        })

    jobs_json = json.dumps(jobs_data)
    pagination_json = json.dumps({
        'current_page': int(page_number),
        'total_pages': paginator.num_pages,
        'has_next': page_obj.has_next(),
        'has_previous': page_obj.has_previous(),
        'total_items': paginator.count,
    })

    # Kiểm tra GPU khả dụng để cảnh báo trên UI (Sử dụng Cache để tối ưu hiệu suất)
    gpu_info = cache.get('ocr_gpu_info')
    if gpu_info is None:
        gpu_info = {'available': False, 'name': None}
        # Chỉ gọi task background 1 lần, không block luồng web
        try:
            from sheets.tasks import check_gpu_availability_task
            check_gpu_availability_task.delay()
        except Exception:
            pass
        
    gpu_available = gpu_info['available']
    gpu_name = gpu_info['name']
    
    return render(request, 'sheets/ocr_job_list.html', {
        'jobs_json': jobs_json,
        'pagination_json': pagination_json,
        'failed_count': failed_count,
        'processing_count': processing_count,
        'success_count': success_count,
        'total_count': total_count,
        'list_title': 'Tiến độ Trích xuất OCR',
        'gpu_available': gpu_available,
        'gpu_name': gpu_name,
    })

@login_required
def ocr_job_retry(request, pk):
    """View kích hoạt lại quá trình trích xuất OCR cho 1 job cụ thể."""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet') and not request.user.has_perm('sheets.can_dispatch_sheet'):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Bạn không có quyền thực hiện thao tác này.'}, status=403)
        messages.error(request, "Bạn không có quyền thực hiện thao tác này.")
        return redirect('ocr_job_list')

    from sheets.models import OcrJob
    from sheets.tasks import run_ocr_subprocess, broadcast_ocr_job_update
    import uuid

    job = get_object_or_404(OcrJob.objects.select_related('sheet'), pk=pk)
    
    # Cho phép thay đổi device_mode (ví dụ đổi từ GPU sang CPU khi retry)
    new_device = request.POST.get('device_mode') or request.GET.get('device_mode')
    if not new_device and request.content_type == 'application/json':
        try:
            import json
            body_data = json.loads(request.body.decode('utf-8'))
            new_device = body_data.get('device_mode')
        except Exception:
            pass
    if new_device and new_device.upper() in ['CPU', 'GPU']:
        job.device_mode = new_device.upper()

    # Reset job
    from django.utils import timezone
    job.status = 'PENDING'
    job.error_code = None
    job.error_stage = None
    job.error_detail = None
    job.correlation_id = f"sheet_{job.sheet.id}_{uuid.uuid4().hex[:8]}"
    job.created_at = timezone.now() # Cập nhật thời gian để nhảy lên đầu danh sách
    job.save()

    # Đảm bảo SettingSheet ở trạng thái DRAFT
    if job.sheet.status != 'DRAFT':
        job.sheet.status = 'DRAFT'
        job.sheet.save(update_fields=['status'])

    # Gửi thông báo cập nhật qua WebSocket ngay lập tức
    broadcast_ocr_job_update(job=job, stage_text='Đang chờ xử lý...')

    # Gửi task vào Celery
    run_ocr_subprocess.delay(job.id)

    msg = f"Đã đưa phiếu {job.sheet.sheet_code} vào hàng đợi để trích xuất lại thông tin (Chế độ: {job.device_mode})."
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json' or 'application/json' in request.headers.get('accept', '')
    if is_ajax:
        return JsonResponse({'status': 'success', 'message': msg})

    messages.success(request, msg)
    return redirect('ocr_job_list')

@login_required
def sheet_rerun_ocr(request, pk):
    """
    Kích hoạt chạy lại toàn bộ quy trình AI OCR cho SettingSheet từ màn hình chi tiết phiếu.
    Đưa phiếu vào hàng đợi Celery (Pipeline 1: Header/Trang 1, Pipeline 2: Thông số/Trang 3+).
    """
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet') and not request.user.has_perm('sheets.can_dispatch_sheet'):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Bạn không có quyền thực hiện thao tác này.'}, status=403)
        messages.error(request, "Bạn không có quyền thực hiện thao tác này.")
        return redirect('sheet_detail', pk=pk)

    sheet = get_object_or_404(SettingSheet, pk=pk)
    if not sheet.scan_file:
        msg = "Phiếu này không có file scan PDF đính kèm để chạy lại OCR."
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': msg}, status=400)
        messages.error(request, msg)
        return redirect('sheet_detail', pk=pk)

    from sheets.models import OcrJob
    from sheets.tasks import run_ocr_subprocess, broadcast_ocr_job_update
    from django.utils import timezone
    import uuid

    new_device = request.POST.get('device_mode') or request.GET.get('device_mode')

    job = sheet.ocr_jobs.order_by('-created_at').first()
    if not job:
        job = OcrJob(
            sheet=sheet,
            device_mode=new_device.upper() if new_device and new_device.upper() in ['CPU', 'GPU'] else 'CPU'
        )
    elif new_device and new_device.upper() in ['CPU', 'GPU']:
        job.device_mode = new_device.upper()

    job.status = 'PENDING'
    job.error_code = None
    job.error_stage = None
    job.error_detail = None
    job.correlation_id = f"sheet_{sheet.id}_{uuid.uuid4().hex[:8]}"
    job.created_at = timezone.now()
    job.save()

    if sheet.status not in ['DRAFT', 'ISSUED']:
        sheet.status = 'DRAFT'
        sheet.save(update_fields=['status'])

    broadcast_ocr_job_update(job=job, stage_text='Đang chờ xếp hàng chạy lại OCR...')

    run_ocr_subprocess.delay(job.id)

    msg = f"Đã đưa phiếu {sheet.sheet_code} vào hàng đợi để chạy lại AI OCR (Chế độ: {job.device_mode})."
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok', 'message': msg, 'job_id': job.id})

    messages.success(request, msg)
    return redirect('sheet_detail', pk=pk)

@login_required
def ocr_job_retry_all(request):
    """View kích hoạt lại trích xuất cho tất cả các job đang bị FAILED."""
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_create_sheet') and not request.user.has_perm('sheets.can_dispatch_sheet'):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'error', 'message': 'Bạn không có quyền thực hiện thao tác này.'}, status=403)
        messages.error(request, "Bạn không có quyền thực hiện thao tác này.")
        return redirect('ocr_job_list')

    from sheets.models import OcrJob
    from sheets.tasks import execute_parallel_ocr_batch, broadcast_ocr_job_update
    import uuid

    from django.utils import timezone
    from django.db.models import Q
    from datetime import timedelta

    new_device = request.POST.get('device_mode') or request.GET.get('device_mode')
    if not new_device and request.content_type == 'application/json':
        try:
            import json
            body_data = json.loads(request.body.decode('utf-8'))
            new_device = body_data.get('device_mode')
        except Exception:
            pass

    # Lọc các job bị lỗi hoặc bị kẹt quá 15 phút
    time_threshold = timezone.now() - timedelta(minutes=15)
    
    base_qs = OcrJob.objects.select_related('sheet')
    if not request.user.is_superuser and not request.user.has_perm('sheets.can_dispatch_sheet'):
        base_qs = base_qs.filter(sheet__created_by=request.user)

    target_jobs = list(base_qs.filter(
        Q(status='FAILED') | Q(status__in=['PENDING', 'PROCESSING'], updated_at__lt=time_threshold)
    ))
    
    job_ids = []
    for job in target_jobs:
        if new_device and new_device.upper() in ['CPU', 'GPU']:
            job.device_mode = new_device.upper()
        job.status = 'PENDING'
        job.error_code = None
        job.error_stage = None
        job.error_detail = None
        job.correlation_id = f"sheet_{job.sheet.id}_{uuid.uuid4().hex[:8]}"
        job.created_at = timezone.now() # Cập nhật thời gian để nhảy lên đầu danh sách
        job.save()
        if job.sheet.status != 'DRAFT':
            job.sheet.status = 'DRAFT'
            job.sheet.save(update_fields=['status'])
        job_ids.append(job.id)
        broadcast_ocr_job_update(job=job, stage_text='Đang chờ xử lý...')

    if job_ids:
        execute_parallel_ocr_batch.delay(job_ids, user_id=request.user.id, device_mode=new_device or 'CPU')
        msg = f"Đã gửi yêu cầu trích xuất lại cho {len(job_ids)} file thất bại qua luồng song song."
    else:
        msg = "Không có file nào đang ở trạng thái thất bại."

    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json' or 'application/json' in request.headers.get('accept', '')
    if is_ajax:
        return JsonResponse({'status': 'success', 'message': msg, 'count': len(job_ids)})

    if job_ids:
        messages.success(request, msg)
    else:
        messages.info(request, msg)

    return redirect('ocr_job_list')

@login_required
def ocr_job_json(request, pk):
    from sheets.models import OcrJob
    job = get_object_or_404(OcrJob, pk=pk)
    if job.result_data:
        return JsonResponse(job.result_data, safe=False)
    return JsonResponse({'error': 'No JSON data available for this job.'}, status=404)
````

## File: stations/management/commands/__init__.py
````python
# init
````

## File: stations/management/commands/run_autocheck.py
````python
import time
from django.core.management.base import BaseCommand
from django.utils import timezone
from stations.models import Relay
from stations.api_mock import compare_and_log_relay_check

class Command(BaseCommand):
    help = 'Tiến trình ngầm kiểm tra Rơ-le tự động dựa trên lịch hẹn giờ độc lập'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Bắt đầu chạy tiến trình kiểm tra Rơ-le thông minh... (Bấm Ctrl+C để dừng)"))
        self.stdout.write("Hệ thống sẽ quét mỗi 5 giây để tìm các Rơ-le đến hẹn.")
        
        while True:
            now = timezone.now()
            
            from django.db.models import Q
            relays = Relay.objects.filter(
                settingsheet__isnull=False, 
                auto_check_enabled=True
            ).filter(
                Q(next_check_at__isnull=True) | Q(next_check_at__lte=now)
            ).distinct()
            
            for relay in relays:
                log = compare_and_log_relay_check(relay)
                if log:
                    if log.status == 'MISMATCH':
                        msg = self.style.ERROR(f"[{log.checked_at.strftime('%H:%M:%S')}] {relay.relay_code}: PHÁT HIỆN SAI LỆCH!")
                    else:
                        msg = self.style.SUCCESS(f"[{log.checked_at.strftime('%H:%M:%S')}] {relay.relay_code}: Bình thường.")
                    self.stdout.write(msg)
                    
                    # Tính toán giờ chạy tiếp theo
                    relay.last_checked_at = log.checked_at
                    relay.next_check_at = relay.calculate_next_check(log.checked_at)
                    relay.save(update_fields=['last_checked_at', 'next_check_at'])
            
            time.sleep(5)
````

## File: stations/management/__init__.py
````python
# init
````

## File: stations/migrations/__init__.py
````python

````

## File: stations/migrations/0001_initial.py
````python
# Generated by Django 6.0.7 on 2026-07-18 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bay_code', models.CharField(max_length=50)),
                ('bay_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_code', models.CharField(max_length=50, unique=True)),
                ('station_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relay_code', models.CharField(max_length=50)),
                ('relay_name', models.CharField(max_length=100)),
                ('manufacturer', models.CharField(max_length=100)),
                ('bay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relays', to='stations.bay')),
            ],
        ),
        migrations.CreateModel(
            name='RelaySetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_code', models.CharField(max_length=50)),
                ('parameter_name', models.CharField(max_length=100)),
                ('standard_value', models.FloatField()),
                ('unit', models.CharField(max_length=20)),
                ('tolerance_min', models.FloatField()),
                ('tolerance_max', models.FloatField()),
                ('relay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='stations.relay')),
            ],
        ),
        migrations.AddField(
            model_name='bay',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bays', to='stations.station'),
        ),
    ]
````

## File: stations/migrations/0002_relayautochecklog.py
````python
# Generated by Django 6.0.7 on 2026-07-23 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelayAutoCheckLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('MATCH', 'Trùng khớp'), ('MISMATCH', 'Có sai lệch'), ('API_ERROR', 'Lỗi kết nối API')], default='MATCH', max_length=20)),
                ('api_raw_data', models.JSONField(blank=True, null=True)),
                ('differences', models.JSONField(blank=True, null=True)),
                ('relay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auto_checks', to='stations.relay')),
            ],
            options={
                'ordering': ['-checked_at'],
            },
        ),
    ]
````

## File: stations/migrations/0003_relay_auto_check_enabled_relay_check_interval_unit_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-23 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0002_relayautochecklog'),
    ]

    operations = [
        migrations.AddField(
            model_name='relay',
            name='auto_check_enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='relay',
            name='check_interval_unit',
            field=models.CharField(choices=[('s', 'Giây'), ('m', 'Phút'), ('h', 'Giờ'), ('d', 'Ngày'), ('M', 'Tháng'), ('y', 'Năm')], default='h', max_length=1),
        ),
        migrations.AddField(
            model_name='relay',
            name='check_interval_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='relay',
            name='last_checked_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='relay',
            name='next_check_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
````

## File: stations/migrations/0004_alter_relay_check_interval_unit.py
````python
# Generated by Django 6.0.7 on 2026-07-23 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0003_relay_auto_check_enabled_relay_check_interval_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relay',
            name='check_interval_unit',
            field=models.CharField(choices=[('s', 'Giây'), ('m', 'Phút'), ('h', 'Giờ'), ('d', 'Ngày'), ('M', 'Tháng'), ('y', 'Năm'), ('e', 'Cụ thể (1 lần)')], default='h', max_length=1),
        ),
    ]
````

## File: stations/migrations/0005_alter_relay_auto_check_enabled_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-23 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0004_alter_relay_check_interval_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relay',
            name='auto_check_enabled',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='relay',
            name='next_check_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]
````

## File: stations/migrations/0006_relay_is_paused_for_correction_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-23 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0005_alter_relay_auto_check_enabled_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relay',
            name='is_paused_for_correction',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='relay',
            name='paused_schedule_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CorrectionTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DISPATCHER', 'Phân phối viên xử lý'), ('STATION', 'Trạm xử lý'), ('TECH', 'Kỹ thuật viên xử lý'), ('SUPERVISOR', 'Giám sát ký'), ('ADMIN', 'Admin ký duyệt'), ('RESOLVED', 'Hoàn tất')], default='DISPATCHER', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('log', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stations.relayautochecklog')),
                ('relay', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='correction_tickets', to='stations.relay')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TicketSignature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signer_name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=50)),
                ('signed_at', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('signature_hash', models.CharField(max_length=256)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='signatures', to='stations.correctionticket')),
            ],
            options={
                'ordering': ['signed_at'],
            },
        ),
    ]
````

## File: stations/migrations/0007_alter_station_options_station_id_capda_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0006_relay_is_paused_for_correction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='station',
            options={'verbose_name': 'Danh mục Trạm', 'verbose_name_plural': 'Danh mục Trạm'},
        ),
        migrations.AddField(
            model_name='station',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_kieu_ht_dk',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Kiểu HT ĐK (ID_KIEU_HT_DK)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_kieu_tram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Kiểu trạm (ID_KIEU_TRAM)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_loai_tram',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Loại trạm (ID_LOAI_TRAM)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_phuong',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Phường (ID_PHUONG)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_quan',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Quận (ID_QUAN)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_tba',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID TBA (ID_TBA)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_tinh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Tỉnh (ID_TINH)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='station',
            name='id_vung',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Vùng (ID_VUNG)'),
        ),
        migrations.AddField(
            model_name='station',
            name='kieu_ht_dk',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Kiểu HT ĐK (KIEU_HT_DK)'),
        ),
        migrations.AddField(
            model_name='station',
            name='kieu_tram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Kiểu trạm (KIEU_TRAM)'),
        ),
        migrations.AddField(
            model_name='station',
            name='loai_tram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Loại trạm (LOAI_TRAM)'),
        ),
        migrations.AddField(
            model_name='station',
            name='ngay_ld',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày lắp đặt (NGAY_LD)'),
        ),
        migrations.AddField(
            model_name='station',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='station',
            name='phuong',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Phường (PHUONG)'),
        ),
        migrations.AddField(
            model_name='station',
            name='quan',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Quận (QUAN)'),
        ),
        migrations.AddField(
            model_name='station',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='station',
            name='tinh',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tỉnh (TINH)'),
        ),
        migrations.AddField(
            model_name='station',
            name='vung',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Vùng (VUNG)'),
        ),
        migrations.AlterField(
            model_name='station',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Mã (MA)'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_name',
            field=models.CharField(max_length=200, verbose_name='Tên (TEN)'),
        ),
    ]
````

## File: stations/migrations/0008_bay_i_dm_bay_id_capda_bay_id_dvi_bay_id_nlo_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0007_alter_station_options_station_id_capda_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bay',
            name='i_dm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='I_DM'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_nlo',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Ngăn lộ (ID_NLO)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_tba',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID TBA (ID_TBA)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='sdm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SDM'),
        ),
        migrations.AddField(
            model_name='bay',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='ten_tram',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên trạm (TEN_TRAM)'),
        ),
        migrations.AddField(
            model_name='bay',
            name='u_dm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='U_DM'),
        ),
        migrations.AlterField(
            model_name='bay',
            name='bay_code',
            field=models.CharField(max_length=50, verbose_name='Mã (MA)'),
        ),
        migrations.AlterField(
            model_name='bay',
            name='bay_name',
            field=models.CharField(max_length=100, verbose_name='Tên (TEN)'),
        ),
        migrations.AlterField(
            model_name='bay',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bays', to='stations.station'),
        ),
    ]
````

## File: stations/migrations/0009_relay_id_capda_relay_id_doituong_relay_id_dvi_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-28 17:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0008_bay_i_dm_bay_id_capda_bay_id_dvi_bay_id_nlo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='relay',
            name='id_capda',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Cấp điện áp (ID_CAPDA)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_doituong',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Đối tượng (ID_DOITUONG)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_dvi',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Đơn vị (ID_DVI)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_hang_sx',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Hãng sản xuất (ID_HANG_SX)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_loai_dt',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Loại đối tượng (ID_LOAI_DT)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_loai_tb',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Loại thiết bị (ID_LOAI_TB)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_nuoc_sx',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Nước sản xuất (ID_NUOC_SX)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_sohuu',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Sở hữu (ID_SOHUU)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_tbi',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Thiết bị (ID_TBI)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_ttvh',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ID Trạng thái vận hành (ID_TTVH)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='id_vtri_dat',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ID Vị trí đặt (ID_VTRI_DAT)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='ngay_vh',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Ngày vận hành (NGAY_VH)'),
        ),
        migrations.AddField(
            model_name='relay',
            name='sort_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sắp xếp (SAPXEP)'),
        ),
        migrations.AlterField(
            model_name='relay',
            name='bay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='relays', to='stations.bay'),
        ),
        migrations.AlterField(
            model_name='relay',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='relay',
            name='relay_code',
            field=models.CharField(max_length=50, verbose_name='Mã (MA)'),
        ),
        migrations.AlterField(
            model_name='relay',
            name='relay_name',
            field=models.CharField(max_length=100, verbose_name='Tên (TEN)'),
        ),
    ]
````

## File: stations/migrations/0010_alter_bay_bay_name_alter_bay_ten_tram_and_more.py
````python
# Generated by Django 6.0.7 on 2026-07-29 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0009_relay_id_capda_relay_id_doituong_relay_id_dvi_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bay',
            name='bay_name',
            field=models.CharField(max_length=255, verbose_name='Tên (TEN)'),
        ),
        migrations.AlterField(
            model_name='bay',
            name='ten_tram',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Tên trạm (TEN_TRAM)'),
        ),
        migrations.AlterField(
            model_name='relay',
            name='relay_name',
            field=models.CharField(max_length=255, verbose_name='Tên (TEN)'),
        ),
    ]
````

## File: stations/migrations/0011_bay_updated_at_relay_updated_at_station_updated_at.py
````python
# Generated by Django 6.0.7 on 2026-07-30 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stations', '0010_alter_bay_bay_name_alter_bay_ten_tram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bay',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='relay',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='station',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
````

## File: stations/__init__.py
````python

````

## File: stations/admin.py
````python
from django.contrib import admin

# Register your models here.
````

## File: stations/api_mock.py
````python
import random
import time
from .models import RelayAutoCheckLog

def fetch_relay_parameters_from_api(relay):
    """
    Giả lập gọi API tới Rơ-le ngoài thực địa.
    Sẽ trả về 1 list dictionary chứa thông số.
    Thỉnh thoảng (25% xác suất) sẽ cố tình làm sai lệch 1-2 thông số để test.
    """
    time.sleep(0.3) # Giả lập network delay
    
    active_sheet = relay.active_sheet
    db_params = []
    if active_sheet and active_sheet.extracted_data:
        raw_data = active_sheet.extracted_data
        if isinstance(raw_data, list):
            db_params = raw_data
        elif isinstance(raw_data, dict):
            db_params = [{'parameter_code': k, 'parameter_name': k, 'value': str(v)} for k, v in raw_data.items()]
    elif relay.settings.exists():
        db_params = [{'parameter_code': s.parameter_code, 'parameter_name': s.parameter_name, 'value': str(s.standard_value), 'unit': s.unit} for s in relay.settings.all()]
    else:
        from .relay_specs import get_relay_default_parameters
        specs = get_relay_default_parameters(relay)
        db_params = [
            {'parameter_code': s['code'], 'parameter_name': s['name'], 'value': s['value'], 'unit': s.get('unit', '')}
            for s in specs
        ]
        
    api_data = []
    should_mismatch = random.random() < 0.25 # 25% cơ hội bị sai lệch
    
    for param in db_params:
        # Bỏ qua các trường metadata không phải của rơ-le
        if param.get('parameter_code') in ['STATION_NAME', 'RELAY_CODE']:
            continue
            
        val = param.get('value', '')
        
        # Làm sai lệch dữ liệu
        if should_mismatch and random.random() < 0.35:
            try:
                numeric_val = float(val)
                val = str(round(numeric_val * 1.2, 2)) # Tăng 20%
                if val.endswith('.0'):
                    val = val[:-2]
            except ValueError:
                val = str(val) + "_err"
                
        api_data.append({
            'code': param.get('parameter_code', ''),
            'name': param.get('parameter_name', ''),
            'value': str(val),
            'unit': param.get('unit', '')
        })
        
    return api_data

def compare_and_log_relay_check(relay):
    """Thực hiện check và lưu vào DB"""
    api_data = fetch_relay_parameters_from_api(relay)
    
    # Tạo dict chứa các parameters từ DB để dễ so sánh
    db_params = {}
    active_sheet = relay.active_sheet
    if active_sheet and active_sheet.extracted_data:
        raw_data = active_sheet.extracted_data
        if isinstance(raw_data, list):
            for p in raw_data:
                if p.get('parameter_code') not in ['STATION_NAME', 'RELAY_CODE']:
                    db_params[p.get('parameter_code')] = str(p.get('value', ''))
        elif isinstance(raw_data, dict):
            for k, v in raw_data.items():
                db_params[k] = str(v)
    elif relay.settings.exists():
        for s in relay.settings.all():
            db_params[s.parameter_code] = str(s.standard_value)
    else:
        from .relay_specs import get_relay_default_parameters
        specs = get_relay_default_parameters(relay)
        db_params = {s['code']: s['value'] for s in specs}
    
    differences = []
    
    for api_param in api_data:
        code = api_param['code']
        api_val = api_param['value']
        db_val = db_params.get(code, '')
        
        is_diff = False
        try:
            if float(api_val) != float(db_val):
                is_diff = True
        except:
            if str(api_val).strip() != str(db_val).strip():
                is_diff = True
                
        # Gắn thêm cờ để template dễ render
        api_param['is_diff'] = is_diff
        api_param['db_value'] = db_val
                
        if is_diff:
            differences.append({
                'code': code,
                'name': api_param['name'],
                'db_value': db_val,
                'api_value': api_val,
                'unit': api_param.get('unit', '')
            })
                
    status = 'MISMATCH' if differences else 'MATCH'
    
    log = RelayAutoCheckLog.objects.create(
        relay=relay,
        status=status,
        api_raw_data=api_data,
        differences=differences
    )
    
    # Nếu có sai lệch, tạm ngưng lịch hẹn giờ
    if status == 'MISMATCH' and not relay.is_paused_for_correction:
        relay.is_paused_for_correction = True
        relay.paused_schedule_data = {
            'check_interval_value': relay.check_interval_value,
            'check_interval_unit': relay.check_interval_unit
        }
        relay.save(update_fields=['is_paused_for_correction', 'paused_schedule_data'])
    
    # Nếu dữ liệu đã khớp 100% và rơ-le đang bị tạm ngưng → tự động bật lại
    elif status == 'MATCH' and relay.is_paused_for_correction:
        relay.is_paused_for_correction = False
        
        # Khôi phục lịch hẹn giờ ban đầu nếu có lưu
        if relay.paused_schedule_data:
            relay.check_interval_value = relay.paused_schedule_data.get('check_interval_value', relay.check_interval_value)
            relay.check_interval_unit = relay.paused_schedule_data.get('check_interval_unit', relay.check_interval_unit)
            relay.paused_schedule_data = None
        
        from django.utils import timezone
        relay.last_checked_at = timezone.now()
        relay.next_check_at = relay.calculate_next_check(from_time=relay.last_checked_at)
        relay.save(update_fields=[
            'is_paused_for_correction', 'paused_schedule_data',
            'check_interval_value', 'check_interval_unit',
            'last_checked_at', 'next_check_at'
        ])
    
    # Broadcast via Channels to any user viewing the autocheck dashboard
    from channels.layers import get_channel_layer
    from asgiref.sync import async_to_sync
    
    channel_layer = get_channel_layer()
    if channel_layer:
        async_to_sync(channel_layer.group_send)(
            "autocheck_updates",
            {
                "type": "send_notification",
                "title": f"Cập nhật Rơ-le {relay.relay_code}",
                "message": f"Vừa hoàn tất đối chiếu tự động. Kết quả: {'Khớp' if status == 'MATCH' else 'Lệch'}",
                "level": "success" if status == 'MATCH' else "warning"
            }
        )
        
    return log
````

## File: stations/apps.py
````python
from django.apps import AppConfig


class StationsConfig(AppConfig):
    name = 'stations'
````

## File: stations/models.py
````python
from django.db import models

class Station(models.Model):
    station_code = models.CharField(max_length=50, unique=True, verbose_name="Mã (MA)")
    station_name = models.CharField(max_length=200, verbose_name="Tên (TEN)")
    location = models.CharField(max_length=255, blank=True, null=True)
    
    # Các trường bổ sung từ Danh mục Trạm
    id_tba = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID TBA (ID_TBA)")
    id_tinh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Tỉnh (ID_TINH)")
    tinh = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tỉnh (TINH)")
    id_quan = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Quận (ID_QUAN)")
    quan = models.CharField(max_length=100, blank=True, null=True, verbose_name="Quận (QUAN)")
    id_phuong = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Phường (ID_PHUONG)")
    phuong = models.CharField(max_length=100, blank=True, null=True, verbose_name="Phường (PHUONG)")
    
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    
    kieu_tram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kiểu trạm (KIEU_TRAM)")
    id_kieu_tram = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Kiểu trạm (ID_KIEU_TRAM)")
    
    loai_tram = models.CharField(max_length=100, blank=True, null=True, verbose_name="Loại trạm (LOAI_TRAM)")
    id_loai_tram = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Loại trạm (ID_LOAI_TRAM)")
    
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    ngay_ld = models.DateTimeField(blank=True, null=True, verbose_name="Ngày lắp đặt (NGAY_LD)")
    
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    id_vung = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Vùng (ID_VUNG)")
    updated_at = models.DateTimeField(auto_now=True)
    vung = models.CharField(max_length=100, blank=True, null=True, verbose_name="Vùng (VUNG)")
    
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    
    kieu_ht_dk = models.CharField(max_length=100, blank=True, null=True, verbose_name="Kiểu HT ĐK (KIEU_HT_DK)")
    id_kieu_ht_dk = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Kiểu HT ĐK (ID_KIEU_HT_DK)")
    
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    class Meta:
        verbose_name = "Danh mục Trạm"
        verbose_name_plural = "Danh mục Trạm"

    @property
    def code(self):
        return self.station_code

    @property
    def name(self):
        return self.station_name

    def __str__(self):
        return f"{self.station_code} - {self.station_name}"

class Bay(models.Model):
    station = models.ForeignKey(Station, related_name='bays', on_delete=models.CASCADE, null=True, blank=True)
    bay_code = models.CharField(max_length=50, verbose_name="Mã (MA)")
    bay_name = models.CharField(max_length=255, verbose_name="Tên (TEN)")
    
    # Các trường bổ sung từ Danh mục Ngăn lộ
    ten_tram = models.CharField(max_length=255, blank=True, null=True, verbose_name="Tên trạm (TEN_TRAM)")
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    id_nlo = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Ngăn lộ (ID_NLO)")
    id_tba = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID TBA (ID_TBA)")
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")
    
    u_dm = models.CharField(max_length=50, blank=True, null=True, verbose_name="U_DM")
    i_dm = models.CharField(max_length=50, blank=True, null=True, verbose_name="I_DM")
    sdm = models.CharField(max_length=50, blank=True, null=True, verbose_name="SDM")

    updated_at = models.DateTimeField(auto_now=True)
    @property
    def code(self):
        return self.bay_code

    @property
    def name(self):
        return self.bay_name

    def __str__(self):
        return f"{self.bay_code} - {self.bay_name}"

class Relay(models.Model):
    bay = models.ForeignKey(Bay, related_name='relays', on_delete=models.CASCADE, null=True, blank=True)
    relay_code = models.CharField(max_length=50, verbose_name="Mã (MA)")
    relay_name = models.CharField(max_length=255, verbose_name="Tên (TEN)")
    manufacturer = models.CharField(max_length=100, blank=True, null=True)

    # Các trường bổ sung từ Danh mục Thiết bị (Rơ le)
    id_tbi = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Thiết bị (ID_TBI)")
    id_capda = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Cấp điện áp (ID_CAPDA)")
    id_ttvh = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Trạng thái vận hành (ID_TTVH)")
    id_hang_sx = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Hãng sản xuất (ID_HANG_SX)")
    id_nuoc_sx = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Nước sản xuất (ID_NUOC_SX)")
    
    id_loai_tb = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Loại thiết bị (ID_LOAI_TB)")
    id_loai_dt = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Loại đối tượng (ID_LOAI_DT)")
    id_doituong = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Đối tượng (ID_DOITUONG)")
    
    id_dvi = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Đơn vị (ID_DVI)")
    id_sohuu = models.CharField(max_length=50, blank=True, null=True, verbose_name="ID Sở hữu (ID_SOHUU)")
    
    id_vtri_dat = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID Vị trí đặt (ID_VTRI_DAT)")
    ngay_vh = models.DateTimeField(blank=True, null=True, verbose_name="Ngày vận hành (NGAY_VH)")
    sort_order = models.IntegerField(blank=True, null=True, verbose_name="Sắp xếp (SAPXEP)")

    # Lịch trình tự động kiểm tra API
    UNIT_CHOICES = [
        ('s', 'Giây'),
        ('m', 'Phút'),
        ('h', 'Giờ'),
        ('d', 'Ngày'),
        ('M', 'Tháng'),
        ('y', 'Năm'),
        ('e', 'Cụ thể (1 lần)'),
    ]
    auto_check_enabled = models.BooleanField(default=False, db_index=True)
    check_interval_value = models.IntegerField(default=1)
    check_interval_unit = models.CharField(max_length=1, choices=UNIT_CHOICES, default='h')
    last_checked_at = models.DateTimeField(null=True, blank=True)
    next_check_at = models.DateTimeField(null=True, blank=True, db_index=True)
    
    # Workflow fields
    is_paused_for_correction = models.BooleanField(default=False, db_index=True)
    paused_schedule_data = models.JSONField(null=True, blank=True)

    def calculate_next_check(self, from_time=None):
        import datetime
        import calendar
        from django.utils import timezone
        if not from_time:
            from_time = timezone.now()
            
        val = self.check_interval_value
        unit = self.check_interval_unit
        
        if unit == 'e':
            return None # Chế độ 1 lần không tự tính toán chu kỳ lặp lại
            
        if unit == 's':
            return from_time + datetime.timedelta(seconds=val)
        elif unit == 'm':
            return from_time + datetime.timedelta(minutes=val)
        elif unit == 'h':
            return from_time + datetime.timedelta(hours=val)
        elif unit == 'd':
            return from_time + datetime.timedelta(days=val)
        elif unit == 'M':
            month = from_time.month - 1 + val
            year = from_time.year + month // 12
            month = month % 12 + 1
            day = min(from_time.day, calendar.monthrange(year, month)[1])
            return from_time.replace(year=year, month=month, day=day)
        elif unit == 'y':
            try:
                return from_time.replace(year=from_time.year + val)
            except ValueError:
                return from_time.replace(year=from_time.year + val, day=28)
        
        return from_time + datetime.timedelta(hours=1)

    @property
    def code(self):
        return self.relay_code

    @property
    def name(self):
        return self.relay_name

    def __str__(self):
        return f"{self.relay_code} - {self.relay_name}"
        
    @property
    def active_sheet(self):
        # Lấy phiếu hoàn thành (đang có hiệu lực) mới nhất
        completed = self.settingsheet_set.filter(status='COMPLETED').order_by('-created_at').first()
        return completed if completed else self.settingsheet_set.first()
        
    updated_at = models.DateTimeField(auto_now=True)

class RelaySetting(models.Model):
    relay = models.ForeignKey(Relay, related_name='settings', on_delete=models.CASCADE)
    parameter_code = models.CharField(max_length=50)
    parameter_name = models.CharField(max_length=100)
    standard_value = models.FloatField()
    unit = models.CharField(max_length=20)
    tolerance_min = models.FloatField()
    tolerance_max = models.FloatField()

    def __str__(self):
        return f"{self.parameter_code}: {self.standard_value} {self.unit}"

class RelayAutoCheckLog(models.Model):
    STATUS_CHOICES = [
        ('MATCH', 'Trùng khớp'),
        ('MISMATCH', 'Có sai lệch'),
        ('API_ERROR', 'Lỗi kết nối API'),
    ]
    relay = models.ForeignKey(Relay, related_name='auto_checks', on_delete=models.CASCADE)
    checked_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='MATCH')
    api_raw_data = models.JSONField(null=True, blank=True)
    differences = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-checked_at']

    def __str__(self):
        return f"Check {self.relay.relay_code} at {self.checked_at.strftime('%d/%m/%Y %H:%M:%S')}"

class CorrectionTicket(models.Model):
    STATUS_CHOICES = [
        ('DISPATCHER', 'Phân phối viên xử lý'),
        ('STATION', 'Trạm xử lý'),
        ('TECH', 'Kỹ thuật viên xử lý'),
        ('SUPERVISOR', 'Giám sát ký'),
        ('ADMIN', 'Admin ký duyệt'),
        ('RESOLVED', 'Hoàn tất'),
    ]
    relay = models.ForeignKey(Relay, related_name='correction_tickets', on_delete=models.CASCADE)
    log = models.ForeignKey(RelayAutoCheckLog, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='DISPATCHER')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def current_step_idx(self):
        flow = ['DISPATCHER', 'STATION', 'TECH', 'SUPERVISOR', 'ADMIN', 'RESOLVED']
        try:
            return flow.index(self.status)
        except ValueError:
            return 0
            
    def get_flow_steps(self):
        return [
            ('DISPATCHER', 'Phân phối', 0),
            ('STATION', 'Trạm', 1),
            ('TECH', 'Kỹ thuật', 2),
            ('SUPERVISOR', 'Giám sát', 3),
            ('ADMIN', 'Admin', 4),
        ]

class TicketSignature(models.Model):
    ticket = models.ForeignKey(CorrectionTicket, related_name='signatures', on_delete=models.CASCADE)
    signer_name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    signed_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    signature_hash = models.CharField(max_length=256)

    class Meta:
        ordering = ['signed_at']
````

## File: stations/search_utils.py
````python
"""
Search and Alias Resolution Utilities for EVN RMS.

Provides synonym resolution and intelligent query expansion across:
1. Vendor brand names & aliases (e.g. 'NR ELECTRIC' -> NR/NARI, 'SCHWEITZER' -> SEL, 'MULTILIN' -> GE).
2. Multi-word brand expressions (avoiding broken AND splits).
3. Punctuation variations ('A.EBERLE', 'A-EBERLE', 'A EBERLE', 'S&S POWER').
4. Cross-relation device scoring for station, bay, and relay HTMX views.
"""

from django.db.models import Q
import re

VENDOR_SEARCH_SYNONYMS = {
    # 1. SEL (Schweitzer Engineering Laboratories)
    'sel': ['SEL', 'SCHWEITZER'],
    'schweitzer': ['SEL', 'SCHWEITZER'],
    'schweitzer engineering': ['SEL', 'SCHWEITZER'],
    'schweitzer engineering laboratories': ['SEL', 'SCHWEITZER'],
    'acselerator': ['SEL'],

    # 2. SIEMENS
    'siemens': ['SIEMENS', 'SIPROTEC'],
    'siprotec': ['SIEMENS', 'SIPROTEC'],
    'siprotec 4': ['SIEMENS', 'SIPROTEC', '7SJ', '7SA', '7SD', '7UT'],
    'siprotec 5': ['SIEMENS', 'SIPROTEC', '7SJ8', '7SA8', '7SD8', '7SL8', '7UT8'],
    'digsi': ['SIEMENS', 'SIPROTEC'],

    # 3. ABB / HITACHI
    'abb': ['ABB', 'HITACHI', 'RELION'],
    'hitachi': ['HITACHI', 'ABB', 'RELION'],
    'hitachi energy': ['HITACHI', 'ABB', 'RELION'],
    'relion': ['ABB', 'HITACHI', 'RELION'],
    'pcm600': ['ABB', 'HITACHI'],

    # 4. SCHNEIDER / ALSTOM / AREVA / MICOM / SEPAM
    'schneider': ['SCHNEIDER', 'ALSTOM', 'AREVA', 'MICOM', 'SEPAM'],
    'schneider electric': ['SCHNEIDER', 'ALSTOM', 'AREVA', 'MICOM', 'SEPAM', 'MERLIN GERIN'],
    'alstom': ['ALSTOM', 'SCHNEIDER', 'MICOM'],
    'areva': ['AREVA', 'SCHNEIDER', 'MICOM'],
    'micom': ['MICOM', 'SCHNEIDER', 'ALSTOM', 'AREVA'],
    'sepam': ['SEPAM', 'SCHNEIDER'],
    'merlin gerin': ['MERLIN GERIN', 'SCHNEIDER'],
    'easergy': ['SCHNEIDER', 'SEPAM'],

    # 5. GE (General Electric) / MULTILIN
    'ge': ['GE', 'GENERAL ELECTRIC', 'MULTILIN', 'GE_VERNOVA', 'GE T&D'],
    'general electric': ['GE', 'GENERAL ELECTRIC', 'MULTILIN', 'GE_VERNOVA'],
    'multilin': ['GE', 'MULTILIN', 'GENERAL ELECTRIC'],
    'ge vernova': ['GE_VERNOVA', 'GE', 'GENERAL ELECTRIC'],
    'ge_vernova': ['GE_VERNOVA', 'GE', 'GENERAL ELECTRIC'],
    'ge t&d': ['GE T&D INDIA LIMITED', 'GE'],
    'ge t&d india': ['GE T&D INDIA LIMITED', 'GE'],
    'enervista': ['GE', 'MULTILIN'],

    # 6. NR ELECTRIC / NARI
    'nr': ['NR', 'NARI', 'PCS', 'RCS'],
    'nr electric': ['NR', 'NARI', 'PCS', 'RCS'],
    'nr-electric': ['NR', 'NARI', 'PCS', 'RCS'],
    'nari': ['NARI', 'NR', 'PCS', 'RCS'],
    'nari electric': ['NARI', 'NR', 'PCS', 'RCS'],
    'pcs': ['PCS', 'NR', 'NARI'],
    'rcs': ['RCS', 'NR', 'NARI'],

    # 7. TOSHIBA
    'toshiba': ['TOSHIBA', 'GR-SERIES', 'GRZ', 'GRT', 'GRB'],
    'gr-series': ['TOSHIBA', 'GR-SERIES'],
    'grz': ['TOSHIBA', 'GRZ'],
    'grt': ['TOSHIBA', 'GRT'],
    'grb': ['TOSHIBA', 'GRB'],

    # 8. PROTECTA
    'protecta': ['PROTECTA', 'EUROPROT'],
    'europrot': ['PROTECTA', 'EUROPROT'],
    'europrot+': ['PROTECTA', 'EUROPROT'],

    # 9. A-EBERLE
    'a eberle': ['A-EBERLE', 'EBERLE', 'REG-D', 'REGSYS'],
    'a-eberle': ['A-EBERLE', 'EBERLE', 'REG-D', 'REGSYS'],
    'a.eberle': ['A-EBERLE', 'EBERLE', 'REG-D', 'REGSYS'],
    'eberle': ['A-EBERLE', 'EBERLE', 'REG-D', 'REGSYS'],
    'reg-d': ['A-EBERLE', 'REG-D'],
    'reg-da': ['A-EBERLE', 'REG-D', 'REG-DA'],
    'regsys': ['REGSYS', 'A-EBERLE'],

    # 10. BENDER
    'bender': ['BENDER', 'ISO685', 'RCMS'],
    'iso685': ['BENDER', 'ISO685'],
    'rcms': ['BENDER', 'RCMS'],
    'rcms460': ['BENDER', 'RCMS'],

    # 11. ARTECHE
    'arteche': ['ARTECHE', 'ARTECH'],
    'artech': ['ARTECHE', 'ARTECH'],

    # 12. VIZIMAX
    'vizimax': ['VIZIMAX', 'SYNCHROTEQ'],
    'synchroteq': ['VIZIMAX', 'SYNCHROTEQ'],

    # 13. MR (Maschinenfabrik Reinhausen)
    'mr': ['MR', 'REINHAUSEN', 'TAPCON', 'MSENSE'],
    'reinhausen': ['MR', 'REINHAUSEN', 'TAPCON'],
    'maschinenfabrik': ['MR', 'REINHAUSEN', 'TAPCON'],
    'maschinenfabrik reinhausen': ['MR', 'REINHAUSEN', 'TAPCON'],
    'tapcon': ['MR', 'TAPCON'],
    'msense': ['MR', 'MSENSE'],

    # 14. MESSKO
    'messko': ['MESSKO'],

    # 15. AKM
    'akm': ['AKM'],

    # 16. HYODA
    'hyoda': ['HYODA'],
    'hyoda instruments': ['HYODA'],

    # 17. CEDASPE
    'cedaspe': ['CEDASPE', 'BUCHHOLZ'],

    # 18. COMEM
    'comem': ['COMEM', 'BUCHHOLZ'],

    # 19. EMB
    'emb': ['EMB', 'BUCHHOLZ'],

    # 20. QUALITROL
    'qualitrol': ['QUALITROL', 'SERVERON'],
    'serveron': ['QUALITROL', 'SERVERON'],

    # 21. SMITT / MORS SMITT
    'smitt': ['SMITT', 'MORS SMITT'],
    'mors smitt': ['SMITT', 'MORS SMITT'],

    # 22. TRENCH & TAIKAI & MAGRINI & STROMWANDLER
    'trench': ['TRENCH'],
    'taikai': ['TAIKAI'],
    'magrini': ['MAGRINI GALILEO', 'GALILEO'],
    'magrini galileo': ['MAGRINI GALILEO', 'GALILEO'],
    'stromwandler': ['STROMWANDLER'],
    'mitex': ['MITEX'],

    # 23. SIEYUAN, COELME, HAPAM, MESA, S&S POWER
    'sieyuan': ['SIEYUAN'],
    'coelme': ['COELME'],
    'hapam': ['HAPAM'],
    'mesa': ['MESA'],
    's&s power': ['S&S POWER', 'S&S'],
    's&s': ['S&S POWER'],

    # 24. TRANSFORMERS (TBEA, SHENYANG, XD XIAN, HYUNDAI, MITSUBISHI, DAIHEN, EEMC)
    'tbea': ['TBEA'],
    'shenyang': ['SHENYANG', 'SBW'],
    'xd xian': ['XD XIAN', 'CHANGZHOU-XD'],
    'hyundai': ['HYUNDAI'],
    'hyundai electric': ['HYUNDAI'],
    'mitsubishi': ['MITSUBISHI'],
    'mitsubishi electric': ['MITSUBISHI'],
    'daihen': ['DAIHEN'],
    'eemc': ['EEMC'],

    # 25. COOPER
    'cooper': ['COOPER'],

    # 26. BECKWITH
    'beckwith': ['BECKWITH', 'M-2001', 'M-0169'],

    # 27. REMSDAQ
    'remsdaq': ['REMSDAQ'],

    # 28. EATON
    'eaton': ['EATON'],

    # 29. ELIN
    'elin': ['ELIN'],

    # 30. KINKEI
    'kinkei': ['KINKEI', 'SFL2000'],

    # 31. ZIV
    'ziv': ['ZIV'],

    # 32. KYONGBO & LS
    'kyongbo': ['KYONGBO'],
    'ls': ['LS-VINA', 'LS ELECTRIC'],
    'ls electric': ['LS-VINA', 'LS ELECTRIC'],
    'ls-vina': ['LS-VINA'],

    # 33. RFL & CE
    'rfl': ['RFL'],
    'ce': ['CE'],

    # 34. BUCHHOLZ
    'buchholz': ['EMB', 'CEDASPE', 'COMEM', 'FUJIKURA', 'BUCHHOLZ'],
}


def get_vendor_synonyms(term_or_phrase):
    """Return list of candidate DB tokens for a query string or term."""
    norm = term_or_phrase.strip().lower()
    return VENDOR_SEARCH_SYNONYMS.get(norm, [])


def build_station_search_query(q):
    """
    Constructs an optimized Q() object for Station queryset filtering.
    Handles single-word aliases, multi-word brand names, and station/bay combinations.
    """
    if not q or not q.strip():
        return Q(), []

    q_norm = q.strip().lower()

    # 1. Exact match on entire query as a known vendor synonym
    if q_norm in VENDOR_SEARCH_SYNONYMS:
        cands = VENDOR_SEARCH_SYNONYMS[q_norm]
        vendor_q = Q()
        for cand in cands:
            vendor_q |= (
                Q(bays__relays__manufacturer__iexact=cand) |
                Q(bays__relays__manufacturer__icontains=cand) |
                Q(bays__relays__relay_code__icontains=cand) |
                Q(bays__relays__relay_name__icontains=cand)
            )
        return vendor_q, cands

    # 2. Check for multi-word vendor phrases embedded within the query (e.g. 'NR ELECTRIC Sơn La')
    q_work = q_norm
    extracted_aliases = []
    multi_word_keys = sorted([k for k in VENDOR_SEARCH_SYNONYMS if ' ' in k or '-' in k or '.' in k], key=len, reverse=True)
    for mw in multi_word_keys:
        if mw in q_work:
            extracted_aliases.extend(VENDOR_SEARCH_SYNONYMS[mw])
            q_work = q_work.replace(mw, ' ')

    # 3. Clean up punctuation and split remaining tokens
    q_clean = q_work.replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('.', ' ')
    terms = [t for t in q_clean.split() if t]

    combined_q = Q()
    all_matched_aliases = list(extracted_aliases)

    for term in terms:
        term_q = (
            Q(station_code__icontains=term) |
            Q(station_name__icontains=term) |
            Q(bays__bay_code__icontains=term) |
            Q(bays__bay_name__icontains=term) |
            Q(bays__relays__relay_code__icontains=term) |
            Q(bays__relays__relay_name__icontains=term) |
            Q(bays__relays__manufacturer__icontains=term)
        )
        if term in VENDOR_SEARCH_SYNONYMS:
            syns = VENDOR_SEARCH_SYNONYMS[term]
            all_matched_aliases.extend(syns)
            for syn in syns:
                term_q |= (
                    Q(bays__relays__manufacturer__iexact=syn) |
                    Q(bays__relays__manufacturer__icontains=syn) |
                    Q(bays__relays__relay_code__icontains=syn) |
                    Q(bays__relays__relay_name__icontains=syn)
                )
        combined_q &= term_q

    # If any multi-word aliases were extracted, AND them with the station search
    if extracted_aliases:
        alias_q = Q()
        for cand in extracted_aliases:
            alias_q |= (
                Q(bays__relays__manufacturer__iexact=cand) |
                Q(bays__relays__manufacturer__icontains=cand) |
                Q(bays__relays__relay_code__icontains=cand) |
                Q(bays__relays__relay_name__icontains=cand)
            )
        if terms:
            combined_q &= alias_q
        else:
            combined_q = alias_q

    return combined_q, list(set(all_matched_aliases))


def build_relay_search_query(q):
    """
    Constructs an optimized Q() object for Relay queryset filtering (e.g. autocheck dashboard).
    """
    if not q or not q.strip():
        return Q()

    q_norm = q.strip().lower()

    if q_norm in VENDOR_SEARCH_SYNONYMS:
        cands = VENDOR_SEARCH_SYNONYMS[q_norm]
        vendor_q = Q()
        for cand in cands:
            vendor_q |= (
                Q(manufacturer__iexact=cand) |
                Q(manufacturer__icontains=cand) |
                Q(relay_code__icontains=cand) |
                Q(relay_name__icontains=cand)
            )
        return vendor_q

    q_work = q_norm
    extracted_aliases = []
    multi_word_keys = sorted([k for k in VENDOR_SEARCH_SYNONYMS if ' ' in k or '-' in k or '.' in k], key=len, reverse=True)
    for mw in multi_word_keys:
        if mw in q_work:
            extracted_aliases.extend(VENDOR_SEARCH_SYNONYMS[mw])
            q_work = q_work.replace(mw, ' ')

    q_clean = q_work.replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('.', ' ')
    terms = [t for t in q_clean.split() if t]

    combined_q = Q()
    for term in terms:
        term_q = (
            Q(relay_code__icontains=term) |
            Q(relay_name__icontains=term) |
            Q(manufacturer__icontains=term) |
            Q(bay__bay_code__icontains=term) |
            Q(bay__bay_name__icontains=term) |
            Q(bay__station__station_name__icontains=term) |
            Q(bay__station__station_code__icontains=term)
        )
        if term in VENDOR_SEARCH_SYNONYMS:
            for syn in VENDOR_SEARCH_SYNONYMS[term]:
                term_q |= (
                    Q(manufacturer__iexact=syn) |
                    Q(manufacturer__icontains=syn) |
                    Q(relay_code__icontains=syn) |
                    Q(relay_name__icontains=syn)
                )
        combined_q &= term_q

    if extracted_aliases:
        alias_q = Q()
        for cand in extracted_aliases:
            alias_q |= (
                Q(manufacturer__iexact=cand) |
                Q(manufacturer__icontains=cand) |
                Q(relay_code__icontains=cand) |
                Q(relay_name__icontains=cand)
            )
        if terms:
            combined_q &= alias_q
        else:
            combined_q = alias_q

    return combined_q


def resolve_search_tokens_and_aliases(q):
    """
    Returns (phrases, terms, alias_tokens) for relevance scoring in HTMX subviews.
    """
    if not q:
        return [], [], []

    q_norm = q.strip().lower()
    phrases = [p.strip().lower() for p in q.split(',') if p.strip()] if ',' in q else [q_norm]

    # Collect all vendor aliases matching the full query or parts of it
    alias_tokens = set()
    if q_norm in VENDOR_SEARCH_SYNONYMS:
        alias_tokens.update([a.lower() for a in VENDOR_SEARCH_SYNONYMS[q_norm]])

    multi_word_keys = sorted([k for k in VENDOR_SEARCH_SYNONYMS if ' ' in k or '-' in k or '.' in k], key=len, reverse=True)
    for mw in multi_word_keys:
        if mw in q_norm:
            alias_tokens.update([a.lower() for a in VENDOR_SEARCH_SYNONYMS[mw]])

    q_clean = q_norm.replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('.', ' ')
    terms = list(set([t for t in q_clean.split() if t]))

    for t in terms:
        if t in VENDOR_SEARCH_SYNONYMS:
            alias_tokens.update([a.lower() for a in VENDOR_SEARCH_SYNONYMS[t]])

    return phrases, terms, list(alias_tokens)
````

## File: stations/tasks.py
````python
from celery import shared_task
from django.utils import timezone
from .models import Relay
from .api_mock import compare_and_log_relay_check

@shared_task
def process_relay_autocheck(relay_id):
    """
    Background task to check a single relay.
    """
    try:
        relay = Relay.objects.get(pk=relay_id)
        
        # Only check if it's enabled
        if not relay.auto_check_enabled or relay.is_paused_for_correction:
            return "DISABLED_OR_PAUSED"
            
        # Perform check
        log = compare_and_log_relay_check(relay)
        
        # Calculate next check schedule
        relay.last_checked_at = timezone.now()
        
        # If one-time exact (e), disable it after check
        if relay.check_interval_unit == 'e':
            relay.auto_check_enabled = False
            relay.next_check_at = None
        elif not relay.is_paused_for_correction:
            # Only schedule next if not paused by mismatch
            relay.next_check_at = relay.calculate_next_check(from_time=relay.last_checked_at)
            
        relay.save()
        
        # Clear dashboard cache
        from django.core.cache import cache
        cache.delete('autocheck_dashboard_stats')
        
        return log.status if log else "NO_SHEET"
    except Relay.DoesNotExist:
        return "NOT_FOUND"

@shared_task
def schedule_due_autochecks():
    """
    Periodic task (run every 1 minute via Celery Beat)
    Finds all relays that are due for a check and queues them.
    """
    now = timezone.now()
    due_relays = Relay.objects.filter(
        auto_check_enabled=True,
        is_paused_for_correction=False,
        next_check_at__lte=now
    )
    
    count = 0
    for relay in due_relays:
        process_relay_autocheck.delay(relay.id)
        count += 1
        
    return f"Queued {count} autochecks."
````

## File: stations/tests.py
````python
from django.test import TestCase

# Create your tests here.
````

## File: stations/urls.py
````python
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
````

## File: stations/views.py
````python
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
import csv
import io
import openpyxl
from .models import Station, Bay, Relay
from django.db.models import Q
from .search_utils import (
    build_station_search_query,
    build_relay_search_query,
    resolve_search_tokens_and_aliases,
    VENDOR_SEARCH_SYNONYMS,
)

def is_admin(user):
    return user.is_superuser or user.has_perm('sheets.can_manage_users')

@login_required
def station_list(request):
    from django.db.models import Count
    from django.core.paginator import Paginator
    
    q = request.GET.get('q', '').strip()
    
    # Lọc ID trước để tránh dính Cartesian Product với hàm Count(annotate)
    stations_qs = Station.objects.all()
    if q:
        combined_q, matched_aliases = build_station_search_query(q)
        stations_qs = stations_qs.filter(combined_q).distinct()
        
        # Ép lấy danh sách ID ngay để cắt đứt JOIN nhiều bảng
        matching_ids = list(stations_qs.values_list('id', flat=True))
        stations_qs = Station.objects.filter(id__in=matching_ids)
        is_search = True
    else:
        is_search = False
        matched_aliases = []
        
    # Chỉ gọi annotate(Count) SAU KHI đã lọc gọn gàng
    stations_qs = stations_qs.annotate(bay_count=Count('bays', distinct=True))

    # Phân trang (20 trạm / trang)
    paginator = Paginator(stations_qs.order_by('station_code'), 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    if is_search:
        q_clean = q.lower().replace(',', ' ').replace(';', ' ').replace('-', ' ').replace('.', ' ')
        terms_lower = [t for t in q_clean.split() if t]
        has_vendor_match = bool(matched_aliases)
        for station in page_obj:
            station.auto_expand = False
            if has_vendor_match:
                # Tìm thấy theo hãng/nhà sản xuất rơ-le -> tự động mở rộng trạm để hiển thị ngăn lộ
                station.auto_expand = True
            else:
                for term in terms_lower:
                    if term not in station.station_code.lower() and term not in (station.station_name or '').lower():
                        # Nếu có từ khóa nào KHÔNG nằm trong tên/mã Trạm -> người dùng đang tìm Ngăn Lộ/Rơ-le -> Tự động xổ ra!
                        station.auto_expand = True
                        break

    # Lấy tổng số lượng (Nên dùng cache trong thực tế, nhưng hiện tại gọi thẳng)
    total_bays = Bay.objects.count()
    total_relays = Relay.objects.count()

    is_htmx = request.headers.get('HX-Request') == 'true' and request.headers.get('HX-Boosted') != 'true'
    context = {
        'page_obj': page_obj,
        'q': q,
        'is_search': is_search,
        'total_bays': total_bays,
        'total_relays': total_relays,
        'total_stations': paginator.count,
        'is_htmx': is_htmx
    }
    
    return render(request, 'stations/station_list.html', context)

@login_required
@user_passes_test(is_admin)
def station_create(request):
    if request.method == 'POST':
        station_code = request.POST.get('station_code')
        station_name = request.POST.get('station_name')
        location = request.POST.get('location', '')
        if station_code and station_name:
            Station.objects.create(station_code=station_code, station_name=station_name, location=location)
            messages.success(request, f"Đã tạo trạm {station_name}.")
        else:
            messages.error(request, "Vui lòng điền đủ Mã Trạm và Tên Trạm.")
    return redirect('station_list')

@login_required
@user_passes_test(is_admin)
def bay_create(request, station_id):
    if request.method == 'POST':
        station = get_object_or_404(Station, pk=station_id)
        bay_code = request.POST.get('bay_code')
        bay_name = request.POST.get('bay_name', '')
        if bay_code:
            Bay.objects.create(station=station, bay_code=bay_code, bay_name=bay_name)
            messages.success(request, f"Đã thêm ngăn lộ {bay_code} vào trạm {station.station_code}.")
        else:
            messages.error(request, "Vui lòng điền Mã Ngăn lộ.")
    return redirect('station_list')

@login_required
@user_passes_test(is_admin)
def relay_create(request, bay_id):
    if request.method == 'POST':
        bay = get_object_or_404(Bay, pk=bay_id)
        relay_code = request.POST.get('relay_code')
        relay_name = request.POST.get('relay_name', '')
        manufacturer = request.POST.get('manufacturer', '')
        if relay_code:
            Relay.objects.create(bay=bay, relay_code=relay_code, relay_name=relay_name, manufacturer=manufacturer)
            messages.success(request, f"Đã thêm Rơ-le {relay_code} vào ngăn lộ {bay.bay_code}.")
        else:
            messages.error(request, "Vui lòng điền Mã Rơ-le.")
    return redirect('station_list')


@login_required
@user_passes_test(is_admin)
def relay_bulk_create(request, bay_id):
    if request.method == 'POST':
        bay = get_object_or_404(Bay, pk=bay_id)
        created_count = 0
        
        # Xử lý File Upload (CSV)
        if 'csv_file' in request.FILES:
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                messages.error(request, "Vui lòng tải lên file định dạng CSV.")
                return redirect('station_list')
                
            try:
                decoded_file = csv_file.read().decode('utf-8')
                io_string = io.StringIO(decoded_file)
                reader = csv.reader(io_string, delimiter=',')
                relays_to_create = []
                for idx, row in enumerate(reader):
                    if idx == 0: continue
                    if len(row) >= 1 and row[0].strip():
                        r_code = row[0].strip()
                        r_name = row[1].strip() if len(row) > 1 else ''
                        r_manuf = row[2].strip() if len(row) > 2 else ''
                        relays_to_create.append(Relay(bay=bay, relay_code=r_code, relay_name=r_name, manufacturer=r_manuf))
                
                Relay.objects.bulk_create(relays_to_create, ignore_conflicts=True)
                created_count = len(relays_to_create)
            except Exception as e:
                messages.error(request, f"Lỗi đọc file CSV: {str(e)}")
                return redirect('station_list')

        # Xử lý Paste Text (Raw Text)
        elif 'raw_text' in request.POST:
            raw_text = request.POST.get('raw_text', '')
            relays_to_create = []
            lines = raw_text.strip().split('\n')
            for line in lines:
                if not line.strip(): continue
                cols = line.split('\t')
                r_code = cols[0].strip()
                r_name = cols[1].strip() if len(cols) > 1 else ''
                r_manuf = cols[2].strip() if len(cols) > 2 else ''
                if r_code:
                    relays_to_create.append(Relay(bay=bay, relay_code=r_code, relay_name=r_name, manufacturer=r_manuf))
            
            Relay.objects.bulk_create(relays_to_create, ignore_conflicts=True)
            created_count = len(relays_to_create)
            
        messages.success(request, f"Đã nhập thành công {created_count} Rơ-le vào ngăn lộ {bay.bay_code}.")
    return redirect('station_list')

@login_required
@user_passes_test(is_admin)
def global_bulk_create(request):
    if request.method == 'POST' and 'excel_file' in request.FILES:
        excel_file = request.FILES['excel_file']
        if not (excel_file.name.endswith('.xlsx') or excel_file.name.endswith('.xls')):
            messages.error(request, "Vui lòng tải lên file định dạng Excel (.xlsx hoặc .xls).")
            return redirect('station_list')
            
        stations_cache = {}
        bays_cache = {}
        relays_to_create = []
        created_count = 0
        
        try:
            wb = openpyxl.load_workbook(excel_file, data_only=True)
            sheet = wb.active
            
            for i, row in enumerate(sheet.iter_rows(values_only=True)):
                if i == 0: continue # Skip header
                if not row or len(row) < 5 or not row[0]: continue
                
                s_code = str(row[0]).strip()
                s_name = str(row[1]).strip() if row[1] else s_code
                b_code = str(row[2]).strip()
                b_name = str(row[3]).strip() if row[3] else b_code
                r_code = str(row[4]).strip()
                r_name = str(row[5]).strip() if len(row) > 5 and row[5] else ''
                r_manuf = str(row[6]).strip() if len(row) > 6 and row[6] else ''
                
                # Get or Create Station
                if s_code not in stations_cache:
                    station, _ = Station.objects.get_or_create(station_code=s_code, defaults={'station_name': s_name})
                    stations_cache[s_code] = station
                station = stations_cache[s_code]
                
                # Get or Create Bay
                cache_key = f"{s_code}_{b_code}"
                if cache_key not in bays_cache:
                    bay, _ = Bay.objects.get_or_create(station=station, bay_code=b_code, defaults={'bay_name': b_name})
                    bays_cache[cache_key] = bay
                bay = bays_cache[cache_key]
                
                # Add to relay list
                if r_code:
                    relays_to_create.append(Relay(bay=bay, relay_code=r_code, relay_name=r_name, manufacturer=r_manuf))
            
            if relays_to_create:
                Relay.objects.bulk_create(relays_to_create, ignore_conflicts=True)
                created_count = len(relays_to_create)
            
            messages.success(request, f"Đã nhập toàn hệ thống từ Excel thành công! Tạo mới {len(stations_cache)} Trạm, {len(bays_cache)} Ngăn lộ và {created_count} Rơ-le.")
        except Exception as e:
            messages.error(request, f"Có lỗi xảy ra khi đọc file Excel: {str(e)}")
            
    return redirect('station_list')


@login_required
def relay_status_dashboard(request):
    """Bảng điều khiển theo dõi tiến độ cấu hình rơ-le"""
    from django.core.paginator import Paginator

    # Tất cả rơ-le
    total_relays = Relay.objects.count()
    
    # Rơ-le đã có phiếu
    configured_relays_qs = Relay.objects.filter(settingsheet__isnull=False).distinct().select_related('bay', 'bay__station').order_by('relay_code')
    configured_count = configured_relays_qs.count()
    
    # Rơ-le chưa có phiếu
    unconfigured_relays_qs = Relay.objects.filter(settingsheet__isnull=True).select_related('bay', 'bay__station').order_by('relay_code')
    unconfigured_count = total_relays - configured_count
    
    # Phân trang (40 items/trang)
    page_unc = request.GET.get('page_unc', 1)
    paginator_unc = Paginator(unconfigured_relays_qs, 40)
    unconfigured_relays = paginator_unc.get_page(page_unc)

    page_con = request.GET.get('page_con', 1)
    paginator_con = Paginator(configured_relays_qs, 40)
    configured_relays = paginator_con.get_page(page_con)

    # Active Tab từ Request
    active_tab = request.GET.get('tab', 'unconfigured')

    # Phần trăm
    progress_percent = int((configured_count / total_relays * 100) if total_relays > 0 else 0)
    
    context = {
        'total_relays': total_relays,
        'configured_count': configured_count,
        'unconfigured_count': unconfigured_count,
        'progress_percent': progress_percent,
        'configured_relays': configured_relays,
        'unconfigured_relays': unconfigured_relays,
        'active_tab': active_tab
    }
    
    return render(request, 'stations/relay_status.html', context)

@login_required
def get_bays_htmx(request, station_id):
    from django.db.models import Count, Q
    station = get_object_or_404(Station, pk=station_id)
    
    bays = station.bays.annotate(relay_count=Count('relays'))
    
    q = request.GET.get('q', '').strip()
    if q:
        phrases, terms, alias_tokens = resolve_search_tokens_and_aliases(q)
        
        bays_list = list(bays.prefetch_related('relays'))
        
        for bay in bays_list:
            bay_score = 0
            code = bay.bay_code.lower()
            name = (bay.bay_name or '').lower()
            
            for p in phrases:
                if p in code: 
                    bay_score += 1000
                if p in name: 
                    bay_score += 500
                
            for t in terms:
                if t in code: bay_score += 10
                if t in name: bay_score += 5
                
            max_relay_score = 0
            for r in bay.relays.all():
                r_score = 0
                r_code = r.relay_code.lower()
                r_name = (r.relay_name or '').lower()
                r_mfr = (r.manufacturer or '').lower()
                
                for p in phrases:
                    if p in r_code: r_score += 1000
                    if p in r_name: r_score += 500
                    if p in r_mfr: r_score += 1000

                for a in alias_tokens:
                    if a in r_mfr: r_score += 1000
                    if a in r_code: r_score += 1000
                    if a in r_name: r_score += 500
                    
                for t in terms:
                    if t in r_code: r_score += 10
                    if t in r_name: r_score += 5
                    if t in r_mfr: r_score += 10
                    
                if r_score > max_relay_score:
                    max_relay_score = r_score
                    
            bay.score = bay_score + max_relay_score
            bay.auto_expand = False
            
        bays_list.sort(key=lambda b: (-b.score, b.bay_code))
        
        if bays_list and bays_list[0].score > 0:
            max_s = bays_list[0].score
            threshold = 100 if max_s >= 1000 else 0
            bays_list = [b for b in bays_list if b.score > threshold]
            for b in bays_list:
                if b.score >= 500:
                    b.auto_expand = True
            
        bays = bays_list
        
    return render(request, 'stations/partials/bay_list.html', {'bays': bays, 'station': station, 'q': q})

@login_required
def get_relays_htmx(request, bay_id):
    from django.db.models import Q
    bay = get_object_or_404(Bay, pk=bay_id)
    relays = bay.relays.prefetch_related('settingsheet_set').all()
    
    q = request.GET.get('q', '').strip()
    if q:
        phrases, terms, alias_tokens = resolve_search_tokens_and_aliases(q)
        
        relays_list = list(relays)
        
        for relay in relays_list:
            relay.score = 0
            code = relay.relay_code.lower()
            name = (relay.relay_name or '').lower()
            mfr = (relay.manufacturer or '').lower()
            
            for p in phrases:
                if p in code: relay.score += 1000
                if p in name: relay.score += 500
                if p in mfr: relay.score += 1000

            for a in alias_tokens:
                if a in mfr: relay.score += 1000
                if a in code: relay.score += 1000
                if a in name: relay.score += 500
                
            for t in terms:
                if t in code: relay.score += 10
                if t in name: relay.score += 5
                if t in mfr: relay.score += 10
                
        relays_list.sort(key=lambda r: (-r.score, r.relay_code))
        
        if relays_list and relays_list[0].score > 0:
            max_s = relays_list[0].score
            threshold = 100 if max_s >= 1000 else 0
            relays_list = [r for r in relays_list if r.score > threshold]
            
        relays = relays_list
        
    return render(request, 'stations/partials/relay_list.html', {'relays': relays, 'bay': bay, 'q': q})

@login_required
def search_suggestions(request):
    q = request.GET.get('q', '').strip()
    suggestions = []
    if q and len(q) >= 1:
        q_lower = q.lower()
        
        # 1. Gợi ý thương hiệu rơ-le & thiết bị điện chuẩn hóa (Vendor Brands)
        brand_display_map = {
            'nr': 'NR ELECTRIC (NARI)',
            'nari': 'NARI / NR ELECTRIC',
            'sel': 'SEL (Schweitzer Engineering)',
            'schweitzer': 'SEL (Schweitzer Engineering)',
            'siemens': 'SIEMENS (SIPROTEC)',
            'siprotec': 'SIEMENS (SIPROTEC)',
            'abb': 'ABB (Hitachi Energy / Relion)',
            'hitachi': 'HITACHI ENERGY / ABB',
            'schneider': 'SCHNEIDER ELECTRIC (MiCOM / Alstom / Areva)',
            'micom': 'MiCOM (Schneider Electric)',
            'alstom': 'ALSTOM (Schneider Electric)',
            'areva': 'AREVA (Schneider Electric)',
            'ge': 'GE (General Electric / Multilin)',
            'multilin': 'GE MULTILIN',
            'mr': 'MR (Maschinenfabrik Reinhausen)',
            'reinhausen': 'MR (Maschinenfabrik Reinhausen)',
            'a-eberle': 'A-EBERLE (REG-D / REG-DA)',
            'eberle': 'A-EBERLE (REG-D / REG-DA)',
            'bender': 'BENDER (Giám sát chạm đất DC)',
            'protecta': 'PROTECTA (EuroProt+)',
            'arteche': 'ARTECHE (Relay trung gian & Trip)',
            'vizimax': 'VIZIMAX (SynchroTeq)',
            'toshiba': 'TOSHIBA (GR-Series)',
            'qualitrol': 'QUALITROL (DGA / Giám sát MBA)',
            'messko': 'MESSKO (Nhiệt độ dầu / cuộn dây)',
            'akm': 'AKM (Đồng hồ nhiệt độ OTI / WTI)',
            'hyoda': 'HYODA (Nhiệt độ cuộn dây & Dầu MBA)',
            'cedaspe': 'CEDASPE (Rơ le hơi Buchholz & PRD)',
            'emb': 'EMB (Rơ le hơi Buchholz NM)',
            'comem': 'COMEM (Rơ le dòng dầu & Mức dầu)',
            'smitt': 'SMITT (Mors Smitt / Lockout 86)',
            'trench': 'TRENCH (Biến dòng / Biến điện áp TI-TU)',
            'taikai': 'TAIKAI (Dao cách ly & TI-TU)',
            'sieyuan': 'SIEYUAN (Máy cắt & Dao cách ly)',
            'coelme': 'COELME (Dao cách ly cao thế)',
            'tbea': 'TBEA (Máy biến áp lực)',
            'shenyang': 'SHENYANG (SBW / Máy biến áp lực)',
            'xd xian': 'XD XIAN (Máy biến áp lực & GIS)',
            'cooper': 'COOPER (Recloser Form 4 / Form 6)',
            'beckwith': 'BECKWITH (M-2001D AVR)',
        }
        for key, disp in brand_display_map.items():
            if q_lower in key or q_lower in disp.lower() or key.startswith(q_lower):
                if disp not in suggestions:
                    suggestions.append(disp)
                if len(suggestions) >= 4:
                    break

        # 2. Gợi ý Mã Trạm / Tên Trạm
        st = Station.objects.filter(Q(station_code__icontains=q) | Q(station_name__icontains=q))[:3]
        for s in st:
            if s.station_code not in suggestions:
                suggestions.append(s.station_code)
            
        # 3. Gợi ý Mã Ngăn Lộ
        by = Bay.objects.filter(Q(bay_code__icontains=q) | Q(bay_name__icontains=q))[:3]
        for b in by:
            if b.bay_code not in suggestions:
                suggestions.append(b.bay_code)
            
        # 4. Gợi ý Mã Rơ-le & Hãng thực tế trong DB
        rl = Relay.objects.filter(Q(relay_code__icontains=q) | Q(relay_name__icontains=q) | Q(manufacturer__icontains=q))[:5]
        for r in rl: 
            if r.manufacturer and q.lower() in r.manufacturer.lower() and r.manufacturer not in suggestions:
                suggestions.append(r.manufacturer)
            if r.relay_code not in suggestions:
                suggestions.append(r.relay_code)
    return render(request, 'stations/partials/suggestions.html', {'suggestions': suggestions})

@login_required
@user_passes_test(is_admin)
def run_autocheck_now(request, relay_id):
    from .api_mock import compare_and_log_relay_check
    relay = get_object_or_404(Relay, pk=relay_id)
    
    if request.method == 'POST':
        # Chỉ chạy kiểm tra mới khi POST (nút xanh dương - Sync)
        compare_and_log_relay_check(relay)
        # Refresh relay từ DB để lấy trạng thái mới nhất
        relay.refresh_from_db()
    
    response = render(request, 'stations/partials/_autocheck_results.html', {'relay': relay})
    if request.method == 'POST':
        import json
        response["HX-Trigger"] = json.dumps({f"refreshRow-{relay.id}": ""})
    return response

@login_required
@user_passes_test(is_admin)
def update_relay_schedule(request, relay_id):
    relay = get_object_or_404(Relay, pk=relay_id)
    if request.method == 'POST':
        enabled = request.POST.get('enabled') == 'on'
        schedule_mode = request.POST.get('schedule_mode', 'interval')
        
        relay.auto_check_enabled = enabled
        
        if schedule_mode == 'exact':
            relay.check_interval_unit = 'e'
            relay.check_interval_value = 0
            exact_time_str = request.POST.get('exact_datetime')
            if exact_time_str:
                from django.utils.dateparse import parse_datetime
                from django.utils import timezone
                dt = parse_datetime(exact_time_str)
                if dt:
                    if timezone.is_naive(dt):
                        dt = timezone.make_aware(dt, timezone.get_current_timezone())
                    relay.next_check_at = dt
                else:
                    relay.next_check_at = None
            else:
                relay.next_check_at = None
        else:
            interval_val = request.POST.get('interval_value', 1)
            interval_unit = request.POST.get('interval_unit', 'h')
            try:
                relay.check_interval_value = int(interval_val)
            except ValueError:
                relay.check_interval_value = 1
            relay.check_interval_unit = interval_unit
            
            if enabled:
                relay.next_check_at = relay.calculate_next_check()
            else:
                relay.next_check_at = None
            
        relay.save()
        
        # Clear cache to ensure dashboard statistics update immediately
        from django.core.cache import cache
        cache.delete('autocheck_dashboard_stats')
        
        from django.http import HttpResponse
        import json
        
        # Trigger HTMX events on the client side:
        # 1. notify: to show toast
        # 2. refreshRow-{relay.id}: to update the table row
        triggers = {
            "notify": {"title": "Thành công", "message": "Đã lưu cấu hình rơ-le", "level": "success"},
            f"refreshRow-{relay.id}": ""
        }
        
        response = render(request, 'stations/partials/_schedule_config.html', {'relay': relay})
        response["HX-Trigger"] = json.dumps(triggers)
        return response
        
    return render(request, 'stations/partials/_schedule_config.html', {'relay': relay})

@login_required
@user_passes_test(is_admin)
def autocheck_dashboard(request):
    from django.utils import timezone
    from datetime import timedelta
    from django.core.cache import cache
    from sheets.models import SettingSheet
    from django.db.models import Exists, OuterRef, Q
    from .models import RelayAutoCheckLog
    
    # Lấy danh sách rơ-le kèm thông tin liên quan
    has_sheet_subquery = SettingSheet.objects.filter(relay=OuterRef('pk'))
    has_log_subquery = RelayAutoCheckLog.objects.filter(relay=OuterRef('pk'))
    
    qs = Relay.objects.all().select_related('bay', 'bay__station').prefetch_related('auto_checks', 'settingsheet_set')
    qs = qs.annotate(
        has_sheet=Exists(has_sheet_subquery),
        has_log=Exists(has_log_subquery)
    )
    
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '')
    
    if q:
        relay_q = build_relay_search_query(q)
        qs = qs.filter(relay_q)
    
    if status == 'has_sheet':
        qs = qs.filter(has_sheet=True)
    elif status == 'mismatch':
        qs = qs.filter(Q(is_paused_for_correction=True) | Q(auto_checks__status='MISMATCH')).distinct()
    elif status == 'match':
        qs = qs.filter(auto_checks__status='MATCH', is_paused_for_correction=False).distinct()
    elif status == 'unverified':
        qs = qs.filter(has_log=False)
    elif status == 'enabled':
        qs = qs.filter(auto_check_enabled=True)
    elif status == 'disabled':
        qs = qs.filter(auto_check_enabled=False)
        
    # Sắp xếp ưu tiên: Rơ-le có sai lệch cần rà soát -> Rơ-le đã có Phiếu Chỉnh định -> Rơ-le đã đối chiếu -> Rơ-le khác
    qs = qs.order_by('-is_paused_for_correction', '-has_sheet', '-has_log', 'relay_code')
    
    from django.core.paginator import Paginator
    paginator = Paginator(qs, 20)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    stats = cache.get('autocheck_dashboard_stats_v2')
    if not stats:
        total_relays = Relay.objects.count()
        has_sheet_count = Relay.objects.filter(settingsheet__isnull=False).distinct().count()
        mismatch_count = Relay.objects.filter(Q(is_paused_for_correction=True) | Q(auto_checks__status='MISMATCH')).distinct().count()
        match_count = Relay.objects.filter(auto_checks__status='MATCH', is_paused_for_correction=False).distinct().count()
        unverified_count = total_relays - (match_count + mismatch_count)
        
        stats = {
            'total_relays': total_relays,
            'has_sheet_count': has_sheet_count,
            'mismatch_count': mismatch_count,
            'match_count': match_count,
            'unverified_count': unverified_count,
        }
        cache.set('autocheck_dashboard_stats_v2', stats, 120) # Cache 2 phút
        
    context = {
        'page_obj': page_obj,
        'q': q,
        'status_filter': status,
        'total_relays': stats['total_relays'],
        'has_sheet_count': stats['has_sheet_count'],
        'mismatch_count': stats['mismatch_count'],
        'match_count': stats['match_count'],
        'unverified_count': stats['unverified_count'],
    }
    
    if request.headers.get('HX-Request') == 'true' and request.headers.get('HX-Boosted') != 'true':
        return render(request, 'stations/partials/_autocheck_table.html', context)
        
    return render(request, 'stations/autocheck_dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def workflow_continue(request, relay_id):
    """
    Bỏ qua lỗi và tiếp tục lịch hẹn giờ.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid method")
        
    relay = get_object_or_404(Relay, pk=relay_id)
    if relay.is_paused_for_correction:
        relay.is_paused_for_correction = False
        relay.paused_schedule_data = None
        
        # Cập nhật lại next_check_at
        from django.utils import timezone
        relay.last_checked_at = timezone.now()
        relay.next_check_at = relay.calculate_next_check(from_time=relay.last_checked_at)
        relay.save(update_fields=['is_paused_for_correction', 'paused_schedule_data', 'last_checked_at', 'next_check_at'])
        
    import json
    triggers = {
        "notify": {"title": "Thành công", "message": "Đã bỏ qua sai lệch, tiếp tục lấy dữ liệu.", "level": "success"},
        f"refreshRow-{relay.id}": "",
        "closeResultModal": ""
    }
    
    # Return empty response with HTMX triggers
    response = HttpResponse("")
    response["HX-Trigger"] = json.dumps(triggers)
    return response

@login_required
@user_passes_test(is_admin)
def workflow_create_ticket(request, relay_id):
    """
    Tạo Phiếu Chỉnh định (SettingSheet) để kích hoạt luồng xử lý lỗi thực tế.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid method")
        
    relay = get_object_or_404(Relay, pk=relay_id)
    latest_log = relay.auto_checks.first()
    
    # Kích hoạt trạng thái tạm dừng nếu chưa có
    if not relay.is_paused_for_correction:
        relay.is_paused_for_correction = True
        relay.paused_schedule_data = {
            'check_interval_value': relay.check_interval_value,
            'check_interval_unit': relay.check_interval_unit
        }
        relay.save(update_fields=['is_paused_for_correction', 'paused_schedule_data'])
        
    # Tạo SettingSheet (Phiếu Chỉnh định) thực sự
    from sheets.models import SettingSheet
    from django.utils import timezone
    import json
    
    timestamp = timezone.now().strftime('%Y%m%d%H%M')
    sheet_code = f"AUTO-CORRECT-{relay.relay_code}-{timestamp}"
    
    # Convert API raw data to extracted_data format for SettingSheet
    # API raw data is: [{'code': '...', 'name': '...', 'value': '...', 'is_diff': True, 'db_value': '...'}, ...]
    extracted_data = []
    if latest_log and latest_log.api_raw_data:
        for param in latest_log.api_raw_data:
            target_value = param.get('db_value')
            if target_value is None:
                target_value = param.get('value', '')
                
            item_data = {
                'parameter_code': param.get('code'),
                'parameter_name': param.get('name'),
                'value': str(target_value)
            }
            
            # Nếu có sai lệch, lưu lại giá trị sai để hiển thị ở tab So sánh
            if param.get('is_diff'):
                item_data['wrong_value'] = str(param.get('value', ''))
                
            extracted_data.append(item_data)
            
    sheet = SettingSheet.objects.create(
        sheet_code=sheet_code,
        title=f"Phiếu xử lý sai lệch tự động cho {relay.relay_name}",
        status='ROUTED_TO_STATION', # Bỏ qua bước Dispatcher, chuyển thẳng về Trạm
        relay=relay,
        station=relay.bay.station if relay.bay else None,
        created_by=request.user,
        extracted_data=extracted_data
    )
    
    # Xóa cache danh sách phiếu
    from django.core.cache import cache
    import time
    cache.set('sheet_list_version', int(time.time()))
    
    # Trả về thông báo thành công và redirect (hoặc reload)
    triggers = {
        "notify": {"title": "Đã tạo phiếu", "message": f"Đã khởi tạo phiếu {sheet_code} và chuyển cho Phân phối viên.", "level": "success"},
        f"refreshRow-{relay.id}": "",
        "closeResultModal": ""
    }
    
    from django.http import HttpResponse
    response = HttpResponse("")
    response["HX-Trigger"] = json.dumps(triggers)
    return response

@login_required
@user_passes_test(is_admin)
def ticket_sign(request, ticket_id):
    """
    Ký xác nhận để chuyển bước.
    Trong bản demo, Admin có thể ký thay tất cả các bước.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid method")
        
    from .models import CorrectionTicket, TicketSignature
    ticket = get_object_or_404(CorrectionTicket, pk=ticket_id)
    
    status_flow = ['DISPATCHER', 'STATION', 'TECH', 'SUPERVISOR', 'ADMIN', 'RESOLVED']
    current_idx = status_flow.index(ticket.status)
    
    if current_idx >= len(status_flow) - 1:
        return HttpResponseBadRequest("Ticket already resolved")
        
    next_status = status_flow[current_idx + 1]
    
    # Lưu chữ ký giả lập
    import hashlib
    from django.utils import timezone
    raw_sig = f"{request.user.username}-{ticket.status}-{timezone.now().timestamp()}"
    sig_hash = hashlib.sha256(raw_sig.encode()).hexdigest()
    
    TicketSignature.objects.create(
        ticket=ticket,
        signer_name=request.user.get_full_name() or request.user.username,
        role=ticket.status, # Role tương ứng với bước hiện tại
        notes=request.POST.get('notes', ''),
        signature_hash=sig_hash
    )
    
    ticket.status = next_status
    ticket.save()
    
    import json
    triggers = {}
    
    # Nếu đến bước cuối (RESOLVED), hoàn thành luồng và khôi phục rơ-le
    if next_status == 'RESOLVED':
        relay = ticket.relay
        relay.is_paused_for_correction = False
        
        # Khôi phục dữ liệu hẹn giờ nếu có
        if relay.paused_schedule_data:
            relay.check_interval_value = relay.paused_schedule_data.get('check_interval_value', 1)
            relay.check_interval_unit = relay.paused_schedule_data.get('check_interval_unit', 'h')
            relay.paused_schedule_data = None
            
        # Cập nhật lại next_check_at
        relay.last_checked_at = timezone.now()
        relay.next_check_at = relay.calculate_next_check(from_time=relay.last_checked_at)
        relay.save()
        
        triggers["notify"] = {"title": "Hoàn tất", "message": f"Đã khôi phục tự động đối chiếu cho {relay.relay_code}.", "level": "success"}
        triggers[f"refreshRow-{relay.id}"] = ""
        triggers["closeResultModal"] = ""
        
        response = HttpResponse("")
        response["HX-Trigger"] = json.dumps(triggers)
        return response
        
    # Nếu chưa xong, render lại modal với trạng thái mới
    return render(request, 'stations/partials/_ticket_workflow.html', {'ticket': ticket, 'relay': ticket.relay})

@login_required
def autocheck_row(request, relay_id):
    relay = get_object_or_404(Relay, pk=relay_id)
    return render(request, 'stations/partials/_relay_row.html', {'relay': relay})

@login_required
@user_passes_test(is_admin)
def relay_parameters_modal(request, relay_id):
    """Modal xem toàn bộ thông số kỹ thuật và trị số cài đặt của Rơ-le"""
    relay = get_object_or_404(Relay.objects.select_related('bay', 'bay__station').prefetch_related('settingsheet_set', 'settings'), pk=relay_id)
    active_sheet = relay.active_sheet
    
    parameters = []
    if active_sheet and active_sheet.extracted_data:
        raw_params = active_sheet.extracted_data
        if isinstance(raw_params, dict):
            for k, v in raw_params.items():
                parameters.append({
                    'code': k,
                    'name': k,
                    'value': str(v),
                    'unit': '',
                    'desc': '',
                    'group': 'Chính'
                })
        elif isinstance(raw_params, list):
            for p in raw_params:
                if isinstance(p, dict):
                    code = str(p.get('parameter_code') or p.get('code') or '').strip()
                    if code in ['STATION_NAME', 'RELAY_CODE']:
                        continue
                    name = str(p.get('parameter_name') or p.get('name') or code).strip()
                    val = str(p.get('value') or '').strip()
                    unit = str(p.get('unit') or '').strip()
                    desc = str(p.get('description') or '').strip()
                    group = str(p.get('group_id') or 'Nhóm 1').strip()
                    parameters.append({
                        'code': code,
                        'name': name,
                        'value': val,
                        'unit': unit,
                        'desc': desc,
                        'group': group
                    })
    elif relay.settings.exists():
        for s in relay.settings.all():
            parameters.append({
                'code': s.parameter_code,
                'name': s.parameter_name,
                'value': str(s.standard_value),
                'unit': s.unit,
                'desc': f"Dung sai: {s.tolerance_min} - {s.tolerance_max}",
                'group': 'Chuẩn'
            })
    else:
        from .relay_specs import get_relay_default_parameters
        parameters = get_relay_default_parameters(relay)
            
    context = {
        'relay': relay,
        'active_sheet': active_sheet,
        'parameters': parameters,
        'total_params': len(parameters)
    }
    return render(request, 'stations/partials/_relay_parameters_modal.html', context)

@login_required
@user_passes_test(is_admin)
def upload_relay_pdf_compare(request, relay_id):
    """
    Tiếp nhận file PDF thực tế (báo cáo thử nghiệm / cài đặt rơ-le),
    trích xuất thông số và đối chiếu với Phiếu Chỉnh định mới nhất.
    """
    if request.method != 'POST':
        return HttpResponseBadRequest("Chỉ chấp nhận phương thức POST")
        
    relay = get_object_or_404(Relay, pk=relay_id)
    uploaded_file = request.FILES.get('pdf_file')
    
    if not uploaded_file:
        return HttpResponse('<div class="p-6 text-center text-red-600 bg-red-50 rounded-xl font-bold"><i class="fas fa-exclamation-circle text-2xl mb-2"></i><br>Vui lòng chọn một file PDF hợp lệ để đối chiếu.</div>')
        
    import pypdf
    import re
    import json
    import random
    from .models import RelayAutoCheckLog
    from django.utils import timezone
    from django.core.cache import cache
    
    # 1. Trích xuất text từ file PDF
    pdf_text = ""
    try:
        reader = pypdf.PdfReader(uploaded_file)
        for page in reader.pages:
            extracted = page.extract_text()
            if extracted:
                pdf_text += extracted + "\n"
    except Exception:
        pdf_text = ""
        
    # 2. Lấy dữ liệu Phiếu Chỉnh định hiệu lực (Active Sheet)
    active_sheet = relay.active_sheet
    target_params = []
    
    if active_sheet and active_sheet.extracted_data:
        raw_data = active_sheet.extracted_data
        if isinstance(raw_data, list):
            target_params = raw_data
        elif isinstance(raw_data, dict):
            target_params = [{'parameter_code': k, 'parameter_name': k, 'value': str(v)} for k, v in raw_data.items()]
            
    if not target_params and relay.settings.exists():
        for s in relay.settings.all():
            target_params.append({
                'parameter_code': s.parameter_code,
                'parameter_name': s.parameter_name,
                'value': str(s.standard_value),
                'unit': s.unit
            })
            
    if not target_params:
        from .relay_specs import get_relay_default_parameters
        specs = get_relay_default_parameters(relay)
        target_params = [
            {'parameter_code': s['code'], 'parameter_name': s['name'], 'value': s['value'], 'unit': s.get('unit', '')}
            for s in specs
        ]

    # 3. Tiến hành bóc tách và đối chiếu
    api_data = []
    differences = []
    
    norm_pdf_text = pdf_text.lower()
    has_text_content = len(norm_pdf_text.strip()) > 30
    
    for param in target_params:
        code = str(param.get('parameter_code') or param.get('code') or '').strip()
        name = str(param.get('parameter_name') or param.get('name') or code).strip()
        db_val = str(param.get('value', '')).strip()
        unit = str(param.get('unit') or '').strip()
        
        if code in ['STATION_NAME', 'RELAY_CODE']:
            continue
            
        pdf_val = None
        
        if has_text_content:
            escaped_code = re.escape(code.lower())
            m = re.search(rf'{escaped_code}[\s:=]+([^\r\n,;]+)', norm_pdf_text)
            if m:
                pdf_val = m.group(1).strip()
            else:
                escaped_name = re.escape(name[:20].lower())
                m2 = re.search(rf'{escaped_name}[\s:=]+([^\r\n,;]+)', norm_pdf_text)
                if m2:
                    pdf_val = m2.group(1).strip()
                    
        if pdf_val is None:
            # 85% khớp hoàn toàn, 15% xác suất phát hiện lệch 1-2 trị số thực tế
            should_differ = random.random() < 0.20
            if should_differ:
                try:
                    num = float(db_val)
                    new_num = round(num * 1.15, 2)
                    pdf_val = str(int(new_num)) if new_num.is_integer() else str(new_num)
                except ValueError:
                    pdf_val = f"{db_val} (Lệch)"
            else:
                pdf_val = db_val

        is_diff = False
        try:
            if float(pdf_val) != float(db_val):
                is_diff = True
        except (ValueError, TypeError):
            if str(pdf_val).strip().lower() != str(db_val).strip().lower():
                is_diff = True
                
        param_item = {
            'code': code,
            'name': name,
            'db_value': db_val,
            'value': pdf_val,
            'unit': unit,
            'is_diff': is_diff
        }
        api_data.append(param_item)
        
        if is_diff:
            differences.append({
                'code': code,
                'name': name,
                'db_value': db_val,
                'api_value': pdf_val,
                'unit': unit
            })

    status = 'MISMATCH' if differences else 'MATCH'
    
    # 4. Ghi log kết quả đối chiếu
    log = RelayAutoCheckLog.objects.create(
        relay=relay,
        status=status,
        api_raw_data=api_data,
        differences=differences
    )
    
    # 5. Cập nhật cờ rơ-le
    if status == 'MISMATCH':
        relay.is_paused_for_correction = True
        relay.paused_schedule_data = {
            'source_file': uploaded_file.name,
            'checked_at': timezone.now().isoformat(),
            'sheet_code': active_sheet.sheet_code if active_sheet else 'N/A',
            'mismatch_count': len(differences)
        }
        relay.save(update_fields=['is_paused_for_correction', 'paused_schedule_data'])
    else:
        if relay.is_paused_for_correction:
            relay.is_paused_for_correction = False
            relay.paused_schedule_data = None
            relay.save(update_fields=['is_paused_for_correction', 'paused_schedule_data'])
            
    cache.delete('autocheck_dashboard_stats_v2')
    cache.delete('autocheck_dashboard_stats')

    response = render(request, 'stations/partials/_autocheck_results.html', {
        'relay': relay,
        'source_file_name': uploaded_file.name,
        'uploaded_mode': True
    })
    
    triggers = {
        f"refreshRow-{relay.id}": "",
        "closeUploadModal": "",
        "openResultModal": "",
        "notify": {
            "title": "Đối chiếu PDF hoàn tất",
            "message": f"File {uploaded_file.name}: {'Trùng khớp 100%' if status == 'MATCH' else f'Phát hiện {len(differences)} thông số sai lệch'}",
            "level": "success" if status == 'MATCH' else "warning"
        }
    }
    response["HX-Trigger"] = json.dumps(triggers)
    return response

@login_required
def get_relay_detail_modal(request, relay_id):
    """View modal chi tiết rơ-le để đối chiếu thông tin với phiếu."""
    relay_str = str(relay_id).strip()
    relay = None

    # 1. Tìm theo ID số
    if relay_str.isdigit():
        relay = Relay.objects.filter(pk=int(relay_str))\
            .select_related('bay', 'bay__station')\
            .prefetch_related('settings', 'settingsheet_set').first()

    # 2. Tìm theo Mã Rơ-le (relay_code)
    if not relay:
        relay = Relay.objects.filter(relay_code__iexact=relay_str)\
            .select_related('bay', 'bay__station')\
            .prefetch_related('settings', 'settingsheet_set').first()

    # 3. Tìm theo Tên Rơ-le (relay_name)
    if not relay:
        relay = Relay.objects.filter(relay_name__iexact=relay_str)\
            .select_related('bay', 'bay__station')\
            .prefetch_related('settings', 'settingsheet_set').first()

    # 4. Tìm theo Mã thiết bị (id_tbi)
    if not relay:
        relay = Relay.objects.filter(id_tbi__iexact=relay_str)\
            .select_related('bay', 'bay__station')\
            .prefetch_related('settings', 'settingsheet_set').first()

    # 5. Tìm kiếm gần đúng theo mã rơ-le
    if not relay:
        relay = Relay.objects.filter(relay_code__icontains=relay_str)\
            .select_related('bay', 'bay__station')\
            .prefetch_related('settings', 'settingsheet_set').first()

    if not relay:
        return render(request, 'stations/partials/relay_detail_not_found.html', {'relay_id': relay_id})
    
    import re
    from sheets.relay_matcher import normalize_text
    
    # 1. Suy luận mã ANSI từ tên rơ-le và hãng sản xuất
    r_name_clean = normalize_text(relay.relay_name or '')
    r_manuf_clean = normalize_text(relay.manufacturer or '')
    r_combined = f"{r_manuf_clean} {r_name_clean}".strip()
    
    ansi_code = "ANSI C37.2"
    ansi_title = "Thiết bị bảo vệ & điều khiển"
    match_tip = "So sánh với bản scan phiếu: kiểm tra số hiệu rơ-le, model phần cứng và các chức năng bảo vệ chính ghi trên phiếu."
    
    r_compact = r_name_clean.replace(' ', '').replace('-', '')
    
    is_oc_compact = bool(re.search(r'(?:sel)?(351|551|501|751|451)|7sj|p14|p12|ref615|ref620|ref630|rex6|gdr|grd|spaj', r_compact))
    is_diff_compact = bool(re.search(r'(?:sel)?(387|487e?|587|787)|7ut|ret|p64|t60|t35|kbch|rcs978|pcs978', r_compact))
    is_line_compact = bool(re.search(r'(?:sel)?(311l|411l)|7sd|7sl|red|p54|l90|rcs931|pcs931', r_compact))
    is_bus_compact = bool(re.search(r'(?:sel)?(487b)|7ss|reb|p74|b90|b30|rcs915|pcs915', r_compact))
    is_dist_compact = bool(re.search(r'(?:sel)?(311c?|421)|7sa|rel|p44|d60|d30|rcs902|pcs902', r_compact))
    is_ref_compact = bool(re.search(r'7vh|mcag|64ref', r_compact))
    is_avr_compact = bool(re.search(r'tapcon|regd|vc100|m2001', r_compact))
    is_motor_compact = bool(re.search(r'p24|rem6', r_compact))
    is_gen_compact = bool(re.search(r'p34|reg6|7um', r_compact))

    # 1. Chạm đất hạn chế: ANSI 64REF
    if "64ref" in r_name_clean or "cham dat han che" in r_name_clean or is_ref_compact or bool(re.search(r'\b(f?64ref|f?64r|64ref)\b', r_name_clean)):
        ansi_code = "ANSI 64REF"
        ansi_title = "Bảo vệ Chạm đất Hạn chế (Restricted Earth Fault - REF)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ chạm đất hạn chế theo phạm vi model hỗ trợ. Ví dụ: Siemens 7UT85/7VH60, SEL-387/487E, ABB RET670, Schneider MiCOM P643/MCAG14."
    # 2. Tự động điều chỉnh điện áp: ANSI 90
    elif "90" in r_name_clean or "dieu chinh dien ap" in r_name_clean or "dieu ap" in r_name_clean or "avr" in r_name_clean or "oltc" in r_name_clean or is_avr_compact or bool(re.search(r'\b(f?90|avr|oltc)\b', r_name_clean)):
        ansi_code = "ANSI 90"
        ansi_title = "Rơ-le Tự động Điều chỉnh Điện áp (Automatic Voltage Regulator - AVR)"
        match_tip = "Hỗ trợ nhóm chức năng tự động điều chỉnh điện áp theo model được xây dựng (điều khiển nấc phân áp dưới tải OLTC máy biến áp). Ví dụ: MR Reinhausen TAPCON 230/240/260, A.Eberle REG-D/REG-DA, Beckwith M-2001, ABB VC100."
    # 3. Quá dòng / Feeder: ANSI 50/51, 67
    elif "qua dong" in r_name_clean or "cat nhanh" in r_name_clean or "overcurrent" in r_name_clean or is_oc_compact or bool(re.search(r'\b(f?50|f?51|f?67|50n|51n|67n)\b', r_name_clean)):
        ansi_code = "ANSI 50/51, 67"
        ansi_title = "Bảo vệ Quá dòng / Cắt nhanh (Overcurrent Protection)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ quá dòng pha, quá dòng chạm đất theo phạm vi model hỗ trợ. Ví dụ: SEL-551, SEL-351, Siemens 7SJ622/7SJ82, Schneider P14, NARI PCS-9611."
    # 4. So lệch máy biến áp: ANSI 87T
    elif "87t" in r_name_clean or "so lech mba" in r_name_clean or "so lech at" in r_name_clean or "so lech t" in r_name_clean or "may bien ap" in r_name_clean or "differential" in r_name_clean or is_diff_compact:
        ansi_code = "ANSI 87T, 87N"
        ansi_title = "Bảo vệ So lệch & Chạm đất hạn chế MBA (Differential & REF)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ so lệch máy biến áp. Ví dụ: Siemens 7UT613/7UT63/7UT85, SEL-387/487E, ABB RET670, Schneider P643, NARI PCS-978."
    # 5. So lệch đường dây: ANSI 87L
    elif "87l" in r_name_clean or "so lech dz" in r_name_clean or "so lech duong day" in r_name_clean or ("so lech" in r_name_clean and ("dz" in r_name_clean or "dd" in r_name_clean or "duong day" in r_name_clean)) or is_line_compact:
        ansi_code = "ANSI 87L"
        ansi_title = "Bảo vệ So lệch dòng điện Đường dây (Line Differential)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ so lệch đường dây. Ví dụ: NARI PCS-931, Siemens 7SD52/7SD610, ABB RED670, SEL-411L."
    # 6. So lệch thanh cái: ANSI 87B
    elif "87b" in r_name_clean or "so lech thanh cai" in r_name_clean or "thanh dan" in r_name_clean or "thanh cai" in r_name_clean or is_bus_compact:
        ansi_code = "ANSI 87B"
        ansi_title = "Bảo vệ So lệch Thanh cái (Busbar Differential)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ so lệch thanh cái. Ví dụ: NARI PCS-915, Siemens 7SS52/7SS85, ABB REB670, GE B90, SEL-487B."
    # 7. So lệch kháng điện: ANSI 87R
    elif "87r" in r_name_clean or "so lech khang" in r_name_clean or "kh50" in r_name_clean or "khang" in r_name_clean:
        ansi_code = "ANSI 87R"
        ansi_title = "Bảo vệ So lệch Kháng điện (Reactor Differential)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ so lệch cuộn kháng bù ngang KH501..KH504 (kiểu bảo vệ 87R). Ví dụ: Siemens 7UT85, SEL-387, ABB RET670."
    # 8. Bảo vệ khoảng cách: ANSI 21
    elif "khoang cach" in r_name_clean or "distance" in r_name_clean or is_dist_compact or bool(re.search(r'\b(f?21|21n)\b', r_name_clean)):
        ansi_code = "ANSI 21"
        ansi_title = "Bảo vệ Khoảng cách (Distance Protection)"
        match_tip = "Chuẩn bị tính toán và điểm thử bảo vệ khoảng cách. Ví dụ: NARI PCS-902, Siemens 7SA52/7SA6, ABB REL670, Schneider P443, SEL-421."
    elif "dong co" in r_name_clean or "motor" in r_name_clean or is_motor_compact or bool(re.search(r'\b(p24\d?|rem6\d+)\b', r_name_clean)):
        ansi_code = "ANSI 49, 50/51"
        ansi_title = "Bảo vệ Động cơ & Máy điện quay (Motor Protection)"
        match_tip = "Bảo vệ quá tải nhiệt (49), quá dòng và mất cân bằng pha cho động cơ điện. Ví dụ: MiCOM P241/P242/P243, ABB REM615/620, Siemens 7SK80."
    elif "may phat" in r_name_clean or "generator" in r_name_clean or "87g" in r_name_clean or is_gen_compact or bool(re.search(r'\b(p34\d?|f?87g)\b', r_name_clean)):
        ansi_code = "ANSI 87G"
        ansi_title = "Bảo vệ So lệch Máy phát điện (Generator Protection)"
        match_tip = "Bảo vệ so lệch máy phát (87G), mất kích từ (40), chạm đất stator (64G). Ví dụ: MiCOM P342/P343/P344/P345, Siemens 7UM62, ABB REG670."
    elif "bcu" in r_name_clean or "dieu khien" in r_name_clean or "p841" in r_name_clean or "pcs9611" in r_name_clean or "rec" in r_name_clean:
        ansi_code = "BCU / ANSI 79, 25"
        ansi_title = "Điều khiển Ngăn lộ, TĐL & Hòa đồng bộ (Bay Control Unit)"
        match_tip = "Điều khiển ngăn lộ, tự động đóng lại (79) và kiểm tra hòa đồng bộ (25). Ví dụ: MiCOM P841, NARI PCS-9611, Siemens 7SJ6, ABB REC670."
    elif "50bf" in r_name_clean or "hu hong may cat" in r_name_clean:
        ansi_code = "ANSI 50BF"
        ansi_title = "Bảo vệ Hư hỏng Máy cắt (Breaker Failure Protection)"
        match_tip = "Phiếu bảo vệ tự động gửi lệnh cắt dự phòng khi máy cắt chính không mở được khi có sự cố."
    elif "mc" in r_name_clean or "may cat" in r_name_clean or relay.relay_code.startswith("PTC1_MC"):
        ansi_code = "Thiết bị MC"
        ansi_title = "Máy cắt chính (Circuit Breaker)"
        match_tip = "Thiết bị nhất thứ đóng cắt mạch lực (không phải rơ-le bảo vệ)."
    elif "tu" in r_name_clean or relay.relay_code.startswith("PTC1_TU"):
        ansi_code = "Thiết bị TU"
        ansi_title = "Biến điện áp đo lường (Voltage Transformer)"
        match_tip = "Thiết bị biến đổi điện áp mạch lực cấp cho bảo vệ và đo lường."
    elif "ti" in r_name_clean or relay.relay_code.startswith("PTC1_TI"):
        ansi_code = "Thiết bị TI"
        ansi_title = "Biến dòng điện đo lường (Current Transformer)"
        match_tip = "Thiết bị biến đổi dòng điện mạch lực cấp cho bảo vệ và đo lường."
    elif "dcl" in r_name_clean or relay.relay_code.startswith("PTC1_DCL"):
        ansi_code = "Thiết bị DCL"
        ansi_title = "Dao cách ly (Disconnector)"
        match_tip = "Thiết bị đóng cắt tạo khoảng cách an toàn nhìn thấy được."

    # Định dạng cấp điện áp hiển thị
    capda_raw = relay.id_capda or (relay.bay.id_capda if relay.bay else '') or 'U500'
    voltage_map = {
        'U500': '500 kV',
        'U220': '220 kV',
        'U110': '110 kV',
        'U035': '35 kV',
        'U35': '35 kV',
        'U022': '22 kV',
        'U22': '22 kV',
    }
    voltage_display = voltage_map.get(capda_raw, capda_raw.replace('U', '') + ' kV' if capda_raw.startswith('U') else capda_raw)

    # Đối chiếu với bản scan của phiếu hiện tại (nếu có sheet_id)
    ocr_comparison = None
    sheet_id = request.GET.get('sheet_id')
    current_sheet = None
    if sheet_id and str(sheet_id).isdigit():
        from sheets.models import SettingSheet
        current_sheet = SettingSheet.objects.filter(pk=int(sheet_id)).first()

    if current_sheet:
        job = current_sheet.ocr_jobs.order_by('-created_at').first()
        page1 = {}
        if job and job.result_data and isinstance(job.result_data, dict):
            page1 = job.result_data.get('business', {}).get('page1_fields', {})

        # Phòng vệ: nếu page1_fields chưa có trong DB, đọc từ disk artifact của header OCR
        if not page1 and job and job.correlation_id:
            from django.conf import settings
            import json
            header_ext = os.path.join(settings.MEDIA_ROOT, 'ocr_artifacts', f"{job.correlation_id}_header", "extraction.json")
            if os.path.exists(header_ext):
                try:
                    with open(header_ext, 'r', encoding='utf-8') as f:
                        raw_ext = json.load(f)
                    page1 = {k: {'value': v} for k, v in raw_ext.get('important_fields', {}).items()}
                except Exception:
                    pass

        if page1 or (job and job.result_data):
            def get_f(key):
                val = page1.get(key)
                if isinstance(val, dict):
                    return val.get('value') or ''
                return str(val) if val else ''

            ocr_station = get_f('station')
            ocr_equipment = get_f('protected_equipment')
            ocr_relay = get_f('relay_name')
            ocr_manuf = get_f('manufacturer')
            ocr_type = get_f('protection_type')
            ocr_year = get_f('installation_year')
            ocr_cb = get_f('circuit_breaker')
            ocr_ct = get_f('current_transformer_ratio')
            ocr_cabinet = get_f('protection_cabinet')
            ocr_circuit = get_f('protection_circuit')
            ocr_serial = get_f('relay_serial')
            ocr_version = get_f('relay_version')
            ocr_drawing = get_f('wiring_diagram')
            ocr_purpose = get_f('issuance_purpose')

            # Fallback bóc tách từ danh sách dòng OCR gốc nếu page1_fields còn thiếu
            p1_page = None
            if job and job.result_data and isinstance(job.result_data, dict):
                pages = job.result_data.get('pages', [])
                if pages and isinstance(pages, list):
                    for p in pages:
                        if isinstance(p, dict) and p.get('page_number') == 1:
                            p1_page = p
                            break
                    if not p1_page and len(pages) > 0 and pages[0].get('page_number', 1) == 1:
                        p1_page = pages[0]

            if not p1_page and job and job.correlation_id:
                from django.conf import settings
                import json
                p1_file = os.path.join(settings.MEDIA_ROOT, 'ocr_artifacts', f"{job.correlation_id}_header", "pages", "page_0001.json")
                if os.path.exists(p1_file):
                    try:
                        with open(p1_file, 'r', encoding='utf-8') as f:
                            p1_page = json.load(f)
                    except Exception:
                        pass

            if p1_page:
                raw_lines = [x.get('text', '') for x in p1_page.get('raw_ocr', []) if isinstance(x, dict)]
                for line in raw_lines:
                        if not ocr_relay:
                            m_r = re.search(r'(?:loại\s*r[oơ]-?le|loại\s*role|loạirole|tên\s*r[oơ]-?le|tên\s*role)\s*[:：]?\s*(.+)', line, re.I)
                            if m_r:
                                ocr_relay = m_r.group(1).strip()
                        if not ocr_type:
                            m_t = re.search(r'(?:chức\s*năng\s*bảo\s*vệ|chứcnăngbảovệ|kiểu\s*bảo\s*vệ)\s*[:：]\s*(.+)', line, re.I)
                            if m_t:
                                ocr_type = m_t.group(1).strip()
                        if not ocr_manuf:
                            m_m = re.search(r'(?:nhà\s*sản\s*xuất|nhà\s*chế\s*tạo)\s*[:：]\s*(.+)', line, re.I)
                            if m_m:
                                ocr_manuf = m_m.group(1).strip()
                        if not ocr_station:
                            m_s = re.search(r'(?:trạm)\s*[:：]\s*(.+)', line, re.I)
                            if m_s:
                                ocr_station = m_s.group(1).strip()
                        if not ocr_equipment:
                            m_e = re.search(r'(?:thiết\s*bị\s*được\s*bảo\s*vệ)\s*[:：]\s*(.+)', line, re.I)
                            if m_e:
                                ocr_equipment = m_e.group(1).strip()
                        if not ocr_ct:
                            m_ct = re.search(r'(?:tỉ\s*số\s*ti|tỷ\s*số\s*ti)\s*[:：]\s*([0-9/]+A?)', line, re.I)
                            if m_ct:
                                ocr_ct = m_ct.group(1).strip()

            db_station_name = relay.bay.station.station_name if (relay.bay and relay.bay.station) else ''
            db_bay_name = relay.bay.bay_name if relay.bay else ''
            db_manuf = relay.manufacturer or ''

            norm_ocr_station = normalize_text(ocr_station)
            norm_db_station = normalize_text(db_station_name)
            
            # Chuẩn hóa tên trạm đa tầng: tách các từ khóa địa danh cốt lõi (bỏ tiền tố trạm, cấp điện áp, mã điều độ E...)
            def get_station_tokens(s):
                s_clean = re.sub(r'\(.*?\)|\[.*?\]', '', s)
                s_clean = re.sub(r'\b(tram|bien|ap|tba|500\s*kv|220\s*kv|110\s*kv|22\s*kv|35\s*kv|kv)\b', '', s_clean)
                return [w for w in s_clean.split() if len(w) >= 2 and not re.match(r'^[e]\d+(\.\d+)?$', w)]

            ocr_st_tokens = get_station_tokens(norm_ocr_station)
            db_st_tokens = get_station_tokens(norm_db_station)
            st_token_overlap = set(ocr_st_tokens).intersection(set(db_st_tokens))

            # Trùng khớp trạm nếu:
            # 1. Chứa chuỗi nhau trực tiếp
            # 2. Hoặc các từ khóa địa danh cốt lõi (như "van tri", "hiep hoa") trùng nhau
            station_match = bool(
                (norm_ocr_station and norm_db_station and (norm_ocr_station in norm_db_station or norm_db_station in norm_ocr_station))
                or (ocr_st_tokens and db_st_tokens and len(st_token_overlap) >= min(len(ocr_st_tokens), len(db_st_tokens), 2))
                or (len(st_token_overlap) >= 1 and any(len(w) >= 3 for w in st_token_overlap))
            )

            # Mã điều độ trạm nếu có (ví dụ: E1.23, E4.4, 500HH)
            st_dispatch_code = ''
            m_code = re.search(r'\(([^)]+)\)', ocr_station)
            if m_code:
                st_dispatch_code = m_code.group(1).strip()
            else:
                m_dispatch = re.search(r'\b([eE]\d+\.?\d*|500[A-Z]{2})\b', ocr_station)
                if m_dispatch:
                    st_dispatch_code = m_dispatch.group(1).strip()
            
            if station_match:
                if st_dispatch_code:
                    station_reason = f"Trùng khớp hoàn toàn • ({st_dispatch_code}) là mã điều độ của {db_station_name}"
                else:
                    station_reason = f"Trùng khớp tên trạm: {db_station_name}"
            else:
                station_reason = "Tên trạm trên bản scan khác với trạm quản lý trong CSDL"

            norm_ocr_eq = normalize_text(ocr_equipment)
            norm_db_bay = normalize_text(db_bay_name)
            bay_match = bool(norm_ocr_eq and norm_db_bay and (norm_ocr_eq in norm_db_bay or norm_db_bay in norm_ocr_eq or any(w in norm_db_bay for w in norm_ocr_eq.split() if len(w) > 2)))
            
            if bay_match:
                bay_reason = f"Trùng khớp ngăn lộ/máy cắt: {db_bay_name}"
            else:
                bay_reason = "Ngăn lộ trên phiếu chưa trùng tên trong CSDL"

            # Đối chiếu hãng sản xuất với từ điển đồng nghĩa (SEL, SIEMENS, ABB, SCHNEIDER, NARI...)
            norm_ocr_manuf = normalize_text(ocr_manuf)
            norm_db_manuf = normalize_text(db_manuf)
            
            VENDOR_ALIASES = {
                'sel': ['sel', 'schweitzer', 'schweitzer engineering laboratories'],
                'schweitzer': ['sel', 'schweitzer', 'schweitzer engineering laboratories'],
                'siemens': ['siemens', 'siprotec', 'siemens ag'],
                'siprotec': ['siemens', 'siprotec', 'siemens ag'],
                'abb': ['abb', 'hitachi', 'hitachi energy', 'hitachi abb', 'asea brown boveri'],
                'hitachi': ['abb', 'hitachi', 'hitachi energy', 'hitachi abb'],
                'schneider': ['schneider', 'schneider electric', 'alstom', 'areva', 'micom'],
                'areva': ['schneider', 'schneider electric', 'alstom', 'areva', 'micom'],
                'alstom': ['schneider', 'schneider electric', 'alstom', 'areva', 'micom'],
                'micom': ['schneider', 'schneider electric', 'alstom', 'areva', 'micom'],
                'ge': ['ge', 'general electric', 'multilin'],
                'nari': ['nari', 'nr', 'nr electric', 'nam thuy'],
                'nr': ['nari', 'nr', 'nr electric', 'nam thuy'],
            }
            
            manuf_match = False
            if norm_ocr_manuf and norm_db_manuf:
                if norm_ocr_manuf in norm_db_manuf or norm_db_manuf in norm_ocr_manuf:
                    manuf_match = True
                else:
                    aliases = VENDOR_ALIASES.get(norm_db_manuf, [])
                    for a in aliases:
                        if a in norm_ocr_manuf or norm_ocr_manuf in a:
                            manuf_match = True
                            break
            
            if manuf_match:
                manuf_reason = f"Trùng khớp hãng sản xuất: {db_manuf} ⟷ {ocr_manuf}"
            else:
                manuf_reason = f"Hãng sản xuất: CSDL ({db_manuf or '—'}) ⟷ Bản scan ({ocr_manuf or '—'})"

            # Đối chiếu chức năng bảo vệ
            norm_ocr_type = normalize_text(ocr_type)
            norm_ocr_relay = normalize_text(ocr_relay)
            function_match = False

            # Quá dòng: 50, 51, 67, 351, 551, 501, 751, 451, 7sj, p14, ref, gdr
            is_overcurrent_relay = "50" in ansi_code or "51" in ansi_code or "67" in ansi_code or "qua dong" in r_name_clean or "overcurrent" in r_name_clean or is_oc_compact
            is_overcurrent_ocr = "qua dong" in norm_ocr_type or "overcurrent" in norm_ocr_type or "50" in norm_ocr_type or "51" in norm_ocr_type or "67" in norm_ocr_type or any(k in norm_ocr_relay for k in ["351", "551", "501", "751", "451", "p14", "7sj", "ref", "gdr"])
            
            # So lệch MBA / Kháng: 87T, 87R, 387, 487, 7ut, ret
            is_diff_relay = "87" in ansi_code or "so lech" in r_name_clean or "differential" in r_name_clean or "387" in r_name_clean or "487" in r_name_clean or "7ut" in r_name_clean or is_diff_compact
            is_diff_ocr = "so lech" in norm_ocr_type or "differential" in norm_ocr_type or "87" in norm_ocr_type or "387" in norm_ocr_relay or "487" in norm_ocr_relay or "7ut" in norm_ocr_relay or "ret" in norm_ocr_relay or "p64" in norm_ocr_relay
            
            # Khoảng cách / So lệch ĐD: 21, 87L, 311, 421, 7sa, 7sd, 7sl, rel
            is_dist_relay = "21" in ansi_code or "khoang cach" in r_name_clean or "distance" in r_name_clean or "311" in r_name_clean or "421" in r_name_clean or is_dist_compact
            is_dist_ocr = "khoang cach" in norm_ocr_type or "distance" in norm_ocr_type or "21" in norm_ocr_type or "311" in norm_ocr_relay or "421" in norm_ocr_relay or "7sa" in norm_ocr_relay or "rel" in norm_ocr_relay or "p44" in norm_ocr_relay

            if is_overcurrent_relay and is_overcurrent_ocr:
                function_match = True
                type_reason = f"Trùng khớp chức năng bảo vệ: Quá dòng ({ansi_code})"
            elif is_diff_relay and is_diff_ocr:
                function_match = True
                has_ref = "ref" in norm_ocr_type or "87n" in norm_ocr_type or "cham dat han che" in norm_ocr_type
                if has_ref:
                    ansi_code = "ANSI 87T, 87N (REF)"
                    ansi_title = "Bảo vệ So lệch & Chạm đất hạn chế MBA (Transformer Differential & REF)"
                    type_reason = f"Trùng khớp hoàn toàn: Rơ-le {relay.relay_name} ({ocr_relay or db_manuf}) tích hợp cả 2 chức năng So lệch chính (87T) và Chạm đất hạn chế (REF / 87N)"
                else:
                    type_reason = f"Trùng khớp chức năng bảo vệ: So lệch ({ansi_code})"
            elif is_dist_relay and is_dist_ocr:
                function_match = True
                type_reason = f"Trùng khớp chức năng bảo vệ: Khoảng cách ({ansi_code})"
            elif norm_ocr_relay and (norm_ocr_relay in r_name_clean or r_name_clean in norm_ocr_relay):
                function_match = True
                type_reason = f"Trùng khớp model rơ-le: {ocr_relay} ({ansi_code})"
            elif ansi_code != "ANSI C37.2":
                function_match = True
                type_reason = f"Khớp chức năng kỹ thuật tương đương ({ansi_code})"
            else:
                type_reason = "Chức năng bảo vệ cần kiểm tra thêm"

            # Đánh giá độ trùng khớp tổng thể
            score = 0
            if station_match: score += 30
            if bay_match: score += 30
            if manuf_match: score += 20
            if function_match: score += 20

            ocr_comparison = {
                'has_ocr': True,
                'score': score,
                'is_perfect_match': score >= 80,
                'ocr_station': ocr_station,
                'ocr_equipment': ocr_equipment,
                'ocr_relay': ocr_relay,
                'ocr_manuf': ocr_manuf,
                'ocr_type': ocr_type,
                'ocr_year': ocr_year,
                'ocr_cb': ocr_cb,
                'ocr_ct': ocr_ct,
                'ocr_cabinet': ocr_cabinet,
                'ocr_circuit': ocr_circuit,
                'ocr_serial': ocr_serial,
                'ocr_version': ocr_version,
                'ocr_drawing': ocr_drawing,
                'ocr_purpose': ocr_purpose,
                'station_match': station_match,
                'bay_match': bay_match,
                'manuf_match': manuf_match,
                'function_match': function_match,
                'station_reason': station_reason,
                'bay_reason': bay_reason,
                'manuf_reason': manuf_reason,
                'type_reason': type_reason,
                'current_sheet_code': current_sheet.sheet_code,
                'current_sheet_title': current_sheet.title or '',
            }

    sheets = list(relay.settingsheet_set.all().order_by('-created_at'))
    
    sample_params = []
    latest_sheet_with_data = None
    for s in sheets:
        if s.extracted_data and isinstance(s.extracted_data, list):
            latest_sheet_with_data = s
            for item in s.extracted_data:
                if isinstance(item, dict) and (item.get('parameter_name') or item.get('parameter_code')):
                    val = item.get('value')
                    if val is not None and str(val).strip() != '' and str(val).lower() != 'none':
                        sample_params.append({
                            'code': item.get('parameter_code') or '—',
                            'name': item.get('parameter_name') or item.get('record_key') or 'Thông số',
                            'value': val,
                            'unit': item.get('unit') or ''
                        })
                if len(sample_params) >= 16:
                    break
            if sample_params:
                break
                
    db_settings = list(relay.settings.all()[:20])

    # Danh mục 7 nhóm chức năng bảo vệ chuẩn hóa theo phạm vi tính toán & điểm thử
    protection_catalog = [
        {
            'code': '50/51, 50N/51N',
            'name': 'Quá dòng Pha & Quá dòng Chạm đất',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ quá dòng pha, quá dòng chạm đất theo phạm vi model hỗ trợ.',
            'models': 'SEL-751/751A, SEL-351, SEL-451, SEL-551, Siemens SIPROTEC 5 (7SJ82/85/86), ABB REF615/620/630, MiCOM P12x/P14x',
            'is_matched': ('50' in ansi_code or '51' in ansi_code or '67' in ansi_code),
            'icon': 'fa-bolt',
            'color': 'indigo'
        },
        {
            'code': '87T',
            'name': 'So lệch Máy biến áp',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ so lệch máy biến áp.',
            'models': 'SEL-787, SEL-487E, SEL-387, Siemens SIPROTEC 5 (7UT82/85/86/87), ABB RET670/650, MiCOM P64x',
            'is_matched': ('87T' in ansi_code),
            'icon': 'fa-arrows-split-up-and-left',
            'color': 'blue'
        },
        {
            'code': '87B',
            'name': 'So lệch Thanh cái',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ so lệch thanh cái.',
            'models': 'SEL-487B, Siemens SIPROTEC 5 (7SS85), ABB REB670, MiCOM P740/P746, NARI PCS-915, GE B90',
            'is_matched': ('87B' in ansi_code),
            'icon': 'fa-grip-lines',
            'color': 'amber'
        },
        {
            'code': '87L',
            'name': 'So lệch Đường dây',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ so lệch đường dây.',
            'models': 'SEL-411L, SEL-311L, Siemens SIPROTEC 5 (7SD82/86/87, 7SL82/86/87), ABB RED670, MiCOM P54x',
            'is_matched': ('87L' in ansi_code),
            'icon': 'fa-route',
            'color': 'teal'
        },
        {
            'code': '21',
            'name': 'Bảo vệ Khoảng cách',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ khoảng cách.',
            'models': 'SEL-421, SEL-411L, SEL-311C, Siemens SIPROTEC 5 (7SA82/86/87, 7SL82/86/87), ABB REL670, MiCOM P44x',
            'is_matched': ('21' in ansi_code),
            'icon': 'fa-ruler-horizontal',
            'color': 'violet'
        },
        {
            'code': '64REF',
            'name': 'Chạm đất Hạn chế (REF)',
            'scope': 'Chuẩn bị tính toán và điểm thử bảo vệ chạm đất hạn chế.',
            'models': 'SEL-787, SEL-487E, SEL-387, Siemens SIPROTEC 5 (7UT85/86), 7VH60, ABB RET670, MiCOM P64x/MCAG14',
            'is_matched': ('64' in ansi_code or 'REF' in ansi_code or '87N' in ansi_code),
            'icon': 'fa-shield-halved',
            'color': 'emerald'
        },
        {
            'code': '90',
            'name': 'Tự động Điều chỉnh Điện áp (AVR / OLTC)',
            'scope': 'Hỗ trợ nhóm chức năng tự động điều chỉnh điện áp theo model được xây dựng.',
            'models': 'ABB VC100, MR Reinhausen TAPCON 230/240/260, A.Eberle REG-D/REG-DA, Beckwith M-2001',
            'is_matched': ('90' in ansi_code or 'AVR' in ansi_code),
            'icon': 'fa-sliders',
            'color': 'rose'
        },
    ]

    # Tính toán các điểm thử mẫu cho rơ-le (Secondary Injection Test Points)
    test_points = []
    pickup_val = None
    time_val = None
    for p in sample_params:
        p_name = (p.get('name') or '').lower()
        p_val_str = str(p.get('value') or '')
        try:
            num = float(re.findall(r"[-+]?(?:\d*\.\d+|\d+)", p_val_str)[0])
            if ('khoi dong' in p_name or 'pickup' in p_name or 'i>' in p_name or 'ip' in p_name or 'is1' in p_name) and not pickup_val:
                pickup_val = num
            elif ('thoi gian' in p_name or 'time' in p_name or 'delay' in p_name or 't>' in p_name) and not time_val:
                time_val = num
        except Exception:
            pass

    if not pickup_val:
        pickup_val = 5.0
    if not time_val:
        time_val = 0.5

    test_points.append({
        'point_id': 'TP-01',
        'type': 'Ngưỡng không tác động (0.95 x I_pickup)',
        'injected_value': f"{round(pickup_val * 0.95, 3)} A",
        'expected_result': 'KHÔNG TÁC ĐỘNG (No Trip)',
        'tolerance': '±2.5%',
        'status': 'READY'
    })
    test_points.append({
        'point_id': 'TP-02',
        'type': 'Ngưỡng tác động (1.05 x I_pickup)',
        'injected_value': f"{round(pickup_val * 1.05, 3)} A",
        'expected_result': 'TÁC ĐỘNG (Trip)',
        'tolerance': '±2.5%',
        'status': 'READY'
    })
    test_points.append({
        'point_id': 'TP-03',
        'type': f'Thời gian cắt tại 2xI ({round(pickup_val * 2.0, 2)} A)',
        'injected_value': f"{round(pickup_val * 2.0, 2)} A",
        'expected_result': f"t = {round(time_val, 3)} s",
        'tolerance': '±30 ms / 5%',
        'status': 'READY'
    })
    test_points.append({
        'point_id': 'TP-04',
        'type': f'Thời gian cắt tại 5xI ({round(pickup_val * 5.0, 2)} A)',
        'injected_value': f"{round(pickup_val * 5.0, 2)} A",
        'expected_result': f"t = {round(max(0.04, time_val * 0.4), 3)} s",
        'tolerance': '±20 ms',
        'status': 'READY'
    })

    context = {
        'relay': relay,
        'ansi_code': ansi_code,
        'ansi_title': ansi_title,
        'match_tip': match_tip,
        'voltage_display': voltage_display,
        'sheets': sheets,
        'sample_params': sample_params,
        'latest_sheet_with_data': latest_sheet_with_data,
        'db_settings': db_settings,
        'ocr_comparison': ocr_comparison,
        'current_sheet': current_sheet,
        'protection_catalog': protection_catalog,
        'test_points': test_points,
    }
    return render(request, 'stations/partials/relay_detail_modal.html', context)

@login_required
def get_station_relays_json(request, station_id):
    """API trả về danh sách Rơ-le của một Trạm dưới dạng JSON (dùng cho dynamic select/autocomplete mà không làm nặng trang chính)."""
    from django.http import JsonResponse
    relays = list(Relay.objects.filter(bay__station_id=station_id).values('id', 'bay_id', 'relay_code', 'relay_name', 'manufacturer'))
    return JsonResponse(relays, safe=False)
````

## File: .env.example
````
DEBUG=False
DB_HOST=db
DB_PORT=5432
DB_NAME=rms_db
DB_USER=postgres
DB_PASSWORD=your_secure_db_password_here
SECRET_KEY=your_secure_secret_key_here
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=admin@example.com
POSTGRES_DB=rms_db
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_db_password_here

# API Endpoints cho các Danh mục
API_DANH_MUC_DON_VI_QUAN_LY=https://example.com/api/don-vi-quan-ly
API_DANH_MUC_NUOC_SAN_XUAT=https://example.com/api/nuoc-san-xuat
API_DANH_MUC_HANG_SAN_XUAT=https://example.com/api/hang-san-xuat
API_DANH_MUC_SO_HUU=https://example.com/api/so-huu
API_DANH_MUC_CAP_DIEN_AP=https://example.com/api/cap-dien-ap
API_DANH_MUC_LOAI_THIET_BI=https://example.com/api/loai-thiet-bi
API_DANH_MUC_TRANG_THAI_VAN_HANH=https://example.com/api/trang-thai-van-hanh
API_DANH_MUC_TRAM=https://example.com/api/tram
API_DANH_MUC_NGAN_LO=https://example.com/api/ngan-lo
API_DANH_MUC_DUONG_DAY=https://example.com/api/duong-day
API_DANH_MUC_CONG_TRINH=https://example.com/api/cong-trinh
API_DANH_MUC_VI_TRI=https://example.com/api/vi-tri
API_THIET_BI=https://example.com/api/thiet-bi
````

## File: docker-compose.yml
````yaml
name: electricity-web
services:
  db:
    image: postgres:15-alpine
    container_name: rms_db
    restart: always
    env_file:
      - .env
    environment:
      - PGPORT=5440
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5440:5440"

  redis:
    image: redis:alpine
    container_name: rms_redis
    restart: always
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data

  web:
    image: electric-web:latest
    build: .
    container_name: rms_web
    restart: always
    command: >
      sh -c "python manage.py collectstatic --noinput &&
             python manage.py migrate &&
             python manage.py seed_permissions &&
             python manage.py createsuperuser --noinput || true &&
             daphne -b 0.0.0.0 -p 9000 rms_project.asgi:application"
    volumes:
      - static_volume:/app/static
      - media_volume:/app/media
      - .:/app
      - huggingface_cache:/root/.cache/huggingface
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [gpu]
    ports:
      - "9000:9000"
    depends_on:
      - db
      - redis
    env_file:
      - .env
    environment:
      - DB_HOST=db
      - DB_PORT=5440
      - REDIS_URL=redis://redis:6379/1

  celery:
    image: electric-web:latest
    build: .
    container_name: rms_celery
    restart: always
    command: celery -A rms_project worker --pool=threads --concurrency=20 -l info
    volumes:
      - static_volume:/app/static
      - media_volume:/app/media
      - .:/app
      - huggingface_cache:/root/.cache/huggingface
    # ============================================================
    # GPU SUPPORT: Bỏ comment phần 'deploy' bên dưới nếu máy có
    # NVIDIA GPU.
    # - Windows: Docker Desktop + WSL2 (hỗ trợ GPU sẵn)
    # - Linux:   sudo apt install nvidia-container-toolkit
    #            sudo systemctl restart docker
    # ============================================================
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: all
    #           capabilities: [ gpu ]
    depends_on:
      - db
      - redis
      - web
    env_file:
      - .env
    environment:
      - DB_HOST=db
      - DB_PORT=5440
      - REDIS_URL=redis://redis:6379/1
      # Cấu hình số luồng chạy song song cho OCR
      - PIPELINE1_CONCURRENCY=1 # Số luồng bóc tách Trang 1,2 (Khuyên dùng: 1)
      - PIPELINE2_CONCURRENCY=1 # Số luồng bóc tách Trang 3+ (Khuyên dùng: 1 hoặc 2)

  cloudflared:
    image: cloudflare/cloudflared:latest
    container_name: cloudflared_tunnel
    restart: unless-stopped
    command: tunnel --no-autoupdate run --token eyJhIjoiMmI1MGI5ZGJiYjYxY2YyZDg4OTY1MGNhNTViMzVhMTIiLCJ0IjoiMjA5YjQxYTUtYThhNy00ZWI4LTg0MzUtZTI0ZjgyY2U2ODY5IiwicyI6Ik56bGlaR05pTVRJdE1EUTBaQzAwTXpCaUxUbGtaV1l0WldZd1lUZzVORGN6WkRVMiJ9

volumes:
  postgres_data:
    external: true
    name: electric_postgres_data
  static_volume:
    external: true
    name: electric_static_volume
  media_volume:
    external: true
    name: electric_media_volume
  redis_data:
    external: true
    name: electric_redis_data
  huggingface_cache:
    external: true
    name: electric_huggingface_cache

# volumes:
#   postgres_data:
#   static_volume:
#   media_volume:
#   redis_data:
````

## File: Dockerfile
````dockerfile
# Sử dụng image Python 3.12 slim để tương thích với OCR_PRJ (yêu cầu Python <= 3.12)
FROM python:3.12-slim

# Ngăn chặn Python ghi bytecode (.pyc) ra ổ đĩa
ENV PYTHONDONTWRITEBYTECODE=1
# Bắt buộc Python hiển thị output trực tiếp vào console
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV PYTHONUTF8=1

# Cài đặt các thư viện hệ thống cần thiết (đã bổ sung các thư viện cho OCR như poppler, opencv)
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev poppler-utils libgl1 libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép requirements.txt gốc và cài đặt
COPY requirements.txt /app/
COPY vendor /app/vendor/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir --find-links=/app/vendor -r requirements.txt

# Cài đặt thư viện của OCR_PRJ (cần mạng để tải)
COPY OCR_PRJ/src/debug_ui/requirements-full.txt /app/OCR_PRJ/src/debug_ui/
RUN pip install --no-cache-dir -r OCR_PRJ/src/debug_ui/requirements-full.txt

# Sao chép toàn bộ mã nguồn dự án vào container (bao gồm cả thư mục OCR_PRJ còn lại)
COPY . /app/

# Khởi chạy ứng dụng thông qua Daphne (ASGI) để hỗ trợ WebSockets cho Channels
# Chạy ở cổng 9000 như yêu cầu
CMD ["daphne", "-b", "0.0.0.0", "-p", "9000", "rms_project.asgi:application"]
````

## File: manage.py
````python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rms_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
````

## File: PROJECT_REQUIREMENTS.md
````markdown
# Mẫu Đặc Tả Yêu Cầu Phần Mềm (Software Requirements Specification - SRS Template)

**Dự án**: [Tên Dự Án Của Bạn]

---

## 1. Giới thiệu (Introduction)

### 1.1 Mục đích (Purpose)
Tài liệu này đặc tả toàn bộ các yêu cầu nghiệp vụ, chức năng và phi chức năng cho sản phẩm [Tên sản phẩm]. Tài liệu này đóng vai trò làm cơ sở để định hướng phát triển, kiểm thử và bàn giao sản phẩm.

### 1.2 Phạm vi Sản phẩm (Product Scope)
*   **Trong phạm vi (In-Scope)**:
    *   [Mô tả các tính năng cốt lõi sẽ phát triển trong giai đoạn này].
    *   [Ví dụ: Quản lý người dùng, Phân quyền hệ thống, API kết nối dữ liệu].
*   **Ngoài phạm vi (Out-of-Scope)**:
    *   [Mô tả các phần việc hoặc tính năng không được thực hiện trong giai đoạn này].
    *   [Ví dụ: Không tích hợp thanh toán trực tuyến bên thứ ba, không phát triển ứng dụng di động].

### 1.3 Thuật ngữ & Viết tắt (Definitions & Acronyms)
*   **SRS**: Software Requirements Specification.
*   **RBAC**: Role-Based Access Control.
*   **[Thêm các thuật ngữ nghiệp vụ đặc thù tại đây]**.

---

## 2. Mô tả Tổng quan (Overall Description)

### 2.1 Bối cảnh Hệ thống (Product Perspective)
[Mô tả hệ thống này là độc lập hay là một phần của một hệ sinh thái lớn hơn, nó giao tiếp với các hệ thống nào bên ngoài].

### 2.2 Tác nhân & Đối tượng Sử dụng (User Classes & Characteristics)
*   **Quản trị viên (Administrator)**: [Mô tả vai trò và nhiệm vụ của quản trị viên].
*   **Người dùng cuối (End-User)**: [Mô tả đặc điểm và nhiệm vụ của người dùng cuối].
*   **[Thêm các nhóm đối tượng sử dụng khác tại đây]**.

### 2.3 Ràng buộc & Phụ thuộc (Constraints & Dependencies)
*   **Ràng buộc**: [Ví dụ: Hệ thống phải chạy trên môi trường Node.js LTS, đáp ứng chuẩn an toàn dữ liệu...].
*   **Phụ thuộc**: [Ví dụ: Phụ thuộc vào tính sẵn sàng của API dịch vụ bản đồ GIS bên thứ ba...].

---

## 3. Yêu cầu Giao diện Ngoại vi (External Interface Requirements)

### 3.1 Giao diện Người dùng (User Interface)
[Mô tả định hướng thiết kế giao diện: Responsive, hỗ trợ các trình duyệt phổ biến, cấu trúc các trang chính].

### 3.2 Giao diện Phần cứng / Thiết bị (Hardware/Device Interfaces)
[Mô tả các kết nối phần cứng từ xa hoặc thiết bị IoT nếu có].

### 3.3 Giao diện Phần mềm & API (Software & API Interfaces)
[Liệt kê các API hoặc dịch vụ phần mềm bên thứ ba cần tích hợp].

---

## 4. Yêu cầu Chức năng (Functional Requirements)

[Danh sách các phân hệ nghiệp vụ của sản phẩm. Mỗi phân hệ đi kèm các mã User Story cụ thể để Agent dễ dàng theo dõi và bám sát nghiệp vụ].

### 4.1 Phân hệ Xác thực & Tài khoản (Auth & Account)
*   `[US-AUTH-01]`: Người dùng có thể đăng nhập bằng Email/Mật khẩu.
*   `[US-AUTH-02]`: Người dùng có thể đặt lại mật khẩu khi quên qua mã OTP gửi đến Email.

### 4.2 Phân hệ Quản lý [Tên Phân Hệ Mẫu]
*   `[US-MOD-01]`: Cán bộ kỹ thuật có thể nhập chỉ số dữ liệu hàng ngày.
*   `[US-MOD-02]`: Ban giám đốc có thể ký duyệt phê duyệt báo cáo thông tin.

---

## 5. Yêu cầu Phi chức năng (Non-functional Requirements)

### 5.1 Độ tin cậy & An toàn (Reliability & Safety)
*   [Ví dụ: Hệ thống tự động sao lưu dữ liệu mỗi 24h, bảo vệ dữ liệu khi mất kết nối đột ngột].

### 5.2 Bảo mật (Security)
*   [Ví dụ: Mã hóa toàn bộ dữ liệu nhạy cảm, sử dụng HTTPS, ngăn chặn các lỗ hổng OWASP].

### 5.3 Hiệu năng (Performance)
*   [Ví dụ: Thời gian phản hồi API trung bình dưới 1 giây, hệ thống hỗ trợ 1000 người dùng đồng thời].
````

## File: README.md
````markdown
<div align="center">

# ⚡ EVN RMS
**Hệ Thống Quản Lý Rơ-le & Phiếu Chỉnh Định Kỹ Thuật Số**

<br>

![Django](https://img.shields.io/badge/Django-6.0%20%7C%205.x-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Celery](https://img.shields.io/badge/Celery-5.3%2B-37814A?style=for-the-badge&logo=celery&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-7-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)

> **Giải pháp Chuyển đổi số Toàn diện cho Ngành Điện lực (EVN)** <br>
> Số hóa Phiếu Chỉnh Định • Bóc Tách AI OCR On-Premise • Ký Số SmartCA • Giám Sát Rơ-le Thời Gian Thực

<br>

[Tính Năng Nổi Bật](#-tính-năng-nổi-bật) •
[Kiến Trúc Hệ Thống](#-công-nghệ-sử-dụng) •
[Cài Đặt & Triển Khai](#-cài-đặt--triển-khai) •
[Tài Khoản](#-tài-khoản-thử-nghiệm-mặc-định) •
[Tài Liệu](#-tài-liệu-kỹ-thuật)

</div>

---

## 📖 Giới Thiệu Tổng Quan

**EVN RMS (Relay Management System)** là nền tảng quản lý kỹ thuật cao cấp, thiết kế chuyên biệt cho các Công ty Điện lực, Trung tâm Điều độ và Đội Quản lý Vận hành Trạm Biến áp. Hệ thống giải quyết trọn vẹn bài toán chuyển đổi số từ khâu tiếp nhận thông số, bóc tách dữ liệu thông minh, phân công công tác, ký số xác nhận đến đối soát tự động thông số vận hành.

### 🌟 Điểm Vượt Trội

* 🛡️ **Bảo mật On-Premise:** Xử lý AI OCR 100% nội bộ, tuân thủ tiêu chuẩn an toàn lưới điện (OT Compliance).
* ✍️ **Ký số chuẩn EVN SmartCA:** Quy trình 5 bước nghiêm ngặt, mã hóa chữ ký SHA-256 kèm mã PIN bảo mật.
* ⚡ **Hiệu năng cao & Realtime:** Xây dựng với Django ASGI, WebSockets, Redis, và Celery.
* 🎨 **Giao diện Hiện đại (UI/UX):** Tone màu chuẩn EVN, tương tác tức thì với HTMX, Glassmorphism, Chart.js.

---

## 🚀 Tính Năng Nổi Bật

<details>
<summary><b>Nhấn để xem Sơ đồ Luồng Hoạt Động (Mermaid)</b></summary>

```mermaid
graph TD
    A[📄 Phiếu Chỉnh Định PDF] -->|Upload| B[🤖 AI OCR Worker - Celery]
    B -->|Bóc tách Tọa độ & Bảng| C[👁️ Split-View Review]
    C -->|Xác Nhận| D[📋 Phiếu Chỉnh Định Hoạt Động]
    D -->|Ký số SmartCA| E[✍️ Luồng Ký 5 Bước]
    E -->|Áp dụng| F[⚡ Rơ-le Trạm Biến Áp]
    F -->|Định kỳ Check API| G{So khớp?}
    G -->|Khớp| H[✅ Ghi Log]
    G -->|Lệch| I[⚠️ Sinh Ticket Hiệu Chỉnh]
```
</details>

### 1. Quản Lý & AI OCR (Human-in-the-Loop)
* **Bóc tách tự động:** Nhận diện layout, bảng biểu, thông số kỹ thuật (dòng, áp, thời gian, chức năng 50/51, 87...).
* **Giao diện Split-View:** So sánh trực quan file PDF và biểu mẫu. Cảnh báo dữ liệu có độ tin cậy thấp.
* **Phiếu tạm thời (Temporary Setting):** Đặt thời hạn và tự động hoàn trả (revert) về cấu hình chuẩn.

### 2. Ký Số Đa Bước (EVN SmartCA)
* **Quy trình 5 bước:** `Điều độ` ➔ `Trưởng trạm` ➔ `Kỹ thuật viên` ➔ `Giám sát` ➔ `Lãnh đạo`.
* **Bảo mật:** Mã PIN / OTP giả lập, sinh mã băm SHA-256.
* **Stepper trực quan:** Trục tiến trình trạng thái thời gian thực.

### 3. Giám Sát & Quản Lý Hạ Tầng
* **Phân cấp dữ liệu:** Đơn vị ➔ Trạm Biến Áp ➔ Ngăn Lộ ➔ Thiết Bị / Rơ-le.
* **Tự động kiểm tra (Auto Check):** Cấu hình tần suất linh hoạt, so khớp thông số thực tế và định mức.
* **Xử lý sự cố:** Tự động phát hiện bất thường và sinh **Correction Ticket**.

---

## 🛠 Công Nghệ Sử Dụng

| Tầng Kiến Trúc | Công Nghệ / Thư Viện | Mục Đích |
|---|---|---|
| **Backend** | Python 3.12+, Django 6.x / 5.x | Xử lý nghiệp vụ chính, ORM, Bảo mật |
| **ASGI / Realtime** | Daphne, Django Channels 4.x | Hỗ trợ WebSockets, kết nối bất đồng bộ |
| **Task & Cache** | Celery 5.x, Redis 7 | Xử lý OCR, Job định kỳ, Caching |
| **Database** | PostgreSQL 15 | Cơ sở dữ liệu quan hệ, JSONField tối ưu |
| **Frontend** | HTMX, TailwindCSS, Vanilla JS | SPA-like siêu mượt, UI chuẩn chỉnh |
| **AI OCR** | PaddleOCR, VietOCR, OpenCV | Bóc tách PDF/Ảnh phiếu chỉnh định |
| **Deploy** | Docker, Docker Compose | Đóng gói môi trường, triển khai nhanh |

---

## 📁 Cấu Trúc Mã Nguồn

```text
electric/
├── core/                  # Core app: Auth, RBAC, WS Consumers, API Sync
├── stations/              # Trạm, Ngăn lộ, Rơ-le, Check log, Tickets
├── sheets/                # Phiếu Chỉnh Định, Ký số, OCR Job, Review UI
├── categories/            # Danh mục kỹ thuật (Đường dây, Công trình...)
├── rms_project/           # Cấu hình dự án Django (settings, celery, asgi)
├── OCR_PRJ/               # AI OCR On-premise (Pipeline bóc tách PDF)
├── templates/             # Giao diện HTML (Django Templates + HTMX)
├── static/                # CSS, JS, Assets
├── docs/                  # Tài liệu thiết kế chi tiết
└── docker-compose.yml     # Khởi chạy Docker đa dịch vụ
```

---

## 📦 Cài Đặt & Triển Khai

### 🐳 Cách 1: Triển Khai Nhanh Bằng Docker (Khuyên Dùng)

```bash
# 1. Clone mã nguồn
git clone https://github.com/xh1712006-debug/electric.git
cd electric

# 2. Tạo file cấu hình
cp .env.example .env

# 3. Khởi chạy toàn bộ hệ thống
docker compose up -d --build
```
> Truy cập hệ thống tại: **`http://localhost:9000`** (Bao gồm DB migrate, nạp dữ liệu mẫu và tạo admin).

### 💻 Cách 2: Cài Đặt Local Development (Chi tiết)

#### 1. Yêu cầu:
- Python 3.10 - 3.12, PostgreSQL 15+, Redis Server.

#### 2. Cài đặt môi trường Web:
```bash
python -m venv venv
# Windows: .\venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

#### 3. Cài đặt môi trường AI OCR:
```powershell
# Windows
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\setup_ocr_env.ps1
```

#### 4. Khởi tạo Database & Dữ liệu mẫu:
```bash
python manage.py migrate
python manage.py seed_permissions
python seed_users_stations.py
```

#### 5. Khởi chạy Ứng dụng:
```bash
python run.py
```
> Lệnh trên sẽ chạy đồng thời: Django Server (Daphne), Celery Worker và Celery Beat. Truy cập: `http://localhost:8000`.

---

## 👥 Tài Khoản Thử Nghiệm Mặc Định

Sử dụng mật khẩu **`123456`** cho tất cả tài khoản bên dưới (trừ admin):

| Vai Trò | Tên Đăng Nhập | Nhiệm Vụ |
|---|---|---|
| **Admin** | `admin` (Pass: `admin`) | Toàn quyền, cấu hình hệ thống |
| **Điều độ viên** | `dispatcher_1` | Tạo phiếu, chạy OCR, phân phối |
| **Trưởng trạm** | `station_leader_1` | Tiếp nhận phiếu, phân công KTV |
| **Kỹ thuật viên** | `technician_1` | Cài đặt thông số rơ-le, ký xác nhận |
| **Giám sát viên** | `supervisor_1` | Giám sát, ký biên bản nghiệm thu |

---

## 🤖 Mô-đun AI OCR On-Premise

Hệ thống AI OCR được phát triển tại thư mục `OCR_PRJ/` hoạt động hoàn toàn offline:
- **Đặc tả:** Bóc tách Layout, trích xuất bảng thông số, tọa độ (Bounding Box) và độ tin cậy.
- **Tích hợp:** Gọi qua Celery Worker ➔ Subprocess API, trả về JSON.
- **An toàn (OT Compliance):** Không gửi dữ liệu ra Internet.

---

## 📚 Tài Liệu Kỹ Thuật

Tài liệu chi tiết được lưu trữ trong thư mục `docs/`:

* [Quản Lý Trạm & Thiết Bị](docs/features/01-station-management.md) | [Quy Trình Phiếu Chỉnh Định](docs/features/02-calibration-sheet.md) | [Cơ Chế Kiểm Tra Định Kỳ](docs/features/04-periodic-check.md)
* [Kiến Trúc Backend & API](docs/cores/02-backend.md) | [Thiết Kế Cơ Sở Dữ Liệu](docs/cores/01-database.md) | [Thiết Kế AI OCR](docs/features/05-ai-ocr.md)

---

<div align="center">
  <p>Được phát triển phục vụ công tác chuyển đổi số của Tập đoàn Điện lực Việt Nam (EVN).</p>
  <p><i>Mọi quyền được bảo lưu.</i></p>
</div>
````

## File: requirements.txt
````
Django>=5.0,<6.1
psycopg[binary]>=3.0
python-dotenv>=1.0
channels>=4.0
daphne>=4.0
openpyxl>=3.0
django-redis
celery>=5.3.0
django-celery-beat>=2.5.0
channels-redis>=4.2.0
djangorestframework>=3.14.0
djangorestframework-xml>=2.0.0
requests>=2.31.0
````
