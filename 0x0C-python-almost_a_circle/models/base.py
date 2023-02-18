#!/usr/bin/python3
""" Base model module """
import json


class Base:
    """ defines the Base class for other geometry shape """
    __nb_object = 0

    def __init__(self, id=None):
        """ instance initialiser """
        if id:
            self.id = id
        else:
            Base.__nb_object += 1
            self.id = Base.__nb_object

        @staticmethod
        def to_json_string(list_dictionaries):
            """ returns the JSON string representation of list_dictionaries:

            list_dictionaries is a list of dictionaries
            If list_dictionaries is None or empty, return the string: "[]"

            Otherwise, return the JSON string 
            representation of list_dictionaries
            """
            if not list_dictionaries or list_dictionaries is None:
                return "[]"
            json_dict = []
            return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
            '''
                Writes the string representation of an object of a class
                into a file
            '''
            file_name = cls.__name__ + ".json"

            content = []
            if list_objs is not None:
                for item in list_objs:
                    item = item.to_dictionary()
                    json_dict = json.loads(cls.to_json_string(item))
                    content.append(json_dict)

            with open(file_name, mode="w") as fd:
                json.dump(content, fd)

        @classmethod
        def create(cls, **dictionary):
            '''
                Returns an instance with all the attributes already set
            '''
            from models.rectangle import Rectangle
            from models.square import Square

            if cls.__name__ == "Rectangle":
                r2 = Rectangle(3, 8)
            elif cls.__name__ == "Square":
                r2 = Square(5)
            r2.update(**dictionary)
            return (r2)
