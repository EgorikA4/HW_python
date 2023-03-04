#include<bits/stdc++.h>

using namespace std;

int main(){
    int n; cin >> n;
    double res = 1, fact_i = 1;
    for(int i = 1; i < n + 1; i++){
        fact_i *= i;
        res += 1 / fact_i;
    }
    cout << res;
}