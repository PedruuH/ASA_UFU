from flask import Flask, url_for, request, json, jsonify
from json import dumps
from aluno import Aluno
from notas import Notas
from disciplina import Disciplina

app = Flask(__name__)
alunos = []
disciplina = []
notas = []

@app.route('/')
def api_root():
    return 'Seja bem-vindo!!'

@app.route('/addaluno', methods = ['POST']) #adicionar aluno
def api_newaluno():
    global alunos
    req_data = request.get_json()
    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    new_aluno = Aluno(id, nome, idade)
    alunos.append(new_aluno)
    res = {'status': 'ok'}
    return jsonify(res)



@app.route('/deletealuno', methods = ['DELETE']) #deletar aluno
def api_deletealuno():
    global alunos
    req_data = request.get_json()
    id = req_data['id']
    for aluno in alunos:
        if (int(id) == aluno.getAlunoId()):
            alunos.remove(aluno)
    res = {'status': 'ok'}        
    return jsonify(res)

@app.route('/listaluno', methods = ['GET']) #listar alunos
def api_listalunos():
    global alunos
    payload = []
    content = {}    
    for aluno in alunos:        
        content = {'id': str(aluno.getAlunoId()),'[nome]': aluno.getAlunoNome(), 
        '[idade]': str(aluno.getAlunoIdade())}
        payload.append(content)
        content = {}
     
    res =  payload 
    return jsonify(res)

@app.route('/updatealuno', methods = ['PUT'])    #atualizar alunos
def api_updatealuno():
    global alunos
    req_data = request.get_json()
    id = req_data['id']
    nome = req_data['nome']
    idade = req_data['idade']
    for aluno in alunos:
        if (int(id) == aluno.getAlunoId()):
            aluno.setAlunoNome (str(nome))
            aluno.setAlunoIdade(str(idade))
    
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/adddisciplina', methods = ['POST'])    #adicionar disciplina
def api_newdisciplina():
    global disciplina
    req_data = request.get_json()
    id = req_data['id']
    nome = req_data['nome']
    cargahoraria = req_data['cargahoraria']
    professor = req_data['professor']
    new_disciplina = Disciplina(id, nome, cargahoraria, professor )
    disciplina.append(new_disciplina)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/listdisciplina', methods = ['GET'])    #listar disciplinas
def api_listdisciplinas():
    global disciplina
    payload = []
    content = {}    
    for disc in disciplina:        
        content = {'id': str(disc.getDisciplinaId()),'[nome]': disc.getDisciplinaNome(), 
        '[cargahoraria]': str(disc.getDisciplinaCargahoraria()), '[professor]': str(disc.getDisciplinaProfessor())}
        payload.append(content)
        content = {}
          
    res =  payload 
    return jsonify(res)

@app.route('/deletedisciplina', methods = ['DELETE']) #deletar disciplina
def api_deletedisciplina():
    global disciplina
    req_data = request.get_json()
    id = req_data['id']
    for disc in disciplina:
        if (int(id) == disc.getDisciplinaId()):
            disciplina.remove(disc)
    res = {'status': 'ok'}        
    return jsonify(res)

@app.route('/updatedisciplina', methods = ['PUT'])    #atualizar disciplina
def api_updatedisciplina():
    global disciplina
    req_data = request.get_json()
    id = req_data['id']
    nome = req_data['nome']
    cargahoraria = req_data['cargahoraria']
    professor = req_data['professor']
    for disc in disciplina:
        if (int(id) == disc.getDisciplinaId()):
            disc.setDisciplinaNome(str(nome))
            disc.setDisciplinaCargahoraria(str(cargahoraria))
            disc.setDisciplinaProfessor(str(professor))
    
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/addnotas', methods = ['POST']) #adicionar notas a alunos cadastrados
def api_addnotas():
    global notas
    req_data = request.get_json()
    idmateria = req_data['idmateria']
    idaluno = req_data['idaluno']
    nota1 = req_data['nota1']
    nota2 = req_data['nota2']
    nota3 = req_data['nota3']
    nota4 = req_data['nota4']
    new_notas = Notas(idmateria, idaluno, nota1, nota2, nota3, nota4)
    notas.append(new_notas)
    res = {'status': 'ok'}
    return jsonify(res)

@app.route('/relatorio', methods = ['GET']) 
def api_relatorio ():
    global notas, disciplina,alunos
    payload = []
    content = {}
    for aluno in alunos:
        for nota in notas:
            for disc in disciplina:
                if (aluno.getAlunoId() == nota.getIdAluno()):
                    if (nota.getIdMateria() == disc.getDisciplinaId()):
                        content = {'[nome]': aluno.getAlunoNome(),
                        '[idade]': str(aluno.getAlunoIdade()),'[medianota]': str(nota.getMediaNotas()),
                        '[disciplina]': disc.getDisciplinaNome(), '[cargahoraria]':str(disc.getDisciplinaCargahoraria()),
                        '[professor]':disc.getDisciplinaProfessor()}
          
        payload.append(content)
        content = {}
    res =  payload 
    return jsonify(res)


if __name__ == '__main__':
    app.run()
