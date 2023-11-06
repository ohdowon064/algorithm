"""
거품정렬
- 서로 인접한 원소를 비교하고, 조건에 맞지않으면 자리 교환
- 시간복잡도: O(n^2)이며 스왑연산이 많아 비효율적이다.
- 공간복잡도: 주어진 배열안에서 교환하므로 O(1)

자바코드
void bubbleSort(int[] arr) {
    int temp = 0;
	for(int i = 0; i < arr.length; i++) {       // 1.
		for(int j= 1 ; j < arr.length-i; j++) { // 2.
			if(arr[j-1] > arr[j]) {             // 3.
                // swap(arr[j-1], arr[j])
				temp = arr[j-1];
				arr[j-1] = arr[j];
				arr[j] = temp;
			}
		}
	}
	System.out.println(Arrays.toString(arr));
}
"""
import timeit


def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

def bubble_sort2(arr: list):
    for i in range(n := len(arr)):
        for j in range(1, n - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]

print(timeit.timeit("bubble_sort(arr)",
                    setup=
                    """from __main__ import bubble_sort;import random;arr = [random.randint(1, 1000) for _ in range(1000)]""",
                    number=10000))

print(timeit.timeit("bubble_sort2(arr)",
                    setup=
                    """from __main__ import bubble_sort2;import random;arr = [random.randint(1, 1000) for _ in range(1000)]""",
                    number=10000))