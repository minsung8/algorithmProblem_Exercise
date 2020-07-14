package sist;

import java.util.Scanner;

public class Boj3 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int cnt = sc.nextInt();
		
		for (int i = 1; i <= cnt; i ++) {
			
			int x1 = sc.nextInt();
			int y1 = sc.nextInt();
			int r1 = sc.nextInt();
			int x2 = sc.nextInt();
			int y2 = sc.nextInt();
			int r2 = sc.nextInt();
			
			double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
			
			if (x1 == x2 && y1 == y2 && r1 == r2) {
				System.out.println(-1);
			} else if ((x1 == x2 && y1 == y2 && r1 != r2) || (distance > r1 + r2) || (distance < Math.abs(r1 - r2))) {
				System.out.println(0);
			} else if ((distance == r1 + r2) || (Math.abs(r1 - r2) == distance)) {
				System.out.println(1);
			} else {
				System.out.println(2);
			}
		
			
		}
		sc.close();
	}

}
