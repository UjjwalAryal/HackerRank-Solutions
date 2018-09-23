#include<stdio.h>
int main(){
    int i,a[26];
    for(i=0;i<26;i++)   scanf("%d",&a[i])  ;
    char c[200];
    i=0;

    while((c[i]=getchar())!=EOF){
      i++;
    }

    int l=i-1;
    int n,n1[l];
    for(i=1;i<=l;i++){
    	n=c[i]-97;  //printf("%c",c[i]);
    	n1[i]=a[n];
    }
    int t=n1[1];
    for(i=2;i<=l;i++){ 
        if (n1[i]>t)  t=n1[i];
    }

    printf("%d",t*l);
    return 0;
}
