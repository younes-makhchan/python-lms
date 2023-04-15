from django.urls import path
from . import views


urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseRetrieve.as_view(), name='course_retrieve'),
    path('courses/<int:course_pk>/lessons/', views.LessonList.as_view(), name='course_lessons'),
    path('courses/<int:course_pk>/quizzes/', views.QuizList.as_view(), name='course_quizzes'),
    path('quizzes/<int:quiz_pk>/questions/', views.QuestionList.as_view(), name='quiz_questions'),
    path('lessons/<int:lesson_pk>/videos/', views.VideoList.as_view(), name='lesson_videos'),
    path('user-responses/', views.UserResponseListCreate.as_view(), name='user_response_list_create'),
]