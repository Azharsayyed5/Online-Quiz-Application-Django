from django.contrib import admin
from Questions.models import Subject,QuestionMaster, webimages
# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id','SName')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','QName','option1','option2','option3','option4','cans','subject')

class webimagesadmin(admin.ModelAdmin):
    list_display = ['id','imagex']



admin.site.register(Subject,SubjectAdmin)
admin.site.register(QuestionMaster,QuestionAdmin)
admin.site.register(webimages,webimagesadmin)

