package com;

import java.io.IOException;


import javax.servlet.*;
import javax.servlet.annotation.*;
import javax.servlet.http.*;
import net.sf.json.JSONObject;
import java.net.URLEncoder;
import com.http;
import java.sql.*;
import javax.sql.*;
import javax.naming.*;

import com.beans.InfoBean;

@WebServlet("/showInfo")
public class showInfo extends HttpServlet {

	
	Connection dbconn;
	PreparedStatement pstmt;
	public void init() {
		DataSource dataSource;
		Context context;
		String sql = "select webName,webUrl,title,href,time from web_info order by time desc limit ?,?";
		try {
			context = new InitialContext();
			dataSource = (DataSource)context.lookup("java:comp/env/jdbc/infopool");
			dbconn = dataSource.getConnection();
			pstmt = dbconn.prepareStatement(sql);
			
		} catch (NamingException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} catch (SQLException e2) {
			// TODO Auto-generated catch block
			e2.printStackTrace();
		}
	}
	
	public void finalize() throws SQLException {
		pstmt.close();
		dbconn.close();
	}

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession(true);
		RequestDispatcher rd = request.getRequestDispatcher("index.jsp");
		ResultSet rst;
		InfoBean info;
		String[] webName=null,url=null,title=null,href=null,time=null;
		int page=0,pageSize=10;
		if(request.getParameter("page")!=null) {
			page = Integer.parseInt(request.getParameter("page"));
		}
		try {
			pstmt.setInt(1, page*pageSize);
			pstmt.setInt(2, pageSize);
			rst = pstmt.executeQuery();
			rst.last();
			int length = rst.getRow();
			webName=new String[length];
			url=new String[length];
			title=new String[length];
			href=new String[length];
			time=new String[length];
			rst.first();
			for(int i=0;i<length;i++) {
				webName[i] = rst.getString("webName");
				url[i] = rst.getString("webUrl");
				title[i] = rst.getString("title");
				href[i] = rst.getString("href");
				time[i] = rst.getString("time");
				rst.next();
			}
			rst.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		info = new InfoBean(webName,url,title,href,time);
		session.setAttribute("info", info);
		session.setAttribute("page", page);
		rd.forward(request, response);
	}
}
