package com.infoPool.dbo;

import java.sql.*;
import javax.sql.DataSource;
import javax.naming.*;
public class BaseDao {
    DataSource dataSource;
    public BaseDao() {
		// TODO Auto-generated constructor stub
    	try {
    		Context context = new InitialContext();
    		dataSource = (DataSource)context.lookup("java:comp/env/jdbc/mysql_test");
    	}catch (Exception e) {
			// TODO: handle exception
    		e.printStackTrace();
		}
	}
    public Connection getConnection() throws Exception{
		return dataSource.getConnection();
	}
}
