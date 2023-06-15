import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int V = Integer.parseInt(br.readLine());
        String[] vote = br.readLine().split("");
        
        int A = 0, B = 0;
        for (String i:vote) {
            if (i.equals("A")) {
                A += 1;
            } else {
                B += 1;
            }
        }

        if (A > B) {
            System.out.print("A");
        } else if (A < B) {
            System.out.print("B");
        } else {
            System.out.print("Tie");
        }
    }
}