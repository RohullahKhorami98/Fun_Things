#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n,q; 
    cin >> n >> q;
    std::vector<std::vector<int>> vectors(n);
    for(int i = 0; i<n; i++){
        int k;
        cin >> k;
        vectors[i].resize(k); //resizing the inner arrays
        for(int j = 0; j<k; j++){
            cin >> vectors[i][j];
        }
    }
    for(int i = 0; i<q; i++){
        int a,b;
        cin >> a >> b;
        std::cout<<vectors[a][b]<<endl;
    }
    return 0;
}