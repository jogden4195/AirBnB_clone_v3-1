#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
import models
from models.base_model import BaseModel

to_json = BaseModel.to_json


class FileStorage:
    """handles long term storage of all class instances"""

    __file_path = './dev/file.json'
    __objects = {}

    def all(self):
        """returns private attribute: __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets / updates in __objects the obj with key <obj class name>.id"""
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        fname = FileStorage.__file_path
        d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            d[bm_id] = bm_obj.to_json()
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(d, f_io)

    def reload(self):
        """if file exists, deserializes JSON file to __objects, else nothing"""
        fname = FileStorage.__file_path
        try:
            with open(fname, mode='r', encoding='utf-8') as f_io:
                new_objs = json.load(f_io)
            for o_id, d in new_objs.items():
                k_cls = d['__class__']
                if not isinstance(d['created_at'], datetime):
                    d['created_at'] = strptime(d['created_at'],
                                               "%Y-%m-%d %H:%M:%S.%f")
                if 'updated_at' in d:
                    if not isinstance(d['updated_at'], datetime):
                        d['updated_at'] = strptime(d['updated_at'],
                                                   "%Y-%m-%d %H:%M:%S.%f")
                FileStorage.__objects[o_id] = CLS[k_cls](**o_dict)
        except:
            pass