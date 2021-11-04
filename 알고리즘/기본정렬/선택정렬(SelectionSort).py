"""
선택정렬
- 특정 위치(제일 앞)에 어떤 원소를 넣을지 선택하는 알고리즘
- 시간복잡도: O(n^2)
- 공간복잡도: 주어진 배열안에서 교환하므로 O(1)

void selectionSort(int[] arr) {
    int indexMin, temp;
    for (int i = 0; i < arr.length-1; i++) {        // 1.
        indexMin = i;
        for (int j = i + 1; j < arr.length; j++) {  // 2.
            if (arr[j] < arr[indexMin]) {           // 3.
                indexMin = j;
            }
        }
        // 4. swap(arr[indexMin], arr[i])
        temp = arr[indexMin];
        arr[indexMin] = arr[i];
        arr[i] = temp;
  }
  System.out.println(Arrays.toString(arr));
}
"""
import random


def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]


def get_random_array():
    arr = list(range(1000))
    random.shuffle(arr)
    return arr


import timeit

print(timeit.timeit(stmt="selection_sort(arr)",
                    setup="""from __main__ import selection_sort, get_random_array;arr = get_random_array();""",
                    number=500))

print(timeit.timeit(stmt="bubble_sort(arr)",
                    setup="""from __main__ import bubble_sort, get_random_array;arr = get_random_array();""",
                    number=500))
