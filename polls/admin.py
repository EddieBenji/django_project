from django.contrib import admin
from .models import Choice, Question


# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


# it'll tell to the admin, that Question objects have an admin interface
# admin.site.register(Question)

# let's customize the form in admin page
class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInLine]

    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)

# We'll display the info of the choices
admin.site.register(Choice)
