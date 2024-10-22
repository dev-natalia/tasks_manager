Descrição da Estrutura:
main.py: O ponto de entrada da aplicação FastAPI.
core/: Contém as configurações centrais do projeto, como variáveis de ambiente e segurança.
api/: Contém as rotas e suas dependências. Aqui, cada versão da API (ex: v1, v2) pode ter seus próprios módulos de rotas.
models/: Modelos de dados (ex: SQLAlchemy ou Pydantic) que representam as tabelas e/ou esquemas da sua aplicação.
db/: Configurações relacionadas ao banco de dados, como conexão e manipulação de sessão.
schemas/: Esquemas de validação com Pydantic para definir como os dados de entrada/saída são estruturados.
services/: Lógica de negócio separada das rotas. Cada serviço pode manipular operações complexas de maneira organizada.
utils/: Funções utilitárias, helpers que não pertencem a um domínio específico (ex: funções genéricas de envio de e-mail, formatação).
tests/: Testes unitários e de integração para a aplicação.

------

Desafio: Criar uma API para um sistema de gerenciamento de tarefas
Descrição do Desafio
Você deve desenvolver uma API RESTful que permita aos usuários criarem contas, autenticarem-se e gerenciarem suas listas de tarefas. O sistema deve incluir:

Autenticação de Usuários:

O usuário deve ser capaz de se registrar e fazer login.
A autenticação deve ser feita usando JWT (JSON Web Tokens).
Gestão de Tarefas (To-Do):

O usuário deve ser capaz de criar, ler, atualizar e deletar tarefas. Cada tarefa tem um título, uma descrição e um status (concluído/não concluído).
As tarefas devem ser exclusivas para cada usuário (ou seja, um usuário não pode ver ou editar as tarefas de outro).
Banco de Dados:

Use um banco de dados relacional (como SQLite ou PostgreSQL) para armazenar usuários e tarefas.
Cada tarefa deve ser associada a um usuário.
Validação de Dados:

Valide os dados de entrada, garantindo que campos obrigatórios sejam fornecidos e que tipos de dados corretos sejam usados.
Autorização:

Apenas usuários autenticados podem acessar e modificar suas próprias tarefas.
O token JWT deve ser usado para autorizar as requisições à API.
Funcionalidades Obrigatórias
Registro de Usuário:

POST /register/ – Registro de um novo usuário.
Campos obrigatórios: username, email, password.
Login de Usuário:

POST /login/ – O login retorna um JWT para autenticação.
Campos obrigatórios: username, password.
Tarefas:

GET /tasks/ – Retorna todas as tarefas do usuário autenticado.
POST /tasks/ – Cria uma nova tarefa.
GET /tasks/{id}/ – Retorna uma tarefa específica do usuário autenticado.
PUT /tasks/{id}/ – Atualiza uma tarefa específica.
DELETE /tasks/{id}/ – Deleta uma tarefa específica.
Stack de Tecnologias
Framework: FastAPI (ou Flask se preferir)
Banco de Dados: SQLite (ou PostgreSQL se preferir)
Autenticação: JWT
Bibliotecas Úteis:
fastapi ou flask
sqlalchemy (ORM para lidar com o banco de dados)
passlib (para hash de senhas)
pyjwt (para geração e verificação de tokens JWT)
Extras (Desafios Adicionais)
Paginação: Implemente paginação para a listagem de tarefas.
Filtros: Adicione a capacidade de filtrar as tarefas por status (concluído/não concluído).
Busca: Implemente uma funcionalidade de busca por título de tarefa.
Testes: Escreva testes unitários e de integração para sua API usando pytest.
Dicas de Implementação
Configuração do FastAPI:

Utilize pip install fastapi[all] para instalar o FastAPI com todas as dependências recomendadas.
Utilize uvicorn para rodar o servidor: uvicorn main:app --reload.
Estrutura Básica:

Estruture seu projeto com um diretório app/ contendo submódulos para rotas, modelos e banco de dados.
Um arquivo main.py que inicializa a API e as rotas.
JWT:

O token JWT deve ser gerado quando o usuário fizer login com sucesso e enviado no cabeçalho das requisições subsequentes.
SQLAlchemy:

Defina as tabelas para User e Task usando SQLAlchemy como ORM para facilitar as interações com o banco de dados.