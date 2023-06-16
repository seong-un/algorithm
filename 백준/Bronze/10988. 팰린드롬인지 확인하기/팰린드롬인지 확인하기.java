import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String str = br.readLine();

        StringBuffer sb = new StringBuffer(str);
        String palindrome = sb.reverse().toString();

        if (str.equals(palindrome)) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}