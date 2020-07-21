package sist6;

import java.util.Scanner;

public class Boj2 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[][] arr = new int[num][3];
		
		for(int i=0; i<arr.length; i++) {
			for(int j=0; j<3; j++) {
				arr[i][j] = sc.nextInt();
			}
		}
		
		for(int i=1; i<arr.length; i++) {
			for(int j=0; j<3; j++) {
				if(j==0) {
					arr[i][j] += Math.min(arr[i-1][1], arr[i-1][2]);
				} else if(j==1) {
					arr[i][j] += Math.min(arr[i-1][0], arr[i-1][2]);
				} else if(j==2) {
					arr[i][j] += Math.min(arr[i-1][0], arr[i-1][1]);
				}
			}
		}
		int answer = 10000;
		
		for (int i=0; i<3; i++) {
			if(answer > arr[num-1][i]) {
				answer = arr[num-1][i];
			}
		}
		System.out.println(answer);
			
	}

}
