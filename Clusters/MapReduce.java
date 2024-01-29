package com;
import java.io.IOException;
import java.util.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.io.*;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;
import java.math.BigInteger;
public class MapReduce extends MapReduceBase implements Mapper<LongWritable,Text,Text,Text> {
	IntWritable one = new IntWritable(1);
    Text locText = new Text();
	Text empty = new Text();
//function to calculate distance between cluster points and if lower distance then poinst are closer
private double distance(double[] a, double[] b) {
	double diff_square_sum = 0.0;
    for (int i = 0; i < a.length; i++) {
		diff_square_sum += (a[i] - b[i]) * (a[i] - b[i]);
	}
	return Math.sqrt(diff_square_sum);
}
//map reduce will call MAP function to process data	
public void map(LongWritable key,Text value,OutputCollector<Text,Text> output,Reporter reporter) throws IOException {
	String line = value.toString(); //read data from hadoop
	if(MainScreen.process > 0) {
		String arr[] = line.split(",");
		double d[] = new double[arr.length-1];
		for(int i=0;i<arr.length-1;i++) {
			d[i] = Double.parseDouble(arr[i]);
		}
		double mindistance = Double.MAX_VALUE;
	    int cluster = -1;
		for(int i=0;i<MainScreen.centroids.size();i++){
			double distance = distance(d, MainScreen.centroids.get(i)); //calculate distnace and put mindistnace in same cluster 
			if(distance < mindistance){
				mindistance = distance;
				cluster = i;
			}
		}
		String name = arr[arr.length-1];
		double distance = distance(d, MainScreen.testData);
		if(distance < 100) {
			Predict p =new Predict();
			p.setCrop(name);
			p.setScore(distance);
			MainScreen.predict.add(p);
		}
		IntWritable winnerCentroid = new IntWritable(cluster);
		MainScreen.addData(winnercentroid,name+","+arr[3]+","+arr[6]);
	}
	MainScreen.process = MainScreen.process + 1;	
}
}