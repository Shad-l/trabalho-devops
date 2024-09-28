from src.main import *
from unittest.mock import patch
import pytest

# ... (testes existentes permanecem aqui)

@pytest.mark.asyncio
async def test_list_estudantes():
    # Limpar o banco de dados simulado
    estudantes_db.clear()
    
    # Adicionar alguns estudantes de teste
    estudantes_db.extend([
        Estudante(name="Alice", curso="Engenharia", ativo=True),
        Estudante(name="Bob", curso="Medicina", ativo=True)
    ])
    
    result = await list_estudantes()
    assert len(result) == 2
    assert result[0].name == "Alice"
    assert result[1].name == "Bob"

@pytest.mark.asyncio
async def test_get_estudante():
    # Limpar o banco de dados simulado
    estudantes_db.clear()
    
    # Adicionar um estudante de teste
    estudantes_db.append(Estudante(name="Charlie", curso="Direito", ativo=True))
    
    result = await get_estudante(0)
    assert result.name == "Charlie"
    assert result.curso == "Direito"
    
    with pytest.raises(HTTPException):
        await get_estudante(1)  # Deve lançar uma exceção para ID inválido

@pytest.mark.asyncio
async def test_update_estudante_info():
    # Limpar o banco de dados simulado
    estudantes_db.clear()
    
    # Adicionar um estudante de teste
    estudantes_db.append(Estudante(name="David", curso="Psicologia", ativo=True))
    
    updated_estudante = Estudante(name="David", curso="Filosofia", ativo=False)
    result = await update_estudante_info(0, updated_estudante)
    
    assert result.curso == "Filosofia"
    assert result.ativo == False
    
    with pytest.raises(HTTPException):
        await update_estudante_info(1, updated_estudante)  # Deve lançar uma exceção para ID inválido

@pytest.mark.asyncio
async def test_get_estudantes_by_curso():
    # Limpar o banco de dados simulado
    estudantes_db.clear()
    
    # Adicionar alguns estudantes de teste
    estudantes_db.extend([
        Estudante(name="Eve", curso="Computação", ativo=True),
        Estudante(name="Frank", curso="Computação", ativo=True),
        Estudante(name="Grace", curso="Física", ativo=True)
    ])
    
    result = await get_estudantes_by_curso("Computação")
    assert len(result) == 2
    assert all(e.curso == "Computação" for e in result)
    
    result = await get_estudantes_by_curso("Física")
    assert len(result) == 1
    assert result[0].name == "Grace"

@pytest.mark.asyncio
async def test_count_estudantes():
    # Limpar o banco de dados simulado
    estudantes_db.clear()
    
    # Adicionar alguns estudantes de teste
    estudantes_db.extend([
        Estudante(name="Hank", curso="Química", ativo=True),
        Estudante(name="Ivy", curso="Biologia", ativo=True),
        Estudante(name="Jack", curso="Matemática", ativo=True)
    ])
    
    result = await count_estudantes()
    assert result == {"total": 3}

    # Adicionar mais um estudante
    estudantes_db.append(Estudante(name="Kelly", curso="Geologia", ativo=True))
    
    result = await count_estudantes()
    assert result == {"total": 4}