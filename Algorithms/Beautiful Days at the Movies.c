#include <stdio.h>
int abs(int x)
    {
    if(x<0) return -x;
    return x;
}
int rev(int x)
    {
    int rev=0;
    do{
       rev=  (rev*10)+ (x%10);
       x/=10;
    }while(x);
    return rev;
}

int main() {
  int i,j,k,c=0;
    scanf("%d%d%d",&i,&j,&k);
    for(int y=i;y<=j;y++)
        {
        if(!((y-rev(y))%k))     c++;

    }
   printf("%d",c);
    return 0;
}
