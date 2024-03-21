import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'primero.settings')

import django
django.setup()

#Configuraciones generales
from nuevaApp.models import Toyota_Legacy
from faker import Faker
faker_generator = Faker()
#Añadir tematicas

#Poblar las tablas
def populate(N=5):
    for entry in range(N):

        primer_nombreF = faker_generator.first_name()
        primer_apellidoF = faker_generator.last_name()
        correoF = faker_generator.email()
        telefonoF = faker_generator.phone_number()

        Toyota_Legacy.objects.get_or_create(primer_nombre=primer_nombreF, primer_apellido=primer_apellidoF, correo=correoF, telefono=telefonoF )[0]

if __name__ == '__main__':
    print("Comienzo a poblar")
    populate(30)
    print("Ya")