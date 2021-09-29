from django.db import models
from django.urls import reverse


# 식당분류 모델
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# 식당 모델
# 식당 기본 정보 : 식당분류, 가게이름, 위치, 전화번호, 오픈시간, 가게사진 (추가예정 : 좋아요(팔로우), 메뉴, 리뷰)
class Restaurant(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    business_open_hour = models.DateTimeField()
    business_close_hour = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('restaurant:restaurant_detail', args=[self.id])


# 메뉴 모델
# 메뉴 기본 정보 : 식당, 메뉴이름, 가격, 음식사진
class FoodMenu(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


# 후기 모델
# 후기 기본 정보 : 식당, 메뉴, 작성일, 음식사진, (추가예정 : 추천, 비추천, 후기를 쓴 사용자)
class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    menu = models.ForeignKey(FoodMenu, on_delete=models.CASCADE)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

