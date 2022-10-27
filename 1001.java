import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    long varA = Long.parseLong(myObj.nextLine()); 
    long vatB = Long.parseLong(myObj.nextLine()); 
    long result = varA + vatB;
    System.out.println("X ="+ result);
  }
}