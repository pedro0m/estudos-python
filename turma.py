turma = [
    {'ra': '2401', 'nome': 'Ana', 'notas': [8.0, 7.5, 9.0], 'faltas': 2},
    {'ra': '2402', 'nome': 'Bruno', 'notas': [5.0, 6.0, 4.5], 'faltas': 8},
    {'ra': '2403', 'nome': 'Carla', 'notas': [9.5, 9.0, 10.0], 'faltas': 0},
    {'ra': '2404', 'nome': 'Diego', 'notas': [6.5, 7.0, 6.0], 'faltas': 12},
    {'ra': '2405', 'nome': 'Elena', 'notas': [7.0, 7.0, 8.0], 'faltas': 4}
]

medias_turma = {aluno['nome']: sum(aluno['notas']) / len(aluno['notas']) for aluno in turma}

aprovados = [aluno['nome'] for aluno in turma if medias_turma[aluno['nome']] >= 7 and aluno['faltas'] < 10]

situacao_final = {aluno['ra']: 'Aprovado' if aluno['nome'] in aprovados else 'Exame ou Reprovado' for aluno in turma}
