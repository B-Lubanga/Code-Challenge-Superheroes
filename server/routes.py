from flask import Blueprint, jsonify, request
from server.models import db, Hero, Power, HeroPower

main = Blueprint('main', __name__)

@main.route('/heroes')
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()])

@main.route('/heroes/<int:id>')
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.to_dict())
    return jsonify({"error": "Hero not found"}), 404

@main.route('/powers')
def get_powers():
    return jsonify([power.to_dict() for power in Power.query.all()])

@main.route('/powers/<int:id>', methods=["GET", "PATCH"])
def handle_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    if request.method == "GET":
        return jsonify(power.to_dict())
    else:
        data = request.get_json()
        try:
            power.description = data['description']
            db.session.commit()
            return jsonify(power.to_dict())
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

@main.route('/hero_powers', methods=["POST"])
def create_hero_power():
    data = request.get_json()
    try:
        hp = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hp)
        db.session.commit()

        hero = Hero.query.get(hp.hero_id)
        return jsonify({
            "id": hp.id,
            "hero_id": hp.hero_id,
            "power_id": hp.power_id,
            "strength": hp.strength,
            "hero": {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            },
            "power": hp.power.to_dict()
        })
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
