import org.apache.hadoop.mapreduce.*;
import java.io.IOException;
import org.apache.hadoop.io.*;


public class rainfallreducer extends Reducer <Text,IntWritable,Text,IntWritable>
{
public void reduce(Text key,Iterable<IntWritable> values,Context context) throws IOException;
{
int max_rainfall = 0;
int count = 0;
for(IntWritable value : values)
           {
                max_rainfall + = value.get();
                count+=1;
}
context.write(key,new IntWritable(max_rainfall/count));
}
}