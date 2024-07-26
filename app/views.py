from django.shortcuts import render

from django.conf import settings
from django.core.mail import send_mail

from .models import User, Courses, Lessons, Videos, Coments, Likes
from .serializers import (UserSerializer, CoursesSerializer, LessonsSerializer, 
                          VideosSerializer, ComentsSerializer, EmailSerializer,
                          LikeSerializer)
from .permisions import CourseAndProfileUpdatePermission, CreatePermission

# Men bu proyektda generic viewlardan foydalandim

from rest_framework.generics import (CreateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView, 
                                     RetrieveAPIView, ListAPIView, DestroyAPIView)
from rest_framework import request, viewsets, filters

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response


# Bu qismda men user ni create yani register qilyapman, u uchun permission bermadim chunki hamma registerdan o'tishi mumkin.

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Profilni ko'rish va agar o'zining profili bo'lsa o'zgartirishi mumkin

class UserProfilView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [CourseAndProfileUpdatePermission]

    def get_queryset(self):
        queryset = User.objects.filter(id = self.kwargs['pk'])
        return queryset
    

# Kurslarni barchasini ko'rish

class CoursesAllView(ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "price"]

# Bu yerda esa Kurslarni CRUD qilishning bir qismi ya'ni UPdate, Delete va Get qilinmoqda

class CourseUpdateDeleteGetView(RetrieveUpdateDestroyAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [CourseAndProfileUpdatePermission]

# Bu yerda esa Kurslarni CRUD qilishning bir qismi ya'ni Create qilinmoqda

class CourseCreateView(ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [CreatePermission]

# Kurslarni barchasini ko'rish

class LessonAllView(ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ["name", "description"]

# Kurslar uchun mavzularni yaratish ya'ni create

class LessonCreateView(ListCreateAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    permission_classes = [CreatePermission]

# Kurslar uchun yaratilgan mavzularni taxrirlash

class LessonUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = LessonsSerializer
    permission_classes = []

    def get_queryset(self):
        queryset = Lessons.objects.filter(id = self.kwargs['pk'])
        return queryset

# Yangi video yaratish

class VideoCreateView(CreateAPIView):
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
    permission_classes = [CreatePermission]

# Videolarni o'chirib tashlash

class VideoDeleteView(DestroyAPIView):
    serializer_class = VideosSerializer
    permission_classes = [CreatePermission]

    def get_queryset(self):
        queryset = Videos.objects.filter(id = self.kwargs['pk'])
        return queryset
    
# Komentraiya yaratish

class ComentsCreateView(CreateAPIView):
    queryset = Coments.objects.all()
    serializer_class = ComentsSerializer
    permission_classes = [IsAuthenticated]

# Komentariyani taxrirlash

class ComentUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = ComentsSerializer
    permission_classes = [CourseAndProfileUpdatePermission]

    def get_queryset(self):
        queryset = Coments.objects.filter(id = self.kwargs['pk'])
        return queryset
    

class SendMassageMailView(APIView):
    def post(self,request: Request):

        serializer = EmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        users = User.objects.all()
        email_user = []
        for user in users:
            if user.email != '':
                email_user.append(user.email)

        

        subject = serializer.validated_data.get('subject')
        message = serializer.validated_data.get('message')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email_user
        fail_silently = False
        send_mail( subject, message, email_from, recipient_list, fail_silently )
        return Response({'massage':'success'})
    

class LikeView(APIView):
    def get(self, request, pk):
        like = len(Likes.objects.filter(like_or_dislike=True, video_id=pk))
        dislike = len(Likes.objects.filter(like_or_dislike=False, video_id=pk))
        return Response({"like":like, "dislike":dislike})


class CreateLikeView(APIView):
    def post(self, request):
        try:
            like_dislike = Likes.objects.filter(author_id=request.data.get("author"))
            for like in like_dislike:
                like.delete()
        except:
            pass

        serializer = Likes(data=request.data)
        serializer.is_valid(raise_exception=True)
        like_or_dislike = serializer.save()

        return Response(Likes(like_or_dislike).data)