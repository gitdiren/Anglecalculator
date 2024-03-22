/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hashmap;


/**
 *
 * @author 19141321
 */
import java.util.HashMap
        
public class HashMap {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        HashMap<String, String> courseList = new HashMap <String, String>();
        courseList. put ("P-05022-23-Q02", "Level 3 Certificate in AI Programming with Python");
        courseList. put (" P-05033-23-Q01", "Level 3 Access to HE Diploma in Computing");
        courseList. put (" P-05036-23-Q01", "Level 4 Diploma for Data Analysts"); 
        System.out.println(courseList);
    }
    
}
