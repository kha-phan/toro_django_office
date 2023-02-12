from django.urls import path
# from django.contrib.auth.views import LogoutView
from .views import LoginViewWithSession, LogoutView


urlpatterns = [
    path('login/', LoginViewWithSession.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
