// Conditions - http://codeforces.com/contest/984/problem/B
#include <stdio.h>
int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    char field[n][m];
    for (int i = 0; i < n; i++){
        scanf("%s", field[i]);
    }
    int correct = 1;
    int count = 0;
    int input_count = 0;
    for (int y = 0; y < n; y++){
        for (int x = 0; x < m; x++){
            if (field[y][x] == '*'){continue;}
            count = 0;
            for (int dy = -1; dy <= 1; dy++){
                for (int dx = -1; dx <= 1; dx++){
                    if (x+dx < 0 || x+dx > m-1 || y+dy < 0 || y+dy > n-1 || (dy == 0 && dx == 0)){continue;}
                    if (field[y+dy][x+dx] == '*'){count++;}
                }
            }
            switch (field[y][x]){
                case '.': input_count = 0; break;
                case '1': input_count = 1; break;
                case '2': input_count = 2; break;
                case '3': input_count = 3; break;
                case '4': input_count = 4; break;
                case '5': input_count = 5; break;
                case '6': input_count = 6; break;
                case '7': input_count = 7; break;
                case '8': input_count = 8; break;
            }
            if (count != input_count){correct = 0;break;}
        }
        if (correct == 0){break;}
    }
    if (correct == 1){printf("YES");}
    else {printf("NO");}
    return 0;
}
// all tests passed - http://codeforces.com/contest/984/submission/38406594