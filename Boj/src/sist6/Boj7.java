
package sist6;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Scanner;

public class Boj7 {

	public static void main(String[] args) {

		LinkedList<Integer> queue = new LinkedList<>();
		String answer = "<";
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt() - 1;
		
		for (int i=0; i<n; i++) {
			queue.add(i + 1);
		}
		int index = m;
		
		while (queue.size() != 1) {
			answer += queue.get(index) + ", ";
			queue.remove(index);
			index = (m + index)%(queue.size());
		}
		answer += queue.get(0) + ">";
		System.out.println(answer);
		
	}
}