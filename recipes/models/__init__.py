from peewee import *
from playhouse.postgres_ext import *

database = PostgresqlExtDatabase('d8o164eqmava48', host="ec2-75-101-142-91.compute-1.amazonaws.com",
                              user="uaipaqgenqqhdo",
                              port="5432",
                              password="b347a0c9c9f5994f09746706dd7e31c14eef23aac2b5aa41b82f7c17999b6d31")

class BaseModel(Model):
    class Meta:
        database=database

class Recipe(BaseModel):
    recipe = CharField()
    ingredients = CharField()
    instructions = CharField()
    menuimgurl = CharField()

class Category(BaseModel):
    category = CharField()
    order = CharField()

class Recipe_Category(BaseModel):
    recipe = ForeignKeyField(Recipe)
    category = ForeignKeyField(Category)
    recipe_id = IntegerField()
    category_id = IntegerField()
