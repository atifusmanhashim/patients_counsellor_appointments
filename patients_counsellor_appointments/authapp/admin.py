from django.contrib import admin

# Register your models here.
from authapp.models import (AppUser,LoginAnalytics)

admin.site.register(AppUser)
admin.site.register(LoginAnalytics)

from appointmentsapp.models import (Patient,Counsellor,Appointment)

admin.site.register(Patient)
admin.site.register(Counsellor)
admin.site.register(Appointment)

from appapi.models import (AppAnalytics)

admin.site.register(AppAnalytics)