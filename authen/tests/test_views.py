from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory


from authen.forms import LoginForm
from authen.models import User
from authen.views import LoginViewWithSession


class TestLoginViewWithSession(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.credentials = {
            'username': 'user1',
            'password': 'abcxyz123'
        }
        User.objects.create(username=cls.credentials['username'], password=make_password(cls.credentials['password']))

    def test_login(self):
        rs = self.client.post('/authen/login/?next=/', self.credentials)
        self.assertRedirects(rs, '/')

    def test_form_valid__without_remember(self):
        credentials = {
            'username': 'user1',
            'password': 'abcxyz123',
            'remember_me': 0
        }
        form = LoginForm(data=credentials)
        form.is_valid()
        rq = RequestFactory().post('/authen/login/?next=/', credentials)
        middleware = SessionMiddleware()
        middleware.process_request(rq)
        view = LoginViewWithSession()
        view.setup(rq)
        view.form_valid(form)
        self.assertEqual(rq.session.get_expiry_age(), 2*7*24*60*60)

    def test_form_valid__with_remember(self):
        credentials = {
            'username': 'user1',
            'password': 'abcxyz123',
            'remember_me': 1
        }
        form = LoginForm(data=credentials)
        form.is_valid()
        rq = RequestFactory().post('/authen/login/?next=/', credentials)
        middleware = SessionMiddleware()
        middleware.process_request(rq)
        view = LoginViewWithSession()
        view.setup(rq)
        view.form_valid(form)
        self.assertEqual(rq.session.get_expiry_age(), settings.COOKIE_EXPIRATION_TIME)
