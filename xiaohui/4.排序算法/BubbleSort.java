import java.util.Arrays;

public class BubbleSort {
    // 基本
    public static void bubbleSort_v1(int[] arr) {
        // 外层循环 i= 0 : n-1 控制回合轮数n-1 
        for (int i = 0; i < arr.length-1; i++) {
            // 内层循环 j= 0 : n-1-i 控制冒泡轮数n-1-i
            for (int j = 0; j< arr.length-1-i; j++) {
                if (arr[j] > arr [j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
    // 优化1 针对剩下序列已经是有序 则提前结束排序
    public static void bubbleSort_v2(int[] arr) {
        for (int i = 0; i < arr.length-1; i++) {
            // 有序标记 每一轮的初始值都是true
            boolean isSorted = true;
            for (int j = 0; j< arr.length-1-i; j++) {
                if (arr[j] > arr [j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    // 若有交换操作 则说明这一轮排序前是无序的
                    isSorted = false;
                }
            }
            if (isSorted) {
                // 说明这一轮没有交换操作 即这一轮排序之前已经是有序的
                // 提前结束大循环 不再下一轮冒泡排序
                break;
            }
        }
    }
    // 优化2 针对序列右侧已为有序时 减少不必要的冒泡操作
    public static void bubbleSort_v3(int[] arr) {
        // 每一轮冒泡排序的边界 也是前一轮最后一次交换的位置
        int sortBorder = arr.length - 1;
        for (int i = 0; i < arr.length-1; i++) {
            // 有序标记 每一轮的初始值都是true
            boolean isSorted = true;
            for (int j = 0; j< sortBorder; j++) {
                if (arr[j] > arr [j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    // 若有交换操作 则说明这一轮排序前是无序的
                    isSorted = false;
                    // 更新最后一次交换的位置
                    sortBorder = j;
                }
            }
            if (isSorted) {
                // 说明这一轮没有交换操作 即这一轮排序之前已经是有序的
                // 提前结束大循环 不再下一轮冒泡排序
                break;
            }
        }
    }
    public static void main(String[] args) {
        int[] arr = new int[] {3, 4, 2, 1, 5, 6, 7, 8};
        bubbleSort_v1(arr);
        bubbleSort_v2(arr);
        bubbleSort_v3(arr);
        System.out.println(Arrays.toString(arr));
    }
}