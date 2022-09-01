from django.contrib import admin

from .models import Users

class users(admin.ModelAdmin):
    list_display =(
        "name",
        "phone_number",
        "gender",
        "IsPremium",
        "IsBlocked",
        "createdAt"
    )
    list_filter = ["createdAt"]
    search_fields = ('phone_number__startswith',)
