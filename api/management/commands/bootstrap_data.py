from django.core.management.base import BaseCommand, CommandError
from api.models import ShoeType, ShoeColor, Shoe


class Command(BaseCommand):
    help = "Chooses shoe attributes, namely, color and type"

    def add_arguments(self, parser):
        # parser.add_argument('shoecolor_id', nargs='+', type=int)
        parser.add_argument(
            '-shoetype',
            choices=['sneaker', 'boot', 'sandal', 'dress', 'other'],
            nargs='+',
            type=str
        )
        parser.add_argument(
            '-shoecolor',
            choices=[
                'red',
                'orange',
                'yellow',
                'green',
                'blue',
                'indigo',
                'violet',
                'white',
                'black'
            ],
            nargs='+',
            type=str
        )

    def handle(self, *args, **options):
        if options['shoetype']:
            each = options['shoetype']

            try:
                ShoeType.objects.get(style=each)

            except ShoeType.MultipleObjectsReturned:
                raise CommandError('ShoeType "%s" already exists. Multiple types detected' % each)

            except ShoeType.DoesNotExist:
                ShoeType.objects.create(style=each)
                print('shoe type added')

            # shoetype.style = 'sneaker'
            # shoetype.save()

            self.stdout.write(self.style.SUCCESS('Shoe Type "%s" now exists' % each))

        if options['shoecolor']:
            each = options['shoecolor']

            try:
                ShoeColor.objects.get(color_name=each)

            except ShoeColor.MultipleObjectsReturned:
                raise CommandError('ShoeColor "%s" already exists. Multiple color types detected' % each)

            except ShoeColor.DoesNotExist:
                ShoeColor.objects.create(color_name=each)
                print('shoe color addded')
            # shoetype.style = 'sneaker'
            # shoetype.save()

            self.stdout.write(self.style.SUCCESS('Shoe Color "%s" now exists' % each))