package com;
import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
public class ReadHdfsDataset{
	Configuration conf;
public ReadHdfsDataset(){
	String hdfsPath = "hdfs://localhost:9000";
    conf = new Configuration();
	conf.set("fs.default.name", hdfsPath);
}
public void read(){
	try{
		FileSystem fileSystem = FileSystem.get(conf);
		Path path = new Path("user/venkatesh/user/Crop_recommendation.csv");
		FSDataInputStream in = fileSystem.open(path);
		OutputStream out = new BufferedOutputStream(new FileOutputStream(new File("com/data.csv")));
		byte[] b = new byte[1024];
		int numBytes = 0;
		while ((numBytes = in.read(b)) > 0) {
			out.write(b, 0, numBytes);
		}
		in.close();
		out.close();
		fileSystem.close();
	}catch(Exception e){
		e.printStackTrace();
	}
}
}