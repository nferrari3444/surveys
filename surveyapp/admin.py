from django.contrib import admin
from .models import Survey, Choices, Results   , Uservotes
# Register your models here.



# Register your models here.
admin.site.register(Survey)
admin.site.register(Choices)
admin.site.register(Results)
admin.site.register(Uservotes)