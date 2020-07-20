package sist5;

import java.util.Arrays;
import java.util.Scanner;

public class Boj7 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		int[][] arr = new int[num][num];
		int temp = 1;
		
		for (int i=0; i<num; i++) {
			for (int j=0; j<temp; j++) {
				arr[i][j] = sc.nextInt();
			}
			temp += 1;
		}
		
		int temp2 = 2;
		
		for (int i=1; i<num; i++) {
			for (int j=0; j<temp2; j++) {
				if (j == 0) {
					arr[i][j] += arr[i - 1][j];
				} else if (j == temp2 - 1){
					arr[i][j] += arr[i - 1][j - 1];
				} else {
					arr[i][j] += Math.max(arr[i - 1][j - 1], arr[i - 1][j]);
				}
			}
			temp2 += 1;
		}
		
		int answer = 0;
		for (int i=0; i<arr[num - 1].length; i++) {
			if (answer < arr[num-1][i]) {
				answer = arr[num-1][i];
			}
			
		}
		System.out.println(answer);
	}

}