#!/usr/bin/py3thon3
"""
The class BaseModel.
"""
from uuid import uuid4
from datetime import datetime
class BaseModel:
  def __init__(self):
    self.id = str(uuid4())
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

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

"""
self.__dict__ = {id : 83242, created_at : 2012 141 125, updated_at : 372923, name : 'vince', my_number : '45'}
"""
