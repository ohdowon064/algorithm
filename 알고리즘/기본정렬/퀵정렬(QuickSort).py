"""
퀵정렬
- 피벗을 기준값으로 좌측에 작은 값, 우측에 큰 값으로 원소들을 분할하고 분할된 배열에 대해 재귀적으로 반복한다.
- 시간복잡도: O(nlogn), 최악(이미정렬)의 경우 O(n^2)
- 공간복잡도: 주어진 배열안에서 수행하므로 O(n)

자바코드
정복
public void quickSort(int[] array, int left, int right) {
    if(left >= right) return;

    // 분할
    int pivot = partition();

    // 피벗은 제외한 2개의 부분 배열을 대상으로 순환 호출
    quickSort(array, left, pivot-1);  // 정복(Conquer)
    quickSort(array, pivot+1, right); // 정복(Conquer)
}

정복
public int partition(int[] array, int left, int right) {
    /**
    // 최악의 경우, 개선 방법
    int mid = (left + right) / 2;
    swap(array, left, mid);
    */

    int pivot = array[left]; // 가장 왼쪽값을 피벗으로 설정
    int i = left, j = right;

    while(i < j) {
        while(pivot < array[j]) {
            j--;
        }
        while(i < j && pivot >= array[i]){
            i++;
        }
        swap(array, i, j);
    }
    array[left] = array[i];
    array[i] = pivot;

    return i;
}
"""
import random
import time
from timeit import timeit


def quick_sort(arr: list, left: int, right: int):
    if left >= right: return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


def partition(arr: list, left: int, right: int):
    # 최악의 경우 개선 방법
    # mid = (left + right) // 2
    # arr[left], arr[mid] = arr[mid], arr[left]
    pivot = arr[left]
    i, j = left, right

    while i < j:
        while pivot < arr[j]:
            j -= 1
        while i < j and pivot >= arr[i]:
            i += 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[left] = arr[i]
    arr[i] = pivot

    return i

arr = [random.randint(1, 100) for _ in range(1000)]
print(arr)
quick_sort(arr, 0, 999)
print(arr)
# print(f"""{timeit(stmt="all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))",
#        setup="from __main__ import arr",
#        number=1):.6f}""")
# print(f"""{timeit(stmt="arr == sorted(arr)",
#        setup="from __main__ import arr",
#        number=1):.6f}""")
# print(f"""{timeit(stmt="all(x <= y for x, y in zip(arr[:-1], arr[1:]))",
#        setup="from __main__ import arr",
#        number=1):.6f}""")

t1 = time.time()
print(all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1)))
t2 = time.time()
print(f"{t2 - t1:.7f}")

t1 = time.time()
print(all(x <= y for x, y in zip(arr[:-1], arr[1:])))
t2 = time.time()
print(f"{t2 - t1:.7f}")

t1 = time.time()
print(arr == sorted(arr))
t2 = time.time()
print(f"{t2 - t1:.7f}")