from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied


NAMESPACE = '{http://www.opengis.net/kml/2.2}'


def permission_check(perm, login_url=None, raise_exception=False):
    """
    Custom permission required check for group permission
    """

    def check_perms(user):
        if isinstance(perm, str):
            perms = (perm,)
        else:
            perms = perm

        # Check permission in group
        groups = user.groups.all()
        for group in groups:
            assigned_perms = group.permissions.all()
            if perm in assigned_perms.values_list('codename', flat=True):
                return True

        # First check if the user has the permission (even anon users)
        if user.has_perms(perms):
            return True

        # In case the 403 handler should be called raise the exception
        if raise_exception:
            raise PermissionDenied
        # As the last resort, show the login form
        return False

    return user_passes_test(check_perms, login_url=login_url)
