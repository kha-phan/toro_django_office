from django.contrib.admin.widgets import FilteredSelectMultiple


class FilteredSelectMultipleWithCustomMedia(FilteredSelectMultiple):
    """
    Uses custom static file instead of Django's built-in.
    """
    class Media:
        extend = False
        css = {'all': ('css/common_pageview/detail_form.css', 'admin/css/widgets.css', 'admin/css/responsive.css',
                       'css/authen_style.css')}
        js = [
            'admin/js/core.js',
            'js/common_pageview/SelectBoxCustom.js',
            'js/common_pageview/SelectFilter2Custom.js',
            'js/common_pageview/DetailPageControl.js'
        ]
