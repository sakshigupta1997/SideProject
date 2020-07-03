package email_application;


public class email {
private String first_name;
private String last_name;
private String password;
private String emailid;
private String department;
private int mailbox_capacity=100;
public void setfirst_name(String first_name)
{
	this.first_name=first_name;
}
public String getfirst_name()
{
	return first_name;
}
public void setlast_name(String last_name)
{
	this.last_name=last_name;
}
public String getlast_name() {
	return last_name;
}
public String random_password()
{
	int len=10;
	String password_range="abcdefghijklmnopqrstuvwxyz123456789!@#$";
	char[] password=new char[len];
	for(int i=0;i<len;i++)
	{
		int random=(int)(Math.random() * password_range.length());
		password[i]=password_range.charAt(random);
	}
	return new String(password);
	
}
public void setmailbox_capacity(int mailbox_capacity)
{
	this.mailbox_capacity=mailbox_capacity;
}
public int getmailbox_capacity()
{
	return mailbox_capacity;
}
public void setemailid(String emailid)
{
  this.emailid=emailid;
}
public String getemailid() {
	return this.emailid;
}
public void setdepartment(String department)
{
	this.department=department;
}
public String getdepartment()
{
	return department;
}
public String generate_emailid()
{
	emailid=first_name + "." + last_name + "@"+department+".companyname.org";
	return this.emailid;
}
public void setchange_password(String password)
{
	this.password=password;
}

}
