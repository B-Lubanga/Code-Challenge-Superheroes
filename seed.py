from server.app import create_app
from server.models import db, Hero, Power,HeroPower

def seed_db():
    app = create_app()

    with app.app_context():
        # Clear any existing data
        db.session.remove()
        db.drop_all()
        # we created the tables
        db.create_all()

        # Heroes data
        h1 = Hero(name="Kamala Khan", super_name="Ms. Marvel")
        h2 = Hero(name="Doreen Green", super_name="Squirrel Girl")
        h3 = Hero(name="Peter Parker", super_name="Spider-Man")
        h4 = Hero(name="Jean Grey", super_name="Phoenix")
        h5 = Hero(name="T'Challa", super_name="Black Panther")
        h6 = Hero(name="Stephen Strange", super_name="Doctor Strange")
        h7 = Hero(name="Ororo Munroe", super_name="Storm")
        h8 = Hero(name="Scott Summers", super_name="Cyclops")

        # Powers data
        p1 = Power(name="super strength", description="Grants the wielder immense, super-human physical power.")
        p2 = Power(name="flight", description="Gives the ability to soar and maneuver through the air effortlessly.")
        p3 = Power(name="telekinesis", description="Allows the user to move objects with their mind from a distance.")
        p4 = Power(name="spidey sense", description="Heightens danger awareness and reflexes with near precognition.")
        p5 = Power(name="energy blasts", description="Generates powerful beams of energy from the eyes or hands.")
        p6 = Power(name="weather control", description="Manipulates natural elements such as wind, rain, and lightning.")

        db.session.add_all([h1, h2, h3, h4, h5, h6, h7, h8, p1, p2, p3, p4, p5, p6])
        db.session.commit()

        # HeroPower data
        hp1 = HeroPower(strength="Strong", hero_id=h1.id, power_id=p1.id)
        hp2 = HeroPower(strength="Average", hero_id=h2.id, power_id=p2.id)
        hp3 = HeroPower(strength="Weak", hero_id=h3.id, power_id=p3.id)
        hp4 = HeroPower(strength="Strong", hero_id=h4.id, power_id=p4.id)
        hp5 = HeroPower(strength="Average", hero_id=h5.id, power_id=p5.id)
        hp6 = HeroPower(strength="Strong", hero_id=h6.id, power_id=p6.id)
        hp7 = HeroPower(strength="Weak", hero_id=h7.id, power_id=p1.id)
        hp8 = HeroPower(strength="Average", hero_id=h8.id, power_id=p2.id)

        # Add HeroPowers to the database
        db.session.add_all([hp1, hp2, hp3, hp4, hp5, hp6, hp7, hp8])
        db.session.commit()

        print("Database seeded with initial data.")

if __name__ == '__main__':
    seed_db()