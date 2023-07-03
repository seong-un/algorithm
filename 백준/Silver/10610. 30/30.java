import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] N = br.readLine().split("");
        ArrayList<String> arr_N = new ArrayList<>();

        int sum_N = 0;
        for (int i=0;i<N.length;i++) {
            sum_N += Integer.parseInt(N[i]);
            arr_N.add(N[i]);
        }

        if (sum_N % 3 == 0) {
            if (arr_N.contains("0")){
                Collections.sort(arr_N);
                Collections.reverse(arr_N);
                for (int i=0;i<arr_N.size();i++){
                    bw.write(arr_N.get(i));
                }
            } else {
                bw.write("-1");
            }
        } else {
            bw.write("-1");
        }

        bw.flush();
        bw.close();
    }
}