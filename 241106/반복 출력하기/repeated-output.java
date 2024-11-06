import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rownum = sc.nextInt();
        printN(rownum);
    }
    public static void printN(int n) {
        for (int i=0 ; i<n ; i++){
            System.out.print("12345^&*()_");
        }
    }
}