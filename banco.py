# Criar a função criar_tabelas(caminho_banco) usando sqlite3.
import sqlite3


def criar_tabelas(caminho_banco):

    # Conectar ao banco de dados (ou criar se não existir)
    conn = sqlite3.connect(caminho_banco)
    cursor = conn.cursor()

    # Criar a tabela fornecedores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fornecedores (
            cnpj TEXT PRIMARY KEY,
            nome TEXT
        )
    ''')

    # Criar a tabela notas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            chave_acesso TEXT PRIMARY KEY,
            cnpj_fornecedor TEXT,
            arquivo TEXT,
            numero TEXT,
            data_emissao TEXT,
            total_produtos REAL,
            frete REAL,
            valor_nota REAL,
            FOREIGN KEY (cnpj_fornecedor) REFERENCES fornecedores(cnpj)
        )
    ''')

    # Criar a tabela itens
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave_acesso TEXT,
            nome_produto TEXT,
            quantidade REAL,
            valor_unitario REAL,
            valor_total REAL,
            FOREIGN KEY (chave_acesso) REFERENCES notas(chave_acesso)
        )
    ''')

    # Salvar (commit) e fechar a conexão
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas("notas.db")









