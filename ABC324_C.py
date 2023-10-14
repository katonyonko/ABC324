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
5 ababc
ababc
babc
abacbc
abdbc
abbac
1 aoki
takahashi
9 atcoder
atoder
atcode
athqcoder
atcoder
tacoder
jttcoder
atoder
atceoder
atcoer
"""

def solve(test):
  N,T=input().split()
  N=int(N)
  S=[input() for _ in range(N)]
  ans=[]
  for i in range(N):
    s=S[i]
    if len(s)<len(T):
      if len(s)==len(T)-1:
        j,k=0,0
        while j<len(s) and k<len(T):
          if s[j]==T[k]:
            j+=1
            k+=1
          else:
            k+=1
        if j==len(s):
          ans.append(i)
    elif len(s)>len(T):
      if len(s)==len(T)+1:
        j,k=0,0
        while j<len(s) and k<len(T):
          if s[j]==T[k]:
            j+=1
            k+=1
          else:
            j+=1
        if k==len(T):
          ans.append(i)
    else:
      d=0
      for j in range(len(T)):
        if s[j]!=T[j]:
          d+=1
      if d<=1:
        ans.append(i)
  print(len(ans))
  print(*[ans[i]+1 for i in range(len(ans))])

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