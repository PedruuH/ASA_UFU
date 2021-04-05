class Aluno:
    __id = None
    __nome = None    
    __idade = None
    __disciplinaMatriculado = []

    def __init__(self, id, nome, idade):
        self.__id = id
        self.__nome = nome        
        self.__idade = idade


    def getAlunoId(self):
        return self.__id

    def getAlunoNome(self):
        return self.__nome

    def getAlunoIdade(self):
        return self.__idade

    def getAlunoName(self, id):
        retorno = ""
        if(self.__id == id):
            retorno = self.__nome
        else:
            retorno = "usuario nao encontrado!!"
        return (retorno)

    def setAlunoNome(self, nome):
        self.__nome = nome

    def setAlunoIdade(self, nome):
        self.__idade = nome    
    