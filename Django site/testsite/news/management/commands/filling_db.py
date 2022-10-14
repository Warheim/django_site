from django.core.management import BaseCommand
from news.models import News


class Command(BaseCommand):
    def handle(self, *args, **options):
        for number in range(6, 11):
            News(title=f'Новость {number}', content=f'Контент новости {number}').save()

