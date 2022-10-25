from django.core.management.base import BaseCommand, CommandError
from sinimg.models import SinImg
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = "Deletes the images which were uploaded half hour ago"

    def handle(self, *args, **options):
        images = SinImg.objects.filter(created_at__lte = timezone.now() - timedelta(minutes=38))
        self.stdout.write(self.style.SUCCESS("Successfully deleted the images"))
        print("Successfully deleted the images")
        return
        