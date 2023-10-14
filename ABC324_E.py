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
3 bac
abba
bcb
aaca
5 xx
x
x
x
x
x
1 y
x
10 ms
mkgn
m
hlms
vmsle
mxsm
nnzdhi
umsavxlb
ffnsybomr
yvmm
naouel
"""

def solve(test):
  ans=0
  N,T=input().split()
  N=int(N)
  S=[input() for _ in range(N)]
  f,b=[],[]
  for i in range(N):
    s=S[i]
    j,k=0,0
    while j<len(s) and k<len(T):
      if s[j]==T[k]:
        j+=1
        k+=1
      else:
        j+=1
    f.append(k)
    j,k=len(s)-1,len(T)-1
    while j>=0 and k>=0:
      if s[j]==T[k]:
        j-=1
        k-=1
      else:
        j-=1
    b.append(len(T)-1-k)
  f.sort(); b.sort(reverse=True)
  now=0
  for i in range(N):
    while now<N and f[i]+b[now]>=len(T): now+=1
    ans+=now
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