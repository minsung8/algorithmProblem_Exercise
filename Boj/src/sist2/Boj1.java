package sist2;

import java.util.Scanner;

public class Boj1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int limit = sc.nextInt();
		
		int[] arr = new int[num];
		
		for (int i = 0; i < num; i++) {
			arr[i] = sc.nextInt();
		}
		
		int dif = limit;
		int answer = 0;
		
		for (int i = 0; i < num - 2; i++) {
			for (int j = i + 1; j < num -1; j++) {
				for (int k = j + 1; k < num; k++) {
					if ((dif > (limit - (arr[i] + arr[j] + arr[k]))) && (limit - (arr[i] + arr[j] + arr[k])) >= 0){
						dif = (limit - (arr[i] + arr[j] + arr[k]));
						answer = arr[i] + arr[j] + arr[k];
					}
				}
			}
		}
		System.out.println(answer);
		sc.close();
	}

}
