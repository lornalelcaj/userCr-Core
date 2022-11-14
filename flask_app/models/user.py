from flask_app.config.mysqlconnection import connectToMySQL
"""for each manualy created table we create
 a diferent py file in models """
class User:
    db_name='userscore'
    def __init__(self,data):
        self.id = data['id']
        self.firts_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def getAllUsers(cls):
        query='SELECT * FROM users;'
        results = connectToMySQL(cls.db_name).query_db(query)
        return results 

    @classmethod
    def createUser(cls,data):
        query = 'INSERT INTO users ( first_name, last_name,email) VALUES (%(first_name)s, %(last_name)s, %(email)s );'
        result= connectToMySQL(cls.db_name).query_db(query, data)
        return result