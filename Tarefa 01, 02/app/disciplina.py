
class Disciplina:
    __id = None
    __nome = None
    __cargahoraria = None
    __professor = None
    __alunosMatriculados=[]

    def __init__(self, id, nome, cargahoraria, professor):
        self.__id = id
        self.__nome = nome        
        self.__cargahoraria = cargahoraria
        self.__professor = professor

    def getDisciplinaId (self):
        return self.__id
    
    def setDisciplinaNome (self, nome):
        self.__nome = nome

    def getDisciplinaNome (self):
        return self.__nome
    
    def setDisciplinaCargahoraria(self,carga):
        self.__cargahoraria = carga

    def getDisciplinaCargahoraria (self):
        return self.__cargahoraria
    
    def setDisciplinaProfessor(self, professor):
        self.__professor = professor

    def getDisciplinaProfessor (self):
        return self.__professor
    def setAlunos (self,aluno):
        self.__alunosMatriculados.append(aluno)
    
    def getAlunos(self):
        return self.__alunosMatriculados
