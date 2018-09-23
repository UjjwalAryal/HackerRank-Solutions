#include <iostream>

using namespace std;

int maxProduct(int arr[20][20]){
    int cur,max = -99;

    //check right
    for(int i=0;i<20;i++){
        for(int j=0;j<17;j++){
            cur = arr[i][j] * arr[i][j+1] * arr[i][j+2] * arr[i][j+3];
            if(cur>max)  max = cur;
        }
    }

    //check down
    for(int i=0;i<17;i++){
        for(int j=0;j<20;j++){
            cur = arr[i][j] * arr[i+1][j] * arr[i+2][j] * arr[i+3][j];
            if(cur>max) max = cur;
        }
    }
    //check diagonal - LtoR
    for(int i=0;i<17;i++){
        for(int j=0;j<17;j++){
            cur = arr[i][j] * arr[i+1][j+1] * arr[i+2][j+2] * arr[i+3][j+3];
            if(cur>max) max = cur;
        }
    }

    //check diagonal - RtoL
    for(int i=3;i<20;i++){
        for(int j=0;j<17;j++){
            cur = arr[i][j] * arr[i-1][j+1] * arr[i-2][j+2] * arr[i-3][j+3];
            if(cur>max) max = cur;
        }
    }
    return max;
}
int main(){
    int arr[20][20];
    for(int i=0;i<20;i++){
        for(int j=0;j<20;j++){
            cin>>arr[i][j];
        }
    }
    cout<<maxProduct(arr);
    return 0;
}
