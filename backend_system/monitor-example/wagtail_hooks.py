from django.conf.urls import url
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.core import hooks
from blog.models import BlogIndexPage
from .models import covid19Country, covid19States,covid19Locals,covid19MAHA


class MyPageModelAdmin1(ModelAdmin):
    model = covid19Country
    menu_label = 'International Table  ' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('country',)

class MyPageModelAdmin2(ModelAdmin):
    model = covid19States
    menu_label = 'National Table' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('states',)

class MyPageModelAdmin3(ModelAdmin):
    model = covid19Locals
    menu_label = 'Mumbai Table' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('locals',)

class MyPageModelAdmin4(ModelAdmin):
    model = covid19MAHA
    menu_label = 'Maharashtra Table' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('mahaArea',)




# Now you just need to register your customised ModelAdmin class with Wagtail

# class MyModelAdminGroup(ModelAdminGroup):
#     menu_label = 'My App'
#     menu_icon = 'folder-open-inverse'  # change as required
#     menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
#     items = (MyPageModelAdmin,)

modeladmin_register(MyPageModelAdmin1)
modeladmin_register(MyPageModelAdmin2)
modeladmin_register(MyPageModelAdmin3)
modeladmin_register(MyPageModelAdmin4)


# modeladmin_register(MyModelAdminGroup)
