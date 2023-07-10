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

        int N = Integer.parseInt(br.readLine());
        String[] str_Ai = br.readLine().split(" ");
        ArrayList<Integer> Ai = new ArrayList<>();
        for (String i:str_Ai) {
            Ai.add(Integer.parseInt(i));
        }
        String[] BC = br.readLine().split(" ");
        int B = Integer.parseInt(BC[0]);
        int C = Integer.parseInt(BC[1]);

        long viewer = 0;
        for (int i:Ai) {
            if (i-B>=0) {
                if ((i-B)%C == 0) {
                    viewer += (i-B)/C + 1;
                } else {
                    viewer += (i-B)/C + 2;
                }
            } else {
                viewer += 1;
            }
        }

        bw.write(viewer + "");
        bw.flush();
        bw.close();
    }
}