from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# Criação do engine
engine = create_engine("sqlite:///example.db")

# Configuração da factory de sessões
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


def get_db():
    """
    Função geradora que fornece uma sessão de banco de dados para cada requisição.

    A função `get_db` utiliza a função `yield` para fornecer uma instância de sessão de banco de dados
    (SessionLocal) durante o tempo de vida de uma requisição em uma aplicação, como uma API web. Ela cria
    uma nova sessão ao ser chamada e, ao finalizar a utilização da sessão, garante que ela será fechada
    corretamente, liberando a conexão com o banco de dados.

    O fluxo da função é:
    - Uma sessão é criada chamando a factory `SessionLocal`.
    - O `yield` retorna a sessão, permitindo que ela seja usada dentro da função ou endpoint que a chamar.
    - No final do ciclo de vida (após o uso do `yield`), o bloco `finally` garante que a sessão é fechada
      adequadamente para evitar vazamento de recursos e garantir a integridade do banco de dados.

    Exemplo de uso:

    Em uma aplicação web, a função `get_db` pode ser usada em um endpoint de API como dependência:

    ```python
    from fastapi import Depends, FastAPI

    app = FastAPI()

    @app.get("/items/")
    def read_items(db: Session = Depends(get_db)):
        return db.query(Item).all()
    ```

    Neste exemplo, a função `get_db` é chamada automaticamente pela dependência `Depends`, garantindo que
    uma nova sessão seja gerada para cada requisição à rota `/items/`, e que ela seja encerrada ao final
    do processamento da requisição.
    """
    db = SessionLocal()
    try:
        yield db  # a sessão é usada
    finally:
        db.close()  # encerramento da sessão ao final
