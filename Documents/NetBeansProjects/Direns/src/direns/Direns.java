/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package direns;

/**
 *
 * @author 19141321
 */
public class Direns {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a = 3;
            int b = 7;
            for (int i =1; i<4 ; i++) {
                a = b - i;
                for (int j = 0; j < 3; j++) {
                    b = a + j;
                    if (a ==b) {
                        System.out.println("a=b when i is ="+i+" and j is "+j);
                  break;
                    }
                }
          
            }
    }

}