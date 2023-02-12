"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.toro, name='toro')
Class-based views
    1. Add an import:  from other_app.views import Toro
    2. Add a URL to urlpatterns:  path('', Toro.as_view(), name='toro')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include

urlpatterns = [
    path('authen/', include(('authen.urls', 'authen'), namespace='authen')),
    path('', include('toro.urls')),
]


handler404 = 'toro.views.page_not_found_view'
handler500 = 'toro.views.error_view'
handler403 = 'toro.views.permission_denied_view'
