from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, func
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

# Criando uma sessão para executar a consulta
with Session() as session:
    resultado = session.query(
    Fornecedor.nome,
    func.sum(Produto.preco).label('total_precos')
).join(Produto, Fornecedor.id == Produto.fornecedor_id).group_by(Fornecedor.id).all()

    # Imprimindo os resultados
    for nome, total_precos in resultado:
        print(f"Fornecedor: {nome}, Total dos Preços dos Produtos: {total_precos}")