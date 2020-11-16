import java.util.Queue;
import java.util.LinkedList;
import java.util.Arrays;

public class BreadthFirstSearch {
    // 二叉树
    private static class TreeNode {
        int data;
        TreeNode leftChild;
        TreeNode rightChild;

        TreeNode(int data) {
            this.data = data;
        }

    }

    // 从线性的链表（前序遍历格式）创建二叉树（非线性的链表）
    public static TreeNode creatBianryTree(LinkedList<Integer> inputList) {
        TreeNode node = null;
        if (inputList==null || inputList.isEmpty()) {
            return null;
        }
        Integer data = inputList.removeFirst();
        if (data != null) {
            node = new TreeNode(data);
            node.leftChild = creatBianryTree(inputList);
            node.rightChild = creatBianryTree(inputList);
        }
        return node;
    }

    // 队列实现层序遍历
    public static void levelOrderTraversal(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            System.out.println(node.data);
            if (node.leftChild != null) {
                queue.offer(node.leftChild);
            }
            if (node.rightChild != null) {
                queue.offer(node.rightChild);
            }
        }
    }

    public static void main(String[] args) {
        LinkedList<Integer> inputList = new LinkedList<Integer>(Arrays.asList(new Integer[] {3,2,9,null,null,10,null,null,8,null,4}));
        TreeNode treeNode = creatBianryTree(inputList);
        System.out.println("层序遍历：");
        levelOrderTraversal(treeNode);      
    }
    
}