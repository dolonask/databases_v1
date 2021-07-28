from django import template

register = template.Library()

@register.filter(name='var_verbose_name')
def get_model_var_verbose_name(model, arg):
    try:
        return model._meta.get_field(arg).verbose_name
    except Exception:
        return 'Error'

@register.filter(name='check_arg_is_none')
def check_arg_is_none(arg):
    if arg is None:
        return True
    else:
        return False


def var_verbose_name_for_word(model, arg):
    try:
        return model._meta.get_field(arg).verbose_name
    except Exception:
        return 'Error'


def check_arg_is_none(arg):
    if arg is None:
        return True
    else:
        return False