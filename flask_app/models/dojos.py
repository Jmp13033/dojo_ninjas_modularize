
from flask_app.config.mysqlconnection import connectToMySQL # import mysqlconnections
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def create_dojo(cls,data):
        query = "INSERT INTO dojos (name, created_at) VALUES(%(name)s, NOW());"
        results = connectToMySQL("dojo_and_ninjas").query_db(query,data)
        return results
    

    @classmethod
    def all_dojos(cls):
        query = "SELECT * FROM dojos " # this is a SELECT query to do this.. 
        results = connectToMySQL ("dojo_and_ninjas").query_db(query)  # pass in the cls results
        dojo_users = []
        for dojo in results:
            dojo_users.append(cls(dojo))
        return dojo_users # return the value of the users
    
    
    @classmethod
    def get_one(cls,data):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL('dojo_and_ninjas').query_db(query,data) # list connect to data base qery db 
        return cls(result[0]) 

