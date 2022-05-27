from django.contrib import admin
from .models import UserModel

# Register your models here.
admin.site.register(UserModel) #이 코드가 나의 UserModel을 admin에 저장해줍니다.
