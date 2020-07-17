// 백준 15652번 문제


package sist4;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Boj3 {
	
	static int n, m;
	static int[] list;
	
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	
	public static void dfs(int idx, int cnt) throws IOException {
		
		if (cnt == m) {
			for (int i=0; i<m; i++) {
				bw.write(String.valueOf(list[i]) + " ");
			}
			bw.newLine();
			return;
		}
		
		for (int i=idx; i<=n; i++) {
			
			list[cnt] = i;
			dfs(i, cnt + 1);
		}	
	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		list = new int[9];
		
		dfs(1, 0);
		br.close();
		bw.flush();
		bw.close();
		
	}
}