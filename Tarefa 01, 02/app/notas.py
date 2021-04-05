class Notas:
    __idmateria = None
    __idaluno = None
    __nota1 = None
    __nota2 = None
    __nota3 = None
    __nota4 = None

    def __init__ (self, idMateria, idAluno, nota1, nota2, nota3, nota4):
        self.__idmateria = idMateria
        self.__idaluno = idAluno
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3
        self.__nota4 = nota4

    def getIdMateria (self):
        return self.__idmateria
    
    def getIdAluno (self):
        return self.__idaluno
    
    def getMediaNotas (self):
        return ((self.__nota1 + self.__nota2 + self.__nota3 + self.__nota4)/4)