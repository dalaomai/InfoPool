package com.servlet;


import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.jasper.tagplugins.jstl.core.Out;

import com.infoPool.bean.User;
import com.infoPool.dbo.UserDao;
import com.alibaba.fastjson.*;
import com.infoPool.bean.LoginMsg;
import com.infoPool.util.JsonRecive;
import com.mysql.cj.Session;
/**
 * Servlet implementation class login
 */
@WebServlet("/login")
public class login extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public login() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		RequestDispatcher rq = request.getRequestDispatcher("/jsp/login.jsp");
		rq.forward(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String requestType = request.getContentType();
		String userName = null;
		String password = null;
		HttpSession session = request.getSession(true);
		//获取提交数据
		if(requestType.indexOf("application/json")!=-1) {	//json处理
			JSONObject json=JsonRecive.receivePost(request);
			userName = json.getString("username");
			password = json.getString("password");
		}else {	//form处理
			userName = request.getParameter("username");
			password = request.getParameter("password");
		}
		LoginMsg loginMsg = null;

		if(userName==null || password==null) {	//信息不全
			loginMsg = new LoginMsg(3,"not enought information about the account","");
		}else {
			UserDao userDao = new UserDao();
			User user = userDao.getUserByName(userName);
			if(user==null) {	//用户不存在
				loginMsg = new LoginMsg(1,"user doesn't exits","");
			}else {		//验证密码
				if(user.verifyPassword(password)) {
					session.setAttribute("user", user);
					loginMsg = new LoginMsg(0,"ok","menu");
				}
				else {
					loginMsg = new LoginMsg(2,"password doesn't right","");
				}
			}
		}

		String result = JSON.toJSONString(loginMsg);
		response.setContentType("application/json; charset=UTF-8");
		response.setCharacterEncoding("utf-8");
		PrintWriter out = response.getWriter();
		out.println(result);
	}

}
