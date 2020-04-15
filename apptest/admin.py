from django.contrib import admin
from apptest.models import Appcase,Appcasestep
# Register your models here.
class AppcasestepAdmin(admin.TabularInline):
    list_display = ['appteststep','apptestobjname','appfindmethod','appevelement','apptestresult','create_time','id','appcase']


class AppcaseAdmin(admin.TabularInline):
    list_play = ['appcasename','apptestresult','create_time','id']


admin.site.register(Appcase,Appcasestep)