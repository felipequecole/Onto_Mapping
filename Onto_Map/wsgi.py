"""
WSGI config for Onto_Map project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application


# project_home = u'/home/ubuntu/ontomap'
# if project_home not in sys.path:
# 	print('not in path')
# 	sys.path.append(project_home)
#
#
# sys.path.append(u'/home/ubuntu/ontomap/ontomap_env/lib/python3.5/site-packages')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Onto_Map.settings")

application = get_wsgi_application()
