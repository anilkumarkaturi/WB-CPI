import org.apache.hadoop.io.*;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.mapreduce.*;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.Output.FileOutputFormat;


public class ppadriver
{
 public static void main(String[] args) throws Exception
 {
  if(args.length!=2)
  {
   System.err.println("please enter the i/p and o.p parameters");
   System.exit(-1);
  }
 Job job=new Job();
 job.setJarByClass(ppadriver.class);
 job.setJobName("Productionperarea");
 
 FileInputFormat.addInputpath(job.new path(args[0]));
 FileOutputFormat.setoutputpath(job.new path(args[1]));

 job.setMapperClass(ppamapper.class);
 job.setReducerClass(prouceperareareducer.class);

 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(IntWritable.class);

 System.exit(job.waitForCompletion(true)?0:1);
}
}