from .extensions import  db
from datetime import  datetime
import string
from random import choices

#Creating a database model
class Link(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    original_url=db.Column(db.String(1024))
    short_url=db.Column(db.String(10),unique=True)
    visits=db.Column(db.Integer,default=0)
    createdTime=db.Column(db.DateTime,default=datetime.now)

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.short_url=self.generate_shorturl()

    def generate_shorturl(self):
        chars=string.digits+string.ascii_letters
        short_url=''.join(choices(chars,k=10))
        link=self.query.filter_by(short_url=short_url).first()

        if(link):
            self.generate_shorturl()
        return short_url


