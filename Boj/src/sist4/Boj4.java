// 백준 11399번 문제

package sist4;

import java.util.Scanner;

public class Boj4 {

	public static void main(String[] args) {
		
		//입력 및 변수 선언
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		int[] arr = new int[num];
		
		// 배열 업데이트
		for (int i=0; i<num; i++) {
			arr[i] = sc.nextInt();
		}
		
		// 오름차순 정렬
		for (int i=0; i<num; i++) {
			for (int j=i+1; j<num; j++) {
				if (arr[i] > arr[j]) {
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		
		// 시간 계산
		int answer = 0;
		int temp = 0;
		for (int i=0; i<num; i++) {
			temp += arr[i];
			answer += temp;
		}
		System.out.println(answer);
	}
}
