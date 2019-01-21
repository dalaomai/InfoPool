package com.infoPool.dbo;
import com.infoPool.dbo.BaseDao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import com.infoPool.bean.*;
public class UserDao extends BaseDao{
	public User getUserByName(String userName) {
		User user = new User();
		String sql = "select id,userName,password,permission,wechatId,wechatName,registerTime,phoneNumber,emailAddress,updateTime from User where userName=?";
		try(
				Connection conn = dataSource.getConnection();
				PreparedStatement pstmt = conn.prepareStatement(sql);
			)
		{
			pstmt.setString(1, userName);
			try(
					ResultSet rst = pstmt.executeQuery();
				)
			{
				if(rst.next()) {
					user.setId(rst.getInt("id"));
					user.setUserName(rst.getString("userName"));
					user.setPassword(rst.getString("password"),false);
					user.setPermission(rst.getString("permission"));
					user.setWechatId(rst.getString("wechatId"));
					user.setWechatName(rst.getString("wechatName"));
					user.setRegisterTime(rst.getDate("registerTime"));
					user.setPhoneNumber(rst.getString("phoneNumber"));
					user.setEmailAddress(rst.getString("emailAddress"));
					user.setUpdateTime(rst.getDate("updateTime"));
					return user;
				}else {
					return null;
				}
			}
		}catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			return null;
		}
	}
	

}
