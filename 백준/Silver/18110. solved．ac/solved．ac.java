import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] difficulties = new int[n];
        
        for (int i=0;i<n;i++){
            int difficulty = Integer.parseInt(br.readLine());
            difficulties[i] = difficulty;
        }

        Arrays.sort(difficulties);

        int trim = (int)Math.round(n * 0.15);
        double sum = 0;
        for (int i=trim;i<n-trim;i++){
            sum += difficulties[i];
        }

        System.out.print((int)Math.round(sum / (n-2*trim)));
    }
}