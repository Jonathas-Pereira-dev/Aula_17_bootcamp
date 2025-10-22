from sqlalchemy import create_engine

#Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão estabelecida com sucesso!")

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

#Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)
session = session()

usuario = session.query(Usuario).filter_by(nome='Alice').first()
print(f'Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}' )