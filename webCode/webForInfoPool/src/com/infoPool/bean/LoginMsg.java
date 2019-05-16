package com.infoPool.bean;

import com.alibaba.fastjson.*;
import com.alibaba.fastjson.annotation.JSONField;

public class LoginMsg {
	@JSONField(name="code")
	private int code;
	
	@JSONField(name="msg")
	private String msg;
	
	@JSONField(name="redirect")
	private String redirect;
	
	public LoginMsg() {
		// TODO Auto-generated constructor stub
	}

	public LoginMsg(int code, String msg, String redirect) {
		super();
		this.code = code;
		this.msg = msg;
		this.redirect = redirect;
	}

	public int getCode() {
		return code;
	}

	public void setCode(int code) {
		this.code = code;
	}

	public String getMsg() {
		return msg;
	}

	public void setMsg(String msg) {
		this.msg = msg;
	}

	public String getRedirect() {
		return redirect;
	}

	public void setRedirect(String redirect) {
		this.redirect = redirect;
	}
	
	
}
