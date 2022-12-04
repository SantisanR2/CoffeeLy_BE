from django.contrib import admin
from .models.user import User
from .models.catacion import Catacion
from .models.cosecha import Cosecha
from .models.despulpado import Despulpado
from .models.fermentacion import Fermentacion
from .models.fertilizacion import Fertilizacion
from .models.finca import Finca
from .models.lavado import Lavado
from .models.lote import Lote
from .models.maquina import Maquina
from .models.molienda import Molienda
from .models.poda import Poda
from .models.riego import Riego
from .models.secado import Secado
from .models.seleccion import Seleccion
from .models.siembra import Siembra
from .models.tostion import Tostion

admin.site.register(User)
admin.site.register(Catacion)
admin.site.register(Cosecha)
admin.site.register(Despulpado)
admin.site.register(Fermentacion)
admin.site.register(Fertilizacion)
admin.site.register(Finca)
admin.site.register(Lavado)
admin.site.register(Lote)
admin.site.register(Maquina)
admin.site.register(Molienda)
admin.site.register(Poda)
admin.site.register(Riego)
admin.site.register(Secado)
admin.site.register(Seleccion)
admin.site.register(Siembra)
admin.site.register(Tostion)