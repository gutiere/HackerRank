import java.io.*;
import java.util.*;

public class JourneyToTheMoon {
   public static void main(String[] args) throws Exception{
        BufferedReader bfr = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = bfr.readLine().split(" ");
        int N = Integer.parseInt(temp[0]);
        int I = Integer.parseInt(temp[1]);

        ArrayList<HashSet<Integer>> countries = new ArrayList<HashSet<Integer>>();
        for (int i = 0; i < N; i++) {
            countries.add(new HashSet<Integer>());
            countries.get(i).add(i);
        }

        for(int i = 0; i < I; i++) {

            temp = bfr.readLine().split(" ");
            int a = Integer.parseInt(temp[0]); // astro 1
            int b = Integer.parseInt(temp[1]); // astro 2

            int country1 = -1;
            int country2 = -1;
            // check if any sets contain a or b
            for (int j = 0; j < countries.size(); j++) {
                if (countries.get(j).contains(a) || countries.get(j).contains(b)) {
                    if (country1 < 0) country1 = j;
                    else {
                        country2 = j;
                        break;
                    }
                }
            }
            if (country1 >= 0 && country2 >= 0) {
                // add countries.
                if (countries.get(country1).size() > countries.get(country2).size()) {
                    countries.get(country1).addAll(countries.get(country2));
                    countries.remove(country2);
                } else {
                    countries.get(country2).addAll(countries.get(country1));
                    countries.remove(country1);
                }

            } else {
                int mutualCountry = -1;
                if (country1 >= 0) mutualCountry = country1;
                else if (country2 >= 0) mutualCountry = country2;
                countries.get(mutualCountry).add(a);
                countries.get(mutualCountry).add(b);
            }
        }

        long combos = 0;

        for (HashSet population : countries) {
            int size = population.size();
            combos = combos + (N - size) * size;
            N = N - size;
        }

        System.out.println(combos);
   }
}
