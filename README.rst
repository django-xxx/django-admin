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

::

    from djadmin import DeleteModelAdmin
    from django.contrib import admin

    class XXXAdmin(admin.ModelAdmin, DeleteModelAdmin):

        def delete_model(self, request, obj):
            obj.delete()
            # Other Codes

    class YYYAdmin(admin.ModelAdmin):
        actions = ['delete_selected']


Disadvantage
============

::

    Will disable ``delete_selected`` for all ``ModelAdmin``
    Will lost delete confirm

