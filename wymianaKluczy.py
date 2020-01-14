"""Napisz program realizujący wymianę kluczy, jednym z podanych algorytmów asymetrycznych,
- użytkownik podaje liczby pierwsze p, q
- program pyta o klucz prywatny Alicji
- program pyta o klucz prywatny Bolka
- program zwraca A=, B= oraz s=
*) Program sprawdza czy p i q są pierwsze."""


def check_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(n, "nie jest pierwsza")
                break
            else:
                print(n, "jest pierwsza")
    else:  # gdy n = 1
        print(n, "nie jest pierwsza.")


x = input("Podaj liczbe p: ")
y = input("Podaj liczbe q: ")
p = int(x)
q = int(y)


keyAlice = int(input("Podaj prywatny klucz Alicji (numeryczny): "))
keyBolek = int(input("Podaj prywatny klucz Bolka (numeryczny): "))


A = (q ** keyAlice) % p
print('A = ', A)

B = (q ** keyBolek) % p
print('B = ', B)

s = (B ** keyAlice) % p
print('s = ', s)
