import jdk.nashorn.internal.runtime.regexp.joni.Regex;

import java.io.*;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.HashSet;
import java.util.regex.*;
import java.util.Date;
/**
 * Created by Eren on 2017-02-15.
 */
public class TitanicParser {
    public static String parse(BufferedReader input, String filename) {
        StringBuilder outputString = new StringBuilder();

        HashSet<String> ticketNotes = new HashSet<String>();
        HashSet<String> titles = new HashSet<String>();


        DateFormat dateFormat = new SimpleDateFormat("MM-dd_HH-mm-ss");
        Date date = new Date();
        dateFormat.format(date);

        String theFilename = filename + dateFormat.format(date) + ".csv";
        PrintWriter outputWriter;
        try{
            outputWriter = new PrintWriter(theFilename, "UTF-8");
        } catch (IOException e) {
            System.out.print("Couldn't create file");
            return null;
        }

        String[] attributes;

        try{
            //Get attributes
            String firstInput = input.readLine();
            attributes = firstInput.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
            outputWriter.write(firstInput + "\n");
            for (String s : attributes){
                System.out.println(s);
            }
            System.out.println("Count: " + attributes.length);


            //Start with data
            String line = input.readLine();
            while ( line != null) {

                String[] values = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", -1);
                int attributeIndex = 0;
                //System.out.println(line);
                for(String value : values) {
                    //System.out.println(attributeIndex);
                    if(attributes[attributeIndex].compareTo("Name") == 0){
                        String title = TitanicParser.getTitle(value);
                        //System.out.println(title);
                        outputString.append(title);
                    } else if(attributes[attributeIndex].compareTo("Cabin") == 0){
                        int cabinCount = 0;
                        if(value.isEmpty() == false){
                            cabinCount = value.split(" ").length;
                        }
                        //System.out.println(cabinCount);
                        outputString.append(cabinCount);
                    } else if(attributes[attributeIndex].compareTo("Ticket") == 0){
                        String ticketNote = "UNKNOWN";
                        Pattern p = Pattern.compile("[A-Za-z]");
                        Matcher m = p.matcher(value);

                        if(m.find()){
                            ticketNote = value.split(" ")[0];
                        }


                        //System.out.println(ticketNote); //Can be ""
                        outputString.append(ticketNote);
                    }  else if(attributes[attributeIndex].compareTo("Age") == 0){ //copy to output
                        int age = -1;
                        if(value.isEmpty() == false){
                            age = 1;
                            if( Double.parseDouble(value) < 18 || Double.parseDouble(value) > 60){
                                age = 0;
                            }
                        }

                        //System.out.println(age);
                        outputString.append(age);
                    } else{
                        outputString.append(value);
                    }
                    outputString.append(",");
                    attributeIndex++;
                }

                outputString.setLength(outputString.length()-1); //Remove last ","
                outputString.append("\n");


                //Write results

                outputWriter.write(outputString.toString());
                outputString = new StringBuilder();
                line = input.readLine();
            }

            input.close();
        }
        catch(Exception e){
            System.err.println("Error: Target File cannot Be Read");
            //System.err.println(e.toString());
        }
        try{
            outputWriter.close();
        }catch (Exception e){
            System.out.println("Could not close file: " + theFilename);
            return null;
        }

        return theFilename;
    }

    private static String getTitle(String name){
        StringBuilder title = new StringBuilder();
        boolean keep = false;
        for(char c : name.toCharArray()){

            if(c == ','){
                keep = true;
            }else if(c == '.'){
                keep = false;
            }
            if(keep == true){
                title.append(c);
            }


        }
        title.delete(0,2); // delete the ", "

        return title.toString();
    }

/**
    public static String parse(String input){
        //Inits
        StringBuilder output = new StringBuilder(input.length());
        String[] attributes = {""};
        String line = "";


        int i = 0;
        while( i < input.length()){
            int j = i;
            while(input.charAt(j) != '\n'){ //get one line
                line += input.charAt(j);
                j++;
            }
            //do stuff with line

            if(i == 0){ //first line of csv file, get attributes
                attributes = line.split(",");
            }else{
                String[] values = line.split(",");
                int attributeIndex = 0;
                for(String value : values) {
                    if(attributes[attributeIndex].compareTo("Name") == 0){
                        output.append(value + ",");
                    } else if(attributes[attributeIndex].compareTo("Cabin") == 0){
                        output.append(value + ",");
                    } else if(attributes[attributeIndex].compareTo("Ticket") == 0){
                        output.append(value + ",");
                    }  else{
                        //copy to output
                        output.append(value + ",");
                    }
                    attributeIndex++;
                }
                output.deleteCharAt(output.length()-1);
                output.append("\n");
            }



            i = j++;
        }


        return output.toString();
    }

**/



}
