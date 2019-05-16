package com.infoPool.bean;

import java.util.Date;
import com.infoPool.util.Md5;

/**
 * @author maizh
 *
 */
public class User {
	private int id;
	private String userName;
	private String password;
	private String permission;
	private String wechatId;
	private String wechatName;
	private Date registerTime;
	private String phoneNumber;
	private String emailAddress;
	private Date updateTime;
	
	public User() {
		// TODO Auto-generated constructor stub
	}

	public User(int id, String userName, String password, String permission, String wechatId, String wechatName,
			Date registerTime, String phoneNumber, String emailAddress, Date updateTime) {
		super();
		this.id = id;
		this.userName = userName;
		this.password = password;
		this.permission = permission;
		this.wechatId = wechatId;
		this.wechatName = wechatName;
		this.registerTime = registerTime;
		this.phoneNumber = phoneNumber;
		this.emailAddress = emailAddress;
		this.updateTime = updateTime;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password,boolean isClearPassword) {
		/*
		 * 转换为Md5
		 */
		if(isClearPassword) {
			Md5 md5 = new Md5();
			this.password = md5.calculate(password);
		}else {
			this.password = password;
		}
		
	}

	public String getPermission() {
		return permission;
	}

	public void setPermission(String permission) {
		this.permission = permission;
	}

	public String getWechatId() {
		return wechatId;
	}

	public void setWechatId(String wechatId) {
		this.wechatId = wechatId;
	}

	public String getWechatName() {
		return wechatName;
	}

	public void setWechatName(String wechatName) {
		this.wechatName = wechatName;
	}

	public Date getRegisterTime() {
		return registerTime;
	}

	public void setRegisterTime(Date registerTime) {
		this.registerTime = registerTime;
	}

	public String getPhoneNumber() {
		return phoneNumber;
	}

	public void setPhoneNumber(String phoneNumber) {
		this.phoneNumber = phoneNumber;
	}

	public String getEmailAddress() {
		return emailAddress;
	}

	public void setEmailAddress(String emailAddress) {
		this.emailAddress = emailAddress;
	}

	public Date getUpdateTime() {
		return updateTime;
	}

	public void setUpdateTime(Date updateTime) {
		this.updateTime = updateTime;
	}
	
	public boolean verifyPassword(String password) {
		/*
		 * 验证密码是否正确
		 */
		Md5 md5 = new Md5();
		password = md5.calculate(password);
		return this.password.equals(password);
	}
}
