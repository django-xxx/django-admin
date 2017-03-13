# -*- coding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _


admin.site.disable_action('delete_selected')


class DeleteModelAdmin():
    actions = ['override_delete_selected']

    def override_delete_selected(self, request, obj):
        for o in obj.all():
            self.delete_model(request, o)

    override_delete_selected.short_description = _(u'Delete selected %(verbose_name_plural)s')
