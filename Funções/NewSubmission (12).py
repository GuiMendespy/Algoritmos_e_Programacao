def ClassificaAluno(n,falt):
    if n>=9.5 and falt<=10:
        return 'APROVADO COM LOUVOR'
    elif 7.0<=n<9.5 and falt<=10:
        return 'APROVADO'
    elif n<7.0 and falt<=10:
        return 'REPROVADO'
    elif falt>10:
        return 'REPROVADO POR FALTAS'
n=float(input())
falt=int(input())
print(ClassificaAluno(n,falt))