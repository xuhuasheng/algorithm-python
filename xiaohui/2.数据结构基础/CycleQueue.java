public class CycleQueue {
    private final int[] array = new int[] {};
    private int front = 0;
    private int rear = 0;

    public MyQueue(final int capacity) {
        this.array = new int[capacity];
    }

    public void enQueue(final int element)  {
        if ((rear + 1) % array.length == front) {
            System.out.println("队列已满");
        }
        array[rear] = element;
        rear = (rear + 1) % array.length;
    }

    public int deQueue() {
        if (front == rear) {
            System.out.println("队列已空");
        }
        final int deQueueElement = array[front];
        front = (front + 1) % array.length;
        return deQueueElement;
    }

    public void output() {
        for (int i = front; i != rear; i = (i + 1) % array.length) {
            System.out.println(array[i]);
        }
    }

    public static void main(final String[] args) {
        final MyQueue myQueue = new MyQueue(6);
        myQueue.enQueue(3);
        myQueue.enQueue(4);
        myQueue.enQueue(5);
        myQueue.enQueue(8);
        myQueue.deQueue();
        myQueue.deQueue();
        myQueue.output();
    }
}