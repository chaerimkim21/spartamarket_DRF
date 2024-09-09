from django.core.management.base import BaseCommand
from django_seed import Seed
from products.models import Product, Hashtag
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "이 커맨드를 통해 랜덤한 Product와 Hashtag 데이터를 만듭니다."

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        User = get_user_model()

        # Hashtag 생성
        seeder.add_entity(Hashtag, 20, {
            'content': lambda x: seeder.faker.word(),
        })

        # author 필드를 위해 생성된 User 인스턴스 받아오기
        created_users = User.objects.all()

        # Product 생성
        seeder.add_entity(Product, 20, {
            'title': lambda x: seeder.faker.word(),
            'content': lambda x: seeder.faker.text(),
            # author로 기존 유저들 중에서 랜덤하게 고름
            'author': lambda x: created_users.order_by('?').first(),
        })

        # product seeding하기
        inserted_product_pks = seeder.execute()[Product]
        self.stdout.write(self.style.SUCCESS(
            f"만들어진 product의 id: {inserted_product_pks}"))
