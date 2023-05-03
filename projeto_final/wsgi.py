import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling, MediaCling


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto_final.settings')

application = Cling(MediaCling(get_wsgi_application()))
