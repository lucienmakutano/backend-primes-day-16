def get_prime_numbers():
    primes = []
    index = 0
    while True:
        if index % 2 != 0:
            primes.append(index)

        if len(primes) == 20:
            break

        index += 1

    return primes


if __name__ == '__main__':
    print(get_prime_numbers())
