import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i=0;i<T;i++){
            String[] AB = br.readLine().split(",");
            System.out.println(Integer.parseInt(AB[0])+Integer.parseInt(AB[1]));
        }
    }
}
