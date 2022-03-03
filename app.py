from config.Config import Config
from config.Database import Database
from dao.ProfessorDao import ProfessorDao
from flask import Flask, request, render_template

from model.Professor import Professor, Professor

app = Flask(__name__)

dao = ProfessorDao(Database(Config().config).conn)

@app.route('/', methods=["GET"])
def iniciar():
       return render_template(
        "main.html"
    )

@app.route('/professor/novo', methods=["GET"])
def novo():
    return render_template("inserir.html")

@app.route('/professor', methods=["POST"])
def inserir():
    professor = Professor()
    professor.nome = request.form.get("nome")
    professor.email = request.form.get("email")
    professor.siape = request.form.get("siape")
    professor.num_alunos = int(request.form.get("num_alunos"))
    professor.idade = int(request.form.get("idade")) 

    dao.inserirProfessor(professor)

    lista = dao.selecionarProfessores()
    return render_template(
        "listagem.html", professor,
        lista=lista
    )

@app.route('/professor', methods=["GET"])
def listar():
    lista = dao.selecionarProfessores()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/professor/<pid>', methods=["GET"])
def editarPagina(pid):
    professor = dao.selecionarProfessor(pid)
    return render_template("editar.html", professor=professor)

@app.route('/professor/editar', methods=["POST"])
def editar():

    professor = Professor()
    professor.pid = request.form.get("pid")
    professor.nome = request.form.get("nome")
    professor.email = request.form.get("email")
    professor.siape = request.form.get("siape")
    professor.num_alunos = int(request.form.get("num_alunos"))
    professor.idade = int(request.form.get("idade")) 
    professor = dao.alterarProfessor(professor)
    
    lista = dao.selecionarProfessores()
    return render_template(
        "listagem.html",
        lista=lista
    )

@app.route('/professor/remover/<pid>', methods=["GET"])
def remover(pid):
    professor = Professor()
    professor.pid = pid
    dao.excluirProfessor(professor)
    
    lista = dao.selecionarProfessores()
    return render_template(
        "listagem.html",
        lista=lista
    )


if __name__ == '__main__':
    app.run()
