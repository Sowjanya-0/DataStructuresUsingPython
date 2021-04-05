def KMPSearch(p, t):
    M = len(p)
    N = len(t)
    lps = [0]*M
    j = 0
    computeLPSArr(p, M, lps)
    i = 0
    while i < N:
        if p[j] == t[i]:
            i += 1
            j += 1
  
        if j == M:
            print ("Pattern is found at index " + str(i-j))
            j = lps[j-1]
  
        elif i < N and p[j] != t[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
  
def computeLPSArr(p, M, lps):
    len = 0
    lps[0]
    i = 1
    while i < M:
        if p[i]== p[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1
  
t = "ABABDABACDABABCABAB"
p = "ABABCABAB"
KMPSearch(p, t)
  