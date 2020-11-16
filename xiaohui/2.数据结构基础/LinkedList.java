
public class LinkedList {
    private Node head;
    private Node last;
    private int size;

    private static class Node {
        int data;
        Node next;
        Node(int data) {
            this.data = data;
        }
    }

    public Node getNode(int index) throws Exception {
        if (index<0 || index>=size-1) {
            throw new IndexOutOfBoundsException();
        }
        Node temp = head;
        for (int i=0; i<=index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    public void insert(int data, int index) throws Exception{
        if (index<0 || index>size) {
            throw new IndexOutOfBoundsException();
        }
        Node insertedNode = new Node(data);
        if (size == 0) {
            head = insertedNode;
            insertedNode.next = null;
        } else if (index == 0) {
            insertedNode.next = head;
            head = insertedNode;
        } else if (index == size) {
            last.next = insertedNode;
            insertedNode.next = null;
        } else {
            Node prevNode = getNode(index-1);
            insertedNode.next = prevNode.next;
            prevNode.next = insertedNode;
        }
        size++;
    }

    public Node remove(int index) throws Exception {
        if (index<0 || index>size) {
            throw new IndexOutOfBoundsException();
        }
        Node removedNode = null;
        if (index == 0) {
            removedNode = head;
            head = head.next;
        } else if (index == size-1) {
            Node prevNode = getNode(index-1);
            removedNode = last;
            last = prevNode;
            prevNode.next = null;
        } else {
            Node prevNode = getNode(index-1);
            removedNode = prevNode.next;
            prevNode.next = removedNode.next;
        }
        size--;
        return removedNode;
    }

    public void output() {
        Node temp = head;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }
}