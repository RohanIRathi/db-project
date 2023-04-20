from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OriginalAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.

class UserAdmin(OriginalAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	model = User

	filter_horizontal=tuple()

	list_display = ("email", "phone",)
	list_filter = ("email", "phone",)
	fieldsets=(
		(None, {"fields": ('email', 'password', 'phone',)}),
		("Permissions", {"fields": ("is_admin",)}),
	)

	add_fieldsets=(
		None, {
			"classes": ("wide",),
			"fields": ("email", "password1", "password2", "is_admin",)
		}
	)

	search_fields=("email",)
	ordering=("email",)

admin.site.register(User, UserAdmin)