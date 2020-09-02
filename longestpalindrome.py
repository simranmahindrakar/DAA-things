# Compute longest common subword using dynamic programming

# lcw[i][j] is length of longest common subword starting at w1[i], w2[j]
#
# lcw[m][j] = 0 for all j
# lcw[i][n] = 0 for all i
# lcw[i][j] = 1 + lcw[i+1][j+1], if w1[i] == w2[j]
#             0, otherwise
#

def lcw(w1,w2):
    m = len(w1)
    n = len(w2)

    maxlen = 0       # Current maximum length
    maxpos = (m,n)   # Position of lexicographically smallest word of max length

    # For DP, initialize (m+1) x (n+1) matrix lcw[][] with 0's
    # This also initializes the base case

    lcw = [ [0 for j in range(n+1)] for i in range(m+1) ]

    # Fill in lcw[][] columnwise and rowwise from bottom right corner
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if w1[i] == w2[j]:
                lcw[i][j] = 1 + lcw[i+1][j+1]

                # Update maxlen and maxpos if maxlen increases
                if lcw[i][j] > maxlen:
                    maxlen = lcw[i][j]
                    maxpos = (i,j)

                # Update maxpos if we find a lexicographically smaller word
                # with length = maxlen
                if lcw[i][j] == maxlen:
                    if w1[maxpos[0]:maxpos[0]+maxlen] > w1[i:i+maxlen]:
                        maxpos = (i,j)
            else:
                lcw[i][j] = 0

    return(maxlen,w1[maxpos[0]:maxpos[0]+maxlen])
            
# main()

# Read input
num = input()  # Discard first line, not needed

word = input().strip()
rword = ''.join(reversed(word))  # Reverse word

# Compute lcw of word and rword
(palinlen,palinpat) = lcw(word,rword)

# Print answer
print(palinlen)
print(palinpat)
