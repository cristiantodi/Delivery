from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cargo

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):    
    list_display = ('username', 'email', 'mostrar_cargos', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email', 'telefono', 'cargo')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'telefono', 'cargo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    def mostrar_cargos(self, obj):
        return ", ".join([c.nombre for c in obj.cargo.all()])
    mostrar_cargos.short_description = 'Cargos'
    

    
# admin.site.register(Usuario, UsuarioAdmin)
# admin.site.register(Cargo, CargoAdmin)

