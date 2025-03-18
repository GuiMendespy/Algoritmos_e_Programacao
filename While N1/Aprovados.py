aprovados = 0
while True:
    questoes_portugues = int(input())
    if questoes_portugues < 0:
        break
    questoes_matematica = int(input())
    nota_redacao = float(input())
    if (questoes_portugues >= 0.8 * 50) and (questoes_matematica >= 0.6 * 35) and (nota_redacao >= 7):
        aprovados += 1
print(aprovados)