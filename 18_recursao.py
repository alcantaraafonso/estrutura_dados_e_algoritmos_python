def recursao(i):
    print('Recursão')
    i += 1
    if i < 5:
        recursao(i)
        
    return


recursao(0)