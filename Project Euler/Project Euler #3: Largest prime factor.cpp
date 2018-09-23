#include <iostream>
#include<cmath>
#define ll long long int
using namespace std;
ll func(ll n)
{
    while(n%2==0)   n/=2;
    if(n==1)    return 2;
    while(n%3==0)   n/=3;
    if(n==1)    return 3;
    for(ll i=5,j=0;i*i<=n;)
    {
        while(n%i==0)   n/=i;
        if(n==1)    return i;
        i+=(2+j*2);
        j=(j+1)%2;
    }
    return n;
}
int main()
{
    int t;
    cin>>t;
    ll n;
    while(t--)
    {
        cin>>n;
        cout<<func(n)<<endl;
    }
    return 0;
}
