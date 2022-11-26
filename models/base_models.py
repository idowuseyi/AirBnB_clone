#!/usr/bin/py3thon3
"""
The class BaseModel.
"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
  def __init__(self, *args, **kwargs):
    if args:
      """ *args should not be used """
      pass
    if len(kwargs) == 0:
      """ If not kwargs or if kwargs is None """
      self.id = str(uuid4())
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
    if kwargs is not None:
      """ If kwargs is not None """
      for key in kwargs.keys():
        if key == '__class__':
          continue
        else:
          if key == "updated_at" or key == "created_at":
            kwargs[key] = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
          setattr(self, key, kwargs[key])

  def __str__(self):
    return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

  def save(self):
    self.updated_at = datetime.now()

  def to_dict(self):
    dic = {}
    for k, v in self.__dict__.items():
      dic[k] = v
      if k in ["created_at", "updated_at"]:
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
    dic['__class__'] = self.__class__.__name__
    return dic
