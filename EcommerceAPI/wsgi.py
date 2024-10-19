import os
import sys

# Add the project directory to the sys.path
project_home = '/home/MaryJeremiah/Ecommerce-django'  # Update this path as necessary
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EcommerceAPI.settings')

try:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception as e:
    # Print out the exception message if there is an error
    print(f"Error importing WSGI application: {e}")
