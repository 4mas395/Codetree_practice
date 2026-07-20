A,B,C = map(int,input().split())
ans = 0

wp1 = min(A,B,C)
wp2 = max(A,B,C)

res = A + B + C
print(res-wp1-wp2)