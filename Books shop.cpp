#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
	int numbooks,money;
	cin>>numbooks,money;
	int price[numbooks+1]; //to store the price array
	int pages[numbooks+1]; //to store number of pages
	for(int i=0; i<numbooks; i++) {
		cin>>price[i];
	}
	for(int i=0; i<numbooks; i++) {
		cin>>pages[i];
	}
	int dp[numbooks+1][money+2];  //dp array
	//base case
	dp[0][0] = 0
	for(int i=1; i<=numbooks; i++)
	{
		for(int j=1; j<=money; j++)
		{
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-price[i]] + pages[i]);
		}
	}
	cout<<dp[numbooks][money];
}

