numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    if i <= 1:
        continue
    elif i == 2:
        primes.append(i)
    elif i % 2 == 0:
        not_primes.append(i)
    else:
        for j in range(3, i + 1, 2):
            if i % j == 0 and i > j:
                not_primes.append(i)
                break
            elif i % j == 0:
                primes.append(i)
                break
            elif i % j == 0 and i == j:
                not_primes.append(i)
                break
print('Primes :', primes)
print('Not Primes :', not_primes)
