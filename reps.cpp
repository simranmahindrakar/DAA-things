#include <iostream>
#include <bits/stdc++.h>
using namespace std; 
int main()
{
	string s;
	cin>>s;
	char ch = 'A';
	int ans=1; //the smallest possbile ans =1
	int count =0;
	for(char c : s)
	{
		if(c==ch)
		{
			count++;
			ans = max(count, ans);
		}
		else {
			ch = c;
			count = 1; // reset count
		}
	}
	cout<<ans;
}
