from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField(
        verbose_name='email',
        unique=True,
    )

    username = models.CharField(
        verbose_name='username',
        unique=True,
        max_length=50,
    )

    last_name = models.CharField(
        verbose_name='last name',
        max_length=100,
        blank=True,
        null=True
    )

    first_name = models.CharField(
        verbose_name='first_name',
        max_length=100,
        blank=True,
        null=True
    )

    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
        help_text='Designates whether this user should be treated as active. Unselect this instead of deleting '
                  'accounts. '
    )

    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this site.'
    )

    is_superuser = models.BooleanField(
        verbose_name='superuser status',
        default=False,
        help_text='Designates that this user has all permissions without explicitly assigning them.'
    )

    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True
    )

    city = models.CharField(
        verbose_name='city',
        max_length=200,
        blank=True,
        null=True
    )

    address_one = models.CharField(
        verbose_name='address 1',
        max_length=200,
        blank=True,
        null=True
    )

    address_two = models.CharField(
        verbose_name='address 2',
        max_length=200,
        blank=True,
        null=True
    )

    zip = models.CharField(
        verbose_name='ZIP',
        max_length=10,
        blank=True,
        null=True
    )

    landmark = models.CharField(
        verbose_name='landmark',
        max_length=200,
        blank=True,
        null=True
    )

    contact_number = models.IntegerField(
        verbose_name='contact_number',
        blank=True,
        null=True
    )

    avatar = models.ImageField(
        verbose_name='avatar',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.username}'
