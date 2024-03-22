/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package addnumbers;

import java.util.Scanner;

/**
 *
 * @author 19141321
 */
public class AddNumbers {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner myScanTool = new Scanner(System.in);
        System.out.println("Enter your first number");
        int firstNumber = myScanTool.nextInt();
        System.out.println("Enter your second number");
        int secondNumber = myScanTool.nextInt();
        int result = firstNumber + secondNumber;
        System.out.println(result);
        // TODO code application logic here
    }
    
}
