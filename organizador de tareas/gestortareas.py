from pymongo import MongoClient

class GestorTareas:
    def __init__(self, uri='mongodb://localhost:27017/'):
        self.cliente = MongoClient(uri)
        self.db = self.cliente['bd_usuarioss'] 
        self.usuarios = self.db['organizador-tareas'] 

    def usuario_existe(self, nombre_usuario: str) -> bool:
        """Busca si el nombre de usuario ya está en la colección"""
        encontrado = self.usuarios.find_one({"usuario": nombre_usuario})
        return encontrado is not None

    def crear_usuario(self, nombre, email, password_hash):
        """Guarda el nuevo usuario"""
        return self.usuarios.insert_one({
            "usuario": nombre,
            "email": email,
            "password": password_hash
        })