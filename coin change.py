
def getWays(n, c):
    memo={}
    for i in range(1,n+1):
       memo[i]=10000000
    memo[0]=1
    if (n=='0'):
        return 0
    if(n<0):
        return 0
    for i in range(1,n+1):
        for c1 in c:
            if (i-c1 > 0):
                memo[i]=(memo[i],1+memo[i-c1])
    return memo[n]
    

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)

#total no. of wyas of making change. not minimum.
N,M = map(int,input().rstrip().split(' '))
coins = list(map(int,input().rstrip().split(' ')))
dp = [0]*(N+1)
dp[0] = 1
for c in coins:
    for i in range(c,len(dp)):
        dp[i] += dp[i-c]

print(dp[N])
