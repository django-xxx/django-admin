============
django-admin
============

Django Admin Extensions

Installation
============

::

    pip install django-admin


Usage
=====

Disable Action::

    from djadmin import DeleteModelAdmin
    from django.contrib import admin

    # Override action ``delete_selected``, call ``delete_model`` for each when ``delete_selected``
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


Export Excel::

    from djadmin import ExportExcelModelAdmin
    from django.contrib import admin

    class XXXAdmin(ExportExcelModelAdmin, admin.ModelAdmin):
        pass


All Fields Readonly::

    from djadmin import ReadonlyModelAdmin
    from django.contrib import admin

    class XXXAdmin(ReadonlyModelAdmin, admin.ModelAdmin):
        pass


Disable Editing::
    from djadmin import ReadOnlyModelAdmin
    from django.contrib import admin

    class XXXAdmin(ReadOnlyModelAdmin, admin.ModelAdmin):
        pass


Disable Add/Delete::
    from djadmin import ChangeOnlyModelAdmin
    from django.contrib import admin

    class XXXAdmin(ChangeOnlyModelAdmin, admin.ModelAdmin):
        pass


Disadvantage
============

::

    Will disable ``delete_selected`` for all ``ModelAdmin``
    Will lost delete confirm

