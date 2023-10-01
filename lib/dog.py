from models import Dog

def create_table(base):
    # Create the table for the Dog model if it doesn't exist
    base.metadata.create_all()

def save(session, dog):
    # Add a Dog object to the session and commit it to the database
    session.add(dog)
    session.commit()

def get_all(session):
    # Retrieve all Dog objects from the database
    return session.query(Dog).all()

def find_by_name(session, name):
    # Find a Dog by name
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    # Find a Dog by its ID
    return session.query(Dog).filter_by(id=id).first()

def find_by_name_and_breed(session, name, breed):
    # Find a Dog by name and breed
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    # Update the breed of a Dog object
    dog.breed = breed
    session.commit()
