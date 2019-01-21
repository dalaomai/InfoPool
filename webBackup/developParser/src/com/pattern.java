package com;

import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.http;
/**
 * Servlet implementation class pattern
 */
@WebServlet("/pattern")
public class pattern extends HttpServlet {
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String url = "http://0.0.0.0:8081/developParser";
		String data = null;
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		BufferedReader reader = request.getReader();
		data = reader.readLine();
		try {
			out.println(http.post(url, data));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

}
