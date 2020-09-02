#include<stdio.h>
main()
{
	int first,second,n=0;
	scanf("%d",first);
	if(first!=-1)
	{
		scanf("d%",&second);
		while(second!=-1)
		{
			if(first<second){
				first=second;
			}
			if(first>n>second){
				n=second;
			}
			
		}
		first=second;
		scanf("%d",&second);
	}
	printf("%d",&n);
}
