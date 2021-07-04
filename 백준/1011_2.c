#include <stdio.h>
#include <math.h>

// sqrt -> 제곱근, pow -> 제곱
// 1. 제곱수 일 때 최대이동거리 + 1
// 2. 두 제곱수 중간값 지날 때 이동횟수 + 1
// 3. 제곱수 다음 수도 이동회수 + 1
// 	제곱수 -> 제곱근 * 2 - 1
// 4. 중간값 이전 값 -> 3.xx * 2 = int(6.xx) => 6
// 5. 중간값 이후 값 -> 제곱근 * 2 + 1
// 	제곱근 * 제곱근 + 제곱근 = 제곱근 * (제곱근 + 1)

int T = 0;
int x, y, length, mid = 0;
int moveCount = 0;

int main() {
    scanf("%d", &T);

    int i = 0;
    for(; i < T; i++) {
        scanf("%d %d", &x, &y);
        length = y - x;
        mid = sqrt(length);

        if(pow(mid, 2) == length) { // 제곱수인 경우
            moveCount = mid * 2 - 1;
        }else { // 제곱수가 아닌 경우
            moveCount = 2 * mid;
        }

        // 중간값 이후값인 경우
        if(length > mid * (mid + 1)) {
            moveCount += 1;
        }

        printf("%d\n", moveCount);
    }

    return 0;
}