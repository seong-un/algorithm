import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine());
        for (int t=0;t<T;t++) {
            String[] dots = br.readLine().split(" ");
            int x1 = Integer.parseInt(dots[0]);
            int y1 = Integer.parseInt(dots[1]);
            int x2 = Integer.parseInt(dots[2]);
            int y2 = Integer.parseInt(dots[3]);

            int n = Integer.parseInt(br.readLine());
            
            int inout = 0;
            for (int i=0;i<n;i++) {
                String[] planet = br.readLine().split(" ");
                int cx = Integer.parseInt(planet[0]);
                int cy = Integer.parseInt(planet[1]);
                int r = Integer.parseInt(planet[2]);

                if (Math.pow(x1 - cx, 2) + Math.pow(y1 - cy, 2) < Math.pow(r, 2) && Math.pow(x2 - cx, 2) + Math.pow(y2 - cy, 2) > Math.pow(r, 2)) {
                    inout += 1;
                }

                if (Math.pow(x1 - cx, 2) + Math.pow(y1 - cy, 2) > Math.pow(r, 2) && Math.pow(x2 - cx, 2) + Math.pow(y2 - cy, 2) < Math.pow(r, 2)) {
                    inout += 1;
                }
            }

            bw.write(inout + "\n");
        }
        bw.flush();
        bw.close();
    }
}