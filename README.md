# Ferramentas WEB API

Este projeto é uma API REST desenvolvida como trabalho prático acadêmico para a disciplina de **Desenvolvimento Full Stack Básico**. O sistema gerencia o catálogo de produtos e categorias de uma loja de ferramentas.

A aplicação foi desenvolvida focando na simplicidade e clareza de código, atendendo os requisitos do projeto, com banco de dados SQLite e documentação com Swagger.

---

## Critérios de Avaliação Atendidos

Para facilitar a correção do trabalho, abaixo está o mapeamento dos requisitos solicitados e como foram implementados:

* **Mínimo de 4 Rotas com Flask (Python):** Implementamos **7 rotas** no total, cobrindo o CRUD completo e endpoints adicionais de listagem de categorias e busca de produtos.
* **Pelo menos uma rota com método POST:** Rota `POST /api/produtos` para inserção de novos produtos no catálogo.
* **Uso de Banco de Dados SQLite:** Utilização do SQLite (através da biblioteca nativa `sqlite3` do Python).
* **Múltiplas Tabelas (Inovação):** Uso de duas tabelas relacionais com dados reais sincronizados: `produtos` e `categorias`.
* **Tratamento de Datas (Inovação):** Registro automático e validação de data e hora de criação dos produtos (`created_at`) no formato datetime.
* **Funcionalidade Extra (Inovação):** Rota de busca textual (`GET /api/produtos/busca`) usando consultas SQL com operador `LIKE` no SQLite.
* **Documentação com Swagger (OpenAPI 3.0):** Documentação interativa via **Flasgger/Swagger UI** configurada e acessível diretamente no navegador, contendo descrição, estrutura de requisição/resposta em JSON e códigos de status HTTP (200, 201, 400, 404).

---

## Tecnologias Utilizadas
- **Python 3.14+**: Linguagem de programação principal.
- **Flask**: Micro-framework para criação das rotas HTTP.
- **SQLite (sqlite3 nativo)**: Banco de dados relacional em arquivo local.
- **Flasgger (Swagger UI)**: Biblioteca para renderização da documentação OpenAPI.
- **PyYAML**: Biblioteca para parsing e carregamento dinâmico da especificação do Swagger (`swagger.yaml`).

---

## Estrutura do Projeto
A estrutura do projeto segue o padrão minimalista e limpo da disciplina:
```text
API_loja/
├── app.py              # Código principal da aplicação Flask e rotas do SQLite
├── carga_inicial.sql   # Script SQL contendo a criação das tabelas e os 10 registros de teste
├── database.db         # Banco de dados SQLite gerado manualmente pelo usuário
├── swagger.yaml        # Especificação OpenAPI 3.0.0 com a documentação detalhada das rotas
├── requirements.txt    # Arquivo com as dependências diretas de instalação do Python
└── README.md           # Guia de instalação e uso do projeto (este arquivo)
```

---

## Carga Inicial de Dados
Para popular a aplicação com dados de demonstração, o arquivo `carga_inicial.sql` deve ser executado manualmente (conforme instruções abaixo). Isso cria a estrutura de tabelas (`produtos` e `categorias`) e insere **10 ferramentas de teste**, facilitando a validação imediata dos endpoints.

---

## Como Executar a Aplicação

### 1. Criar o Ambiente Virtual (venv)
No terminal do seu sistema operacional, dentro do diretório do projeto, execute o comando correspondente ao seu sistema para criar um ambiente virtual chamado `env`:

**No Windows (PowerShell):**
```powershell
python -m venv env
```

**No Linux/macOS:**
```bash
python3 -m venv env
```

### 2. Ativar o Ambiente Virtual

**No Windows (PowerShell):**
```powershell
.\env\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
source env/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas necessárias listadas no `requirements.txt`:
```bash
pip install -r requirements.txt
```

> [!TIP]
> Caso o comando `pip` não seja reconhecido no seu terminal (erro comum no Windows), utilize a chamada alternativa pelo módulo do Python:
> ```bash
> python -m pip install -r requirements.txt
> ```


### 4. Inicializar o Banco de Dados Manualmente
O banco de dados do SQLite (`database.db`) deve ser inicializado manualmente antes de iniciar a aplicação. Você pode fazer isso de duas formas simples:

#### Opção A: Executando via terminal
Como você já possui o Python configurado, basta executar o comando abaixo no terminal do projeto para ler o script `carga_inicial.sql` e criar o banco `database.db` populado:

```bash
python -c "import sqlite3; conn=sqlite3.connect('database.db'); conn.executescript(open('carga_inicial.sql', encoding='utf-8').read()); conn.close(); print('Banco database.db criado e populado com sucesso!')"
```

#### Opção B: Usando a interface gráfica (DB Browser for SQLite)
1. Abra o **DB Browser for SQLite** no seu computador.
2. Clique em **"Open Database"** (ou crie um novo caso queira começar do zero).
3. Vá até a aba **"Execute SQL"** (Executar SQL).
4. Abra o arquivo `carga_inicial.sql` (ou copie e cole seu conteúdo dentro do editor).
5. Clique no ícone de **Play** (Executar) para rodar o script.
6. Clique no botão **"Write Changes"** (Gravar Alterações) no topo para salvar os dados no arquivo `database.db`.


### 5. Executar a Aplicação
Execute o script principal para iniciar o servidor do Flask:
```bash
python app.py
```

O servidor será iniciado por padrão no endereço: `http://localhost:5000`

---

## Como Acessar a Documentação Swagger
Com a aplicação em execução, acesse pelo seu navegador:
[http://localhost:5000/swagger](http://localhost:5000/swagger)

A rota padrão do servidor `/` também redirecionará você automaticamente para a documentação interativa.

---

## Guia de Testes no Swagger UI (Exemplo por Rota)

Aqui está o guia passo a passo de como interagir e consultar as informações de cada rota usando a interface do Swagger UI:

### 1. Listar todas as categorias
Retorna todas as categorias de produtos cadastradas no banco de dados.

* **Rota:** `GET /api/categorias`
* **Como testar no Swagger UI:**
  1. Clique na barra azul `GET /api/categorias` para expandir.
  2. Clique em **"Try it out"**.
  3. Clique em **"Execute"**.
  4. O Swagger exibirá a lista completa de categorias com status `200`.
* **Exemplo de Resposta (Status 200 OK):**
```json
[
  {
    "id": 1,
    "name": "Ferramentas Manuais"
  },
  {
    "id": 2,
    "name": "Elétricas"
  },
  {
    "id": 3,
    "name": "EPIs"
  },
  {
    "id": 4,
    "name": "Construção"
  },
  {
    "id": 5,
    "name": "Jardinagem"
  }
]
```

---

### 2. Listar todos os produtos
Retorna a lista completa de ferramentas cadastradas no banco de dados.

* **Rota:** `GET /api/produtos`
* **Como testar no Swagger UI:**
  1. Clique na barra azul `GET /api/produtos` para expandir.
  2. Clique no botão **"Try it out"** no canto superior direito do bloco.
  3. Clique no botão azul grande **"Execute"** logo abaixo.
  4. Veja a lista com as 10 ferramentas de teste na área **"Server response"** (Status `200`).
* **Exemplo de Resposta (Status 200 OK):**
```json
[
  {
    "id": 1,
    "name": "Martelo de Garra",
    "price": 35.9,
    "category": "Ferramentas Manuais",
    "description": "Martelo de ferro 20mm com cabo de madeira",
    "created_at": "2026-06-21 09:14:00"
  },
  {
    "id": 2,
    "name": "Chave de Fenda",
    "price": 15.5,
    "category": "Ferramentas Manuais",
    "description": "Chave de fenda simples em aço",
    "created_at": "2026-06-18 15:22:00"
  }
]
```

---

### 3. Cadastrar novo produto
Cadastra uma nova ferramenta no banco de dados.

* **Rota:** `POST /api/produtos`
* **Como testar no Swagger UI:**
  1. Clique na barra verde `POST /api/produtos` para expandir.
  2. Clique em **"Try it out"**.
  3. No painel **"Request body"**, substitua o JSON existente pelo seguinte exemplo:
     ```json
     {
       "name": "Alicate de Pressão",
       "price": 45.90,
       "category": "Ferramentas Manuais",
       "description": "Alicate de pressão em aço carbono 10 polegadas"
     }
     ```
  5. Clique em **"Execute"**.
  6. A resposta mostrará o produto criado com a data/hora atual e o ID gerado automaticamente (`11`) com o status `201`.
* **Exemplo de Resposta (Status 201 Created):**
```json
{
  "id": 11,
  "name": "Alicate de Pressão",
  "price": 45.9,
  "category": "Ferramentas Manuais",
  "description": "Alicate de pressão em aço carbono 10 polegadas",
  "created_at": "2026-07-04 20:30:15"
}
```

---

### 4. Buscar produto por nome (Busca com LIKE)
Busca ferramentas cujo nome contenha o termo pesquisado.

* **Rota:** `GET /api/produtos/busca`
* **Como testar no Swagger UI:**
  1. Clique na barra azul `GET /api/produtos/busca` para expandir.
  2. Clique em **"Try it out"**.
  3. No parâmetro **`nome`** (abaixo de "Parameters"), digite o termo `Chave`.
  4. Clique em **"Execute"**.
  5. A API retornará todas as ferramentas contendo o termo "Chave" no nome (ex: Chave de Fenda, Jogo de Chaves Allen) com status `200`.
* **Exemplo de Resposta (Status 200 OK):**
```json
[
  {
    "id": 2,
    "name": "Chave de Fenda",
    "price": 15.5,
    "category": "Ferramentas Manuais",
    "description": "Chave de fenda simples em aço",
    "created_at": "2026-06-18 15:22:00"
  },
  {
    "id": 9,
    "name": "Jogo de Chaves Allen",
    "price": 42.5,
    "category": "Ferramentas Manuais",
    "description": "Estojo com 9 chaves Allen abauladas de 1.5 a 10mm",
    "created_at": "2026-05-27 08:33:00"
  }
]
```

---

### 5. Excluir produto
Remove uma ferramenta definitivamente do banco de dados pelo seu ID.

* **Rota:** `DELETE /api/produtos/{id}`
* **Como testar no Swagger UI:**
  1. Clique na barra vermelha `DELETE /api/produtos/{id}` para expandir.
  2. Clique em **"Try it out"**.
  3. Digite o **`id`** do produto que deseja deletar (ex: `11` - o alicate cadastrado no passo 3).
  4. Clique em **"Execute"**.
  5. O servidor retornará uma mensagem confirmando a remoção com o status `200`.
* **Exemplo de Resposta (Status 200 OK):**
```json
{
  "mensagem": "Produto removido com sucesso.",
  "id": 11
}
```

---

### 6. Buscar produto por ID
Retorna os detalhes de um produto específico através de seu ID numérico.

* **Rota:** `GET /api/produtos/{id}`
* **Como testar no Swagger UI:**
  1. Clique na barra azul `GET /api/produtos/{id}` para expandir.
  2. Clique em **"Try it out"**.
  3. No campo de parâmetro **`id`** (abaixo de "Parameters"), digite o valor `3`.
  4. Clique em **"Execute"**.
  5. A resposta trará os dados da "Furadeira de Impacto" (ID `3`) com status `200`. Se digitar um ID inexistente (ex: `99`), receberá status `404`.
* **Exemplo de Resposta - Sucesso (Status 200 OK):**
```json
{
  "id": 3,
  "name": "Furadeira de Impacto",
  "price": 299.9,
  "category": "Elétricas",
  "description": "Furadeira potente de 500W com maleta",
  "created_at": "2026-05-30 11:05:00"
}
```
* **Exemplo de Resposta - Não Encontrado (Status 404 Not Found):**
```json
{
  "erro": "Produto não encontrado."
}
```

---

### 7. Atualizar produto
Atualiza as informações de uma ferramenta existente com base no seu ID.

* **Rota:** `PUT /api/produtos/{id}`
* **Como testar no Swagger UI:**
  1. Clique na barra laranja `PUT /api/produtos/{id}` para expandir.
  2. Clique em **"Try it out"**.
  3. No campo **`id`**, insira o ID do produto que deseja editar (ex: `1`).
  4. No painel **"Request body"**, cole o JSON com as alterações desejadas:
     ```json
     {
       "name": "Martelo de Garra Cabo Emborrachado",
       "price": 39.90,
       "category": "Ferramentas Manuais",
       "description": "Martelo de garra 20mm com cabo de borracha"
     }
     ```
  5. Clique em **"Execute"**.
  6. A resposta exibirá o registro atualizado (Status `200`).
* **Exemplo de Resposta (Status 200 OK):**
```json
{
  "id": 1,
  "name": "Martelo de Garra Cabo Emborrachado",
  "price": 39.9,
  "category": "Ferramentas Manuais",
  "description": "Martelo de garra 20mm com cabo de borracha",
  "created_at": "2026-07-04 12:00:00"
}
```
