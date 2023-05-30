import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br= new BufferedReader(new InputStreamReader(System.in));

        int N=Integer.parseInt(br.readLine());
        
        for (int i=N-1; i>=0; i--){
            int b=i;
            while (b>=1){
                System.out.print(" ");
                b--;
            }

            int c=N-i;
            while (c>=1){
                System.out.print("*");
                c--;
            }
            System.out.print("\n");
        }
    }
}
