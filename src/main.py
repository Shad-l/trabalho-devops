from fastapi import FastAPI, HTTPException
from typing import Union, List
from pydantic import BaseModel
import random

app = FastAPI()

class Estudante(BaseModel):
    name: str
    curso: str
    ativo: bool

# Simulando um banco de dados em memória
estudantes_db = []

@app.get("/helloword")
async def root():
    return {"message": "Hello World"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0, 57000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    estudantes_db.append(estudante)
    return estudante

@app.put("/estudante/update/{id_estudante}")
async def update_estudante(id_estudante: int):
     return id_estudante > 0

@app.delete("/estudante/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
     return id_estudante > 0

# Novas funções

@app.get("/estudantes", response_model=List[Estudante])
async def list_estudantes():
    return estudantes_db

@app.get("/estudantes/{estudante_id}", response_model=Estudante)
async def get_estudante(estudante_id: int):
    if estudante_id < 0 or estudante_id >= len(estudantes_db):
        raise HTTPException(status_code=404, detail="Estudante não  encontrado")
    return estudantes_db[estudante_id]

@app.put("/estudantes/{estudante_id}", response_model=Estudante)
async def update_estudante_info(estudante_id: int, estudante: Estudante):
    if estudante_id < 0 or estudante_id >= len(estudantes_db):
        raise HTTPException(status_code=404, detail="Estudante não encontrado")
    estudantes_db[estudante_id] = estudante
    return estudante

@app.get("/estudantes/curso/{curso}", response_model=List[Estudante])
async def get_estudantes_by_curso(curso: str):
    return [e for e in estudantes_db if e.curso == curso]

@app.get("/estudantes/count")
async def count_estudantes():
    return {"total": len(estudantes_db)}