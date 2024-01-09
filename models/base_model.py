#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self):
        """
        """
        self.id = uuid4()
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """"
        """
        return("[{}] ({}) {}".format(self.__class__.__name__,self.id, self.__dict__))
    
    def save(self):
        """
        """
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """
        """
        final_dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key == "created_at":
                final_dict[key] = datetime.isoformat(value)
            if key == "updated_at":
                final_dict[key] = datetime.isoformat(value)
            if key == "id":
                final_dict[key] = str(value)
            else:
                final_dict[key] = value
        
        return(final_dict)

    


model = BaseModel()
print(model.__init__())
# model.name = "User"
# print(model.__dict__)
# print("Custom Dict")
# my_model = model.to_dict()
# print(my_model)
