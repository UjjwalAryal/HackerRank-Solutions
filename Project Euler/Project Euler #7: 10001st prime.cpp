#include <iostream>
#include<cmath>

using namespace std;
#define MAX 1000000
int arr[MAX+1];

void formEranthoses(){
    for(int i=1; i<=MAX; i++) arr[i]=i;
    int root = (int) pow(MAX,0.5);
    for(int i=2 ; i<=root ; i++){
        for(int j = 2; j<= MAX/2 ; j++){
            if(i*j <= MAX)  arr[i*j] = 0;
        }
    }

    for(int i=2,count=1;i<MAX;i++){
        if(arr[i]) arr[count++] = arr[i];
    }
}
int main(){
    int t,i;
    cin >> t;
    formEranthoses();
    while(t--){
        cin >> i;
        cout<<arr[i]<<endl;
    }
    return 0;
}
