from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import ValidationError
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("phone number required.")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    is_driver = models.BooleanField(default=False)

    rating = models.DecimalField(max_digits=5, decimal_places=1, default=5.0)

    driver_license = models.ImageField(
        upload_to="driver_license/",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["full_name"]

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if self.is_driver and not self.driver_license:
            raise ValidationError("Driver license is required.")

        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.phone_number)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
