import java.util.Arrays;

// 计数排序：基于数组下标和频数统计（线性时间复杂度）
// 原始数组规模为n，极差为m
// 时间复杂度：o(3n+m) => o(n+m)
// 空间复杂度：o(m+1) => o(m)
// 局限性：1.不适合极值差m过大的
//        2.待排序列是存在小数的，无法建立统计数组
public class CountSort {
    public static int[] countSort(int[] arr) {
        // 1.遍历原始数组o(n)，求最大值和最小值，计算差值
        int max = arr[0];
        int min = arr[0];
        for (int i=0; i<arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        int d = max-min;
        // 2.建立统计数组o(m+1)，遍历原始数组o(n)，统计元素频数
        int[] countArray = new int[d+1];
        for (int i=0; i<arr.length; i++) {
            countArray[arr[i]-min]++;
        }
        // 3.对统计数组做变形，从第二个元素开始遍历o(m)，累加前面的频数
        for (int i = 1; i < countArray.length; i++) {
            countArray[i] += countArray[i-1];
        }
        // 4.倒序遍历原始数组o(n)，从变形后的统计数组中找到排位，填入结果数组(索引=排位-1), 统计数组对应的频数自减一
        int[] sortedArray = new int[arr.length];
        for (int i = arr.length-1; i >= 0; i--) {
            sortedArray[countArray[arr[i]-min]-1] = arr[i];
            countArray[arr[i]-min]--;
        }
        return sortedArray;
    }
    public static void main(String[] args) {
        int[] arr = new int[] {95,84,91,98,99,90,99,93,91,92};
        System.out.println(Arrays.toString(arr));
        int[] sortedArray = countSort(arr);
        System.out.println(Arrays.toString(sortedArray));
    }
}