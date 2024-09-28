from src.main import *
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def teste_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def teste_funcaoteste():
    with patch('random.randint', return_value=12345):
        result = await funcaoteste()
    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def teste_create_estudante():
    estudante_teste = Estudante(name="Fulano", curso="Curso Teste", ativo=False)
    result = await create_estudante(estudante_teste)
    assert result == estudante_teste

@pytest.mark.asyncio
async def teste_update_estudante_negativo():
    result = await update_estudante(-5)
    assert result == False

@pytest.mark.asyncio
async def teste_update_estudante_positivo():
    result = await update_estudante(10)
    assert result == True

@pytest.mark.asyncio
async def teste_delete_estudante_negativo():
    result = await delete_estudante(-5)
    assert result == False

@pytest.mark.asyncio
async def teste_delete_estudante_positivo():
    result = await delete_estudante(5)
    assert result == True