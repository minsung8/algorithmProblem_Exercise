package sist6;

import java.util.Arrays;
import java.util.Scanner;

public class Boj3 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] dp = new int[num];
		int[][] arr = new int[num][2];
		
		for (int i=0; i<num; i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = sc.nextInt();
		}
			
		for (int i=0; i<num; i++) {
			for (int j=i+1; j<num; j++) {
				if (arr[i][0] > arr[j][0]) {
					int[] temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		System.out.println(Arrays.toString(arr));
		dp[0] = 1;
		for (int i=1; i<num; i++) {
			dp[i] = 1;
			for (int j=0; j<i; j++) {
				if (arr[i][1] > arr[j][1]) {
					dp[i] = Math.max(dp[j] + 1, dp[i]);
				}
			}
		}
		
		int answer = 0;
		for (int i=0; i<num; i++) {
			if (dp[i] > answer) {
				answer = dp[i];
			}
		}
		System.out.println(num - answer);
	}
}
