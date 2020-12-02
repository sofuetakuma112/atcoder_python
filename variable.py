#!/usr/bin/env python
# -*- coding: utf-8 -*-

# x = list(map(int, input().split()))
# print(x)

# x = [int(i) for i in input().split()]
# print(x)

# x = list(input().split())
# print(x)

# x = [i for i in input().split()]
# print(x)

# x = int(input())
# y = int(input())
# print(x, y)

# x = [int(input()) for i in range(2)]
# print(x)

# x = [input() for i in range(5)]
# print(x)

# rows = int(input())
# x = [int(input()) for i in range(rows)]
# print(x)

# rows = int(input())
# x = [input() for i in range(rows)]
# print(x)

# x = [list(map(int, input().split())) for i in range(3)]
# print(x)

# rows = int(input())
# x = [list(map(int, input().split())) for i in range(rows)]
# print(x)

# rows = int(input())
# x = [[int(j) for j in input().split()] for i in range(rows)]
# print(x)

# rows = int(input())
# x = []
# for i in range(rows):
#   x.append(list(map(int, input().split())))
# print(x)

# rows = int(input())
# number = []
# alphabet = []
# for i in range(rows):
#   n, a = input().split()
#   number.append(int(n))
#   alphabet.append(a)
# print(number)
# print(alphabet)

# H1 = int(input())
# H2 = int(input())
# print(H1 - H2)

# n = int(input())
# print(n*2)

# n, m = list(map(int, input().split()))
# print((n-1)*(m-1))

# n, m = map(int, input().split())
# print(n*m-(n+m-1))

# H, W = map(int, input().split())
# h, w = map(int, input().split())
# print(H*W-W*h-w*(H-h))

# A, B = map(int, input().split())
# print(A*B)

# a = int(input())
# print(a+a*a+a*a*a)

# import math
# print(math.factorial(5))

# import math
# N = int(input())
# print(math.factorial(N) % (10**9+7))

# N = int(input())
# A = int(input())
# print(N**2 - A)

# R = int(input())
# print(3*R**2)

# N = int(input())
# print(N**3)

# r = int(input())
# print(r**2)

# x = 12
# y = 3
# print(x/y)

# T, X = map(int, input().split())
# print(T / X)

# x, y = map(int, input().split())
# print(y//x)

# N = int(input())
# print(N//3)

# X, Y = map(int, input().split())
# print(X+Y//2)

# X, Y, Z = map(int, input().split())
# print(X*Y//2)

# import math
# print(math.ceil(1.1))

# import math
# A, B = map(int, input().split())
# print(math.ceil(B/A))

# import math
# x, y = map(int, input().split())
# print(math.ceil((x+y)/2))

# N = int(input())
# print((N%12)+1)

# print(not False)

# x = 3
# if x == 1:
#   print("x is 1")
# elif x == 2:
#   print("x is 2")
# else:
#   print("x is not 1 and 2")

# N = int(input())
# if N == 1:
#   print("ABC")
# elif N == 2:
#   print("chokudai")

# R = int(input())
# if R < 1200:
#   print("ABC")
# elif R < 2800:
#   print("ARC")
# else:
#   print("AGC")

# A, B, K = map(int, input().split())
# for i in range(K):
#   if A >= 1:
#     A = A - 1
#   elif B >= 1:
#     B = B - 1
# print(A, B)

# x = 1
# print("x is 1" if x == 1 else "x is not 1")

# x = 2
# print("x is 1" if x == 1 else "x is 2" if x == 2 else "x is 3" if x == 3 else "other")

# H1, W1 = map(int, input().split())
# H2, W2 = map(int, input().split())
# print("YES" if H1 == H2 or H1 == W2 or W1 == H2 or W1 == W2 else "NO")

# A = int(input())
# B = int(input())
# print("GREATER" if A > B else "LESS" if A < B else "EQUAL")

# x = "Hello world!"
# print("e include" if "e" in x else "e don't include")

# N = int(input())
# print("YES" if N % 3 == 0 else "NO")

# N = input()
# print("YES" if N in "369" else "NO")

# N = input()
# print("YES" if "7" in N else "NO")

# A, B, C = map(int, input().split())
# print("YES" if A <= C <= B else "NO")

# A, B = map(int, input().split())
# print(A*B if 1 <= A <= 9 and 1 <= B <= 9 else -1)

# S = input()
# print("Good" if S[0] != S[1] != S[2] != S[3] else "Bad")

# K, X = map(int, input().split())
# for i in range(X-K+1, X+K):
#   print(i, end=" ")

# N = int(input())
# x = N // 15
# y = N % 15
# total = x*60
# for i in range(N-y+1, N+1):
#   if not (i % 15 == 0 or i % 3 == 0 or i % 5 == 0):
#     total = total + i
# print(total)

# N = int(input())
# total = 0
# for i in range(1, N+1):
#   if (i % 3) != 0 and (i % 5) != 0:
#     total = total+i
# print(total)

# N, K = map(int, input().split())
# people = list(map(int, input().split()))
# count = 0
# for i in people:
#   if i >= K:
#     count = count + 1
# print(count)

# A, B = map(int, input().split())
# count = 0
# x = 1
# while x < B:
#   x = x - 1 + A
#   count = count + 1
# print(count)

# N, K = map(int, input().split())
# digits = 0
# while(N > 0):
#   N = N//K
#   digits = digits+1
# print(digits)

# X = int(input())
# print(int(X**(1/4)))

# N = int(input())
# print(int(N**(1/2))**2)

# S = input()
# print(S + "pp")

# print("HelloWorld!"*2)

# D = int(input())
# print("Christmas" + " Eve" * (25 - D))

# a, b = input().split()
# print(a*int(b) if a < b else b*int(a))

# S = input()
# print("x"*len(S))

# s = input()
# i = int(input())
# print(s[i-1])

# S = input()
# print("YES" if S[-1] == "T" else "NO")

# S = input()
# print("Heisei" if S <= "2019/04/30" else "TBD")

# S = input()
# print(S.count("A"), S.count("B"), S.count("C"), S.count("D"), S.count("E"), S.count("F"))

# A, B = map(int, input().split())
# S = input()
# print("YES" if S.count("-") == 1 and S[A] == "-" else "NO")

# N = input()
# S = input()
# print(S.count("ABC"))

# S = input()
# print("2018"+S[4:])

# s = input()
# print(s[::1])

# S = input()
# if S == S[::-1] and S[0:(len(S)-1)/2] == S[0:(len(S)-1)/2:-1]:
#   print("YES")

# S = input()
# N = len(S)
# S1 = S[0:(N-1)//2]
# S2 = S[(N+3)//2-1:N]
# print("YES" if S == S[::-1] and S1 == S1[::-1] and S2 == S2[::-1] else "NO")

# array = list(map(int, input().split()))
# print("YES" if array.count(5) == 2 and array.count(7) == 1 else "NO")

# x = [1, 2, 3, 2, 1, 3]
# print((set(x)))

# x = [2, 1, 3]
# print(sorted(x)[::-1])
# print(max(x), min(x), sum(x))

# x = 1234
# print(list(map(int, str(x))))

# x = 1
# x += 1
# print(x)