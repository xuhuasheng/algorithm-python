import java.util.Arrays;

public class SelectSort {
    // 基本
    public static void selectSort(int[] arr) {
        // 外层循环 i= 0 : n-1 控制回合轮数n-1 
        for (int i = 0; i < arr.length-1; i++) {
            // 内层循环 j= 0 : n-1-i 控制冒泡轮数n-1-i
            for (int j = i+1; j< arr.length; j++) {
                if (arr[j] > arr [j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    public static void main(String[] args) {
        int[] arr = new int[] {3, 4, 2, 1, 5, 6, 7, 8};
        System.out.println(Arrays.toString(arr));
        selectSort(arr);
        System.out.println(Arrays.toString(arr));
    }
)