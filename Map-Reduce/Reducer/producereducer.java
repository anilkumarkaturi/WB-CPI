public calss prouceperareareducer{
import org.apache.hadoop.mapreduce.*;

public class prouceperareareducer extends Reducer <Text,IntWritable,Text,IntWritable>
{
public void reduce(Text key,Iterable<IntWritable> values,Context context) throws IOException;
{
int area = 0;
int production = 0;
int productionperarea=0;
for(IntWritable value : values)
           {
                production + = value.get();
}
context.write(key,new IntWritable(production/area));
}
}