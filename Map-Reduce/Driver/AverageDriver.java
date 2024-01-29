import org.apache.hadoop.io.*;

public class AverageDriver
{
 public void main(String[] args) throws Exception
 {
  if(args.length!=2)
  {
   System.err.println("please enter the i/p and o.p parameters");
   System.exit(-1);
  }
 Job job=new Job();
 job.setJarByClass(AverageDriver.class);
 job.setJobName("Max temperature");
 
 FileInputFormat.addInputpath(job.new path(args[0]));
 FileOutputFormat.setoutputpath(job.new path(args[0]));

 job.setMapperClass(AverageMapper.class);
 job.setReducerClass(AverageReducer.class);

 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(IntWritable.class);

 System.exit(job.waitForCompletion(true)?0:1);
}
}
 

 
 