import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] str_length = br.readLine().split(" ");
        int length_A = Integer.parseInt(str_length[0]);
        int length_B = Integer.parseInt(str_length[1]);

        String[] str_A = br.readLine().split(" ");
        HashSet set_A = new HashSet();
        for (int i=0;i<length_A;i++) {
            set_A.add(Integer.parseInt(str_A[i]));
        }

        String[] str_B = br.readLine().split(" ");
        HashSet set_B = new HashSet();
        for (int i=0;i<length_B;i++) {
            set_B.add(Integer.parseInt(str_B[i]));
        }

        HashSet<Integer> ANB = new HashSet<>(set_A);
        ANB.retainAll(set_B);
        set_A.removeAll(ANB);
        set_B.removeAll(ANB);

        System.out.println(set_A.size()+set_B.size());
    }
}