from django import template

from django.template.loader import get_template
from django.utils.html import escape
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(name='custom_select_field')
def custom_select_field(field):
    template_path = 'fields/custom_select_field.html'
    template = get_template(template_path)
    return template.render({'field': field})


@register.filter(name='hidden_label_field')
def hidden_label_field(field, placeholder=None, type_class='textinput'):
    field.field.widget.attrs.update({
                    'class': f'form-control form-control-user data-input {type_class}',
                    'placeholder': placeholder if placeholder else
                    f'{field.label}' + '*' if field.field.required else '',
                    'id': f'id-{field.name}'
                })
    template_path = 'fields/hidden_label_field.html'
    template = get_template(template_path)
    return template.render({'field': field})


@register.filter(name='custom_textinput_field')
def custom_textinput_field(field, type_class='textinput'):
    field.field.widget.attrs.update({
                    'class': f'form-control custom-outline-textbox {type_class}'
                })
    if field.field.required:
        field.field.widget.attrs.update({
                    'required': True
                })

    template_path = 'fields/custom_textinput_field.html'
    template = get_template(template_path)
    return template.render({'field': field})


@register.filter(name='custom_area_field')
def custom_area_field(field, type_class='textarea'):
    field.field.widget.attrs.update({
                    'class': f'form-control {type_class}',
                    'rows': 5
                })
    template_path = 'fields/custom_area_field.html'
    template = get_template(template_path)
    return template.render({'field': field})


@register.filter(name='custom_radio_field')
def custom_radio_field(field, type_class='radioinput'):
    field.field.widget.attrs.update({
                    'class': f' {type_class}',
                    'required': True
                })
    template_path = 'fields/custom_radio_field.html'
    template = get_template(template_path)
    return template.render({'field': field})


@register.filter()
def nbsp(value):
    if isinstance(value, str):
        value = escape(value)
        return mark_safe("&nbsp;".join(value.split(' ')))
    return value
