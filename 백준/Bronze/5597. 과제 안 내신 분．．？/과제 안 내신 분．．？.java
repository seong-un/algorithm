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

        ArrayList<Integer> students = new ArrayList<>();
        for (int i=0; i<31; i++) {
            students.add(1);
        }

        for (int i=0; i<28; i++) {
            students.set(Integer.parseInt(br.readLine()), 0);
        }

        for (int i=1; i<31; i++) {
            if (students.get(i) == 1) {
                bw.write(i + "\n");
            }
        }

        bw.flush();
        bw.close();
    }
}