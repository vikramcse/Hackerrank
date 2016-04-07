import java.io.BufferedReader;
import java.io.InputStreamReader;

class Solution {
  public static void getZeros(int num) {
    int zeros = 0;

    for (int i = 5; num / i >= 1; i = i * 5) {
      zeros = zeros + num / i;
    }

    System.out.println(zeros);
  }

  public static void main(String args[])throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String line = br.readLine();
    int N = Integer.parseInt(line);

    Solution.getZeros(N);
  }
}
