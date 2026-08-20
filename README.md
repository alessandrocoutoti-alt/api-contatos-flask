# 📞 API de Contatos

Uma API RESTful para gerenciamento de contatos, desenvolvida em **Python** utilizando o framework **Flask** e o banco de dados relacional **SQLite**.

---

## 🔗 Projeto Relacionado

Esse backend serve dados para o front-end React:
👉 [frontend-contatos](https://github.com/alessandrocoutoti-alt/frontend-contatos)

---

## 🚀 Tecnologias Utilizadas

*   **Linguagem:** [Python 3.x](https://www.python.org/)
*   **Framework Web:** [Flask](https://flask.palletsprojects.com/)
*   **CORS:** [Flask-CORS](https://flask-cors.readthedocs.io/) (para integração com o front-end)
*   **Banco de Dados:** [SQLite](https://www.sqlite.org/) (em arquivo local: `contatos.db`)

---

## 🛠️ Instalação e Execução

Siga os passos abaixo para configurar e executar a API localmente:

### 1. Clonar o repositório
```bash
git clone <url-do-repositorio>
cd api-contatos-flask
```

### 2. Configurar o ambiente virtual (Recomendado)
No terminal, crie e ative um ambiente virtual Python:

*   **No Windows (PowerShell):**
    ```powershell
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    ```
*   **No Linux / macOS:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Instalar as dependências
Como o SQLite é nativo do Python, precisamos instalar o Flask e o Flask-CORS:
```bash
pip install Flask flask-cors
```

### 4. Executar a aplicação
Inicie o servidor de desenvolvimento local:
```bash
python app.py
```
A API estará acessível em `http://127.0.0.1:5000/`.

---

## 🔌 Documentação dos Endpoints

Abaixo estão descritos todos os endpoints disponíveis na API, com detalhes de como testá-los utilizando `curl` (ou ferramentas como Bruno, Postman e Insomnia).

### 1. Verificar Status da API
Retorna uma mensagem simples para confirmar que o servidor está rodando.

*   **Método:** `GET`
*   **URL:** `/`
*   **Resposta de Sucesso:**
    *   **Código:** `200 OK`
    *   **Corpo:** `API de Contatos no ar!`
*   **Como Testar (cURL):**
    ```bash
    curl http://127.0.0.1:5000/
    ```

### 2. Listar Todos os Contatos
Retorna a lista completa de contatos salvos no banco de dados.

*   **Método:** `GET`
*   **URL:** `/contatos`
*   **Resposta de Sucesso:**
    *   **Código:** `200 OK`
    *   **Corpo (Exemplo):**
        ```json
        [
          {
            "id": 1,
            "nome": "João Silva",
            "telefone": "(11) 99999-9999",
            "email": "joao@email.com"
          }
        ]
        ```
*   **Como Testar (cURL):**
    ```bash
    curl http://127.0.0.1:5000/contatos
    ```

### 3. Adicionar Novo Contato
Cadastra um novo contato. O campo `nome` é obrigatório.

*   **Método:** `POST`
*   **URL:** `/contatos`
*   **Headers:** `Content-Type: application/json`
*   **Corpo da Requisição (Body):**
    ```json
    {
      "nome": "Maria Souza",
      "telefone": "(21) 98888-8888",
      "email": "maria@email.com"
    }
    ```
*   **Resposta de Sucesso:**
    *   **Código:** `201 Created`
    *   **Corpo:**
        ```json
        {
          "mensagem": "Contato 'Maria Souza' adicionado!"
        }
        ```
*   **Resposta de Erro (Sem Nome):**
    *   **Código:** `400 Bad Request`
    *   **Corpo:**
        ```json
        {
          "erro": "O campo 'nome' é obrigatório."
        }
        ```
*   **Como Testar (cURL):**
    *   **Linux / macOS / PowerShell (moderno):**
        ```bash
        curl -X POST http://127.0.0.1:5000/contatos \
          -H "Content-Type: application/json" \
          -d '{"nome": "Maria Souza", "telefone": "(21) 98888-8888", "email": "maria@email.com"}'
        ```
    *   **Windows (cmd.exe clássico):**
        ```cmd
        curl -X POST http://127.0.0.1:5000/contatos -H "Content-Type: application/json" -d "{\"nome\": \"Maria Souza\", \"telefone\": \"(21) 98888-8888\", \"email\": \"maria@email.com\"}"
        ```

### 4. Atualizar um Contato Existente
Modifica os dados de um contato baseado no ID fornecido na URL.

*   **Método:** `PUT`
*   **URL:** `/contatos/<id_contato>`
*   **Headers:** `Content-Type: application/json`
*   **Corpo da Requisição (Body):**
    ```json
    {
      "nome": "Maria Souza de Oliveira",
      "telefone": "(21) 97777-7777",
      "email": "maria.novo@email.com"
    }
    ```
*   **Resposta de Sucesso:**
    *   **Código:** `200 OK`
    *   **Corpo:**
        ```json
        {
          "mensagem": "Contato atualizado com sucesso!"
        }
        ```
*   **Resposta de Erro (Contato Não Encontrado):**
    *   **Código:** `404 Not Found`
    *   **Corpo:**
        ```json
        {
          "erro": "Contato não encontrado."
        }
        ```
*   **Como Testar (cURL):**
    *   **Linux / macOS / PowerShell (moderno):**
        ```bash
        curl -X PUT http://127.0.0.1:5000/contatos/1 \
          -H "Content-Type: application/json" \
          -d '{"nome": "Maria Souza de Oliveira", "telefone": "(21) 97777-7777", "email": "maria.novo@email.com"}'
        ```

### 5. Remover um Contato
Exclui permanentemente um contato pelo ID especificado na URL.

*   **Método:** `DELETE`
*   **URL:** `/contatos/<id_contato>`
*   **Resposta de Sucesso:**
    *   **Código:** `200 OK`
    *   **Corpo:**
        ```json
        {
          "mensagem": "Contato removido com sucesso!"
        }
        ```
*   **Resposta de Erro (Contato Não Encontrado):**
    *   **Código:** `404 Not Found`
    *   **Corpo:**
        ```json
        {
          "erro": "Contato não encontrado."
        }
        ```
*   **Como Testar (cURL):**
    ```bash
    curl -X DELETE http://127.0.0.1:5000/contatos/1
    ```

---

## 🗄️ Estrutura do Banco de Dados

O banco de dados SQLite (`contatos.db`) é inicializado automaticamente na primeira execução e contém a tabela `contatos` com a seguinte estrutura:

| Campo | Tipo | Restrições | Descrição |
| :--- | :--- | :--- | :--- |
| `id` | `INTEGER` | `PRIMARY KEY AUTOINCREMENT` | Identificador único do contato |
| `nome` | `TEXT` | `NOT NULL` | Nome completo do contato |
| `telefone` | `TEXT` | | Número de telefone/celular |
| `email` | `TEXT` | | Endereço de e-mail |
