from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    help = 'Заполняет базу данных образцовыми данными'

    def handle(self, *args, **options):
        # Удаление старых данных
        self.stdout.write(self.style.NOTICE('Deleting old data...'))
        Category.objects.all().delete()

        # Заполнение новыми данными
        self.stdout.write(self.style.NOTICE('Populating new data...'))
        categories_data = [
            {'title': 'Электроника', 'description': 'Широкий ассортимент электронных устройств и аксессуаров. От современных смартфонов и ноутбуков до умных гаджетов для дома.'},
            {'title': 'Одежда и обувь', 'description': 'Обновите свой гардероб с нами. У нас есть все, что нужно, от повседневных нарядов до эксклюзивных дизайнов.'},
            {'title': 'Дом и быт', 'description': 'Создайте уют и гармонию в своем доме с нашим широким выбором мебели, предметов интерьера и бытовой техники.'},
            {'title': 'Спорт и отдых', 'description': 'Поддерживайте свою форму и активный образ жизни с нашими спортивными товарами. У нас есть все, чтобы помочь вам достичь своих спортивных целей.'},
            {'title': 'Красота и здоровье', 'description': 'Заботьтесь о своей красоте и здоровье с нашими товаров для ухода за кожей, волосами, зубами и телом.'},
        ]

        categories_to_add = [Category(**category_data) for category_data in categories_data]
        Category.objects.bulk_create(categories_to_add)

        self.stdout.write(self.style.SUCCESS('Data populated successfully'))



