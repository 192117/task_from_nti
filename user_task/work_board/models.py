from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Вы не ввели Email")
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    first_name = models.CharField(verbose_name='name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='surname', max_length=30, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()


class Tasks(models.Model):
    id_workers = models.TextField(verbose_name='id_workers', blank=True)
    title = models.CharField(verbose_name='title', max_length=30, blank=True)
    description = models.TextField(verbose_name='description', default=True)
    completion_date = models.DateTimeField(verbose_name='completion date')
    owner = models.TextField(verbose_name='email_owner')

