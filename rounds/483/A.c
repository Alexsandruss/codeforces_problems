// Conditions - http://codeforces.com/contest/984/problem/A
#include <stdio.h>
int main() {
    int n;
    scanf("%d", &n);
    int array[n];
    for (int i = 0; i < n; i++){
        scanf("%d", (array+i));
    }
    int temp;
    for (int j = 0; j < n; j++){
        for (int k = 0; k < n-1; k++){
            if (array[k] > array[k+1]){
                temp = array[k];
                array[k] = array[k+1];
                array[k+1] = temp;
            }
        }
    }
    if (n % 2 == 1){
        printf("%d", array[(n-1)/2]);
    } else {
        printf("%d", array[n/2-1]);
    }
    return 0;
}
// all tests passed - http://codeforces.com/contest/984/submission/38354404