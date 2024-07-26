from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator


# Bu class foydalanuvchi yarratildi. Yani djangoni o'zini AbstractUser degan modelini polimarfizm usuli bilan o'zimga moslashtirdim.

class User(AbstractUser):
    image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, default='default/default.jpg')
    phone_number = models.CharField(max_length=13, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    

    # Str dondermetodi bu yerda class haqida boshlang'ich ma'lumotni beradi, agar first_name bo'lsa shuni bo'lmasa usernameni qaytaradi.

    def __str__(self) -> str:
        if self.first_name == None:
            return self.first_name + self.last_name
        else:
            return self.username
        
# Bu kurslar uchun qilingan model

class Courses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_course') # Bu yerda kurs uchun user tanlanmoqda (Biriktirilgan shaxs)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()

    # Bu yerda Meta class classga qoshimcha vazifa yuklayapti, ya'ni classdan yaratilayotgan objectlarning "name" ni uniq bo'lsin deyapti

    class Meta:
        unique_together = ['name']
    
    def __str__(self) -> str:
        return self.name
    
# Bu esa mavzular uchun ajratilgan model

class Lessons(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course')
    name = models.CharField(max_length=150)
    description = models.TextField()
    
    # Bu yerda Meta class classga qoshimcha vazifa yuklayapti, ya'ni classdan yaratilayotgan objectlarning "name" ni uniq bo'lsin deyapti
    
    class Meta:
        unique_together = ['name']
    
    def __str__(self) -> str:
         return self.name
    
# Bu yerda esa Mavzularning Videolari uchun class

class Videos(models.Model):
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='lesson')
    videos = models.FileField(upload_to='massege/videos/', validators=[
        FileExtensionValidator(allowed_extensions=['mp4', 'MOV', 'AVI', 'MVB'])  # Bu yerda videolikka tekshirmoqda
    ])
    created = models.DateField(auto_now_add=True) # Bu video yuklangan vaqtni avtomatik o'ziga yuklab oladi
    

# Bu esa darsning videosi uchun comentariya

class Coments(models.Model):
    videos = models.ForeignKey(Videos, on_delete=models.CASCADE, related_name='video')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_coment')
    text = models.TextField()

    # Str dondermetodi bu yerda class haqida boshlang'ich ma'lumotni beradi, agar first_name bo'lsa shuni bo'lmasa usernameni qaytaradi.

    def __str__(self) -> str:
        return self.user.username
    

class Likes(models.Model):
    video = models.ForeignKey(Videos, on_delete=models.CASCADE)
    like_or_dislike = models.BooleanField()
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)


        
