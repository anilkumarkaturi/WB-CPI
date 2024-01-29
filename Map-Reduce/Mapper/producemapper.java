import org.apache.hadoop.io.*;
public class ppamapper extends Mapper <LongWritable,Text,Text,IntWritable>
{
public static final int MISSING = 9999;
public void map(LongWritable key,Text value,Context context) throws IOException, InterruptedException
{
    String Line = value.toString();
    String year = line.SubString(21,31);
    int production;
    int area;
    production = Integer.parseInt(line.substring(60,92));
    area = Integer.parseInt(line.substring(64,67));
    String quality = line.substring(11);
    if (production !=MISSING && quality.matches("[01459]"))
    context.write(new Text(year),new intWritable(production));
    if (area != MISSING && quality.matches("[01459]"))
              context.write(new Text(year),new IntWritable(area));
}
}