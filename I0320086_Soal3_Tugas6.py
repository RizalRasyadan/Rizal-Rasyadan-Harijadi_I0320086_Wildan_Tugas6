for angka in range(1,50):
    for i in range(2,angka):
        if (angka % i) == 0:
            print(angka,"bukan prima")
            break
    else:
        print(angka,"adalah bilangan prima")