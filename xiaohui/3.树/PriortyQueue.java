import java.util.Arrays;

//最大优先队列-最大堆实现
public class PriortyQueue {
    private int size;
    private int[] array;

    public PriortyQueue() {
        // 队列初始长度32
        this.array = new int[32];
        this.size = 0;
    }

    // 入队-上浮
    public void enQueue(int key) {
        if (this.size >= array.length) {
            resize();
        }
        array[this.size] = key;
        this.size++;
        upAdjust(array);
    }

    // 出队-下沉
    public int deQueue() throws Exception {
        if (this.size <= 0) {
            throw new Exception("the queue is empty");
        }
        int head = array[0];
        array[0] = array[--this.size];
        downAdjust(array, 0);
        return head;
    }

    // 最大堆上浮调整
    public void upAdjust(int[] arr) {
        int childIndex = this.size - 1;
        int parentIndex = (childIndex - 1)/2;
        int temp = arr[childIndex];
        while (childIndex > 0 && temp > arr[parentIndex]) { //只有没有浮到头 且 能够浮
            // 向下单向赋值
            arr[childIndex] = arr[parentIndex];
            childIndex = parentIndex;
            parentIndex = (childIndex-1)/2;
        }
        arr[childIndex] = temp;
        // while (childIndex > 0 && arr[childIndex] > arr[parentIndex]) {
        //     // 上浮过程层层交换
        //     int tmp = arr[childIndex];
        //     arr[childIndex] = arr[parentIndex];
        //     arr[parentIndex] = tmp;
        //     childIndex = parentIndex;
        //     parentIndex = (childIndex-1)/2;
        // }
    }

    // 最大堆下沉调整
    public void downAdjust(int[] arr, int parentIndex) {
        int temp = arr[parentIndex]; //下沉的元素
        int childIndex = parentIndex*2 + 1; //暂定左孩子
        while (childIndex < this.size) {   //只要没有沉底
            if (childIndex + 1 < arr.length && arr[childIndex+1] > arr[childIndex]) {//“与”的短路原则保证不溢出
                // 如果右孩子存在 且 右孩子比左孩子大 则 切换为右孩子
                childIndex++;
            }
            // 如果父节点比子节点最大的还大 直接跳出
            if (temp >= arr[childIndex]) {
                break;
            }
            arr[parentIndex] = arr[childIndex];
            parentIndex = childIndex;
            childIndex = parentIndex*2+1;
        }
        arr[parentIndex] = temp;
    }
    // 队列扩容
    public void resize() {
        int newzSize = this.size * 2;
        this.array = Arrays.copyOf(this.array, newzSize);
    }
    public static void main(String[] args) throws Exception {
        PriortyQueue priortyQueue = new PriortyQueue();
        priortyQueue.enQueue(3);
        priortyQueue.enQueue(5);
        priortyQueue.enQueue(10);
        priortyQueue.enQueue(2);
        priortyQueue.enQueue(7);
        System.out.println("出队元素：" + priortyQueue.deQueue());
        System.out.println("出队元素：" + priortyQueue.deQueue());
    }
}