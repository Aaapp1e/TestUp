from django import template
from menu.models import Menu, MenuItem


register = template.Library()


# Для отрисовки начала дерева
@register.simple_tag()
def menu():
    return Menu.objects.all()


# для отрисовки последующих элеметов дерева
@register.inclusion_tag('menu/menu.html')
def draw_menu(menu, parent=0):
    if parent == 0:
        items = MenuItem.objects.filter(menu=menu, parent__isnull=True)
    else:
        items = MenuItem.objects.filter(menu=menu, parent=parent)
    return {'item': items}
