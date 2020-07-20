// 백준 2748번 문제

package sist5;

import java.util.Scanner;

public class Boj6 {

	public static void main(String[] args) {
			
		long a = 0;
		long b = 1;
		long c = 0;
		
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		
		if(num==1) {
   			System.out.println(1);
   		}else {
   		for(int i=1; i<num; i++) {
   			c=a+b;
   			a=b;
   			b=c;
   		}
   		System.out.println(c);
   		}
	}
}
