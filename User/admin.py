from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Cargo
# from .forms import UsuarioCreationForm, UsuarioChangeForm

class UserAdmin(UserAdmin):
    # add_form = UsuarioCreationForm
    # form = UsuarioChangeForm
    model = Usuario

    list_display = ('username', 'email', 'mostrar_cargos', 'local', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
                (None,{"fields": (
                        'username', 
                        'password', 
                        'cargo', 
                        'local',                        
                    ),
                }),
                ('Personal Information', {"fields": (
                        'first_name',
                        'last_name', 
                        'email'
                    ),
                }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'cargo', 'local', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

    def mostrar_cargos(self, obj):
        return ", ".join([c.nombre for c in obj.cargo.all()])
    mostrar_cargos.short_description = 'Cargo(s)'

admin.site.register(Usuario, UserAdmin)
admin.site.register(Cargo)
