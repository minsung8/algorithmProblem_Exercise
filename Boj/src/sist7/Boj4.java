package sist7;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Boj4 {
	
	static int[][] check = new int[1001][1001];
	static boolean[] checked = new boolean[1001];
	static int n;
	static int m;
	static int start;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		start = sc.nextInt();
		
		for (int i=1; i<=m; i++) {
			int x = sc.nextInt();
			int y = sc.nextInt();
			
			check[x][y] = check[y][x] = 1;
		}
		dfs(start);
		checked = new boolean[1001];
		System.out.println();
		bfs();
	}
	
	public static void dfs(int i) {
		checked[i] = true;
		System.out.print(i + " ");
		
		for (int j=1; j<=n; j++) {
			if (check[i][j] == 1 && checked[j] == false) {
				dfs(j);
			}
		}
	}
	
	public static void bfs() {
		
		Queue<Integer> queue = new LinkedList<Integer>();
		System.out.print(start + " ");
		queue.offer(start);
		checked[start] = true;
		
		while (!queue.isEmpty()) {
			int temp = queue.poll();
			
			for (int j=1; j<=n; j++) {
				if (check[temp][j] == 1 && checked[j] == false) {
					queue.offer(j);
					checked[j] = true;
					System.out.print(j + " ");
				}
			}
		}	
	}
}