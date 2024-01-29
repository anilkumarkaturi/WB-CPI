import org.apache.hadoop.io.*;



public class rainfalldriver
{
 public static void main(String[] args) throws Exception
 {
  if(args.length!=2)
  {
   System.err.println("please enter the i/p and o.p parameters");
   System.exit(-1);
  }
 Job job=new Job();
 job.setJarByClass(rainfalldriver.class);
 job.setJobName("Max Rainfall");
 
 FileInputFormat.addInputpath(job.new path(args[0]));
 FileOutputFormat.setoutputpath(job.new path(args[1]));

 job.setMapperClass(rainfallmapper.class);
 job.setReducerClass(rainfallreducer.class);

 job.setOutputKeyClass(Text.class);
 job.setOutputValueClass(IntWritable.class);

 System.exit(job.waitForCompletion(true)?0:1);
}
}