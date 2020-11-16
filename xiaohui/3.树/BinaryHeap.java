import java.util.Arrays;

// 二叉堆
public class BinaryHeap {
    // 最小堆的上浮
    public static void upAdjust(int[] array) {
        int childIndex = array.length-1;
        int parentIndex = (childIndex-1)/2;

        int temp = array[childIndex];
        while (childIndex>0 && temp<array[parentIndex]) {
            array[childIndex] = array[parentIndex];
            childIndex = parentIndex;
            parentIndex = (childIndex-1)/2;
        }
        array[childIndex] = temp;        
    }

    // 最小堆的下沉
    public static void downAdjust(int[] array, int parentIndex, int length) {
        int temp = array[parentIndex];
        int childIndex = 2*parentIndex +1;
        while (childIndex < length) {
            if (childIndex+1 < length && array[childIndex+1] < array[childIndex]) {
                childIndex++;
            }
            if (temp <= array[childIndex])
                break;
            array[parentIndex] = array[childIndex];
            parentIndex = childIndex;
            childIndex = 2*parentIndex + 1;
        }
        array[parentIndex] = temp;
    }

    // 构建最小/最大堆
    public static void buildHeap(int[] array) {
        // 从最后一个非叶子节点开始，依次做下沉
        for (int i=(array.length-1 - 1)/2; i>=0; i--) {
            downAdjust(array, i, array.length);
        }
    }

    public static void main(String[] args) {
        int[] array = new int[] {1,3,2,6,5,7,8,9,10,0};
        upAdjust(array);
        System.out.println(Arrays.toString(array));

        array = new int[] {7,1,3,10,5,2,8,9,6};
        buildHeap(array);
        System.out.println(Arrays.toString(array));
    }
}