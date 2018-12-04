from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from demand.models import Demand, App, Comments


class DemandAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

class CommentsAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Demand, DemandAdmin)
admin.site.register(App)
admin.site.register(Comments, CommentsAdmin)
