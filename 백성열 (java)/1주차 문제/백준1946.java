import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class backjoon1946 {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(bf.readLine());

        for(int i =0;i<N;i++){
            int employees = Integer.parseInt(bf.readLine());
            int result = employees;
            employee list[] = new employee[employees];
            for(int j = 0;j<employees;j++){
                String grade = bf.readLine();
                StringTokenizer st = new StringTokenizer(grade);
                list[j] = new employee(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
            }
            Arrays.sort(list, new Comparator<employee>() {
                @Override
                public int compare(employee c1, employee c2) {
                    return Integer.compare(c1.test1,c2.test1);
                }
            });
            int bestTest2 = list[0].test2;
            for (int j = 1; j < employees; j++) {
                if (list[j].test2 < bestTest2) {
                    result++;
                    bestTest2 = list[j].test2;
                }
            }
            System.out.println(result);
        }


    }
}
class employee{

    
    int test1;
    int test2;
    employee(int test1, int test2){
        this.test1 = test1;
        this.test2 = test2;
    }
}
