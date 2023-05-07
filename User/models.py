from django.db import models
from django.contrib import admin
from django.contrib.auth.models import (
    BaseUserManager,AbstractBaseUser , PermissionsMixin, AbstractUser
)
from django.forms import CharField
from Room.models import Room
# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, full_name, password = None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('User must have an email address')
        
        user = self.model(
            username= username,
            email = self.normalize_email(email),
            password = password,
            full_name = full_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, username, email, full_name , password = None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            full_name=full_name,
        )

        user.is_owner = True
        user.save(using = self._db)
        return user
    

class MyUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length =255, unique=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
    )
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, null = True)
    address = models.CharField(max_length=255, null =True)
    is_active = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS  = ['email', 'full_name']

    def __str__(self):
        if self.phone_number is None:
            return "{}-{}".format(self.full_name,self.phone_number)
        else:
            return  "{}-{}".format(self.full_name,self.phone_number[0:3])

    def has_perm(self, perm, obj = None):
        'Does the user have a specific permission?'
        # Simplest possible answer: Yes, always
        return True
    
    def has_module_perms(self, app_label):
        'Does the user have permissions to view the app `app_label`?'
        # Simplest possible answer: Yes, always
        return True
    
    @property
    def is_staff(self):
        'Is the user a member of staff?'
        # Simplest possible answer: All admins are staff
        return self.is_owner
    

class Renter(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='renter',on_delete=models.CASCADE)
    citizen_id = models.CharField(max_length=15, null = True)

    def __str__(self):
        return "{}-{}- Room number : {}".format(self.user.id, self.user.full_name, self.room.room_number)
    
