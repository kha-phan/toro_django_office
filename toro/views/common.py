from django.shortcuts import render


def permission_denied_view(request, exception):
    return render(request, 'error_pages/403_page.html', {'exception_msg': str(exception)})


def page_not_found_view(request, exception):
    return render(request, 'error_pages/404_page.html')


def error_view(request):
    return render(request, 'error_pages/500_page.html')