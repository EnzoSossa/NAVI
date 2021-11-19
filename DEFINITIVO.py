import numpy as np
import math as mt
#import time


# Questão 1)

#tic = time.process_time()
i=1
soma=0
for i in range(1,5000001):
    if (-1)**i>0:
        if i%49==0:
            if i%37==0: 
                soma=soma+1
#tok = time.process_time()
#print("Computation time = "+str((tok - tic ))+"s")                
print("1°) Existem ", soma, " números pares, múltiplos de 49 e 37 simultaneamente, no intervalo de 1 até 5 milhões")





# Questão 2)

X = np.array(range(0,10))                 
for i in range(1,10):
    if i % 2 == 0:
        X[i] = 3**i +7* mt.factorial(i)
    else:
        X[i] = (2**i) + 4 * mt.log(i)
 
print("2°) O maior elemento desse vetor se encontra na ", np.argmax(X)+1, "° posição.")
print("2°)","%.2f" % X.mean(), "é a média dos elementos contidos nesse vetor.")






# Questão 3)

parameters = {}
main_grades = float(input("Entre com a nota de 5 alunos: "))
parameters["Nota de 5 alunos"] = main_grades 

for i in range(1,6):
    alunos = "Aluno "+ str(i)
    notas = float(input("Entre com a nota do " + str(alunos) +" : "))
    parameters[alunos] = notas 
    
parameters_students = {k: v for k, v in parameters.items() if k not in {'Nota de 5 alunos'}}
best_students = [k for k, v in parameters_students.items() if v == max(parameters_students.values())]
best_grade = max(parameters_students.values())
print("3°) O(s) aluno(s) com maior nota foi/foram: ", best_students, "com nota = ", best_grade)












