import java.util.LinkedList;
import java.util.Arrays;
import java.util.Stack;

// 二叉树深度优先搜索（递归实现）
public class DepthFirstSearch {
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
    // 前序遍历：根节点，左孩子，右孩子
    public static void preOrderTraveral(TreeNode node) {
        if (node==null) return;
        System.out.println(node.data);
        preOrderTraveral(node.leftChild);
        preOrderTraveral(node.rightChild);
    }

    // 中序遍历：左孩子，根节点，右孩子
    public static void inOrderTraveral(TreeNode node) {
        if (node==null) return;
        inOrderTraveral(node.leftChild);
        System.out.println(node.data);
        inOrderTraveral(node.rightChild);
    }

    // 后续遍历：左孩子，右孩子，根节点
    public static void postOrderTraveral(TreeNode node) {
        if (node==null) return;
        postOrderTraveral(node.leftChild);
        postOrderTraveral(node.rightChild);
        System.out.println(node.data);
    }

    // 用栈实现前序遍历
    public static void preOrderTraveralWithStack(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode treeNode = root;
        while (treeNode!=null || !stack.isEmpty()) {
            while (treeNode != null) {
                System.out.println(treeNode.data);
                stack.push(treeNode);
                treeNode = treeNode.leftChild;
            }
            if (!stack.isEmpty()) {
                treeNode = stack.pop();
                treeNode = treeNode.rightChild;
            }
        }
    }



    public static void main(String[] args) {
        LinkedList<Integer> inputList = new LinkedList<Integer>(Arrays.asList(new Integer[] {3,2,9,null,null,10,null,null,8,null,4}));
        TreeNode treeNode = creatBianryTree(inputList);
        System.out.println("前序遍历：");
        preOrderTraveral(treeNode);
        System.out.println("中序遍历：");
        inOrderTraveral(treeNode);
        System.out.println("后序遍历：");
        postOrderTraveral(treeNode);
    }
        
        
}