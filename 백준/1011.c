#include <stdio.h>
#include <math.h>

int T = 0;
int x, y, length, mid = 0;
int moveCount = 0;

int main(void) {
    scanf("%d", &T);
    for(int i = 0; i < T; i++) {
        scanf("%d %d", &x, &y);
        length = y - x;
        mid = sqrt(length); // 1. 제곱근 계산

        if (pow(mid, 2) == length) {
            moveCount = 2 * mid - 1;
        }else {
            moveCount = 2 * mid;
        }

        if(length > mid * (mid + 1)) {
            moveCount += 1;
        }

        printf("%d\n", moveCount);
    }
}