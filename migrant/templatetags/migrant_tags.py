from django import template

register = template.Library()

from migrant.models import Case

@register.filter(name='var_verbose_name')
def get_model_var_verbose_name(model, arg):
    return model._meta.get_field(arg).verbose_name

@register.filter(name='check_model_is_none')
def check_model_is_none(model):
    if model is None:
        return True
    else:
        return False