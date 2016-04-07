import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

class Solution {
  public static void calculate(int[] arr, int N) {
    ArrayList<Integer> list = new ArrayList<>();

    for (int i = 0; i < N; i++) {
      boolean flag = true;
      for (int j = 0; j < N; j++) {
        if (i != j && arr[i] % arr[j] == 0) {
          flag = false;
          break;
        }
      }

      if (flag) {
        System.out.print(arr[i]);
        if (i != N) {
          System.out.print(" ");
        }
      }
    }

  }

  public static void main(String args[] ) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String line = br.readLine();
    int N = Integer.parseInt(line);
    int[] arr = new int[N];

    String[] input = br.readLine().split(" ");

    for (int i = 0; i < N; i++) {
      arr[i] = Integer.parseInt(input[i]);
    }

    Solution.calculate(arr, N);
  }
}
