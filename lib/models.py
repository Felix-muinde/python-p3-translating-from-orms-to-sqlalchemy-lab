#!/usr/bin/env python3

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite database engine
DATABASE_URL = 'sqlite:///dogs.db'  # Change the database URL as needed
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Dog(Base):
    __tablename__ = 'dogs'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

# Create the 'dogs' table in the database (if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# CRUD operations

# Create a new dog record
def create_dog(name, breed):
    dog = Dog(name=name, breed=breed)
    session.add(dog)
    session.commit()

# Retrieve all dogs from the database
def get_all_dogs():
    return session.query(Dog).all()

# Find a dog by its ID
def find_dog_by_id(dog_id):
    return session.query(Dog).filter_by(id=dog_id).first()

# Find a dog by its name
def find_dog_by_name(name):
    return session.query(Dog).filter_by(name=name).first()

# Update a dog's breed by its ID
def update_dog_breed(dog_id, new_breed):
    dog = find_dog_by_id(dog_id)
    if dog:
        dog.breed = new_breed
        session.commit()

# Delete a dog by its ID
def delete_dog_by_id(dog_id):
    dog = find_dog_by_id(dog_id)
    if dog:
        session.delete(dog)
        session.commit()

# Example usage

if __name__ == '__main__':
    # Create and save new dog records
    create_dog("Joey", "Cocker Spaniel")
    create_dog("Fanny", "Cockapoo")

    # Retrieve and print all dogs
    all_dogs = get_all_dogs()
    for dog in all_dogs:
        print(f"Dog ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}")

    # Update a dog's breed
    update_dog_breed(1, "Golden Retriever")

    # Delete a dog by its ID
    delete_dog_by_id(2)

    # Find and print a dog by its name
    found_dog = find_dog_by_name("Joey")
    if found_dog:
        print(f"Found dog: Name: {found_dog.name}, Breed: {found_dog.breed}")
