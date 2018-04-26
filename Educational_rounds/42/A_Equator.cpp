// Conditions - http://codeforces.com/contest/962/problem/A
#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    int summary = 0;
    for (int i = 0; i < n; i++){
        summary += a[i];
    }
    float half = (float)summary/2;
    float sum = 0.000;
    int day;
    for (int i = 0; i < n; i++){
        sum += float(a[i]);
        if (sum >= half){
            day = i+1;
            break;
        }
    }
    cout << day;
    return 0;
}
/*
All tests passed
Time: 265 ms
Memory: 4340 KB
http://codeforces.com/contest/962/submission/37483600
*/