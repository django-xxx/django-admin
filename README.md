# django-admin
Django Admin Extensions

## Installation
```shell
pip install django-admin
```

## Usage
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

## Disadvantage
* Will disable ``delete_selected`` for all ``ModelAdmin``
* Will lost delete confirm
