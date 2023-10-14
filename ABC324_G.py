import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
10
1 8 7 4 5 6 3 2 9 10
5
2 0 4
1 1 2
2 0 2
2 2 5
1 0 1
8
6 7 8 4 5 1 3 2
5
2 0 0
1 1 0
2 2 0
1 3 8
2 2 3
30
20 6 13 11 29 30 9 10 16 5 8 25 1 19 12 18 7 2 4 27 3 22 23 24 28 21 14 26 15 17
10
1 0 22
1 0 21
2 0 15
1 0 9
1 3 6
2 3 18
1 6 2
1 0 1
2 5 20
2 7 26
"""

def solve(test):
  N=int(input())
  A=list(map(int, input().split()))
  Q=int(input())
  query=[list(map(int, input().split())) for _ in range(Q)]
  ans=0
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(1)