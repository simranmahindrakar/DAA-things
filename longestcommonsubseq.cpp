#include<stdio.h>
main()
{
	int prev,curr,len=0,maxlen=0;
	scanf("%d",&prev);
	if(prev!=-1)
	{
		len=1;
		maxlen=1;
		scanf("%d",&curr);
		while(curr!=-1)
		{
			if(prev<curr)
			{
				len=len+1;
				}
			else{
				if(maxlen<len){
					maxlen=len;
				}
				len=1; //reset len
			}
			prev=curr;
			scanf("%d",&curr);	
		}
	}
	if(maxlen<len){
		maxlen=len;
	}
	printf("the length of the longest common subseq is %d",maxlen);
	}

