package sist3;

import java.util.Scanner;

public class Boj1 {
	
	static int n, m;
	static int[] list, visited;
	
	public static void dfs(int cnt) {
		
		if (cnt==m) {
			for (int i=0; i<m; i++) {
				System.out.print(list[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i=1; i<=n; i++) {
			if (visited[i] == 1) continue;
			
			visited[i] = 1;
			list[cnt] = i;
			dfs(cnt + 1);
			visited[i] = 0;
		}
		
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		list = new int[9];
		visited = new int[9];
		
		dfs(0);
		
	}

}	