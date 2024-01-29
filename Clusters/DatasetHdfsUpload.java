package com;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FSDataOutputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import java.io.BufferedInputStream;
import java.io.File;
import java.io.InputStream;
import java.io.FileInputStream;
public class DatasetHdfsUpload {
	File source_file;
	Configuration conf;
public DatasetHdfsUpload(File source_file){
	this.source_file = source_file;
	String hdfsPath = "hdfs://localhost:9000";
    conf = new Configuration();
	conf.set("fs.default.name", hdfsPath);
	//start();
}
public void upload(){
	try{
		FileSystem fileSystem = FileSystem.get(conf);
		String dest = "user/"+source_file.getName();
		Path path = new Path(dest);
		FSDataOutputStream out = fileSystem.create(path);
		InputStream in = new BufferedInputStream(new FileInputStream(source_file));
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