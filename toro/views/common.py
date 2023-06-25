from django.shortcuts import render
from django.utils.html import escape
from django.utils.safestring import mark_safe


def permission_denied_view(request, exception):
    return render(request, 'error_pages/403_page.html', {'exception_msg': str(exception)})


def page_not_found_view(request, exception):
    return render(request, 'error_pages/404_page.html')


def error_view(request):
    return render(request, 'error_pages/500_page.html')

def render_textfield(value):
    value = escape(value)
    value = "&nbsp;".join(value.split(' ')) if isinstance(value, str) else value
    return mark_safe(value)
