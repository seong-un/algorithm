import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.Map.Entry;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        Map<String, Integer> books = new HashMap<>();
        for (int i = 0; i < N; i++) {
            String book = br.readLine();
            if (!books.containsKey(book)) {
                books.put(book, 1);
            } else {
                books.put(book, books.get(book) + 1);
            }
        }

        int max_book = 0;
        ArrayList bestseller = new ArrayList();
        for (Entry<String, Integer> entry : books.entrySet()) {
            if (max_book < entry.getValue()) {
                max_book = entry.getValue();
                bestseller.clear();
                bestseller.add(entry.getKey());
            } else if (max_book == entry.getValue()) {
                bestseller.add(entry.getKey());
            }
        }

        bestseller.sort(Comparator.naturalOrder());
        System.out.println(bestseller.get(0));
    }
}