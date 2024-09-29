from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    mobile = models.CharField(max_length=32)


class Departments(models.Model):
    title = models.CharField(max_length=16)

# create table app01_userinfo(
#     id bigint auto_increment primary key,
# name varchar(32),
# password varchar(64),
# age int
# )