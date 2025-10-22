
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Integer)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    # Estabelece o relacionamento com produto - Fornecedor
    fornecedor = relationship("Fornecedor")


engine = create_engine('sqlite:///desafio.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

# Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(nome="Fornecedor A", telefone="123456789", email="contato@a.com", endereco="Rua A, 123"),
            Fornecedor(nome="Fornecedor B", telefone="987654321", email="contato@b.com", endereco="Rua B, 456"),
            Fornecedor(nome="Fornecedor C", telefone="456123789", email="contato@c.com", endereco="Rua C, 789"),
            Fornecedor(nome="Fornecedor D", telefone="321654987", email="contato@d.com", endereco="Rua D, 321"),
            Fornecedor(nome="Fornecedor E", telefone="654987321", email="contato@e.com", endereco="Rua E, 654"),
        ]
        session.add_all(fornecedores)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir fornecedores: {e}")

#Inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(nome="Produto 1", descricao="Descrição do Produto 1", preco=100, fornecedor_id=1),
            Produto(nome="Produto 2", descricao="Descrição do Produto 2", preco=200, fornecedor_id=2),
            Produto(nome="Produto 3", descricao="Descrição do Produto 3", preco=150, fornecedor_id=3),
            Produto(nome="Produto 4", descricao="Descrição do Produto 4", preco=300, fornecedor_id=4),
            Produto(nome="Produto 5", descricao="Descrição do Produto 5", preco=250, fornecedor_id=5),
        ]
        session.add_all(produtos)
        session.commit()
except SQLAlchemyError as e:
    print(f"Erro ao inserir produtos: {e}")