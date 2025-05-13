from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(registration)
# admin.site.register(Chatbot)
admin.site.register(internalmarklist)
admin.site.register(internalexammarklist)
admin.site.register(Attendence)
admin.site.register(Fee_Payment)
admin.site.register(Events)
admin.site.register(StudentGPA)