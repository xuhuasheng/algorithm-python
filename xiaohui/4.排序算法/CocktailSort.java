import java.util.Arrays;

public class CocktailSort {
    // 鸡尾酒排序：左右双向冒泡
    public static void cocktailSort(int[] arr) {
        // 外层大循环控制所有排序回合数 n/2
        for (int i = 0; i < arr.length/2; i++) {
            boolean isSorted = true;
            // 奇数轮： 从左往右冒泡 [i, n-1-i)
            for (int j = i; j < arr.length-1-i; j++) {
                if (arr[j] > arr[j+1]) {
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                    isSorted = false;
                }
            }
            if(isSorted) {
                break;
            }

            isSorted = true;
            // 偶数轮： 从右往左冒泡 [n-1-i, i)
            for (int j = arr.length-1-i; j > i; j--) {
                if (arr[j] < arr[j-1]) {
                    int temp = arr[j];
                    arr[j] = arr[j-1];
                    arr[j-1] = temp;
                    isSorted = false;
                }
            }
            if(isSorted) {
                break;
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = new int[] {2, 3, 4, 5, 6, 7, 8, 1};
        System.out.println(arr);
        cocktailSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}