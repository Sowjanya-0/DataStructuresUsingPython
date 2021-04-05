def search(p, t):
    M = len(p)
    N = len(t)
    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (t[i + j] != p[j]):
                break
            j += 1
        if (j == M): 
            print("Pattern is found at index ", i)
if __name__ == '__main__':
    t = "AABAACAADAABAAABAA"
    p = "AA"
    search(p, t)
