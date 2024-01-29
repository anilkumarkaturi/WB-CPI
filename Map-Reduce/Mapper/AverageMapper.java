import org.apache.hadoop.io.*;

public class AverageMapper extends Mapper <LongWritable, Text, Text, IntWritable>
{
 public static final int Missing=9999;
 public void Map(LongWritable key, Text Value,Text Value,Text Value, Context context)throws IOException, InterruptedException
 {
  String line=value.toString();
  String year=line.substring(6,10);
  String region;
  int temperature;
  temperature=Integer.parseInt((line.substring(86,92));
  String quality=line.substring(11);
  if(temperature !=Misssing && quality.Matches("[01458]"));
  context.write(new Text(year),new IntWritable(temperature));
 }
}