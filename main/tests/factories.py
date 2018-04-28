from faker import Faker
from main import models
from sqlalchemy import orm

import factory
import factory.alchemy
import main
import random
import sqlalchemy

fake = Faker()


class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = models.User
        sqlalchemy_session = main.db.session

    id = factory.Sequence(lambda n: n)
    username = factory.LazyAttribute(lambda x: fake.user_name())
    password = factory.LazyAttribute(lambda x: fake.password())
