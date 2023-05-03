from django.contrib import admin
from . models import Cargo, Funcionario, Menu, TipoCardapio


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'modificado')
    
    
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'modificado')
    
    
@admin.register(TipoCardapio)
class TipoCardapioAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'modificado')
    
    
@admin.register(Menu)
class MEnuAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'modificado')

    
    