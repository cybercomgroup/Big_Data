/**

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.util.*;

public class Titanic extends Configured implements Tool {

    public static void main(String args[]) throws Exception {
        int res = ToolRunner.run(new Titanic(), args);
        System.exit(res);
    }

    public int run(String[] args) throws Exception {
        Path inputPath = new Path(args[0]);
        Path outputPath = new Path(args[1]);

        Configuration conf = getConf();
        Job job = new Job(conf, this.getClass().toString());

        FileInputFormat.setInputPaths(job, inputPath);
        FileOutputFormat.setOutputPath(job, outputPath);

        job.setJobName("Titanic");
        job.setJarByClass(Titanic.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        job.setMapperClass(Map.class);
        job.setCombinerClass(Reduce.class);
        job.setReducerClass(Reduce.class);

        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        @Override
        public void map(LongWritable key, Text value,
                        Mapper.Context context) throws IOException, InterruptedException {
            String line = value.toString();
            StringTokenizer tokenizer = new StringTokenizer(line);
            while (tokenizer.hasMoreTokens()) {
                word.set(tokenizer.nextToken());
                context.write(word, one);
            }
        }
    }

    public static class Reduce extends Reducer<Text, IntWritable, Text, IntWritable> {

        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
            int sum = 0;
            for (IntWritable value : values) {
                sum += value.get();
            }

            context.write(key, new IntWritable(sum));
        }
    }

}

 **/







import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.StringReader;
import java.nio.charset.StandardCharsets;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import au.com.bytecode.opencsv.CSVReader;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.aggregate.DoubleValueSum;
import org.apache.hadoop.mapreduce.lib.input.*;
import org.apache.hadoop.mapreduce.lib.output.*;
import org.apache.hadoop.util.*;
import weka.classifiers.evaluation.output.prediction.CSV;

public class Titanic extends Configured implements Tool {

    public static void main(String args[]) throws Exception {
        int res = ToolRunner.run(new Titanic(), args);
        System.exit(res);
    }

    public int run(String[] args) throws Exception {
        Path inputPath = new Path(args[0]);
        Path outputPath = new Path(args[1]);

        Configuration conf = getConf();

        Job job = Job.getInstance(conf, this.getClass().toString());

        FileInputFormat.setInputPaths(job, inputPath);
        FileOutputFormat.setOutputPath(job, outputPath);

        job.setJobName("Titanic");
        job.setJarByClass(Titanic.class);
        job.setInputFormatClass(TextInputFormat.class);
        job.setOutputFormatClass(TextOutputFormat.class);
        job.setMapOutputKeyClass(Text.class);
        job.setMapOutputValueClass(IntWritable.class);
        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        job.setMapperClass(Map.class);
        //job.setCombinerClass(Reduce.class);
        job.setNumReduceTasks(0);
        //job.setReducerClass(Reduce.class);

        return job.waitForCompletion(true) ? 0 : 1;
    }

    public static class Map extends Mapper<LongWritable, Text, Text, IntWritable> {
        private final static IntWritable one = new IntWritable(1);
        private Text word = new Text();

        @Override
        public void map(LongWritable key, Text value, Mapper.Context context) throws IOException, InterruptedException {
            // Skip the first header
            if (Integer.parseInt(key.toString()) == 0) {
                return;
            }

            CSVReader reader = new CSVReader(new StringReader(value.toString()), ',');
            List<String> csv = Arrays.asList(reader.readNext());

            /*
            0   PassengerId
            1   Survived
            2   Pclass
            3   Name - getTitle()
            4   Sex
            5   Age  - group by 0-18 + 60-* and the rest (Exposed and not exposed)
            6   SibSp
            7   Parch
            8   Ticket - Only the letters
            9   Fare
            10  Cabin - Map letter order as value
            11  Embarked
            */

            // Replace name with only title
            csv.set(3, getTitle(csv.get(3)));

            //Group ages
            if(csv.get(5).length() > 0) {
                Double age = Double.parseDouble(csv.get(5));
                if(age > 18 && age < 60) {
                    csv.set(5, "1");
                } else {
                    csv.set(5, "0");
                }
            } else{
                csv.set(5, "-1");
            }


            // Removes the numbers from the ticket
            csv.set(8, csv.get(8).replaceAll("[0-9 ]*", "")); //Toxic as shits, replaces in the wrong places


            // Ranks the cabin based on letter order or 0
            if (csv.get(10).isEmpty() == false) {
                csv.set(10, (String.valueOf(csv.get(10).charAt(0) - 'A' + 1)));

            } else {
                csv.set(10, "0");
            }

            // Write the result
            word.set(String.join(",", csv));
            context.write(word, one);
        }
    }

    private static String getTitle(String name){
        StringBuilder title = new StringBuilder();
        boolean keep = false;
        for(char c : name.toCharArray()){
            if(c == ','){
                keep = true;
            }else if(c == '.'){
                break;
            }
            if(keep){
                title.append(c);
            }
        }
        title.delete(0,2); // delete the ", "
        return title.toString();
    }


}

