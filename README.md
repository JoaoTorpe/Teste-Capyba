# ⚙️Instalação

Clone o repositório para sua máquina local:

```bash
git clone https://github.com/JoaoTorpe/Teste-Capyba.git
````
Crie um ambiente virtual para isolar as dependências:
```bash
python -m venv venv
````
Ative o ambiente virtual:
```bash
source .venv/bin/activate     # Para Unix/macOS

venv\Scripts\activate.ps1     # Para Windows (Usar terminal como administrador)

source .venv/Scripts/activate # Caso esteja usando um terminal Unix-like no Windows, Git Bash por exemplo

````
Caso não consiga ativar no windows acesse esse [link](https://cursos.alura.com.br/forum/topico-nao-consigo-criar-o-venv-da-aula-1-do-curso-142958)
<br>
<br>
Acesse o diretório do projeto:
```bash
cd Teste-Capyba
````
Instale as dependências:
```bash
pip install -r requirements.txt
````
Crie as migrações:
```bash
python manage.py makemigrations
````
Aplique as migrações:
```bash
python manage.py migrate
````
Rode o script para popular o banco:
```bash
python populate_database.py
````
Comando para rodar os testes unitários:
```bash
python manage.py test
````

Execute o servidor:
```bash
python manage.py runserver
````

# 🔗Endpoints abertos
Swagger disponível em: 
  <a href="http://127.0.0.1:8000/openapi/docs/">http://127.0.0.1:8000/openapi/docs/</a>
# Endpoint para o registro de usuário:
```bash
POST /api/register
````
 Exemplo de requisição:
```json
{
  "username": "username",
  "email": "email@email.com",
  "password": "senha123"
}
````
# Endpoint para o login do usuário:
```bash
POST /api/login
````
 Exemplo de requisição:
```json
{
  "email": "email@email.com",
  "password": "senha123"
}
````
Essa requisição retorna o token de acesso para o usuário:
```json
{
  "token": "fd4f9e286f317f58112ef57704fb1678a7"
}
````
Para ter acesso aos endpoints protegidos, o token precisa ser inserido no compo 'Authorize' do Swagger com o prefixo 'Token':
![image](https://github.com/user-attachments/assets/69f6dc4a-adbf-47d1-b022-9171eef1c543)

# 🔗Endpoints protegidos

# Endpoint para mudar senha do usuário com confirmação da senha atual:
```bash
POST /api/changepass
````
 Exemplo de requisição:
```json
{
  "current_password": "senha123",
  "new_password": "pass123"
}
````

# Endpoint para mudar cadastro do usuário:
```bash
PUT /api/updatedata
````
 Exemplo de requisição:
```json
{
  "username": "novo_username",
  "email": "novo@email.com"
}
````
# Endpoint de logout:
```bash
POST /api/logout
````
 Exemplo de requisição:
```json
{}
````
# Endpoint para a lista de itens paginada
Esse endpoit possui diversos parâmetros para filtragem dos dados, permitindo que sejam utilizados simultaneamente para refinar os resultados.
```bash
GET /movies/filmes
````
## Parâmetros:
<br>
<table>
  <thead>
    <tr>
      <th>Nome do Parâmetro</th>
      <th>Descrição</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ordering</td>
      <td>Critério de ordenação (por título ou ano de lançamento)</td>
    </tr>
    <tr>
      <td>page</td>
      <td>Decide qual página da paginação será listada (Precisa definir o page_size para funcionar)</td>
    </tr>
    <tr>
      <td>page_size</td>
      <td>Número de itens por página na paginação</td>
    </tr>
    <tr>
      <td>search</td>
      <td>Termo de busca que filtra no título e gênero</td>
    </tr>
    <tr>
      <td>premiado</td>
      <td>Filtra por filmes premiados (True/False)</td>
    </tr>
    
  </tbody>
</table>

## Exemplos:

````bash
GET/movies/filmes?ordering=ano_de_lancamento
````
````json
{
  "Total de itens na base de dados": 41,
  "response": [
    {
      "id": 7,
      "titulo": "O Poderoso Chefão",
      "genero": "Crime",
      "premiado": true,
      "ano_de_lancamento": 1972
    },
    {
      "id": 18,
      "titulo": "O Exorcista",
      "genero": "Terror",
      "premiado": false,
      "ano_de_lancamento": 1973
    },
    {
      "id": 30,
      "titulo": "Os Caça-Fantasmas",
      "genero": "Comédia",
      "premiado": false,
      "ano_de_lancamento": 1984
    },
````
````bash
GET/movies/filmes?page_size=3&page=1
````
````json
{
 {
  "Total de itens na base de dados": 41,
  "response": [
    {
      "id": 1,
      "titulo": "O Senhor dos Anéis",
      "genero": "Fantasia",
      "premiado": true,
      "ano_de_lancamento": 2001
    },
    {
      "id": 2,
      "titulo": "Matrix",
      "genero": "Sci-Fi",
      "premiado": false,
      "ano_de_lancamento": 1999
    },
    {
      "id": 3,
      "titulo": "A Espera de um Milagre",
      "genero": "Drama",
      "premiado": true,
      "ano_de_lancamento": 1999
    }
  ]
}
````
````bash
GET/movies/filmes?premiado=True
````
````json

 {
  "Total de itens na base de dados": 41,
  "response": [
    {
      "id": 1,
      "titulo": "O Senhor dos Anéis",
      "genero": "Fantasia",
      "premiado": true,
      "ano_de_lancamento": 2001
    },
    {
      "id": 3,
      "titulo": "A Espera de um Milagre",
      "genero": "Drama",
      "premiado": true,
      "ano_de_lancamento": 1999
    },
    {
      "id": 4,
      "titulo": "A Origem",
      "genero": "Ação",
      "premiado": true,
      "ano_de_lancamento": 2010
    },
]
}
````
````bash
GET/movies/filmes?search=Crime
````
````json
{
 {
  "Total de itens na base de dados": 41,
  "response": [
    {
      "id": 6,
      "titulo": "Pulp Fiction",
      "genero": "Crime",
      "premiado": true,
      "ano_de_lancamento": 1994
    },
    {
      "id": 7,
      "titulo": "O Poderoso Chefão",
      "genero": "Crime",
      "premiado": true,
      "ano_de_lancamento": 1972
    },
    {
      "id": 10,
      "titulo": "Os Infiltrados",
      "genero": "Crime",
      "premiado": true,
      "ano_de_lancamento": 2006
    },
    {
      "id": 11,
      "titulo": "Coringa",
      "genero": "Crime",
      "premiado": true,
      "ano_de_lancamento": 2019
    }
  ]
}
}
````







  
