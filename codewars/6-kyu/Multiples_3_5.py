#SOMA DE TODOS OS NÚMEROS MENORES QUE N QUE SÃO MÚLTIPLOS DE 3 OU 5
def solution(number):
    sum:int = 0
    if number > 0:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum
    else:
        return 0

print(solution(4))