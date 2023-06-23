// 체스판의 모든 8*8 격자판을 보는 브루트포스 알고리즘을 선택한다.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        String[][] chess = new String[N][M];
        for (int i=0;i<N;i++){
            chess[i] = br.readLine().split("");
        }

        // 모든 8*8 격자판의 수정횟수를 저장하는 ArrayList
        ArrayList<Integer> min_chess = new ArrayList<>();

        // 한 8*8 격자판의 시작점 (i, j)
        for (int i=0;i<N-7;i++) {
            for (int j=0;j<M-7;j++) {

                // 나올 수 있는 완벽한 격자판의 색깔은 두 가지가 있다.
                // 첫 번째는 W부터 시작하는 W격자판
                // 두 번째는 B부터 시작하는 B격자판
                // 두 격자판에 대하여 수정 횟수를 모두 기록하여
                // 두 수정횟수 중 가장 작은 값을 min_chess에 저장한다.
                int min_value = 0; // 시작점이 W라고 했을 경우의 수정횟수
                String color = "W"; // 현재 지점의 색깔

                // 시작점부터 시작하여 8*8 격자판을 모두 돌면서
                // 수정해야하는 부분에서는 수정횟수를 증가시킨다.
                for (int k=0;k<8;k++) {
                    for (int l=0;l<8;l++) {
                        // 기대하는 색깔(color)와 실제 색깔(chess[i+k][j+l])
                        // 두 개가 일치하지 않을 때는 min_value_W를 1 증가.
                        if (!chess[i+k][j+l].equals(color)){
                            min_value += 1;
                        }

                        // 기대되는 색깔을 바꾸는 과정이다.
                        // W면 B로, B면 W로 바꾼다.
                        // 마지막 열에 도달하고, 다음 행 첫 열로 돌아갔을 때는
                        // 기대되는 색깔이 변하지 않으므로 마지막 열에서는
                        // 색깔을 바꾸지 않는다.
                        if (l < 7){
                            // 기대 색깔이 W라면 B로 바꾸고,
                            if (color.equals("W")) {
                                color = "B";
                            // 기대 색깔이 B라면 W로 바꾼다.
                            } else {
                                color = "W";
                            }
                        }
                    }
                }

                min_chess.add(min_value < 32 ? min_value : 64-min_value);
            }
        }
        
        int result = min_chess.get(0);
        for (int i=1;i<min_chess.size();i++) {
            if (result > min_chess.get(i)) {
                result = min_chess.get(i);
            }
        }

        System.out.println(result);
    }
}