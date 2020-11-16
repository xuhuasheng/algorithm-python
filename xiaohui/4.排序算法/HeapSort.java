import java.util.Arrays;

public class HeapSort {
    // 最大堆的下沉
    public static void downAdjust(int[] array, int parentIndex, int length) {
        int temp = array[parentIndex];
        int childIndex = 2*parentIndex + 1;
        while (childIndex < length) {
            if (childIndex+1 < length && array[childIndex+1] > array[childIndex]) {
                childIndex++;
            }
            if (temp >= array[childIndex])
                break;
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2*parentIndex + 1;
        }
        array[parentIndex] = temp;
    }
    public static void heapSort(int[] arr) {
        for (int i=(arr.length-1-1)/2; i>=0; i--) {
            downAdjust(arr, i, arr.length);
        }
        System.out.println(Arrays.toString(arr));
        for (int i=arr.length-1; i>0; i--) {
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;
            downAdjust(arr, 0, i);
        }
    }
    public static void main(String[] args) {
        int[] arr = new int[] {1,3,2,6,5,7,8,9,10,0};
        heapSort(arr);
        System.out.print(Arrays.toString(arr));
    }
}