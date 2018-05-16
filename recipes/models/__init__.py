from peewee import *
database = PostgresqlDatabase('d8o164eqmava48', host="ec2-75-101-142-91.compute-1.amazonaws.com",
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
    category = CharField()

