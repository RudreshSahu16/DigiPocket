
from django.contrib import admin
from .models import Fieldview,SubFieldView,UploadedFile
# Register your models here.
admin.site.register(Fieldview)
admin.site.register(SubFieldView)
admin.site.register(UploadedFile)

