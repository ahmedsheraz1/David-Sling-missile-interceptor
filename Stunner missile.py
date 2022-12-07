Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
        # Now call the function we just defined:

        
fib(300)
0 
1 
1 
2 
3 
5 
8 
13 
21 
34 
55 
89 
144 
233 
