package com;

import java.io.IOException;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.ResponseHandler;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.apache.http.entity.StringEntity;

public class http {
	public static void main(String[] args) throws Exception {
		System.out.println(get("https://baidu.com"));
	}
	
    public static String get(String url) throws Exception{
        CloseableHttpClient httpclient = HttpClients.createDefault();
        HttpEntity httpEntity = null;
        String result = null;
        try{
            HttpGet httpGet = new HttpGet(url);
            CloseableHttpResponse response = httpclient.execute(httpGet);
            httpEntity = response.getEntity();
        }finally{
        	if(httpEntity != null) {
            	result = EntityUtils.toString(httpEntity,"UTF-8");
            }
            httpclient.close();
        }
        return result;
    }
    
   public static String post(String url,String data) throws Exception{
	   CloseableHttpClient httpclient = HttpClients.createDefault();
       HttpEntity httpEntity = null;
       String result = null;
       System.out.print(data);
       try{
           HttpPost httpPost = new HttpPost(url);
           StringEntity stringEntity = new StringEntity(data,"UTF-8");
           httpPost.setEntity(stringEntity);
           CloseableHttpResponse response = httpclient.execute(httpPost);
           httpEntity = response.getEntity();
       }finally{
       	if(httpEntity != null) {
           	result = EntityUtils.toString(httpEntity,"UTF-8");
           }
           httpclient.close();
       }
       return result;
   }
}