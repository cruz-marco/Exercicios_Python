for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if a + b + c == 1000 and a * a + b * b == c * c:
                print(f'{a}, {b}, {c}')
