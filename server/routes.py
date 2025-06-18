from flask import Blueprint, jsonify, request
from server.models import db, Hero, Power, HeroPower

# Creates a Blueprint object for the routes. This helps in organizing the application.
main = Blueprint('main', __name__)


# this one Defines a route for the "/heroes" endpoint to handle GET requests and return a list of all heroes.na it happens to all the others
@main.route('/heroes')
def get_heroes():
     # Here, we get to Query the database for all Hero instances and serialize/put them into dictionaries.
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
        except Exception as error:
            return jsonify({"errors": [str(error)]}), 400

@main.route('/hero_powers', methods=["POST"])
def create_hero_power():
    data = request.get_json()
    #here we get to Define the required fields for creating a HeroPower instance and check if any are missing
    required_fields = ['strength', 'hero_id', 'power_id']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        hero = Hero.query.get(data['hero_id'])
        power = Power.query.get(data['power_id'])

        if not hero or not power:
            return jsonify({"error": "Hero or Power not found"}), 404
         
        # Create a new HeroPower instance with the provided data and add it to the database session
        hp = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        db.session.add(hp)
        db.session.commit()

        # Serialize the new HeroPower instance and its associated Hero and Power into dictionaries.
        return jsonify({
            "id": hp.id,
            "hero_id": hp.hero_id,
            "power_id": hp.power_id,
            "strength": hp.strength,
            "hero": hero.to_dict(),
            "power": power.to_dict()
        })
    except Exception as error:
         # You catch the error if an exception occurs and Rollback this database session and this returns an error
        db.session.rollback()  
        return jsonify({"errors": [str(error)]}), 400