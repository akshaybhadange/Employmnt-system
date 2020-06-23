from django.conf.urls import url
from django.urls import reverse
from wagtail.admin.menu import MenuItem
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup
from wagtail.core import hooks
from .models import Team,Student


class MyPageModelAdmin1(ModelAdmin):
    model = Team
    menu_label = 'Add Team ' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('project',)


class MyPageModelAdmin2(ModelAdmin):
    model = Student
    menu_label = 'Add Student ' # ditch this to use verbose_name_plural from model
    menu_icon = 'group' # change as required
    menu_order = 200 # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False # or True to add your model to the Settings sub-menu
    search_fields = ('project',)



modeladmin_register(MyPageModelAdmin1)
modeladmin_register(MyPageModelAdmin2)




# modeladmin_register(MyModelAdminGroup)
