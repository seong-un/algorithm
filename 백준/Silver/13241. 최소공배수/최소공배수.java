import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] numbers = br.readLine().split(" ");
        long A = Long.parseLong(numbers[0]);
        long B = Long.parseLong(numbers[1]);

        long lcm = A < B ? A : B;
        while (true) {
            if (A % lcm == 0) {
                if (B % lcm == 0) {
                    break;
                }
            }
            lcm -= 1;
        }

        System.out.println(A * B / lcm);
    }
}