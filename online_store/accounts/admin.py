from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomeUser 



class CustomeUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomeUser
    list_display = [
        'email',
        'username',
        'age',
        'is_staff',
    ]

fieldsets =UserAdmin.fieldsets + ((None,{"fields:('age,)"}),)
add_fieldsets =UserAdmin.add_fieldsets + ((None,{"fields:('age,)"}),)



admin.site.register(CustomeUser,CustomeUserAdmin)