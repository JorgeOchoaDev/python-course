def factorial(integer):
    accumulator = integer + 1
    for number in range(integer + 1,1,-1):
        accumulator *= (number -1)
    factorial = int(accumulator/(integer+1))
    print (factorial)

# Como el factorial calcula permutaciones posibles de n objetos, la fórmula general n! = (n-1) (n-2)...
# Es incorrecta para calcular el factorial de 0 ya que en combinatoria hay 1 forma de permutar 0 objetos.
# Es por esto que la fórmula correcta para calcular el factorial es n! = n+1!/n

factorial(15)