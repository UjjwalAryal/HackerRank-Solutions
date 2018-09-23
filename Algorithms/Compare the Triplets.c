#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(){
    int a0,a1,a2,b0,b1,b2;

    scanf("%d %d %d",&a0,&a1,&a2);

    scanf("%d %d %d",&b0,&b1,&b2);

    int s1=0,s2=0;

    if (a0>b0) s1=s1+1;
    if (a0<b0) s2=s2+1;
    if (a1>b1) s1=s1+1;
    if (a1<b1) s2=s2+1;
    if (a2>b2) s1=s1+1;
    if (a2<b2) s2=s2+1;
printf("%d %d",s1,s2);
    return 0;
}
