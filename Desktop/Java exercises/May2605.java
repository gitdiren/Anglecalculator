/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package may2605;

import java.util.ArrayList;

/**
 *
 * @author 19141321
 */
public class May2605 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       ArrayList<String> classmates = new ArrayList <>();
       classmates.add("Ludmila");
       classmates.add("David");        
       classmates.add("Najma");
       classmates.forEach((i) -> {
           System.out.println(i);
        });
    }
    
}
