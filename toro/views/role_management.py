from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django_tables2.tables import Table, columns
from django_tables2.views import SingleTableMixin
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.urls import reverse_lazy

from toro.common.table import CounterColumnTableMixin
from toro.forms.role import RoleForm
from toro.utils import permission_check
from toro.views.common import render_textfield


DEFAULT_ROLES = ('administrator', 'qa', 'infra')


class RoleActionColumn(columns.templatecolumn.TemplateColumn):
    def render(self, record, table, value, bound_column, **kwargs):
        if record.name in DEFAULT_ROLES:
            return ''
        return super().render(record, table, value, bound_column, **kwargs)


class RoleTable(CounterColumnTableMixin, Table):
    permissions = columns.Column(empty_values=(), orderable=False, attrs={'th': {'style': 'width: 65%'}})
    actions = RoleActionColumn(
        template_name='role/action_buttons.html',
        orderable=False, attrs={'th': {'class': 'action-header'}}
    )

    def render_name(self, value):
        return render_textfield(value)

    def render_permissions(self, record):
        text = ''
        for p in record.permissions.all():
            text += f'<button class="btn btn-primary item-btn disabled">{escape(p.name)}</button>'
        text = f'<div style="max-height:100px; overflow: scroll">{text}</div>'
        return mark_safe(text)

    class Meta:
        model = Group
        sequence = ('row_number', 'name', 'permissions', 'actions')
        exclude = ('id',)


@method_decorator(login_required, name='dispatch')
class RoleListView(SingleTableMixin, ListView):
    paginate_by = 15
    table_class = RoleTable
    queryset = Group.objects.all().prefetch_related('permissions')
    template_name = "components/table_listview.html"
    ordering = ['id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Roles'
        context['segment'] = {
            'name': 'Users & Permissions',
            'title': 'Roles Management',
            'submenu': 'Roles',
            'create_url': reverse_lazy('create-role'),
            }
        context['has_creation_perm'] = self.request.user.has_perm('auth.add_role')
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_check('view_role', raise_exception=True), name='dispatch')
class RoleUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'role/role_detail.html'
    model = Group
    form_class = RoleForm
    success_url = reverse_lazy('view-role')
    success_message = 'Role %(name)s was updated successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Roles'
        context['form_title'] = 'Edit Permissions'
        context['segment'] = {
            'name': 'Users & Permissions',
            'title': 'Roles Management',
            'submenu': 'Roles',
            'action': 'Edit',
            }

        return context

    def get_object(self):
        obj = super().get_object()
        if obj.name in DEFAULT_ROLES:
            raise PermissionDenied
        return obj


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_check('view_role', raise_exception=True), name='dispatch')
class RoleCreateView(SuccessMessageMixin, CreateView):
    template_name = 'role/role_detail.html'
    model = Group
    form_class = RoleForm
    success_url = reverse_lazy('view-role')
    success_message = 'Role %(name)s was created successfully'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Roles'
        context['form_title'] = 'Create Roles'
        context['segment'] = {
            'name': 'Users & Permissions',
            'title': 'Roles Management',
            'submenu': 'Roles',
            'action': 'Create',
            }

        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(permission_check('view_role', raise_exception=True), name='dispatch')
class RoleDeleteView(SuccessMessageMixin, DeleteView):
    model = Group
    success_url = reverse_lazy('view-role')
    success_message = 'Role %(name)s was deleted successfully'

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.name in DEFAULT_ROLES:
            raise PermissionDenied
        res = super().delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message % obj.__dict__)
        return res
