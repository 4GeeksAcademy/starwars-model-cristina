from flask import request, jsonify
from models import db, Personaje

def people_routes(app):

    #  GET all 
    @app.route("/people", methods=["GET"])
    def get_people():
        people = Personaje.query.all()
        return jsonify([p.serialize() for p in people]), 200

    #  GET by ID 
    @app.route("/people/<int:people_id>", methods=["GET"])
    def get_person(people_id):
        person = Personaje.query.get(people_id)
        if not person:
            return jsonify({"msg": "Personaje no encontrado"}), 404
        return jsonify(person.serialize()), 200

    #  POST 
    @app.route("/people", methods=["POST"])
    def create_person():
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"msg": "El nombre es obligatorio"}), 400

        new_person = Personaje(
            name=data["name"],
            height=data.get("height"),
            mass=data.get("mass"),
            hair_color=data.get("hair_color"),
            skin_color=data.get("skin_color"),
            eye_color=data.get("eye_color"),
            birth_year=data.get("birth_year"),
            gender=data.get("gender")
        )
        db.session.add(new_person)
        db.session.commit()
        return jsonify(new_person.serialize()), 201

    #  PUT 
    @app.route("/people/<int:people_id>", methods=["PUT"])
    def update_person(people_id):
        person = Personaje.query.get(people_id)
        if not person:
            return jsonify({"msg": "Personaje no encontrado"}), 404

        data = request.get_json()
        for field in ["name", "height", "mass", "hair_color", "skin_color", "eye_color", "birth_year", "gender"]:
            if field in data:
                setattr(person, field, data[field])

        db.session.commit()
        return jsonify(person.serialize()), 200

    #  DELETE 
    @app.route("/people/<int:people_id>", methods=["DELETE"])
    def delete_person(people_id):
        person = Personaje.query.get(people_id)
        if not person:
            return jsonify({"msg": "Personaje no encontrado"}), 404
        db.session.delete(person)
        db.session.commit()
        return jsonify({"msg": f"Personaje {people_id} eliminado"}), 200