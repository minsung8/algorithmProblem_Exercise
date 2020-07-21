package sist6;

import java.util.Arrays;
import java.util.Scanner;

public class Boj1 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int[] arr = new int[num];
		int[] answer_arr = new int[num];
		int[] answer_arr2 = new int[num];
		
		for (int i=0; i<arr.length; i++) {
			arr[i] = sc.nextInt();
		}
		
		Arrays.fill(answer_arr, 1);
		
		for (int i=1; i<arr.length; i++) {
			for (int j=0; j<i; j++) {
				if ((arr[i] > arr[j]) && (answer_arr[i] <= answer_arr[j])) {
					answer_arr[i] = answer_arr[j] + 1;
				}
			}
		}
		Arrays.fill(answer_arr2, 1);

		for (int i=arr.length-2; i>-1; i--) {
			for (int j=arr.length-1; j>i; j--) {
				if ((arr[i] > arr[j]) && (answer_arr2[i] <= answer_arr2[j])) {
					answer_arr2[i] = answer_arr2[j] + 1;
				}
			}
		}
		int answer = 0;
		int temp;
		for (int i=0; i<arr.length; i++) {
			temp = answer_arr[i] + answer_arr2[i];
			if (answer < temp) {
				answer = temp;
			}
		}
		System.out.println(answer - 1);
		
	}

}
