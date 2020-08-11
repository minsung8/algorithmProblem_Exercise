package sist8;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj1 {

	public static void main(String[] args) throws Exception {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int i, n = Integer.parseInt(br.readLine());
		Tree t = new Tree();
		
		char[] data;
		
		for (i=0; i<n; i++) {
			data = br.readLine().replaceAll(" ", "").toCharArray();
			t.add(data[0], data[1], data[2]);
		}
		
		t.preorder(t.root);
		System.out.println();
		t.inorder(t.root);
		System.out.println();
		t.postorder(t.root);
		br.close();
	}
}

class Node {
	
	char data;
	Node left, right;
	
	public Node(char data) {
		this.data = data;
	}
	
}

class Tree {
	
	Node root;
	
	public void add(char data, char leftdata, char rightdata) {
		
		if (root == null) {
			if (data != '.') root = new Node(data);
			if (leftdata != '.') root.left = new Node(leftdata);
			if (rightdata != '.') root.right = new Node(rightdata);
		} else search(root, data, leftdata, rightdata);
	}
	
	public void search(Node root, char data, char leftdata, char rightdata) {
		if (root == null) return;
		
		else if (root.data == data) {
			if (leftdata != '.') root.left = new Node(leftdata);
			if (rightdata != '.') root.right = new Node(rightdata);
		} else {
			search(root.left, data, leftdata, rightdata);
			search(root.right, data, leftdata, rightdata);
		}
	}
		
	public void preorder(Node root) {				// 전위순회
		System.out.print(root.data);
		if (root.left != null) preorder(root.left);
		if (root.right != null) preorder(root.right);
	}
	
	public void inorder(Node root) {				// 중위순회
		if (root.left != null) inorder(root.left);
		System.out.print(root.data);
		if (root.right != null) inorder(root.right);
	}
	
	public void postorder(Node root) {				// 후위순회
		if (root.left != null) postorder(root.left);
		if (root.right != null) postorder(root.right);
		System.out.print(root.data);
	}
}