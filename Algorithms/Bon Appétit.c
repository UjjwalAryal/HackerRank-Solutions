#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
int n,k;
    scanf("%d%d",&n,&k);
    int a[n],ba=0,bc=0;
    for(int i=0;i<n;i++)
        {
        scanf("%d",&a[i]);
        if(i!=k)
            {
               ba+=a[i];
            }}

    scanf("%d",&bc);
    ba/=2;
      if((ba-bc)!=0)
          printf("%d",bc-ba);
        else
            printf("Bon Appetit");
    return 0;
}
