package sist7;import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Boj3 {
	
	public static int[] heap = new int[100001];
	public static int size = 0;
	public static StringBuilder sb = new StringBuilder();
	
	public static void swap(int x, int y) {
		int temp = heap[y];
		heap[y] = heap[x];
		heap[x] = temp;
	}
	
	public static void push(int x) {
		size += 1;
		heap[size] = x;
		
		for (int i=size; i>1; i/=2) {
			if (heap[i] < heap[i/2]) {
				break;
			} else {
				swap(i/2, i);
			}
		}
	}
	
	public static void pop() {
		sb.append(heap[1] + "\n");
		heap[1] = heap[size];
		heap[size] = 0;
		size -= 1;
		
		for (int i=1; 2*i<=size;) {
			
			if (heap[i] > heap[2*i] && heap[i] > heap[2*i + 1]) {
				break;
			} else if (heap[2*i] > heap[2*i + 1]) {
				swap(i, 2*i);
				i = 2*i;
			} else {
				swap(i, 2*i + 1);
				i = 2*i + 1;
			}
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		
		for (int i=0; i<n; i++) {
			int temp = Integer.parseInt(br.readLine());
			
			if (temp == 0) {
				
				if (size == 0) {
					sb.append(0 + "\n");
				} else {
					pop();
				}
			} else {
				push(temp);
			}
			
		}
		System.out.print(sb.toString());
	}
}