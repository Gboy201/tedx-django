from django.contrib import admin
from .models import sponsorRequests, teamMember, sponsorList, speaker

# Register your models here.
admin.site.register(sponsorRequests)
admin.site.register(teamMember)
admin.site.register(sponsorList)
admin.site.register(speaker)