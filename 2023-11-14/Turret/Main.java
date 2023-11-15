package Turret;
import java.io.*;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int x1 = Integer.parseInt(st.nextToken());
			int y1 = Integer.parseInt(st.nextToken());
			int r1 = Integer.parseInt(st.nextToken());
			int x2 = Integer.parseInt(st.nextToken());
			int y2 = Integer.parseInt(st.nextToken());
			int r2 = Integer.parseInt(st.nextToken());

			double pointDist = Math.pow((x1 - x2), 2) + Math.pow((y1 - y2), 2);
			double cirDist = Math.pow((r1 + r2), 2);
			double insDist = Math.pow((r1 - r2), 2);
			
			// 두 원이 같을 경우
			if (x1 == x2 && y1 == y2 && r1 == r2) { System.out.println("-1"); }
			// 두 원이 완전히 떨어져 있을 경우 && 한 원이 다른 원 안에 완전히 포함될 경우
			else if (pointDist > cirDist || pointDist < insDist) { System.out.println("0"); }
			// 두 원이 외접 혹은 내접할 경우
			else if (pointDist == cirDist || pointDist == insDist) { System.out.println("1"); } 
			// 그 외의 모든 경우
			else { System.out.println("2"); }
		}
	}
}