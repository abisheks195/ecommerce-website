from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)

class UserManager(BaseUserManager):
    def create_user(self, email, fullname=None, password=None, is_staff=False, is_admin=False, is_active=True):
        if not email:
            raise ValueError('Users must have a valid email');
        if not password:
            raise ValueError('Users must have a valid password');

        user_obj = self.model(
            email = self.normalize_email(email),
            fullname = fullname
        );
        user_obj.set_password(password);
        user_obj.staff = is_staff;
        user_obj.admin = is_admin;
        user_obj.active = is_active;
        user_obj.save(using=self._db);
        return user_obj;

    def create_staffuser(self, email, fullname=None, password=None):
        user_obj = self.create_user(
            email, fullname=fullname, password=password, is_staff=True
        );
        return user_obj;

    def create_superuser(self, email, fullname=None, password=None):
        user_obj = self.create_user(
            email, fullname=fullname, password=password, is_staff=True, is_admin=True
        );
        return user_obj;

class User(AbstractBaseUser):
    email       = models.EmailField(max_length=255, unique=True);
    fullname    = models.CharField(max_length=255, blank=True, null=True);
    active      = models.BooleanField(default=True);
    staff       = models.BooleanField(default=False);
    admin       = models.BooleanField(default=False);
    timestamp   = models.DateTimeField(auto_now_add=True);

    USERNAME_FIELD = 'email';

    REQUIRED_FIELDS = [];

    objects = UserManager();

    def __str__(self):
        return self.email;

    def get_full_name(self):
        if self.fullname:
            return self.fullname;
        return self.email;

    def get_short_name(self):
        return self.email;

    def has_perm(self, perm, obj=None):
        return True;

    def has_module_perms(self, app_label):
        return True;

    @property
    def is_staff(self):
        return self.staff;

    @property
    def is_admin(self):
        return self.admin;

    @property
    def is_active(self):
        return self.active;

class GuestEmail(models.Model):
    email       = models.EmailField();
    active      = models.BooleanField(default=True);
    update      = models.DateTimeField(auto_now=True);
    timestamp   = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.email;
