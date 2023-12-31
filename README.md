# AirBnB_clone

The goal of this project is to write a command interpreter to manage AirBnB objects, which is this is the first step towards building your first full web application: the AirBnB clone.

# Flow/Features

- A parent class (called BaseModel) to take care of the initialization, serialization and deserialization of future instances.
- A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- Classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- An abstracted storage engine of the project: File storage.

# Unittests

- Tested instance initiation and instance methods of the <code>BaseModel</code> class
- Tested re-creating an instance given dictionary representation.
- Tested <code>file storage</code>.
- Tested State, City, Amenity, Place, Review, classes that inherit from <code>BaseModel</code>
