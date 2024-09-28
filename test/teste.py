from src.main import *
from unittest.mock import path

def teste_root():
    assert root() == {"message": "Hello World"}

def teste_funcaoteste():
    with path('random.randint', return_value = 12345):
        result = funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

def teste_create_estudante(estudante:Estudante):
    estudante_teste = Estudante(name="Fulano", curso="Curso Teste", ativo="false")
    assert estudante_teste == create_estudante(estudante_teste)

def teste_update_estudante_negativo(id_estudante: int):
    assert not update_estudante(-5)

def teste_update_estudante_positivo(id_estudante: int):
    assert update_estudante(10)

def teste_delete_estudante_negativo(id_estudante: int):
    assert not delete_estudante(-5)

def teste_delete_estudante_positivo(id_estudante: int):
    assert delete_estudante(5)

