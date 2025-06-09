## 🛠️ Requisitos Técnicos

- Python 3.12+
- Django 5.2
- SQLite (base de datos por defecto)
- Dependencias adicionales en `requirements.txt`

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPO]
```

2. Crear y activar entorno virtual:
```bash
python -m venv virtual
source virtual/bin/activate  # Linux/Mac
.\virtual\Scripts\activate  # Windows
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno (opcional):
```bash
cp .env.example .env
```

5. Ejecutar migraciones:
```bash
python manage.py migrate
```

6. Crear superusuario (opcional):
```bash
python manage.py createsuperuser
```

7. Iniciar servidor de desarrollo:
```bash
python manage.py runserver
```
