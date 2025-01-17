# project_settings.py
from pathlib import Path
import os
# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Clave secreta y debug
SECRET_KEY = 'django-insecure-jocox=t1y3oie&ow1l2-5d2@g@iiy&&qr&-fo0(eprxo7cd34!'

DEBUG = True



# Configuración de la base de datos
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'FqioM5AbYf6N8yrT',
        'HOST': 'db.qdapsrodtqvrajvmtqqw.supabase.co',
        'PORT': '',
    }
}

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# defino la url para que mande al admin
LOGIN_REDIRECT_URL = '/admin/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
