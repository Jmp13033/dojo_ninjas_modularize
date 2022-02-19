
from flask_app.config.mysqlconnection import connectToMySQL # import mysqlconnections


class Ninja:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    

    @classmethod
    def get_dojo_ninjas(cls,data):
        query = "SELECT * FROM ninjas WHERE ninjas.dojo_id = %(id)s;" # 
        results = connectToMySQL ("dojo_and_ninjas").query_db(query,data) 
        print(results) # pass in the cls results
        dojo_ninja = []
        for ninja in results:
            dojo_ninja.append(cls(ninja))
        return dojo_ninja # return the value of the users
        