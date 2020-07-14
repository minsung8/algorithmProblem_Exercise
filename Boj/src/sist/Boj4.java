package sist;

import java.util.Scanner;

public class Boj4 {
	
	static int answer = 1;
	static int n = 0;
	
	static void solution(int n, int cnt) {
		n += 1;
		answer *= n;
		if (n >= cnt) {
			return;
		}else {
			solution(n, cnt);
		}
		
	}

	public static void main(String[] args) {
			
		Scanner sc = new Scanner(System.in);
		
		int cnt = sc.nextInt();
		solution(n, cnt);
		
		System.out.println(answer);
		sc.close();
	}

}
