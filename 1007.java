
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    long varA = Long.parseLong(myObj.nextLine()); 
    long varB = Long.parseLong(myObj.nextLine()); 
    long varC = Long.parseLong(myObj.nextLine()); 
    long varD = Long.parseLong(myObj.nextLine()); 
    long result = ((varA * varB) - (varC * varD));
    System.out.println("DIFERENCA ="+ result);
  }
}