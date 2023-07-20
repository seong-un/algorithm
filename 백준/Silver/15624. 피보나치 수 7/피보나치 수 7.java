import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        long i_2 = 0;
        long i_1 = 1;
        long result = i_2 + i_1;

        for (int i = 2; i < n; i++) {
            i_2 = i_1;
            i_1 = result;
            result = (i_2 + i_1) % 1000000007;
        }
        bw.write(result + "");


        bw.flush();
        bw.close();
    }
}