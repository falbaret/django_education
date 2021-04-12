from django import template

register = template.Library()

@register.filter(name='cut') #Decorator to register custom filter

def cut(value,arg):
    """
    This cuts out all values of "arg from the string
    """

    return value.replace(arg,'')

# register.filter('cuttag', cut) #'cut" is the string to call the function when you use it in the template tag  cut is the call to the function