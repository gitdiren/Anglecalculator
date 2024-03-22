/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package mynames;

import java.util.Scanner;

/**
 *
 * @author 19141321
 */
public class MyNames {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner myScanTool = new Scanner(System.in);
        System.out.println("Enter your first name");
        String firstname = myScanTool.next();
        System.out.println("Enter your lastname");
        String lastname = myScanTool.next();
        String fullname = firstname + " " + lastname;
        System.out.println(fullname);

// TODO code application logic here
    }
    
}
