from django.contrib import admin
from .models import Question, Choice
# from django.contrib.auth.models import User


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# class UserInline(admin.TabularInline):
#     model = User
#     extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

    inlines = [ChoiceInline]
    # inlines = [ChoiceInline, UserInline]


admin.site.register(Question, QuestionAdmin)

# Register your models here.
