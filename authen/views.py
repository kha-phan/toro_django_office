from django.contrib.auth.views import LogoutView, LoginView
from django.conf import settings
from authen.forms import LoginForm


class LogoutView(LogoutView):
    pass


class LoginViewWithSession(LoginView):
    form_class = LoginForm
    template_name = 'authen/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        if form.cleaned_data['remember_me']:
            self.request.session.set_expiry(settings.COOKIE_EXPIRATION_TIME)
        return super().form_valid(form)
