// 백준 15650번 문제

package sist4;

import java.util.Scanner;

public class Boj1 {
	
	static int n, m;
	static int[] list, check;
	
	public static void dfs(int idx, int cnt) {
		
		if (cnt == m) {
			for (int i=0; i<m; i++) {
				System.out.print(list[i] + " ");
			}
			System.out.println();
			return;
		}
		
		for (int i=idx+1; i<=n; i++) {
			if (check[i] == 1) break;
			check[i] = 1;
			list[cnt] = i;
			dfs(i, cnt + 1);
			check[i] = 0;
		}	
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		n = sc.nextInt();
		m = sc.nextInt();
		
		list = new int[9];
		check = new int[9];
		
		dfs(0, 0);
		
		sc.close();	
	}
}
