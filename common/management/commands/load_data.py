from django.core.management.base import BaseCommand, CommandError
import csv

from articles.models import Articles
from shipments.models import Carriers, Shipments


class Command(BaseCommand):
    help = 'Load DB data from csv file'

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            help='Path to the CSV file',
            type=str,
            default='./shipment.csv',
        )

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'r') as file:
            reader = csv.DictReader(file, quoting=csv.QUOTE_ALL)

            for row in reader:
                carrier, created = Carriers.objects.get_or_create(
                    name=row['carrier']
                )
                shipment, created = Shipments.objects.get_or_create(
                    tracking_number=row['tracking_number'],
                    sender_address=row['sender_address'],
                    receiver_address=row['receiver_address'],
                    status=row['status'],
                    carrier=carrier
                )

                article, created = Articles.objects.get_or_create(
                    name=row['article_name'],
                    quantity=row['article_quantity'],
                    price=row['article_price'],
                    sku=row['SKU']
                )

                if row['tracking_number'] == shipment.tracking_number:
                    shipment.articles.add(article)

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
