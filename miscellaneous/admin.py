from django.contrib import admin
from .models import Miscellaneous
# Register your models here.


class MiscellaneousAdmin(admin.ModelAdmin):
    pass


admin.site.register(Miscellaneous, MiscellaneousAdmin)
