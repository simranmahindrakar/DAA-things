#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,k;
	cin>>n>>k;
	int height[n+1];
	for(int i=0; i<n; i++)
	{
		cin>>height[i];
	}
	vector<int> dp(n+2, 1e9);
	dp[0]=0;
	for(int i=0; i<=n; i++)
	{
		for(int j=i+1; j<=n; j++) //iterate over the next i+k
		{
			if(j<n)
			{
				dp[j] = min(dp[j] , dp[i] + abs((height[i] - height[j]) * (height[i] - height[j])));
			}
		}
	}
	cout<<dp[n-1];
	
}
