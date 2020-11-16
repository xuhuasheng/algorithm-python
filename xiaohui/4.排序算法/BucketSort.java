import java.util.Collections;
import java.util.LinkedList;

public class BucketSort {
    public static double[] bucketSort(double[] arr) {
        // 1.得到最大值和最小值，计算极差
        double max = arr[0];
        double min = arr[0];
        for (int i=0; i<arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
            if (arr[i] < min) {
                min = arr[i];
            }
        }
        // 2.创建桶 桶的数量=元素的数量
        int bucketNum = arr.length;
        ArrayList<LinkedList<Double>> bucketList = new ArrayList<LinkedList<Double>>(bucketNum);
        for (int i=0; i<bucketNum; i++) {
            bucketList.add(new LinkedList<Double>());
        }
        // 3.遍历原始数组，将每个元素放入桶中
        // 除最后一个桶只包含max外，前面的各个桶的区间=(max-min)/(桶的数量-1)
        for (int i=0; i<arr.length; i++) {
            int bucketIndex = (int)((arr[i]-min) * (bucketNum-1) / d);
            bucketList.get(bucketIndex).add(array[i]);
        }
        // 4.对每个桶内部进行排序 o(nlogn)
        for (int i=0; i<bucketList.size(); i++) {
            Collections.sort(bucketList.get(i));
        }
        // 5.输出全部元素
        double[] sortedArray = new double[arr.length];
        int index = 0;
        for (LinkedList<Double> list : bucketList) {
            for (double element : list) {
                sortedArray[index] = element;
                index++;
            }
        } 
        return sortedArray;
    }
    public static void main(String[] args) {
        double[] arr = new double[] {4.12,6.421,0.0023,3.0,2.123,8.123,4.12,10.09};
        double[] sortedArray = bucketSort(arr);
        System.out.println(sortedArray);
    }
}