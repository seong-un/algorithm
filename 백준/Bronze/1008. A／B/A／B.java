import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        String[] str=br.readLine().split(" ");
        double a=Double.parseDouble(str[0]);
        double b=Double.parseDouble(str[1]);

        System.out.println(a/b);
    }
}
