# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from excel_response2 import ExcelResponse


if not hasattr(settings, 'DISABLE_ACTION') or settings.DISABLE_ACTION:
    admin.site.disable_action('delete_selected')


class DeleteModelAdmin():
    actions = ['override_delete_selected']

    def override_delete_selected(modeladmin, request, queryset):
        for query in queryset:
            modeladmin.delete_model(request, query)

    override_delete_selected.short_description = _(u'Delete selected %(verbose_name_plural)s')


class ExportExcelModelAdmin():
    actions = ['export_excel']

    def export_excel(modeladmin, request, queryset):
        return ExcelResponse(queryset)

    export_excel.short_description = _(u'Export selected %(verbose_name_plural)s as Excel')


class ReadonlyModelAdmin():
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + tuple(f.name for f in self.model._meta.fields)
        return self.readonly_fields
