#include<stdio.h>
main()
{
int i,j;
long int a[5];
for(i=0;i<5;i++)   scanf("%ld",&a[i]);
int t=0;


for (i = 0; i < 5; ++i)
    {
        for (j = i + 1; j < 5; ++j)
        {
            if (a[i] > a[j])
            {
                t=  a[i];
                a[i] = a[j];
                a[j] = t;
            }
        }
    }

long int min=a[0]+a[1]+a[2]+a[3]  ,   max=a[1]+a[2]+a[3]+a[4] ;
printf("%ld %ld",min,max);
}
