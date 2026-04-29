#!/usr/bin/python3
"""Defines the CustomObject class that displays, serializes, and deserializes data using the pickle module."""

import pickle

class CustomObject:
    """A class that represents a custom object with attributes for name, age, and student status.
    
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.
    
    Methods:
        __init__(self, name, age, is_student): Initializes a new CustomObject with the provided attributes.
        display(self): Displays the object's attributes.
        serialize(self, filename): Serializes the current instance of the object and saves it to a file.
        deserialize(cls, filename): Deserializes an object from a file and returns the object instance.
    """

    def __init__(self, name, age, is_student):
        """Initializes a new instance of CustomObject with name, age, and student status.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes: name, age, and is_student.
        
        This method prints the attributes of the object in a human-readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of the object and saves it to a file.
        
        Args:
            filename (str): The name of the file where the object should be serialized.
        
        This method uses the pickle module to convert the object into a byte stream and writes
        it to the file in binary mode. If an error occurs during the process, None is returned.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            print(f"Object successfully serialized to {filename}")
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file and returns the object instance.
        
        Args:
            filename (str): The name of the file containing the serialized object.
        
        Returns:
            CustomObject or None: Returns the deserialized object if successful, otherwise None.
        
        This method reads the binary file, converts the byte stream back into a CustomObject instance,
        and returns it. If an error occurs during deserialization, None is returned.
        """
        try:
            with open(filename, "rb") as f:
                ret = pickle.load(f)
            print(f"Object successfully deserialized from {filename}")
            return ret
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None
#!/usr/bin/python3
"""Defines the CustomObject class that displays, serializes, and deserializes data using the pickle module."""

import pickle

class CustomObject:
    """A class that represents a custom object with attributes for name, age, and student status.
    
    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        is_student (bool): Whether the person is a student or not.
    
    Methods:
        __init__(self, name, age, is_student): Initializes a new CustomObject with the provided attributes.
        display(self): Displays the object's attributes.
        serialize(self, filename): Serializes the current instance of the object and saves it to a file.
        deserialize(cls, filename): Deserializes an object from a file and returns the object instance.
    """

    def __init__(self, name, age, is_student):
        """Initializes a new instance of CustomObject with name, age, and student status.
        
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student or not.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Displays the object's attributes: name, age, and is_student.
        
        This method prints the attributes of the object in a human-readable format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serializes the current instance of the object and saves it to a file.
        
        Args:
            filename (str): The name of the file where the object should be serialized.
        
        This method uses the pickle module to convert the object into a byte stream and writes
        it to the file in binary mode. If an error occurs during the process, None is returned.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            print(f"Object successfully serialized to {filename}")
        except Exception as e:
            print(f"Error during serialization: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserializes an object from a file and returns the object instance.
        
        Args:
            filename (str): The name of the file containing the serialized object.
        
        Returns:
            CustomObject or None: Returns the deserialized object if successful, otherwise None.
        
        This method reads the binary file, converts the byte stream back into a CustomObject instance,
        and returns it. If an error occurs during deserialization, None is returned.
        """
        try:
            with open(filename, "rb") as f:
                ret = pickle.load(f)
            print(f"Object successfully deserialized from {filename}")
            return ret
        except Exception as e:
            print(f"Error during deserialization: {e}")
            return None

