package zooauthenticationsystem;

import java.io.File;
import java.io.FileNotFoundException;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

import java.util.Scanner;

//
//
// @author lee.yates_snhu
//
public class ZooAuthenticationSystem {

    //
    // @param args the command line arguments
    //
    public static void main(String[] args) throws NoSuchAlgorithmException, FileNotFoundException {
        
        //Create a scanner object named getInput to get user input
        @SuppressWarnings("resource")
		Scanner getInput = new Scanner(System.in);

        //Variable to track the number of user input attempts
        int attempts = 0;

        //Repeat until a successful attempt has been made or
        //three unsuccessful attempts have been made
        while (true) {

            //Request user input for name
            System.out.print("Enter user name: ");

            //Assign variable userName to user input for user name
            String userName = getInput.nextLine();

            //Request user input for password
            System.out.print("Enter password: ");

            //Assign variable original to user input for user password
            String original = getInput.nextLine();

            //Convert the password using a message digest five (MD5) hash
            MessageDigest md = MessageDigest.getInstance("MD5");

            md.update(original.getBytes());

            byte[] digest = md.digest();

            StringBuffer sb = new StringBuffer();

            for (byte b : digest) {

                sb.append(String.format("%02x", b & 0xff));

            }

            //Declare a boolean variable to keep track of login success
            boolean authSuccess = false;

            //Open credentials file
            File file = new File("credentials.txt");
            @SuppressWarnings("resource")
			Scanner readCred = new Scanner(file);

            //Search for the user credentials in the credentials file
            while (readCred.hasNextLine()) {

                //Read a record
                String record = readCred.nextLine();

                //Split the record into separate columns
                String columns[] = record.split("\t");

                //Check the credentials against the valid credentials in the file
                //Check user name
                if (columns[0].trim().equals(userName)) {

                    //If user name is matched, check whether the Converted password using
                    //a message digest five password with hashed password in the second column
                    if (columns[1].trim().equals(sb.toString()))//Check password
                    {

                        //If the passwords are same, set the boolean value
                        //authSuccess to true
                        authSuccess = true;//Login success

                        //Open the role file
                        @SuppressWarnings("resource")
						Scanner readRole = new Scanner(new File(columns[3].trim() + ".txt"));

                        //Display the information stored in the role file
                        while (readRole.hasNextLine()) {

                            System.out.println(readRole.nextLine());

                        }

                        break;

                    }

                }

            }

            //If login successful, ask the user whether the user wants to log out or not
            if (authSuccess) {

                System.out.println("Do you want to log out(y/n): ");

                String choice = getInput.nextLine();

                //If user wants to log out, exit the system.
                if (choice.toLowerCase().charAt(0) == 'y') {

                    System.out.println("Successfully loged out.");

                    break;

                } 
                //If user wants to continue, set the boolean value
                //authSuccess to true for new login
                else {

                    authSuccess = false;

                }

            } 
            //If login is not successful, update the number of attempts
            else {

                attempts++;

                //If maximum attempts reached, notify the user and exit the program
                if (attempts == 3) {

                    System.out.println("Maximum attempts reached!\nExiting...");

                    break;

                } 
                //otherwise, prompt to enter credentials again
                else {

                    System.out.println("Please enter correct credentials!");

                }

            }

        }
        
    }
    
}
