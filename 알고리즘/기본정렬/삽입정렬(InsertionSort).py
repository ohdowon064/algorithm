"""
삽입정렬
- 2번째 원소를 앞 원소들과 비교하여 삽입할 위치를 지정한 후 원소를 뒤로 옮기고 지정된 자리에 원소를 삽입
- 시간복잡도: 최선(이미정렬됨)의 경우 O(n), 평균/최악 O(n^2)
- 공간복잡도: 해당 배열 안에서 교환하므로 O(1)

자바코드
void insertionSort(int[] arr)
{
   for(int index = 1 ; index < arr.length ; index++){ // 1.
      int temp = arr[index];
      int prev = index - 1;
      while( (prev >= 0) && (arr[prev] > temp) ) {    // 2.
         arr[prev+1] = arr[prev];
         prev--;
      }
      arr[prev + 1] = temp;                           // 3.
   }
   System.out.println(Arrays.toString(arr));
}
"""
import random


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        temp = arr[i]
        prev = i - 1

        while prev >= 0 and arr[prev] > temp:
            arr[prev + 1] = arr[prev]
            prev -= 1

        arr[prev + 1] = temp

arr = list(range(100))
random.shuffle(arr)
print(arr)
insertion_sort(arr)
print(arr)
