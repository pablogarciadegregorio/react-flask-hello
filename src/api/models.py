from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String

db = SQLAlchemy()



class User(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    lastname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    suscriptiondate = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "lastname": self.lastname,
            "email": self.email,
            "suscriptiondate": self.suscriptiondate,
            "password": self.password,

            
        }
    
class Planets(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    population = db.Column(db.String(250))
    size = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    field = db.Column(db.String(250), nullable=False)
    

    def __repr__(self):
        return '<Planets %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "size": self.size,
            "gravity": self.gravity,
            "field": self.field,

            
        }


class People(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    birth = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    eyes = db.Column(db.String(250), nullable=False)
    hair = db.Column(db.String(250), nullable=False)
    weight = db.Column(db.String(250), nullable=False)
    
    

    def __repr__(self):
        return '<People %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "birth": self.birth,
            "gender": self.gender,
            "eyes": self.eyes,
            "hair": self.hair,
            "weight": self.weight,

            
        }
    
class Favorite(db.Model):
  
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(250), nullable=False)
    planet_id = db.Column(db.String(250), nullable=False)
    people_id = db.Column(db.String(250), nullable=False)
    
   
    

    def __repr__(self):
        return '<Favorite %r>' % self.id
    
    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id,
                       
        }