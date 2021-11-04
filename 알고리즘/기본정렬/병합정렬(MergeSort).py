"""
병합정렬
- 배열을 쪼갠 후 병합하면서 정렬하는 방식
- 퀵소트는 피벗을 기준으로 정렬 후 다시 분할하는 방식
- 병합정렬을 배열을 쪼갤 수 있을 만큼 쪼갠 후 병합하면서 정렬하는 방식
- 순차비교로 정렬을 진행하므로 연결리스트의 정렬에 사용하면 효율적이다.
- 퀵소트로 연결리스트를 정렬하면 오버헤드 발생
- 시간복잡도: O(nlogn)
- 공간복잡도: 병합 결과를 저장할 배열이 추가로 필 O(n)

public static void mergeSort(int[] array, int left, int right) {
    if (left < right) {
        int mid = (left + right) / 2;

        mergeSort(array, left, mid);
        mergeSort(array, mid + 1, right);
        merge(array, left, mid, right);
    }
}

public static void merge(int[] array, int left, int mid, int right) {
    int[] L = Arrays.copyOfRange(array, left, mid + 1);
    int[] R = Arrays.copyOfRange(array, mid + 1, right + 1);

    int i = 0, j = 0, k = left;
    int ll = L.length, rl = R.length;

    while (i < ll && j < rl) {
        if (L[i] <= R[j]) {
            array[k] = L[i++];
        } else {
            array[k] = R[j++];
        }
        k++;
    }

    while (i < ll) {
        array[k++] = L[i++];
    }

    while (j < rl) {
        array[k++] = R[j++];
    }
}
"""
import random


def merge_sort(arr: list, left: int, right: int):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

def merge(arr: list, left: int, mid: int, right: int):
    l_arr = arr[left: mid + 1]
    r_arr = arr[mid + 1: right + 1]

    i = j = 0
    k = left

    while i < len(l_arr) and j < len(r_arr):
        if l_arr[i] <= r_arr[j]:
            arr[k] = l_arr[i]
            i += 1
        else:
            arr[k] = r_arr[j]
            j += 1

        k += 1

    while i < len(l_arr):
        arr[k] = l_arr[i]
        i += 1
        k += 1

    while j < len(r_arr):
        arr[k] = r_arr[j]
        j += 1
        k += 1

arr = list(range(1000))
random.shuffle(arr)
merge_sort(arr, 0, len(arr))
print(arr == sorted(arr))






















