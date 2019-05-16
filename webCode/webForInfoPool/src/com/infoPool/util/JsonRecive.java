package com.infoPool.util;

import com.alibaba.fastjson.*;
import javax.servlet.http.HttpServletRequest;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
public class JsonRecive {
	public static JSONObject receivePost(HttpServletRequest request) throws UnsupportedEncodingException, IOException {
		BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(request.getInputStream(), "utf-8"));
		String line = null;
		StringBuilder sBuilder = new StringBuilder();
		while((line=bufferedReader.readLine())!=null) {
			sBuilder.append(line);
		}
		JSONObject json=JSONObject.parseObject(sBuilder.toString());
		return json;
	}
}
