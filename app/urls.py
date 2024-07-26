from django.urls import path

from .views import (UserRegisterView, UserProfilView, CourseUpdateDeleteGetView, 
                    CourseCreateView, LessonCreateView, LessonUpdateView,
                    CoursesAllView, LessonAllView, VideoCreateView, VideoDeleteView, 
                    ComentsCreateView, ComentUpdateView, SendMassageMailView,
                    LikeView, CreateLikeView)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name= 'register'),
    path('accounts/profile/<int:pk>/', UserProfilView.as_view(), name= 'profile'),
    path('courses/all/', CoursesAllView.as_view(),name='all_courses'),
    path('courses/update/<int:pk>/', CourseUpdateDeleteGetView.as_view(), name= 'course_update'),
    path('courses/create/', CourseCreateView.as_view(), name= 'create_course'),
    path('lesson/create/', LessonCreateView.as_view(), name= 'create_lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateView.as_view(), name= 'lesson_update'),
    path('lesson/all/', LessonAllView.as_view(),name='all_lesson'),
    path('video/create/', VideoCreateView.as_view(), name= 'create_video'),
    path('video/delete/<int:pk>/', VideoDeleteView.as_view(),name='video_delete'),
    path('coment/create/', ComentsCreateView.as_view(), name= 'coment_video'),
    path('coment/update/<int:pk>/', ComentUpdateView.as_view(), name= 'coment_update'),
    path('send/message/email/',SendMassageMailView.as_view()),
    path('like/<int:pk>/',LikeView.as_view()),
    path('create/like/',CreateLikeView.as_view())
]  