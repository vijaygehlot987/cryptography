/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aes_cipher;
import java.security.*;
import javax.crypto.*;
/**
 *
 * @author admin
 */
public class Aes_cipher {
    Cipher ecipher;
    Cipher dcipher;
    Aes_cipher(SecretKey key,String algorithm)
    {	
try
{
    ecipher=Cipher.getInstance(algorithm);
    dcipher=Cipher.getInstance(algorithm);
    ecipher.init(Cipher.ENCRYPT_MODE,key);
    dcipher.init(Cipher.DECRYPT_MODE,key);
        }
catch(Exception e)
        {
            e.printStackTrace();
        }
    }
public String encrypt(String str)
    {
        try
        {
            //Encode the string into bytes using utf-8
            byte[] utf8=str.getBytes("UTF8");

            //Encrypt
            byte[] enc=ecipher.doFinal(utf8);

            //Encode bytes to base64 to get a string
            return new sun.misc.BASE64Encoder().encode(enc);
        }
catch(Exception e)
        {
            e.printStackTrace();
        }
return null;
    }
public String decrypt(String str)
    {
        try
        {
            //Deode base64 to get bytes
            byte[] dec=new sun.misc.BASE64Decoder().decodeBuffer(str);

            //Decrypt
            byte[] utf8=dcipher.doFinal(dec);

            //Decode using utf-8
            return new String(utf8,"UTF8");
        }
        catch(Exception e)
        {
            e.printStackTrace();
        }
return null;
    }
public static void testUsingSecretKey()
    {
try
        {
            String secretString="Hello World";
            
            SecretKey deskey=KeyGenerator.getInstance("AES").generateKey();
            Aes_cipher desEncrypter=new Aes_cipher(deskey,deskey.getAlgorithm());

            //Encrypt the string
            String desEncrypted=desEncrypter.encrypt(secretString);

            //Decrypt the string
            String desDecrypted=desEncrypter.decrypt(desEncrypted);
            System.out.println("AES Original String "+secretString);
            System.out.println("AES Encrypted String "+desEncrypted);
            System.out.println("AES Decrypted String "+desDecrypted);
        }
catch(NoSuchAlgorithmException e)
        {
            e.printStackTrace();
        }
    }
    /**
     * @paramargs the command line arguments
     */
public static void main(String[] args) {
        // TODO code application logic here
        testUsingSecretKey();
    }

}
