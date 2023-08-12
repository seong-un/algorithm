import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        if (n == 1 || n == 3) {
            bw.write(-1 + "");
        } else {
            int result = 0;
    
            result += n / 5;
            if (n % 5 % 2 == 1) {
                result -= 1;
                n = n % 5 + 5;
            } else {
                n = n % 5;
            }
            result += n / 2;
            
            bw.write(result + "");
        }


        bw.flush();
        bw.close();
    }
}