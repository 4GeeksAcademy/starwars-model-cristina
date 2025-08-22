from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    nombre: Mapped[str] = mapped_column(String(50), nullable=False)
    apellido: Mapped[str] = mapped_column(String(50), nullable=False)
    fecha_subscripcion: Mapped[str] = mapped_column(Date, nullable=False)
    

    favoritos: Mapped[list["Favorito"]] = relationship(back_populates="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "fecha_subscripcion": str(self.fecha_subscripcion)
        }


class Personaje(db.Model):
    __tablename__ = "personaje"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    height: Mapped[str] = mapped_column(String(20))
    mass: Mapped[str] = mapped_column(String(20))
    hair_color: Mapped[str] = mapped_column(String(50))
    skin_color: Mapped[str] = mapped_column(String(50))
    eye_color: Mapped[str] = mapped_column(String(50))
    birth_year: Mapped[str] = mapped_column(String(20))
    gender: Mapped[str] = mapped_column(String(20))

    favoritos: Mapped[list["Favorito"]] = relationship(back_populates="personaje")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }


class Planeta(db.Model):
    __tablename__ = "planeta"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    climate: Mapped[str] = mapped_column(String(50))
    terrain: Mapped[str] = mapped_column(String(50))
    population: Mapped[str] = mapped_column(String(50))
    diameter: Mapped[str] = mapped_column(String(50))

    favoritos: Mapped[list["Favorito"]] = relationship(back_populates="planeta")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "terrain": self.terrain,
            "population": self.population,
            "diameter": self.diameter
        }


class Vehiculo(db.Model):
    __tablename__ = "vehiculo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100))
    manufacturer: Mapped[str] = mapped_column(String(100))
    consumables: Mapped[str] = mapped_column(String(50))
    length: Mapped[str] = mapped_column(String(50))
    crew: Mapped[str] = mapped_column(String(50))
    passengers: Mapped[str] = mapped_column(String(50))

    favoritos: Mapped[list["Favorito"]] = relationship(back_populates="vehiculo")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "consumables": self.consumables,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers
        }


class Favorito(db.Model):
    __tablename__ = "favorito"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    personaje_id: Mapped[int] = mapped_column(ForeignKey("personaje.id"))
    planeta_id: Mapped[int] = mapped_column(ForeignKey("planeta.id"))
    vehiculo_id: Mapped[int] = mapped_column(ForeignKey("vehiculo.id"))

    user: Mapped["User"] = relationship(back_populates="favoritos")
    personaje: Mapped["Personaje"] = relationship(back_populates="favoritos")
    planeta: Mapped["Planeta"] = relationship(back_populates="favoritos")
    vehiculo: Mapped["Vehiculo"] = relationship(back_populates="favoritos")

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "personaje_id": self.personaje_id,
            "planeta_id": self.planeta_id,
            "vehiculo_id": self.vehiculo_id
        }