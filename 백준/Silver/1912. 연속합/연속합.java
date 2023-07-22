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
        String[] array = br.readLine().split(" ");

        ArrayList<Integer> arrayList = new ArrayList<>();
        for (String i:array) {
            int j = Integer.parseInt(i);
            arrayList.add(j);
        }

        ArrayList<Integer> dp = new ArrayList<>();
        dp.add(arrayList.get(0));
        for (int i = 1; i<arrayList.size(); i++) {
            if (dp.get(i-1) + arrayList.get(i) > arrayList.get(i)) {
                dp.add(dp.get(i-1) + arrayList.get(i));
            } else {
                dp.add(arrayList.get(i));
            }
        }

        int max_value = Integer.MIN_VALUE;
        for (int i:dp) {
            if (max_value < i) {
                max_value = i;
            }
        }

        bw.write(max_value + "");

        bw.flush();
        bw.close();
    }
}