import sqlite3
from pathlib import Path

# Caminho do banco (dentro de dados/)
RAIZ = Path(__file__).parent.parent
CAMINHO_BANCO = RAIZ / "dados" / "dop.db"

def conectar():
    """Abre conexão com o banco SQLite local."""
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabelas():
    """Cria as tabelas iniciais se não existirem."""
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS eventos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            descricao TEXT,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conexao.commit()
    conexao.close()

if __name__ == "__main__":
    criar_tabelas()
    print("Banco criado em:", CAMINHO_BANCO)