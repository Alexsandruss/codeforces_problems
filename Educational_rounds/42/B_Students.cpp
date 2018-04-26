// Conditions - http://codeforces.com/contest/962/problem/B
#include <iostream>
#include <string>
using namespace std;
int main() {
    int n, a, b;
    string car;
    cin >> n >> a >> b >> car;
    int count = 0;
    string previous = "j";
    for (int i = 0; i < car.length(); i++) {
        if (a <= 0 and b <= 0) {
            break;
        }
        if (previous == "j") {
            if (a > b) {
                previous = "s";
            } else {
                previous = "p";
            }
        }
        if (car[i] == '*') {
            previous = "j";
        } else {
            if (previous == "p") {
                if (b > 0) {
                    count++;
                }
                previous = "s";
                b--;
            } else {
                if (a > 0) {
                    count++;
                }
                previous = "p";
                a--;
            }
        }
    }
    cout << count;
    return 0;
}
/*
All tests passed
Time: 61 ms
Memory: 3824 KB
http://codeforces.com/contest/962/submission/37485348
*/