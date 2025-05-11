def soma(n):
    print('soma')
    if n == 0:
        return 0
        
    return n + soma(n - 1)


print(soma(5))