#include <iostream>
#include <cstring>
using namespace std;
#define ll long long int
const int siz=5000001;
ll arr[siz];
ll collatz(ll n)
{
    if(n>5000000)
    {
        if(n%2==0)  return collatz(n/2)+1;
        else return collatz(3*n+1)+1;
    }
    if(arr[n]==0)
    {
        if(n%2==0)  arr[n]=collatz(n/2)+1;
        else arr[n]=collatz(3*n+1)+1;
    }
    return arr[n];
}
int main() {
    ll t,n;
    cin>>t;
    memset(arr,0,sizeof(0));
    arr[1]=1;
    for(int i=2,j=2;i<siz;i*=2,j++)
        arr[i]=j;
    for(int i=3;i<siz;i++)
        collatz(i);
    int result[siz];
    result[1]=1;
    for(int i=2;i<siz;i++)
    {
        if(arr[i]>=arr[result[i-1]])
        {
            result[i]=i;
        }
        else result[i]=result[i-1];
    }
    while(t--)
    {
        cin>>n;
        cout<<result[n]<<endl;
    }
    return 0;
}
