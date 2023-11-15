import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		while (T-- > 0) {		
			String str = br.readLine();
			System.out.println(check_vps(str));
		}
	}

	private static String check_vps(String str) {
		Stack<Character> stack = new Stack<Character>();
		char c;

		for (int i = 0; i < str.length(); i++) {
			c = str.charAt(i);

			if (c == '(') {
				stack.push(c);
			}
			else if (c == ')' && !stack.isEmpty()) {
				stack.pop();
			}
			else {
				return "NO";
			}
		}

		if (stack.isEmpty()) {
			return "YES";
		}
		else {
			return "NO";
		}
	}
}