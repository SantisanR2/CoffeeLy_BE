from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password
from .finca import Finca
from postgres_copy import CopyManager

class UserManager(BaseUserManager, CopyManager):
    
    def create_user(self, correo, password=None):
        """
        Crea y guarda el usuario con el correo y contraseña dada.
        """
        if not correo:
            raise ValueError('Los usuarios deben tener un correo')
        user = self.model(correo=correo)
        user.set_password(password)
        user.save(using=self._db)
        return user
    


class User(AbstractBaseUser, PermissionsMixin):

    RECOLECTOR = 1
    ADMIN_FINCA = 2
    OPERADOR = 3
    ADMIN_EMPRESA = 4

    ROLE_CHOICES = (
        (RECOLECTOR, 'Recolector'),
        (ADMIN_FINCA, 'AdminFinca'),
        (OPERADOR, 'Operador'),
        (ADMIN_EMPRESA, 'AdminEmpresa')
    )

    id = models.BigAutoField(primary_key=True)
    name = models.CharField('Nombre', max_length = 30)
    password = models.CharField('Password', max_length = 256)
    correo = models.EmailField('Correo', max_length = 100, unique=True)
    finca = models.ForeignKey(Finca, related_name='Finca', on_delete=models.CASCADE, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)
    is_active = models.BooleanField(default=True)
    cedula = models.CharField('Cedula', max_length = 30)
    celular = models.CharField('Celular', max_length = 30)
    fecha = models.DateField('FechaNacimiento',auto_now=False) 

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password, some_salt)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'correo'