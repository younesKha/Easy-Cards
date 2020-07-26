

from django import template

register = template.Library()

def update_variable(data,value):
    data = value
    return data

register.filter('update_variable', update_variable)


def pprint(value,elements):
    return str(44)+str(value) + str(elements)

register.filter('pprint', pprint)




