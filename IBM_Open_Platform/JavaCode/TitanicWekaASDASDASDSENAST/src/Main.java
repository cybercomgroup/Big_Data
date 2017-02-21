
/**

 import weka.core.Attribute;
 import weka.core.Instance;
 import weka.core.Instances;
 import weka.core.converters.ConverterUtils;
 import weka.classifiers.trees.J48;
 import java.io.BufferedReader;
 import java.io.FileReader;
 import java.io.IOException;


 public class Main {
 public static void main(String[] args) {
 Instances data;
 try {    //Read inputfile to instances

 data = new Instances(new ConverterUtils.DataSource(args[0]).getDataSet());
 } catch (Exception e) {

 System.err.println(e.toString());
 System.err.println(e.getStackTrace());
 System.out.println("File not found or wrong format");
 return;
 }
 if (data.classIndex() == -1) { //Make sure classindex is set correctly
 data.setClassIndex(data.numAttributes() - 1);
 }

 String[] options = new String[1];
 options[0] = "-U";            // unpruned tree
 J48 tree = new J48();
 try{
 tree.setOptions(options);     // set the options
 tree.buildClassifier(data);   // build classifier
 // new instance of tree
 }catch (Exception e){
 System.err.println("Exception throwin in tree setup");
 System.err.println(e.toString());
 System.err.println(e.getStackTrace());
 }


 }

 }
 **/

/**
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ArffLoader;
import weka.classifiers.bayes.NaiveBayesUpdateable;
**/
public class Main {

    public static void main(String[] args) throws Exception {
        /**

        // load data
        ArffLoader loader = new ArffLoader();
        Path path = new Path("hdfs://eren.tamazin.com:8081/"+ args[0]);
        FileSystem fs = FileSystem.get(new Configuration());
        loader.setSource(fs.open(path));

        System.out.print("asd");

        Instances structure = loader.getStructure();
        structure.setClassIndex(structure.numAttributes() - 1);

        // train NaiveBayes
        NaiveBayesUpdateable nb = new NaiveBayesUpdateable();
        nb.buildClassifier(structure);
        Instance current;
        while ((current = loader.getNextInstance(structure)) != null)
            nb.updateClassifier(current);

        // output generated model
        System.out.println(nb);

         **/
        System.out.println("Ost");
    }
}