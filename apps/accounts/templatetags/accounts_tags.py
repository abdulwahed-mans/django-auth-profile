from django import template

register = template.Library()


@register.filter
def avatar_initial(user):
    """Return the user's avatar initial letter."""
    if user.first_name:
        return user.first_name[0].upper()
    return user.username[0].upper()
