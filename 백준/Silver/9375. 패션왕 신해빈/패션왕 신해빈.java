import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
            int n = Integer.parseInt(br.readLine());
            HashMap<String, Integer> hashmap = new HashMap<>();
            for (int i = 0; i < n; i++) {
                String[] clothes = br.readLine().split(" ");
                if (hashmap.get(clothes[1]) == null) {
                    hashmap.put(clothes[1], 1);
                } else {
                    hashmap.put(clothes[1], hashmap.get(clothes[1]) + 1);
                }
            }
            
            int result = 1;
            for (int i:hashmap.values()) {
                result *= i+1;
            }

            bw.write(result-1 + "\n");
        }

        bw.flush();
        bw.close();
    }
}