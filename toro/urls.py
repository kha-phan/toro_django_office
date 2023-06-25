from django.urls import path
from django.views import i18n

from toro import views
from toro.utils import permission_check

urlpatterns = [
    # Dashboard
    path('', views.dashboard.index),

    # Users, Roles and Permissions
    path('role-management',
         permission_check('view_role', raise_exception=True)(
             views.role_management.RoleListView.as_view()),
         name='view-role'),
    path('role-management/<int:pk>/update',
         permission_check('change_role', raise_exception=True)(
             views.role_management.RoleUpdateView.as_view()),
         name='update-role'),
    path('role-management/create',
         permission_check('add_role', raise_exception=True)(
             views.role_management.RoleCreateView.as_view()),
         name='create-role'),
    path('role-management/<int:pk>/delete',
         permission_check('delete_role', raise_exception=True)(
             views.role_management.RoleDeleteView.as_view()),
         name='delete-role'),

    path('jsi18n/', i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]
