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

class XXXAdmin(admin.ModelAdmin, DeleteModelAdmin):

    def delete_model(self, request, obj):
        obj.delete()
        # Other Codes
```
