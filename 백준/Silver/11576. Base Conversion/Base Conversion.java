import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] AB = br.readLine().split(" ");
        Integer A = Integer.parseInt(AB[0]);
        Integer B = Integer.parseInt(AB[1]);

        Integer m = Integer.parseInt(br.readLine());

        String[] str_A = br.readLine().split(" ");
        ArrayList<Integer> int_A = new ArrayList();
        for (int i=0;i<m;i++) {
            int_A.add(Integer.parseInt(str_A[i]));
        }

        int numberA = 0;
        for (int i:int_A) {
            m -= 1;
            numberA += i*Math.pow(A, m);
        }

        ArrayList<Integer> int_B = new ArrayList();
        while (numberA>0) {
            int_B.add(numberA%B);
            numberA = (numberA - numberA%B)/B;
        }

        for (int i=int_B.size()-1;i>=0;i--){
            System.out.println(int_B.get(i));
        }
    }
}