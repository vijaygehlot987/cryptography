/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com;
import java.io.*;
import java.security.*;
/**
 *
 * @author admin
 */
public class md5send {

    /**
     * @paramargs the command line arguments
     */
public static void main(String[] args) {
        // TODO code application logic here
try
        {
FileOutputStream fos=new FileOutputStream("C:\\test.txt");
MessageDigest md=MessageDigest.getInstance("MD5");
ObjectOutputStream oos=new ObjectOutputStream(fos);
String data="Hello world";
byte buf[]=data.getBytes();
md.update(buf);
oos.writeObject(data);
oos.writeObject(md.digest());
        }
catch(Exception e)
        {}
    }

}
