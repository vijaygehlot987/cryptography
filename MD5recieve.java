/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;
import java.io.*;
import java.security.*;

public class MD5recieve {
public static void main(String[] args) {
        // TODO code application logic here
try
        {
FileInputStream fis=new FileInputStream("C:\\ty\\test.txt");
ObjectInputStream ois=new ObjectInputStream(fis);
Object o=ois.readObject();
if(!(o instanceof String)){
    System.out.println("Unexpected data in file");
    System.exit(-1);
}
String data=(String) o;
System.out.println("Got message"+data);
o=ois.readObject();
if(!(o instanceof byte[])){
    System.out.println("Unexpected data in file");
    System.exit(-1);
}
byte origDigest[]=(byte [])o;
MessageDigest md=MessageDigest.getInstance("MD5");
md.update(data.getBytes());
if(MessageDigest.isEqual(md.digest(), origDigest)){
    System.out.println("\n\n\n--->Message is valid");}
else{
    System.out.println("\n\n\n--->Message is corrupted");
}
        }
catch(Exception e)
{
    System.out.println("\n\n\n-->Message is corrupted");
}
}
}
