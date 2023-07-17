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

        String[] NM = br.readLine().split(" ");
        int N = Integer.parseInt(NM[0]);
        int M = Integer.parseInt(NM[1]);

        String[] str_Hi = br.readLine().split(" ");
        ArrayList<Integer> Hi = new ArrayList<>();
        for (int i = 0; i < N ; i++) {
            Hi.add(Integer.parseInt(str_Hi[i]));
        }

        int depression = M;
        int total = 0;
        for (int i = 0; i < N; i++) {
            depression -= Hi.get(i) + 1;
            total += Hi.get(i) + 1;
        }
        
        int result = 0;
        if (total < M) {

            for (int i = 0; i < depression / (N + 1) + 1; i++) {
                result += i * i * (N + 1);
            }
            
            result += (depression / (N + 1) + 1) * (depression / (N + 1) + 1) * (depression % (N + 1));
        }
        bw.write(result + "");
        
        bw.flush();
        bw.close();
    }
}