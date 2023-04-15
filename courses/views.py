from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, permissions
from .models import Course, Lesson, Quiz, Question, UserResponse, Video
from .serializers import CourseSerializer, LessonSerializer, QuizSerializer, QuestionSerializer, UserResponseSerializer, VideoSerializer, UserRegistrationSerializer

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseRetrieve(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Lesson.objects.all()
        course_pk = self.kwargs['course_pk']
        queryset = queryset.filter(course__pk=course_pk)
        return queryset

class QuizList(generics.ListAPIView):
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Quiz.objects.all()
        course_pk = self.kwargs['course_pk']
        queryset = queryset.filter(course__pk=course_pk)
        return queryset

class QuestionList(generics.ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Question.objects.all()
        quiz_pk = self.kwargs['quiz_pk']
        queryset = queryset.filter(quiz__pk=quiz_pk)
        return queryset

class VideoList(generics.ListAPIView):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Video.objects.all()
        lesson_pk = self.kwargs['lesson_pk']
        queryset = queryset.filter(lesson__pk=lesson_pk)
        return queryset

class UserResponseListCreate(generics.ListAPIView, generics.CreateAPIView):
    queryset = UserResponse.objects.all()
    serializer_class = UserResponseSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]