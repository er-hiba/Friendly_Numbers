M = int(input("Enter an integer: "))
while M <= 0:
    M = int(input("Enter a positive non-null integer: "))

N = int(input("Enter an integer: "))
while N <= 0:
    N = int(input("Enter a positive non-null integer: "))

divisors_M = 0
divisors_N = 0
i = 2
j = 2
sum_M = 0
sum_N = 0

while i < M :
    if M % i == 0 :
        divisors_M += 1
        sum_M = sum_M + i
    i += 1
print("The sum of the proper divisors of",M,"is", sum_M)

while j < N :
    if N % j == 0 :
        divisors_N += 1
        sum_N = sum_N + j
    j += 1

print("The sum of the proper divisors of",N,"is", sum_N)

if sum_N == M and sum_M == N :
    print(N,"and",M,"are friendly numbers.")
else :
    print(N,"and", M,"are not friendly numbers.")
