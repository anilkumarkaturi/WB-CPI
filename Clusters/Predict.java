package com;
import java.util.Comparator;
public class Predict implements Comparator<Predict>{
	String crop;
	double score;
public void setCrop(String crop){
	this.crop = crop;
}
public String getCrop(){
	return crop;
}

public void setScore(double score){
	this.score = score;
}
public double getScore(){
	return score;
}
public int compare(Predict p1,Predict p2){
	double s1 = p1.getScore();
    double s2 = p2.getScore();
	if (s1 == s2)
		return 0;
    else if (s1 > s2)
    	return 1;
    else
		return -1;
}
}