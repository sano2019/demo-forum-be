from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.crypto import get_random_string
from django.utils.translation import ugettext_lazy as _
from reversion.admin import VersionAdmin

from django.contrib.auth.forms import UserCreationForm

from common.admin import SoftDeleteAdmin
from common.models import SoftDeleteFilter

from core.models import (
    User,
)


class CustomUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(CustomUserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2

    class Meta:
        model = User
        fields = ('email', )


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    add_form = CustomUserCreationForm
    list_display_links = ('id', 'email')
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'is_staff',
    )

    search_fields = ('email', 'first_name', 'last_name',)
    ordering = ('email',)

    def save_model(self, request, obj, form, change):
        if not change and (not form.cleaned_data['password1'] or not obj.has_usable_password()):
            # Django's PasswordResetForm won't let us reset an unusable
            # password. We set it above super() so we don't have to save twice.
            obj.set_password(get_random_string())

        super(CustomUserAdmin, self).save_model(request, obj, form, change)

    def get_fieldsets(self, request, obj=None):
        if not obj:
            password_fields = ('email', 'password1', 'password2')
        else:
            password_fields = ('email', 'password')
        if request.user.is_superuser:
            perm_fields = (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        else:
            perm_fields = ('is_active', 'is_staff', )
        return [
            (None, {'fields': password_fields}),
            (
                _('Personal info'),
                {
                    'fields': (
                        'first_name',
                        'last_name',
                        'phone_number',
                        'title',
                    )
                },
            ),
            (_('Permissions'), {'fields': perm_fields}),
            (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        ]

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(CustomUserAdmin, self).get_readonly_fields(
            request, obj
        )
        if request.user.is_superuser:
            return readonly_fields
        else:
            return readonly_fields + ('is_onboarded',)
