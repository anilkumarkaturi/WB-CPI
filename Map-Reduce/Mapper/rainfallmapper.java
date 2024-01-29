import org.apache.hadoop.io.*;
public class rainfallmapper extends Mapper <LongWritable,Text,Text,IntWritable>
{
public static final int MISSING = 9999;
public void map(LongWritable key,Text value,Context context) throws IOException, InterruptedException
{
    String Line = value.toString();
    String year = line.SubString(14,10);
    int rainfall;
    rainfall = Integer.parseInt(lint.substring(88,92))
    
    String quality = line.substring(11);
    if (rainfall !=MISSING && quality.matches("[01459]"))
    context.write(new Text(year),new intWritable(rainfall));
    
}
}