# python3
import sys


def find_pattern(pat, txt): 
  M = len(pat) 
  N = len(txt) 
  lps = [0]*M 
  j = 0
  out = []
  computeLPSArray(pat, M, lps) 

  i = 0
  while i < N: 
    if pat[j] == txt[i]: 
      i += 1
      j += 1

    if j == M: 
      out.append(i-j) 
      j = lps[j-1] 
    elif i < N and pat[j] != txt[i]: 
      if j != 0: 
        j = lps[j-1] 
      else: 
        i += 1
  return out

def computeLPSArray(pat, M, lps): 
  len = 0
  lps[0]
  i = 1

  while i < M: 
    if pat[i]== pat[len]: 
      len += 1
      lps[i] = len
      i += 1
    else:
      if len != 0: 
        len = lps[len-1] 
      else: 
        lps[i] = 0
        i += 1

if __name__ == '__main__':
  pattern = input().strip()
  text = input().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

