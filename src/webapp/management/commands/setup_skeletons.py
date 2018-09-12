from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError


def get_admin():
    """Return the default admin, creating it if not present."""
    admin = settings.ADMIN_USER
    model = get_user_model()
    if model is None:
        raise ImportError("Cannot import the specified User model")
    username = model.USERNAME_FIELD
    restrict = [username, 'password']
    defaults = {x: True for x in ['is_staff', 'is_superuser', 'is_active']}
    env_vals = {k: v for k, v in admin.items() if k not in restrict}
    defaults.update(env_vals)
    try:
        values = {username: admin[username], 'defaults': defaults}
        user, new = model.objects.get_or_create(**values)
    except IntegrityError:
        raise AttributeError("Admin user not found or able to be created.")
    if new:
        user.set_password(admin['password'])
        user.save()
    return user


def get_site():
    """Return the default site, creating it if not present."""
    defaults = {
        'name': settings.APP_NAME,
        'domain': settings.URL.hostname,
    }
    kwargs = {
        'pk': settings.SITE_ID,
        'defaults': defaults,
    }
    return Site.objects.get_or_create(**kwargs)[0]


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(f'Running setup for {settings.APP_NAME}')
        get_admin()
        get_site()