from django.urls import path
from django.views import i18n

from toro import views
from toro.utils import permission_check

urlpatterns = [
    # Dashboard
    path('', views.dashboard.index),

    # # Audit
    # path('auditlogs',
    #      permission_check(
    #         'view_logentry', raise_exception=True)(views.audit_log_management.AuditLogsListView.as_view()),
    #      name='view-logs'),

    path('jsi18n/', i18n.JavaScriptCatalog.as_view(), name='jsi18n'),
]
