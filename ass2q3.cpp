#include<stdio.h>
main()
{
	int curr, prev,diff=0;
	scanf("%d",&prev);
	scanf("%d",&curr);
	diff=curr-prev;
	printf("%d",&diff);
	do
	{
		prev=curr;
		scanf("%d",&curr);
		if(curr==-1){
			printf("\n");
			break;
		}
		diff=curr-prev;
		printf("%d",&diff);
		} while(1);
	
}
