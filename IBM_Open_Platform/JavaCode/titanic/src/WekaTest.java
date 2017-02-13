import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;

import org.apache.commons.io.FilenameUtils;
import weka.classifiers.Classifier;
import weka.classifiers.Evaluation;
import weka.classifiers.evaluation.NominalPrediction;
import weka.classifiers.rules.DecisionTable;
import weka.classifiers.rules.PART;
import weka.classifiers.trees.DecisionStump;
import weka.classifiers.trees.J48;
import weka.core.FastVector;
import weka.core.Instances;




public class WekaTest {



    public static BufferedReader readDataFile(String filename) throws Exception{
        String[] compatibleExtension = {"arff", "csv"};

        BufferedReader inputReader = null;

        String extension = FilenameUtils.getExtension(filename);



        if(extension.compareTo(compatibleExtension[0]) == 0){ //arff
            try {
                inputReader = new BufferedReader(new FileReader(filename));
            } catch (FileNotFoundException ex) {
                System.err.println("File not found: " + filename);
            }
        } else if(extension.compareTo(compatibleExtension[1]) == 0){ //csv

        }else{
            throw new Exception("Not compatible extension:(" + extension + ")\nCompatible extensions: " + compatibleExtension.toString());
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




    }
}