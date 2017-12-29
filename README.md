# django-admin
Django Admin Extensions

## Installation
```shell
pip install django-admin
```

## Usage
* Disable Action
  ```python
  from djadmin import DeleteModelAdmin
  from django.contrib import admin

  # Override ``delete_selected``, call ``delete_model`` for each when ``delete_selected``
  class XXXAdmin(admin.ModelAdmin, DeleteModelAdmin):
      def delete_model(self, request, obj):
          obj.delete()
          # Other Codes

  # Reopen action ``delete_selected`` after ``admin.site.disable_action('delete_selected')``
  class YYYAdmin(admin.ModelAdmin):
      actions = ['delete_selected']

  # Disable ``actions``
  class ZZZAdmin(admin.ModelAdmin):
      actions = None
  ```
* Export Excel
  ```python
  from djadmin import ExportExcelModelAdmin, AdvancedExportExcelModelAdmin
  from django.contrib import admin

  class XXXAdmin(ExportExcelModelAdmin, admin.ModelAdmin):
      pass

  class YYYAdmin(AdvancedExportExcelModelAdmin, admin.ModelAdmin):
      excel_fields = ()
      excel_fields_exclude = ()
      extra_excel_fields = ()

      def add_extra_excel_fields(self, request, query):
          return []
  ```
* All Fields Readonly
  ```python
  from djadmin import ReadonlyModelAdmin
  from django.contrib import admin

  class XXXAdmin(ReadonlyModelAdmin, admin.ModelAdmin):
      pass
  ```
* Disable Editing
  ```python
  from djadmin import ReadOnlyModelAdmin
  from django.contrib import admin

  class XXXAdmin(ReadOnlyModelAdmin, admin.ModelAdmin):
      pass
  ```
  * Should add ``django_admin`` in ``INSTALLED_APPS``
    ```python
    INSTALLED_APPS = [
        ...
        'django_admin',
        ...
    ]
    ```
* Disable Add/Delete
  ```python
  from djadmin import ChangeOnlyModelAdmin
  from django.contrib import admin

  class XXXAdmin(ChangeOnlyModelAdmin, admin.ModelAdmin):
      pass
  ```

## Disadvantage
* Will disable ``delete_selected`` for all ``ModelAdmin``
* Will lost delete confirm
