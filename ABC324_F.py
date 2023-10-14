import io
import sys
import pdb
from collections import defaultdict, deque, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop
from bisect import bisect_right, bisect_left
from math import gcd
import math

_INPUT = """\
6
5 7
1 2 3 6
1 3 9 5
2 3 1 5
2 4 5 3
2 5 1 9
3 4 4 8
4 5 2 7
3 3
1 3 1 1
1 3 2 1
1 3 3 1
10 20
3 4 1 2
7 9 4 5
2 4 4 5
4 5 1 4
6 9 4 1
9 10 3 2
6 10 5 5
5 6 1 2
5 6 5 2
2 3 2 3
6 10 4 4
4 6 3 4
4 8 4 1
3 5 3 2
2 4 3 2
3 5 4 2
1 5 3 4
1 2 4 2
3 7 2 2
7 8 1 3
"""

def solve(test):
  N,M=map(int, input().split())
  G=[[] for _ in range(N)]
  edge=[[] for _ in range(N)]
  for _ in range(M):
    u,v,b,c=map(int, input().split())
    G[u-1].append(v-1)
    edge[u-1].append((v-1,b,c))
  l,r=0,10**4+1
  for _ in range(60):
    mid=(l+r)/2
    dp=[None]*N
    dp[0]=0
    for u in range(N-1):
      if dp[u]==None: continue
      for v,b,c in edge[u]:
        if dp[v]==None:
          dp[v]=dp[u]+b-c*mid
        else:
          dp[v]=max(dp[v], dp[u]+b-c*mid)
    if dp[N-1]>=0: l=mid
    else: r=mid
  ans=r
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
main(0)