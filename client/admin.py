from django.contrib import admin
from .models import Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ('nombres','apellidos', 'direccion', 'telefono', 'email',)
	list_filter = ('nombres',)

