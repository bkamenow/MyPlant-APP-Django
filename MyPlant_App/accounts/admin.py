from django.contrib import admin

from MyPlant_App.accounts.models import UserModel


# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')


admin.site.register(UserModel, UserAdmin)
