#!/usr/bin/python3

from datetime import datetime
from uuid import uuid4


class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        """

        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if (len(kwargs) != 0):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        datetime.strptime(value, date_format)
                    if key == "updated_at":
                        datetime.strptime(value, date_format)
                    setattr(self, key, value)

        else:
            self.id = uuid4()
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """
        """

        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
        """

        final_dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            final_dict[key] = value
            if key == "created_at":
                final_dict[key] = datetime.isoformat(value)
            if key == "updated_at":
                final_dict[key] = datetime.isoformat(value)
            if key == "id":
                final_dict[key] = str(value)
        return(final_dict)
