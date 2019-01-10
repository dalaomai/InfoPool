package com.beans;

import net.sf.json.JSONObject;

public class InfoBean {
	//数组均为浅复制
	
	private String[] webName;
	private String[] title;
	private String[] href;
	private String[] url;
	private String[] time;

	
	public InfoBean(String[] webName,String[] url,String[] title,String[] href,String[] time) {
		this.webName = webName;
		this.title = title;
		this.href = href;
		this.url = url;
		this.time = time;
	}
	public InfoBean() {}
	
	public String[] getWebName() {return this.webName;}
	public String[] getTitle() {return this.title;}
	public String[] getHref() {return this.href;}
	public String[] getUrl() {return this.url;}
	public String[] getTime() {return this.time;}

	
	public void setWebName(String[] webName) {this.webName=webName;}
	public void setTitle(String[] title) {this.title=title;}
	public void setHref(String[] href) {this.href=href;}
	public void setUrl(String[] url) {this.url=url;}
	public void setTime(String[] time) {this.time=time;}
}
