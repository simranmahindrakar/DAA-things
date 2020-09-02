#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
const long long M = 10e9+7;

int main()
{

	int t;
	cin>>t;
	while(t--)
	{
		int n;
		ll ans=0;
		ll d1,d2;
		ll min_a = M;
	    ll min_b = M;
		cin>>n;
		ll a[n+1];
		ll b[n+1];
		for(ll i=0; i<n ; i++)
		{
			cin>>a[i];
			min_a =  min(min_a, a[i]);   //get minimum of array a[]
		}
		for(ll i=0; i<n ; i++)
		{
			cin>>b[i];
			min_b =  min(min_b, b[i]);   //get minimum of array b[]
		}
		for(ll i =0; i<n ; i++)
		{
			 d1 = a[i] - min_a;
			 d2 = b[i] - min_b;
			 ans += max(d1,d2);
		}
		
		cout<<ans;
	}
}
