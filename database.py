#import sqlite3
import peewee
from peewee import *

db = peewee.SqliteDatabase('artists.sqlite')

class Artist(Model):
    id = AutoField()


    name = CharField(unique =True)
    email = CharField()

    class Meta():
        database = db
        constraints = [SQL('UNIQUE( name COLLATE NOCASE)')]

    def _str_(self):
        return f'Artist_ID:{self.id:}, Name:{self.name}, Email:{self.email}'


class Artwork(Model):
    id =AutoField()
    artist = ForeignKeyField(Artist, backref = 'art')
    artwork_name = CharField()
    price = FloatField()
    artwork_available = BooleanField(default=True)
    
    
    class Meta():
        database = db
        constraints = [SQL('UNIQUE( artwork_name COLLATE NOCASE)')]

    def _str_(self):
        return f'Artwork_ID:{self.id:},Artist_Name:{self.artist}, Artwork:{self.artwork_name}, Price{self.price}, ArtworkAvailable{self.artwork_available}'
    
db.connect()
db.create_tables([Artist, Artwork])



db.close()

