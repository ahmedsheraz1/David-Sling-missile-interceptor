Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
[1]
print(f(2))
[1, 2]
print(f(3))
[1, 2, 3]
