import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int N1 = Integer.parseInt(br.readLine());
        String[] N2 = br.readLine().split("");

        System.out.println(N1*Integer.parseInt(N2[2]));
        System.out.println(N1*Integer.parseInt(N2[1]));
        System.out.println(N1*Integer.parseInt(N2[0]));
        System.out.println(N1*(Integer.parseInt(N2[0])*100+Integer.parseInt(N2[1])*10+Integer.parseInt(N2[2])));
    }
}
