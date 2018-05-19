// Conditions - http://codeforces.com/contest/919/problem/A
#include <stdio.h>
int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    float costs[n];
    int a, b;
    for (int i = 0; i < n; i++){
        scanf("%d %d", &a, &b);
        costs[i] = (float)a/b;
    }
    float min = 10000;
    for (int i = 0; i < n; i++){
        if (costs[i] < min){min = costs[i];}
    }
    printf("%f", min*m);
    return 0;
}
// all tests passed - http://codeforces.com/contest/919/submission/38441383