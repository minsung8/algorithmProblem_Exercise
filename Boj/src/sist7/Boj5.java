package sist7;import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node implements Comparable<Node>{
	
	int end;
	int weight;
	
	public Node (int end, int weight) {
		this.end = end;
		this.weight = weight;
	}

	@Override
	public int compareTo(Node o) {
		return weight - o.weight;
	}
	
}

public class Boj5 {
	
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	
	static List<Node>[] list;
	static int[] dist;
	
	private static int vertex, edge, k;
	private static final int INF = 100_000_000;
	
	public static void main(String[] args) throws IOException {
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		vertex = Integer.parseInt(st.nextToken());
		edge = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(br.readLine());
		
		list = new ArrayList[vertex + 1];
		dist = new int[vertex + 1];
		
		Arrays.fill(dist, INF);
		
		for (int i=1; i<=vertex; i++) {
			list[i] = new ArrayList<Node>();
		}
		
		for (int i=1; i<=vertex; i++) {
			
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int weight = Integer.parseInt(st.nextToken());
			
			list[start].add(new Node(end, weight));
		}
		
		daicstra(k);
		
		StringBuilder sb = new StringBuilder();
		
		for (int i=1; i<=vertex; i++) {
			if (dist[i] == INF) sb.append("INF\n");
			else sb.append(dist[i] + "\n");
		}
		bw.write(sb.toString());
		bw.close();
		br.close();
	}
	
	public static void daicstra(int start) {
		dist[start] = 0;
		
		PriorityQueue<Node> queue = new PriorityQueue<Node>();
		
		boolean[] visited = new boolean[vertex + 1];
		
		queue.add(new Node(start, 0));
		
		while (!queue.isEmpty()) {
			Node temp_node = queue.poll();
			int temp = temp_node.end;
			
			if (visited[temp] == true) continue;
			visited[temp] = true;
			
			for (Node node : list[temp]) {
				if ( dist[node.end] > dist[temp] + node.weight ) {
					dist[node.end] = dist[temp] + node.weight;
					queue.add(new Node(node.end, dist[node.end]));
				}			
			}
		}	
	}
}