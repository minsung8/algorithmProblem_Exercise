package sist2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;

public class Boj2 {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int num = Integer.parseInt(br.readLine());
		
		int[] arr = new int[num];
		int total = 0;
		
		// 배열 초기값 할당 및 총합 업데이트
		for (int i=0; i<num; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			total += arr[i];
		}
		
		// 배열 정렬
		Arrays.sort(arr);
		
		// 빈도 인덱스 배열
		int[] index = new int[8001];

		for (int i = 0; i < arr.length; i++) {
			index[arr[i] + 4000] += 1;
		}
		int max_idx = 0;
		
		ArrayList<Integer> list = new ArrayList<>();
		for (int i = 0; i < index.length; i++) {
			if(index[i] > index[max_idx]) {
				max_idx = i;
				list.clear();
				list.add(i - 4000);
			} else if(index[i] != 0 && index[i] == index[max_idx]) {
				list.add(i - 4000);
			}
		}

		System.out.println((int)(Math.round((double)total / num)));
		System.out.println(arr[(int)(num / 2)]);
		if (list.size() == 1) {
			System.out.println(list.get(0));
		} else {	
			System.out.println(list.get(1));
		}
		System.out.println(arr[num - 1] - arr[0]);
	
	}
}
