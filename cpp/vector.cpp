#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    std::vector<int> numbers;
    int n; 
    int q;
    cin >> n;
    cin >> q;
    //numbers.push_back(n);
    //numbers.push_back(q);
    for(int i = 0; i<n; i++){
        int temp;
        cin >> temp;
        numbers.push_back(temp);
    }
    for(int j = 0; j<numbers.size(); j++){
        std::cout<<numbers.at(j)<<std::endl;
    }

    return 0;
}