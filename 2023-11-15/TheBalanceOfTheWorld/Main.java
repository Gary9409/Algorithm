import java.util.*;
import java.io.*;

public class Main {
	public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		while (str != ".") {
			System.err.println(solution(str));
			str = br.readLine();
		}
	}

	private static String solution(String str) {
		Stack<Character> stack = new Stack<Character>();
		char c;
		for (int i = 0; i < str.length(); i++) {
			c = str.charAt(i);
			if (c == '(' || c == '[') {
				stack.push(c);
			}
			else if (c != '(' && c != ')' && c != '[' && c != ']') {
				continue;
			}
			else {
				if (pair(stack.peek(), c)) {
					stack.pop();
				}
				else {
					return "no";
				}
			}
		}

		if (stack.empty()) {
			return "yes";
		}
		else {
			return "no";
		}
	}

	private static boolean pair(char peek, char c) {
		if (peek == '(' && c == ')') {
			return true;
		}
		else if (peek == '[' && c == ']') {
			return true;
		}
		else {
			return false;
		}
	}
}