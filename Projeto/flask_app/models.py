from sqlalchemy import Column, Integer, String, MetaData, Float
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(100), unique=True)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)

class Aeroportos(Base):
    __tablename__ = 'aeroportos'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    sigla = Column(String(3)) #padrão IATA (International Air Transport Association)
    endereço = Column(Sting(100))
    aero_ligacao1 = Column(String(3))
    aero_ligacao2 = Column(String(3))
    aero_ligacao3 = Column(String(3))

    def __init__(self,name=None,sigla = None, endereço=None, aero_ligacao1 = None, aero_ligacao2 = None, aero_ligacao3 = None):
        self.name = name
        self.sigla = sigla
        self.endereço = endereço
        self.aero_ligacao1 = aero_ligacao1
        self.aero_ligacao2 = aero_ligacao2
        self.aero_ligacao3 = aero_ligacao3


class Voos(Base):
    __tablename__ = 'voos'
    id = Column(Integer, primary_key=True)
    origem = Column(String(3))
    destino = Column(String(3))
    data = Column(String(8))
    tarifa_base = Column(Float)
    num_aviao = Column(String(6))
    passageiros = Column(Integer)
    cia_aerea = Column(String(20))

    def __init__(self, origem=None, destino=None,data=None,tarifa_base=None,num_aviao=None,passageiros=None, cia_aerea=None):
        self.origem = origem
        self.destino = destino
        self.data = data
        self.tarifa_base= tarifa_base
        self.num_aviao= num_aviao
        self.passageiros = passageiros
        self.cia_aerea=cia_aerea

class Reservas(Base):
    __tablename__ = 'reservas'
    id = Column(Integer, primary_key=True) #localizador da reserva
    voos = Column(String(20))
    tickets = (String(20), unique=True)

    def __init__(self, voos=None,tickets=None):
        self.voos = voos
        self.tickets = tickets



