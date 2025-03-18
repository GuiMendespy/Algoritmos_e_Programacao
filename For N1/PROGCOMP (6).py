count=1
menor_idade=float('inf')
maior_idade=float('-inf')
for count in range (1,101):
    idade=int(input())
    count+=1
    menor_idade=min(idade,menor_idade)
    maior_idade=max(idade,maior_idade)
print('mais novo:',menor_idade)
print('mais velho:',maior_idade)