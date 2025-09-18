# routesPlanets.py
from flask import request, jsonify
from models import db, Planeta

def planets_routes(app):

    #  GET all 
    @app.route("/planets", methods=["GET"])
    def get_planets():
        planets = Planeta.query.all()
        return jsonify([p.serialize() for p in planets]), 200

    #  GET by ID 
    @app.route("/planets/<int:planet_id>", methods=["GET"])
    def get_planet(planet_id):
        planet = Planeta.query.get(planet_id)
        if not planet:
            return jsonify({"msg": "Planeta no encontrado"}), 404
        return jsonify(planet.serialize()), 200

    #  POST  
    @app.route("/planets", methods=["POST"])
    def create_planet():
        data = request.get_json()
        if not data or "name" not in data:
            return jsonify({"msg": "El nombre es obligatorio"}), 400

        new_planet = Planeta(
            name=data["name"],
            climate=data.get("climate"),
            terrain=data.get("terrain"),
            population=data.get("population"),
            diameter=data.get("diameter")
        )
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(new_planet.serialize()), 201

    #  PUT 
    @app.route("/planets/<int:planet_id>", methods=["PUT"])
    def update_planet(planet_id):
        planet = Planeta.query.get(planet_id)
        if not planet:
            return jsonify({"msg": "Planeta no encontrado"}), 404

        data = request.get_json()
        for field in ["name", "climate", "terrain", "population", "diameter"]:
            if field in data:
                setattr(planet, field, data[field])

        db.session.commit()
        return jsonify(planet.serialize()), 200

    #  DELETE 
    @app.route("/planets/<int:planet_id>", methods=["DELETE"])
    def delete_planet(planet_id):
        planet = Planeta.query.get(planet_id)
        if not planet:
            return jsonify({"msg": "Planeta no encontrado"}), 404
        db.session.delete(planet)
        db.session.commit()
        return jsonify({"msg": f"Planeta {planet_id} eliminado"}), 200
