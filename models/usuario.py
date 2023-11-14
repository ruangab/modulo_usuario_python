from pydantic import BaseModel
from database import Database
 

class Usuario(BaseModel):
    nome: str
    senha: str
    descricao: str

    @staticmethod
    def get_usuario(nome):
        usuario = Database.find_document(query={"nome_usuario":nome}, collection="usuarios")
        usuario.pop("_id")
        usuario.pop("senha_usuario")

        return usuario

    @staticmethod
    def update_usuario(nome, descricao, senha):
        usuario = Database.update_document(query={"nome_usuario":nome}, document = {"$set":{"nome_usuario":nome, "senha_usuario":senha, "descricao_usuario":descricao}}, collection="usuarios")
        
    @staticmethod
    def insert_usuario(nome, descricao, senha):
        usuario = Database.insert_document(query={"nome_usuario":nome}, document={"nome_usuario":nome, "senha_usuario":senha, "descricao_usuario":descricao}, collection="usuarios")

    @staticmethod
    def delete_usuario(nome):
        usuario = Database.delete_document(query={"nome_usuario":nome}, collection="usuarios")
        