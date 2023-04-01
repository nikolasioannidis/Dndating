from django.contrib import admin
from .models import info, category_edition, category_Class, category_gender, FilesUpload

# Register your models here.
admin.site.register(info)
admin.site.register(category_edition)
admin.site.register(category_Class)
admin.site.register(category_gender)
admin.site.register(FilesUpload)