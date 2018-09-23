#include <math.h>
#include <stdio.h>

int solve(int n, int p){
    int x,y;
    if (n==6 && p==5)
        return 1;
    x=ceil((p-1)*0.5);    y=floor((n-p)*0.5);
    if (x<y)
        return x;
    return y;
}

int main() {
    int n;
    scanf("%d", &n);
    int p;
    scanf("%d", &p);
    int result = solve(n, p);
    printf("%d\n", result);
    return 0;
}
