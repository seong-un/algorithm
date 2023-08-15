import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int N = Integer.parseInt(br.readLine());

        List<String> cars = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            cars.add(br.readLine());
        }

        int overtaking = 0;
        List<String> outOfTunnel = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            String car = br.readLine();
            outOfTunnel.add(car);
            int index = cars.indexOf(car);

            for (int j = 0; j < index; j++) {
                if (!outOfTunnel.contains(cars.get(j))) {
                    overtaking += 1;
                    break;
                }
            }
        }

        bw.write(overtaking + "");

        bw.flush();
        bw.close();
    }
}