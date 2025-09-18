# routesFavs.py
from flask import request, jsonify
from models import db, Favorito, Personaje, Planeta

def favorites_routes(app):

    #  GET favorites del usuario actual 
    @app.route("/users/favorites", methods=["GET"])
    def get_user_favorites():
        user_id = 1  # Simulando usuario actual
        favoritos = Favorito.query.filter_by(user_id=user_id).all()
        return jsonify([f.serialize() for f in favoritos]), 200

    #  ADD planet favorite 
    @app.route("/favorite/planet/<int:planet_id>", methods=["POST"])
    def add_fav_planet(planet_id):
        user_id = 1
        planet = Planeta.query.get(planet_id)
        if not planet:
            return jsonify({"msg": "Planeta no encontrado"}), 404

        fav = Favorito(user_id=user_id, planeta_id=planet_id)
        db.session.add(fav)
        db.session.commit()
        return jsonify(fav.serialize()), 201

    #  ADD people favorite 
    @app.route("/favorite/people/<int:people_id>", methods=["POST"])
    def add_fav_people(people_id):
        user_id = 1
        person = Personaje.query.get(people_id)
        if not person:
            return jsonify({"msg": "Personaje no encontrado"}), 404

        fav = Favorito(user_id=user_id, personaje_id=people_id)
        db.session.add(fav)
        db.session.commit()
        return jsonify(fav.serialize()), 201

    #  DELETE planet favorite 
    @app.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
    def delete_fav_planet(planet_id):
        user_id = 1
        fav = Favorito.query.filter_by(user_id=user_id, planeta_id=planet_id).first()
        if not fav:
            return jsonify({"msg": "Favorito no encontrado"}), 404
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"msg": f"Planeta {planet_id} eliminado de favoritos"}), 200

    #  DELETE people favorite 
    @app.route("/favorite/people/<int:people_id>", methods=["DELETE"])
    def delete_fav_people(people_id):
        user_id = 1
        fav = Favorito.query.filter_by(user_id=user_id, personaje_id=people_id).first()
        if not fav:
            return jsonify({"msg": "Favorito no encontrado"}), 404
        db.session.delete(fav)
        db.session.commit()
        return jsonify({"msg": f"Personaje {people_id} eliminado de favoritos"}), 200
