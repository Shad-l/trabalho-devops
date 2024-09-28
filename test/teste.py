from src.main import *
from unittest.mock import patch

def teste_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def teste_funcaoteste():
    with patch('random.randint', return_value = 12345):
        result = funcaoteste()
        yield result
    assert result == {"teste": True, "num_aleatorio": 12345}

def teste_create_estudante(estudante:Estudante):
    estudante_teste = Estudante(name="Fulano", curso="Curso Teste", ativo="false")
    result = create_estudante(estudante_teste)
    yield result
    assert estudante_teste == result

def teste_update_estudante_negativo(id_estudante: int):
    result = update_estudante(-5)
    yield result
    assert not result

def teste_update_estudante_positivo(id_estudante: int):
    result = update_estudante(10)
    yield result
    assert not result

def teste_delete_estudante_negativo(id_estudante: int):
    result = delete_estudante(-5)
    yield result
    assert not result

def teste_delete_estudante_positivo(id_estudante: int):
    result = delete_estudante(5)
    yield result
    assert not result


