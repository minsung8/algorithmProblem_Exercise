package sist6;

import java.util.Scanner;

public class Boj5 {

	public static void main(String[] args) throws Exception {
		
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		int[] arr = new int[1100000];
		
		arr[1] = 1;
		arr[2] = 2;
		
		for (int i=3; i<=num; i++) {
			
			arr[i] = (arr[i - 1] + arr[i - 2]) % 15746;
			 
		}
		System.out.println(arr[num]);
		
		sc.close();
		
	}
	
}