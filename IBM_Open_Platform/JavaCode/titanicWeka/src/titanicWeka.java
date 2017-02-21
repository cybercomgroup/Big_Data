

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import weka.core.Instance;
import weka.core.Instances;
import weka.core.converters.ArffLoader;
import weka.classifiers.bayes.NaiveBayesUpdateable;


public class TitanicWeka {

    public static void main(String[] args) throws Exception {
        // load data
        ArffLoader loader = new ArffLoader();
        //Path path = new Path("hdfs://eren.tamazin.com:8081/"+ args[0]);
        Path path = new Path("hdfs://computer1.philiplaine.com:8020/"+ args[0]);
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
    }
}