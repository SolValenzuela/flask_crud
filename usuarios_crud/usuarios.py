from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self,data):
        self.id=data['id']
        self.first_name= data['first_name']
        self.last_name= data['last_name']
        self.email= data['email']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']


    @classmethod 
    def get_all(cls):
        query="SELECT * FROM usuarios;"
        result=connectToMySQL('usuarios_schema').query_db(query)
        usuarios=[]
        for u in result:
            usuarios.append(cls(u))
        return usuarios

    @classmethod
    def agregar(cls,data):
        query="INSERT INTO usuarios (first_name, last_name, email,created_at) VALUES (%(first_name)s,%(last_name)s,%(email)s, NOW());"
        result=connectToMySQL('usuarios_schema').query_db(query,data)
        return result
    
    @classmethod
    def get_one(cls,data):
        query="SELECT * FROM usuarios WHERE id=%(id)s;"
        result= connectToMySQL('usuarios_schema').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def actualizar(cls,data):
        query="UPDATE usuarios SET first_name=%(first_name)s, last_name=%(last_name)s,email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
        return connectToMySQL('usuarios_schema').query_db(query,data)

    @classmethod
    def eliminar(cls,data):
        query  = "DELETE FROM usuarios WHERE id = %(id)s;"
        return connectToMySQL('usuarios_schema').query_db(query,data)    
    
    


