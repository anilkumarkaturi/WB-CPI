package com;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;
import javax.swing.JScrollPane;
import javax.swing.JFrame;
import java.awt.Font;
import javax.swing.table.TableColumn;
public class ViewPrediction extends JFrame{
	DefaultTableModel dtm;
	JScrollPane jsp;
	JTable table;
public ViewPrediction(String title){
	setTitle(title);
	dtm = new DefaultTableModel(){
		public boolean isCellEditable(){
			return false;
		}
	};
	dtm.addColumn("Predicted Crop Name");
	dtm.addColumn("Crop Growth for given input");
	table = new JTable(dtm);
	table.getTableHeader().setFont(new Font("Courier New",Font.BOLD,15));
	table.setFont(new Font("Courier New",Font.BOLD,14));
	table.setRowHeight(30);
	jsp = new JScrollPane(table);
	getContentPane().add(jsp);
}
}