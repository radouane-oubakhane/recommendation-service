from django.core.management.base import BaseCommand
from ...consumer import ConsumerGenerateRecommendationsForAllUsers


class Command(BaseCommand):
    help = 'Starts the generate recommendations for all users consumer'

    def handle(self, *args, **options):
        consumer = ConsumerGenerateRecommendationsForAllUsers()
        consumer.consume()


