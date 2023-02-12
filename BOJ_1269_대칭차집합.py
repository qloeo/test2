# BOJ_1269_대칭차집합.py
import heapq

# T = list(map(int, input().split()))
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

A = [ 1, 2, 4]
B = [2, 3, 4, 5, 6]

heap = set(A) ^ set(B)
print(len(heap))