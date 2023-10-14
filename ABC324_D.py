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
4
4320
3
010
13
8694027811503
"""

def solve(test):
  N=int(input())
  S=input()
  c=[0]*10
  for i in range(N):
    c[int(S[i])]+=1
  ans=0
  m=''
  for i in range(10):
    if c[i]>0:
      m+=str(i)*c[i]
  m=int(m)
  n=''
  for i in reversed(range(10)):
    if c[i]>0:
      n+=str(i)*c[i]
  n=int(n)
  k,l=max(0,int(m**0.5)-1),int(n**0.5)+2
  for i in range(k,l):
    x=str(i**2)
    x='0'*(N-len(x))+x
    c2=[0]*10
    for j in range(len(x)):
      c2[int(x[j])]+=1
    if c==c2: ans+=1
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