package FlyMeToTheAlphaCentauri;
import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
		int T = Integer.parseInt(br.readLine());

		while (T-- > 0) {
			StringTokenizer st = new StringTokenizer(br.readLine(), " ");
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			int d = y - x;
			int sqrt = (int)Math.sqrt(d);
			int count = sqrt * 2 - 1;
			int offset = d - sqrt * sqrt;
			if (offset > sqrt) { count += 2; }
			else if (offset > 0) { count += 1; }
			System.out.println(count);
		}
	}
}