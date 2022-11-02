from flask import flash
from flask import app


class SharedDrive:

    def __init__(self,data):
        self.folderID = data['folderID']
        self.name = data['name']
        self.location = data['location']
        
