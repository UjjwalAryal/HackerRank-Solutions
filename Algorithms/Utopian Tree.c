#include <stdio.h>
int main(){
    int t;
    scanf("%d",&t);
   while(t--)
       {
       int n;
       scanf("%d",&n);
       int h=1;
       for(int i=0;i<n;i++)
           {
           if(i%2==0)
               h*=2;
           else
               h+=1;
       }
       printf("%d\n",h);



   }
    return 0;
}
