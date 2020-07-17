// 백준 10773번 문제

package sist4;

import java.util.ArrayList;
import java.util.Scanner;

public class Boj5 {

	public static void main(String[] args) {

		// Arraylist과 Scanner를 선언 
		ArrayList<Integer> list = new ArrayList<Integer>();
		Scanner sc = new Scanner(System.in);
		
		// 변수 선언 
		int num = sc.nextInt();
		
		// 조건에 맞게 list 업데이트
		for (int i=0; i<num; i++) {
			int temp = sc.nextInt();
			if ((temp == 0) && (list.size() > 0)){
				
				list.remove(list.size() - 1);
				
			} else {
				
				list.add(temp);
			}
		}
		
		// list 총합 계산 및 출력
		int answer = 0;
		for (int i=0; i<list.size(); i++) {
			answer += list.get(i);
		}
		System.out.println(answer);	
	}
}
