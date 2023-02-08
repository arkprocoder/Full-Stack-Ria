from django.contrib import admin
from riaapp.models import Register,Payments,Courses,Documents,Certificate
# Register your models here.
admin.site.register(Register)
admin.site.register(Courses)
admin.site.register(Payments)
admin.site.register(Documents)
admin.site.register(Certificate)
