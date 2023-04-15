from django.core.management.base import BaseCommand
from courses.models import Course, Lesson, Video, Quiz, Question
from faker import Faker

class Command(BaseCommand):
    help = 'Inserts dummy data into the database'

    def handle(self, *args, **options):
        fake = Faker()

        # Create sample courses
        courses = [Course.objects.create(title=fake.sentence(), description=fake.paragraph()) for _ in range(10)]

        # Create sample video lessons
        videos = [Video.objects.create(title=fake.sentence(), video_url=fake.url()) for _ in range(30)]

        # Assign videos to courses
        for i, course in enumerate(courses):
            for j in range(3):
                Lesson.objects.create(course=course, title=fake.sentence(),
                                      content=fake.paragraph(), video=videos[i * 3 + j])

        # Create sample quizzes
        quizzes = [Quiz.objects.create(course=course, title=fake.sentence()) for course in courses]

        # Create sample questions
        questions = []
        for quiz in quizzes:
            for _ in range(5):
                question_text = fake.sentence()
                correct_answer = fake.word()
                question = Question(quiz=quiz, text=question_text, correct_answer=correct_answer)
                questions.append(question)
        Question.objects.bulk_create(questions)

        self.stdout.write(self.style.SUCCESS('Successfully inserted dummy data'))
