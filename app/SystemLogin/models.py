from django.contrib.auth import models as djangoModel
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils import timezone

class MyUserManager(djangoModel.BaseUserManager):
    def create_user(self, email, first_name, last_name, gender, birth_date, password=None, **other_fields):
        if not email:
            raise ValueError(_('Necesitas un correo electronico'))
        
        if not first_name:
            raise ValueError(_('Necesitas un nombre'))
        
        if not last_name:
            raise ValueError(_('Necesitas apellido'))

        if not gender:
            raise ValueError(_('Necesitas genero'))

        if not birth_date:
            raise ValueError(_('Necesitas una fecha de nacimiento'))

        #giving permission
        other_fields.setdefault('is_staff',True)
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            birth_date = birth_date,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, first_name, last_name, gender, birth_date, password=None, **other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        
        return self.create_user(
            email=email,
            first_name = first_name,
            last_name = last_name,
            gender = gender,
            birth_date = birth_date,
            password = password,
            **other_fields
        )

class MyUser(djangoModel.AbstractBaseUser, djangoModel.PermissionsMixin):

    GENDER_USER = (
        (_('Female'),'Female'),
        (_('Male'),'Male'),
        (_('Personalized'),'Personalized'),
    )

    email = models.EmailField(_('correo electrónico'), unique=True)
    first_name = models.CharField(_('nombre'),max_length=255, null=True)
    last_name = models.CharField(_('apellido'),max_length=255, null=True)
    gender = models.CharField(_('sexo'),max_length=255, null=True, choices = GENDER_USER)
    birth_date = models.DateField(_('fecha de nacimiento'), max_length=255, null=True)
    start_date = models.DateTimeField(_('fecha de inicio'),max_length=255, default=timezone.now)
    is_active = models.BooleanField(_('activo'),default=True)
    is_staff = models.BooleanField(_('personal'),default=False)
    is_superuser = models.BooleanField(_('administrador'),default=False)

    #Manager
    objects = MyUserManager()

    #Login User
    USERNAME_FIELD = 'email'

    #When you create
    REQUIRED_FIELDS = ['first_name','last_name','gender','birth_date']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"