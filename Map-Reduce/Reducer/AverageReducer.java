import org.apache.hadoop.mapreduce.*;

public class AverageReducer extends Reducer<Text, IntWritable,Text, IntWritable>
{
 public void reduce(Text key, Iterable<IntWritable> values, Context context)throws IOException
 {
  int max_temp=0;
  int count=0;
  for(IntWritable value:values)
  {
    max_temp+=value.get();
    count+=1;
  }
  context.write(key, new IntWritable(max_temp/count));
 }
}