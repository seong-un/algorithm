// 문자열을 뒤집는 함수 reverse는 StringBuffer 패키지에 있다.

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[][] text = new String[5][];
        int m = 0;
        for (int i = 0; i < 5; i++) {
            text[i] = br.readLine().split("");
            if (m < text[i].length) {
                m = text[i].length;
            }
        }

        String output = "";
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < 5; j++) {
                try {
                    output += text[j][i];
                } catch(ArrayIndexOutOfBoundsException e) {
                    continue;
                }
            }
        }

        System.out.println(output);
    }
}