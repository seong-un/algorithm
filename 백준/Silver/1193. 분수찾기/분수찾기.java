import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int X = Integer.parseInt(br.readLine());
        int count = 1;
        while (true) {
            if (X <= count) {
                break;
            }

            X = X - count;
            count += 1;
        }

        if (count % 2 == 1) {
            bw.write(count-X+1 + "/");
            bw.write(X + "");
        } else {
            bw.write(X + "/");
            bw.write(count-X+1 + "");
        }

        bw.flush();
        bw.close();
    }
}