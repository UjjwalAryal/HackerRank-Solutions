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
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    double p=0,e=0,z=0;
    for(int i=0;i<n;i++){
        if(arr[i]==0)
            z=z+1;
        else if (arr[i]>0)
            p=p+1;
        else
            e=e+1;
    }
    printf("%lf\n%lf\n%lf",(p/n),(e/n),(z/n));
    return 0;
}
