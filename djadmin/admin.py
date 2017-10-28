# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from excel_response2 import ExcelResponse


if not hasattr(settings, 'DISABLE_ACTION') or settings.DISABLE_ACTION:
    admin.site.disable_action('delete_selected')


class DeleteModelAdmin(object):
    actions = ['override_delete_selected']

    def override_delete_selected(modeladmin, request, queryset):
        for query in queryset:
            modeladmin.delete_model(request, query)

    override_delete_selected.short_description = _(u'Delete selected %(verbose_name_plural)s')


class ExportExcelModelAdmin(object):
    actions = ['export_excel']

    def export_excel(modeladmin, request, queryset):
        return ExcelResponse(queryset, output_name=modeladmin.model._meta.verbose_name_plural)

    export_excel.short_description = _(u'Export selected %(verbose_name_plural)s as Excel')


class AdvancedExportExcelModelAdmin(object):
    actions = ['advanced_export_excel']

    def excel_item(modeladmin, query, field):
        foo_field = 'get_{0}_display'.format(field)
        return getattr(query, foo_field)() if hasattr(query, foo_field) else getattr(query, field)

    def excel_data(modeladmin, request, query, model_fields, has_extra_excel_fields):
        excel_item = [modeladmin.excel_item(query, field) for field in model_fields]
        return excel_item + list(modeladmin.add_extra_excel_fields(request, query)) if has_extra_excel_fields else excel_item

    def advanced_export_excel(modeladmin, request, queryset):
        has_excel_fields = hasattr(modeladmin, 'excel_fields')
        has_excel_fields_exclude = hasattr(modeladmin, 'excel_fields_exclude')
        has_extra_excel_fields = hasattr(modeladmin, 'extra_excel_fields')  # Add by call add_extra_excel_fields

        model_fields = list(modeladmin.excel_fields) if has_excel_fields else [f.name for f in modeladmin.model._meta.fields]
        if has_excel_fields_exclude:
            model_fields = [field for field in model_fields if field not in set(modeladmin.excel_fields_exclude)]

        excel_data = [model_fields + list(modeladmin.extra_excel_fields) if has_extra_excel_fields else model_fields]
        excel_data += [modeladmin.excel_data(request, query, model_fields, has_extra_excel_fields) for query in queryset]

        return ExcelResponse(excel_data, output_name=modeladmin.model._meta.verbose_name_plural)

    advanced_export_excel.short_description = _(u'Advanced Export selected %(verbose_name_plural)s as Excel')


class ReadonlyModelAdmin(object):
    def get_readonly_fields(self, request, obj=None):
        if not hasattr(self, 'readonly_fields_exclude'):
            self.readonly_fields_exclude = ()
        if obj:  # editing an existing object
            return tuple(set(self.readonly_fields) | set(f.name for f in self.model._meta.fields) - set(self.readonly_fields_exclude))
        return tuple(set(self.readonly_fields) - set(self.readonly_fields_exclude))


class ReadOnlyModelAdmin(ReadonlyModelAdmin):
    """ Disables all editing capabilities. """
    change_form_template = 'admin/view.html'

    def __init__(self, *args, **kwargs):
        super(ReadOnlyModelAdmin, self).__init__(*args, **kwargs)

    def get_actions(self, request):
        actions = super(ReadOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        pass

    def delete_model(self, request, obj):
        pass

    def save_related(self, request, form, formsets, change):
        pass


class ChangeOnlyModelAdmin(ReadonlyModelAdmin):
    """ Disables add/delete capabilities. """

    def __init__(self, *args, **kwargs):
        super(ChangeOnlyModelAdmin, self).__init__(*args, **kwargs)

    def get_actions(self, request):
        actions = super(ChangeOnlyModelAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def delete_model(self, request, obj):
        pass
