from fastapi import FastAPI
from models.usuario import Usuario

app = FastAPI()

#rota inicial
@app.get("/")
def ola_mundo():
    return "<h1> olá mundo </h1>"

@app.get("/usuario/")
def get_usuario(usuario:str):
    usuario_return = Usuario.get_usuario(usuario)

    return {"Usuario":usuario_return}

@app.post("/usuario/")
def add_usuario(usuario:Usuario):
    usuario_return = Usuario.insert_usuario(nome= usuario.nome, senha = usuario.senha, descricao= usuario.descricao)

    return {"msg":"usuario inserido"}

@app.put("/usuario/")
def edit_usuario(usuario:Usuario):
    usuario_return = Usuario.update_usuario(nome= usuario.nome, senha = usuario.senha, descricao= usuario.descricao)

    return {"msg":"usuario alterado"}

@app.delete("/usuario/{nome}")
def del_usuario(nome:str):
    usuario_return = Usuario.delete_usuario(nome=nome)

    return {"msg":"usuario deletado"}

#verifica se o programa está rodando diretamente ou como um módulo
if __name__   == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=3090, reload=True)