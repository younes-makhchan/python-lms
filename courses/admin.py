from django.contrib import admin

from .models import Course, Lesson, Video, Quiz, Question, UserResponse

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Video)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserResponse)