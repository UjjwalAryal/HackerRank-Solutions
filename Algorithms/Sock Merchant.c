#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int n;
    scanf("%d",&n);
  int c[n];
    for(int i=0;i<n;i++)  scanf("%d",&c[i]);
    int a=0;

    for(int i=0;i<n;i++)
        {
        for(int j=i+1;j<n;j++)
           { if(c[i]==c[j])
           { a++; c[j]=rand(); break;
                            }}
    }
    printf("%d",a);
    return 0;
}
