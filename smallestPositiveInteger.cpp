#include <iostream>
#include <vector>
using namespace std;

int solution(vector<int> &A){
    int large = 0;
    int small;
    for(int i=0;i<A.size();i++){
        if(i>large)
            large = i;
    }
    for(int j=1; j<large;j++){
        if(A[j-1] == j){
            continue;
        }else{
            small = A[j-1];
            break;
        }
    }
    return small;
}

int main(){
    
}