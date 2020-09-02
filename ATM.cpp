#include<stdio.h>
main()
{
	int x;
	float y;
	scanf("%d",&x);
	scanf("%f",&y);
	if(x%5==0)
	{
		if((x+0.50)<y)
		{
			float currbal= y - (x+0.50);
			printf("%f",currbal);
		}
		else{
			printf("%f",y);
		}
	}
	else{
		printf("%f",y);
	}
}
