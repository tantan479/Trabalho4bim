from model.Professor import Professor


class ProfessorDao:
    def __init__(self, connection):
        self.connection = connection

    def selecionarProfessores(self) -> list:
        c = self.connection.cursor()
        sql = 'SELECT * FROM professor ORDER BY pid'
        c.execute(sql)
        recset = c.fetchall()
        c.close()

        lista = []
        for item in recset:
            professor = Professor()
            professor.pid = item[0]
            professor.nome = item[1]
            professor.email = item[2]
            professor.siape = item[3]
            professor.num_alunos = item[4]
            professor.idade = item[5]

            lista.append(professor)

        return lista

    def selecionarProfessor(self, pid) -> Professor:
        c = self.connection.cursor()
        c.execute(f"SELECT * FROM professor WHERE pid = {pid}")
        recset = c.fetchone()
        c.close()

        print(recset)

        professor = Professor()
        professor.pid = recset[0]
        professor.nome = recset[1]
        professor.email = recset[2]
        professor.siape = recset[3]
        professor.num_alunos = recset[4]
        professor.idade = recset[5]
        

        return professor

    def inserirProfessor(self, professor: Professor) -> Professor:
        c = self.connection.cursor()
        c.execute("""
            insert into professor(nome, email, senha, siape, num_alunos, idade)
            values('{}', '{}', '{}', '{}', '{}') RETURNING pid
        """.format(professor.nome, professor.email, professor.siape, professor.num_alunos, professor.idade))

        self.connection.commit()

    def alterarProfessor(self, professor: Professor) -> Professor:
        c = self.connection.cursor()
        c.execute("""
            update professor
            SET nome = '{}', email = '{}', siape = '{}', num_alunos = '{}', idade = '{}'
            WHERE pid = '{}';
        """.format(professor.nome, professor.email, professor.siape, professor.num_alunos, professor.idade, professor.pid))

        self.connection.commit()

    def excluirProfessor(self, professor: Professor) -> Professor:
        c = self.connection.cursor()
        c.execute("""
            delete from professor
            where pid = '{}'
        """.format(professor.pid))
        self.connection.commit()
