import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;


import weka.classifiers.trees.J48;

import weka.core.Instances;




public class WekaTest {
    public static BufferedReader readDataFile(String filename) throws Exception{
        //String[] compatibleExtension = {"arff", "csv"};
        //String extension = FilenameUtils.getExtension(filename);

        BufferedReader inputReader = null;
        try {
            inputReader = new BufferedReader(new FileReader(filename));
        } catch (FileNotFoundException ex) {
            System.err.println("File not found: " + filename);
        }
        return inputReader;
    }





    public static void main(String[] args) throws Exception {

        //Init input and output instances

        BufferedReader inputFile = readDataFile(args[0]);
        BufferedReader outputFile = readDataFile(args[1]);

        Instances input = new Instances(inputFile);
        Instances output = new Instances(outputFile);

        input.setClassIndex(input.numAttributes() - 1);
        output.setClassIndex(output.numAttributes() - 1);

        String[] options = new String [1];
        options[0] = "-U"; //unpruned tree
        J48 tree = new J48(); //The tree algorithm instance
        tree.setOptions(options);
        tree.buildClassifier(input);

    }
}