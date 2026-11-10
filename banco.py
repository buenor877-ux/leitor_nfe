# Criar a função criar_tabelas(caminho_banco) usando sqlite3.
import sqlite3

# Abre a conexão, liga a checagem de chave estrangeira e devolve a conexão.
def conectar_banco(caminho_banco):
    conn = sqlite3.connect(caminho_banco)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def criar_tabelas(caminho_banco):
 # Conectar ao banco de dados (ou criar se não existir)
    conn = conectar_banco(caminho_banco)
    try:
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

        conn.commit()
    finally:
        conn.close()


def gravar_nota(caminho_banco, nota_info):
    conn = conectar_banco(caminho_banco)
    try:
        cursor = conn.cursor()

        # Verifica se a chave já está no banco antes de gravar
        cursor.execute(
            "SELECT 1 FROM notas WHERE chave_acesso = ?",
            (nota_info["chave_acesso"],)
        )
        if cursor.fetchone():
            return False

        # 1. gravar o fornecedor (ignorar se o CNPJ já existir)
        cursor.execute(
            '''
            INSERT OR IGNORE INTO fornecedores (cnpj, nome)
            VALUES (?, ?)
            ''',
            (nota_info["cnpj_fornecedor"], nota_info["fornecedor"])
        )

        # 2. gravar a nota
        cursor.execute(
            '''
            INSERT INTO notas (chave_acesso, cnpj_fornecedor, arquivo, numero,
                               data_emissao, total_produtos, frete, valor_nota)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (nota_info["chave_acesso"], nota_info["cnpj_fornecedor"], nota_info["arquivo"],
             nota_info["numero"], nota_info["data_emissao"], nota_info["total_produtos"],
             nota_info["frete"], nota_info["valor_nota"])
        )

        # 3. gravar os itens da nota
        for produto in nota_info.get("produtos", []):
            cursor.execute(
                '''
                INSERT INTO itens (chave_acesso, nome_produto, quantidade,
                                   valor_unitario, valor_total)
                VALUES (?, ?, ?, ?, ?)
                ''',
                (nota_info["chave_acesso"], produto["nome"], produto["quantidade"],
                 produto["valor_unitario"], produto["valor_total"])
            )        

        conn.commit()
        return True
    finally:
        conn.close()


if __name__ == "__main__":
    criar_tabelas("notas.db")









