# This file is part of HappySchool.
#
# HappySchool is the legal property of its developers, whose names
# can be found in the AUTHORS file distributed with this source
# distribution.
#
# HappySchool is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# HappySchool is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with HappySchool.  If not, see <http://www.gnu.org/licenses/>.

import json

from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin

from django_filters import rest_framework as filters

from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.views import BaseFilters, BaseModelViewSet, get_app_settings
from core.utilities import get_menu

from .models import {{ camel_case_app_name }}SettingsModel
from .serializers import {{ camel_case_app_name }}SettingsSerializer


def get_menu_entry(active_app, user):
    if not user.has_perm("{{ app_name }}.view_{{ app_name }}"):
        return {}
    return {
            "app": "{{ app_name }}",
            "display": "{{ app_name }}",
            "url": "/{{ app_name }}/",
            "active": active_app == "{{ app_name }}"
    }


def get_settings():
    return get_app_settings({{ camel_case_app_name }}SettingsModel)


class {{ camel_case_app_name }}View(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    TemplateView
):
    template_name = "{{ app_name }}/{{ app_name }}.html"
    #permission_required = ('{{ app_name }}.view_{{ app_name }}')
    filters = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['menu'] = json.dumps(get_menu(self.request.user, "{{ app_name }}"))
        context['filters'] = json.dumps(self.filters)
        context['settings'] = json.dumps(({{ camel_case_app_name }}SettingsSerializer(get_settings()).data))

        return context


#class {{ camel_case_app_name }}Filter(BaseFilters):
    #class Meta:
        #fields_to_filter = (,)
        #model = {{ camel_case_app_name }}
        #fields = BaseFilters.Meta.generate_filters(fields_to_filter)
        #filter_overrides = BaseFilters.Meta.filter_overrides


#class {{ camel_case_app_name }}ViewSet(BaseModelViewSet):
    #queryset = {{ camel_case_app_name }}Model.objects.all()
    #serializer_class = {{ camel_case_app_name }}Serializer
    #permission_classes = (IsAuthenticated, DjangoModelPermissions,)
    #filter_class = {{ camel_case_app_name }}Filter
    #ordering_fields = []
