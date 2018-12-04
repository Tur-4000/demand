from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from demand.models import Demand, App


class DemandAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)


admin.site.register(Demand, DemandAdmin)
admin.site.register(App)
