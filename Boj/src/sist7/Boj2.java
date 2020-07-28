package sist7;

import java.util.Arrays;
import java.util.Scanner;

public class Boj2 {
	
	public int solution(int[] arr, int k) {
		int start = 0, end = arr.length - 1, mid = 0;
		
		while (start <= end) {
			mid = (start + end) / 2;
			
			if (arr[mid] == k) {
				return 1;
			} else if (arr[mid] > k) {
				end = mid - 1;
			}else {
				start = mid + 1;
			}
		}
		return 0;
		
	}

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		
		int[] n_arr = new int[sc.nextInt()];
		
		for(int i=0; i<n_arr.length; i++) {
			n_arr[i] = sc.nextInt();
		}
		Arrays.sort(n_arr);
		
		int m = sc.nextInt();
		
		for (int i=0; i<m; i++) {
			System.out.println(new Boj2().solution(n_arr, sc.nextInt()));
		}
	}
}