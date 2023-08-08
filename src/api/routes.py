"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.utils import generate_sitemap, APIException
from api.models import db, User, Planets, People, Favorite
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


api = Blueprint('api', __name__)


# ---------- ENDPOINTS ------------#

####GET ALL ####

@api.route('/users', methods=['GET'])
def get_all_users():
    users_query = User.query.all()
    results = list(map(lambda item: item.serialize(),users_query))
    print(users_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /user response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@api.route('/planets', methods=['GET'])
def get_all_planets():
    planets_query = Planets.query.all()
    results = list(map(lambda item: item.serialize(),planets_query))
    print(planets_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /Planets response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@api.route('/people', methods=['GET'])
def get_all_people():
    people_query = People.query.all()
    results = list(map(lambda item: item.serialize(),people_query))
    print(people_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /people response ",   
        "results": results 
    }

    return jsonify(response_body), 200


@api.route('/favorite', methods=['GET'])
def get_all_favorite():
    favorite_query = Favorite.query.all()
    results = list(map(lambda item: item.serialize(),favorite_query))
    print(favorite_query)
    print(results)

    response_body = {
        "msg": "Hello, this is your GET /favorite response ",   
        "results": results 
    }

    return jsonify(response_body), 200


#### GET SINGLE ####

@api.route('/users/<int:user_id>', methods=['GET'])
def get_one_user(user_id):
    user_query = User.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(user_query)

    response_body = {
        "msg": "ok ",   
        "results": user_query.serialize() 
    }

    return jsonify(response_body), 200


@api.route('/planets/<int:user_id>', methods=['GET'])
def get_one_planet(user_id):
    planet_query = Planets.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(planet_query)

    response_body = {
        "msg": "ok ",   
        "results": planet_query.serialize() 
    }

    return jsonify(response_body), 200


@api.route('/people/<int:user_id>', methods=['GET'])
def get_one_person(user_id):
    people_query = People.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(people_query)

    response_body = {
        "msg": "ok ",   
        "results": people_query.serialize() 
    }

    return jsonify(response_body), 200


@api.route('/favorite/<int:user_id>', methods=['GET'])
def get_one_favorite(user_id):
    favorite_query = Favorite.query.filter_by(id=user_id).first()
    
    print(user_id)
    print(favorite_query)

    response_body = {
        "msg": "ok ",   
        "results": favorite_query.serialize() 
    }

    return jsonify(response_body), 200



#### POST ####

@api.route('/users', methods=['POST'])
def create_user():

    request_body = request.get_json(force=True)   
    user = User(name=request_body["name"],lastname=request_body["lastname"], email=request_body["email"], password=request_body["password"], suscriptiondate=request_body["suscriptiondate"])
    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "user created ",  
        
    }

    return jsonify(response_body), 200


@api.route('/planets', methods=['POST'])
def create_planet():

    request_body = request.get_json(force=True)   
    planet = Planets(name=request_body["name"],population=request_body["population"], size=request_body["size"], gravity=request_body["gravity"], field=request_body["field"])
    db.session.add(planet)
    db.session.commit()

    response_body = {
        "msg": "planet created ",  
        
    }

    return jsonify(response_body), 200


@api.route('/people', methods=['POST'])
def create_person():

    request_body = request.get_json(force=True)   
    person = People(name=request_body["name"],height=request_body["height"], birth=request_body["birth"], gender=request_body["gender"], eyes=request_body["eyes"], hair=request_body["hair"],weight=request_body["weight"])
    db.session.add(person)
    db.session.commit()

    response_body = {
        "msg": "person created ",  
        
    }

    return jsonify(response_body), 200


@api.route('/favorite', methods=['POST'])
def create_favorite():

    request_body = request.get_json(force=True)   
    favorite = Favorite(user_id=request_body["user_id"],planet_id=request_body["planet_id"], people_id=request_body["people_id"])
    db.session.add(favorite)
    db.session.commit()

    response_body = {
        "msg": "favorite created ",  
        
    }

    return jsonify(response_body), 200


#### DELETE ####

@api.route('/users/<int:user_id>/favoritos/', methods=['DELETE'])
def del_favorite(user_id):

    body = request.get_json(force=True)
    
    if body["characters_id"] is None:
        favorito_query= Favorite.query.filter_by(user_id=user_id).filter_by(planet_id=body["planet_id"]).first()
    
    else:
        favorito_query= Favorite.query.filter_by(user_id=user_id).filter_by(people_id=body["people_id"]).first()
   

    db.session.delete(favorito_query)
    db.session.commit()


    response_body = {
        'msg':'ok',
        "results": 'Favorite deleted'
    }

    return jsonify(response_body), 200


##### PUT  ####

@api.route('/users/<int:user_id>', methods=['PUT', 'GET'])
def get_single_user(user_id):

    body = request.get_json(force=True) 
    if request.method == 'PUT':
        user1 = User.query.get(user_id)
        user1.email = body["email"]
        db.session.commit()
        return jsonify(user1.serialize()), 200
    if request.method == 'GET':
        user1 = User.query.get(user_id)
        return jsonify(user1.serialize()), 200

    return "Invalid Method", 404


@api.route('/login', methods=['POST'])
def login():
    email = request.json.get("email",None) 
    password = request.json.get("password",None) 

    user = User.query.filter_by(email=email).first()
    print(user)

    if user is None:
        return jsonify({"msg": "user doesnt exist"}), 404
    
    if email != user.email or password != user.password:
        return jsonify({"msg": "Bad username or password"}), 401
    
    access_token = create_access_token(identity=email)
    return jsonify(acess_token=access_token)

@api.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200




@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200