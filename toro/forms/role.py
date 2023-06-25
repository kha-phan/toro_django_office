from functools import reduce
from operator import or_

from django import forms
from django.contrib.auth.models import Group as PermissionGroup, Permission
from django.db.models import Q

from toro.forms.custom_fields import FilteredSelectMultipleWithCustomMedia


class RoleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        excluded_perms = [
            '_permission',
            '_contenttype',
            '_session',
            'add_logentry',
            'change_logentry',
            'delete_logentry',
            'clienthasstates',
            'gamblingtype',
            'variant',
            'taggedboundary',
            'landmark',
            'solution',
            '_userprofile',
            'operator',
            'config',
            'group'
        ]

        query = reduce(or_, (Q(codename__endswith=p) for p in excluded_perms))
        res = Permission.objects.all().exclude(query).exclude(content_type_id=1).order_by('content_type')
        self.fields['permissions'].choices = res.values_list('id', 'name')
    name = forms.CharField(
        required=True,
        max_length=32,
    )
    permissions = forms.ModelMultipleChoiceField(
        label='',
        required=False,
        queryset=Permission.objects.all(),
        widget=FilteredSelectMultipleWithCustomMedia("permissions", is_stacked=False, ),
    )

    class Meta:
        model = PermissionGroup
        fields = ('name', 'permissions')

    def clean_name(self):
        name = self.cleaned_data['name']
        return name.lower()
