import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        String[] str_list = br.readLine().split(" ");
        ArrayList<Integer> int_array = new ArrayList<>();
        for (int i=0;i<str_list.length;i++) {
            int_array.add(Integer.parseInt(str_list[i]));
        }

        Collections.sort(int_array);

        for (int i:int_array) {
            System.out.print(i+" ");
        }
    }
}