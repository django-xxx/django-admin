# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


if not hasattr(settings, 'DISABLE_ACTION') or settings.DISABLE_ACTION:
    admin.site.disable_action('delete_selected')


class DeleteModelAdmin():
    actions = ['override_delete_selected']

    def override_delete_selected(self, request, obj):
        for o in obj.all():
            self.delete_model(request, o)

    override_delete_selected.short_description = _(u'Delete selected %(verbose_name_plural)s')


class ReadonlyModelAdmin():
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + tuple(f.name for f in self.model._meta.fields)
        return self.readonly_fields
