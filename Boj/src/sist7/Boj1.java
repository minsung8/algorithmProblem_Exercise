package sist7;

import java.util.Arrays;
import java.util.Scanner;

public class Boj1 {
	
	private static int[][] arr;
	private static int white = 0; 
	private static int blue = 0; 

	public static void main(String[] args) throws Exception{

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		arr = new int[n][n];
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				arr[i][j] = sc.nextInt();
			}
		}

		dfs(0, 0, n);
		System.out.println(white);
		System.out.println(blue);
		
	}
		
	private static void dfs(int x, int y, int n) {
		if (n == 1) {
			 if (arr[y][x] == 1) {
				 blue += 1;
			 } else {
				 white += 1;
			 }
			 return;
		}
		int temp_white = 0;
		int temp_blue = 0;
		
		for (int i=0; i<n; i++) {
			for (int j=0; j<n; j++) {
				
				if (arr[i + y][j + x] == 1) {
					temp_blue += 1;
				} else {
					temp_white += 1;
				}
				
				if ((temp_white * temp_blue) != 0) {
					int temp = n / 2;
					dfs(x, y, temp);
					dfs(x + temp, y, temp);
					dfs(x, y + temp, temp);
					dfs(x + temp, y + temp, temp);
					return;
				}
			}
		}
		if (temp_white == 0) {
			blue += 1;
		} else {
			white += 1;
		}
		return;
	} 
}	