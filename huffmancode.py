wordarr = []
S = [.3, .15, .2, .1, .08, .1, .05, .02]
S= sorted(S,reverse=True)
r = 2
extraDigit = 1%(r-1)

if extraDigit == 0:
    pass
else:
    S.append(0)  #Only works for r = 3


    
def WordLengthArr(S,r):
    
    n = len(S) -1
    if r == 2:
        if n == 1:
            wordarr.append(1)
        else:
            combinedDigit = S[n] + S[n-1]
            wordarr.append(combinedDigit)
            S.pop(n)
            S.pop(n-1)
            S.append(combinedDigit)
            S= sorted(S,reverse=True)
            WordLengthArr(S,r)
    if r == 3:
        if n == 2:
            wordarr.append(1)
        else:
            combinedDigit = S[n] + S[n-1] + S[n-2]
            wordarr.append(combinedDigit)
            S.pop(n)
            S.pop(n-1)
            S.pop(n-2)
            S.append(combinedDigit)
            S= sorted(S,reverse=True)
            WordLengthArr(S,r)
    return wordarr

        
    
if __name__ == "__main__":
    WordLengthArr(S,r)
    wordLength = sum(wordarr)
    print("Word Length: ", wordLength)
