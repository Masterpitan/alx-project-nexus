from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Setup database with migrations and create superuser'

    def handle(self, *args, **options):
        self.stdout.write('Making migrations...')
        call_command('makemigrations')
        
        self.stdout.write('Applying migrations...')
        call_command('migrate')
        
        # Create superuser if none exists
        if not User.objects.filter(is_superuser=True).exists():
            self.stdout.write('Creating superuser...')
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superuser created: admin/admin123')
        
        self.stdout.write(self.style.SUCCESS('Database setup complete!'))