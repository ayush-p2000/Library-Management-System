import streamlit as st
import mysql.connector
import pandas as pd
import datetime
st.title("LIBRARY MANAGEMENT SYSTEM")
st.sidebar.image("https://www.skoolbeep.com/blog/wp-content/uploads/2020/12/HOW-DO-YOU-DESIGN-A-LIBRARY-MANAGEMENT-SYSTEM-min.png")
choice=st.sidebar.selectbox("My Menu",("HOME","USER REGISTER","USER LOGIN","ADMIN LOGIN"))



if(choice=="HOME"):
    st.image("https://img.freepik.com/free-vector/female-smiling-librarian-standing-counter-book-shelf-paper-flat-vector-illustration-city-library-knowledge_74855-8364.jpg")
    st.markdown("<center><h1>WELCOME</h1></center>",unsafe_allow_html=True)
    st.write("This is a Data Management Application which is developed by Ayush")



elif(choice=="USER LOGIN"):


    if 'login' not in st.session_state:
        st.session_state['login']=False     
    uid=st.text_input("Enter User ID")
    pwd=st.text_input("Enter Password")                          
    btn=st.button("LOGIN")


    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
        c=mydb.cursor()
        c.execute("select * from users")
        for row in c:

            if(uid==row[0] and pwd==row[1]):
                st.session_state['login']=True
                break

        if(st.session_state['login']==False):
            st.header("Incorrect ID or Password")


    if(st.session_state['login']):
        st.header("Login Successfull")
        choice2=st.selectbox("Features",("None","View All Books","Issue All Books"))

        if(choice2=="View All Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
            df=pd.read_sql("select * from books",mydb)
            link=df._get_value(0,'authorname')
            st.image(link)
            st.dataframe(df)

        elif(choice2=="Issue All Books"):
            bid=st.text_input("Enter Book ID")
            usid=st.text_input("Enter your User ID")
            btn3=st.button("Issue")

            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
                c=mydb.cursor()
                issueid=str(datetime.datetime.now())
                c.execute("insert into issue values(%s,%s,%s)",(issueid,bid,usid))
                mydb.commit()
                st.write("Book Issued Successfully at ID:",issueid)




elif(choice=="ADMIN LOGIN"):


    if 'admlgn' not in st.session_state:
        st.session_state['admlgn']=False
    aid=st.text_input("Enter Admin ID")
    pwd=st.text_input("Enter Password")   
    btn=st.button("LOGIN")


    if btn:
        mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
        c=mydb.cursor()
        c.execute("select * from admins")

        for row in c:

            if(aid==row[0] and pwd==row[1]):
                st.session_state['admlgn']=True
                break

        if(st.session_state['admlgn']==False):
            st.header("Incorrect ID or Password")

    if(st.session_state['admlgn']):
        st.header("Login Successfull")
        choice2=st.selectbox("Features",("None","View Issue Books","Add the Books"))

        if(choice2=="View Issue Books"):
            mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
            df=pd.read_sql("select * from issue",mydb)
            st.dataframe(df)

        elif(choice2=="Add the Books"):
            bid=st.text_input("Enter Book ID")
            bookname=st.text_input("Enter Book Name")
            aname=st.text_input("Enter Author Name")
            btn3=st.button("Add Book")

            if btn3:
                mydb=mysql.connector.connect(host="localhost",user="root",password="123456789",database="library")
                c=mydb.cursor()
                c.execute("insert into books values(%s,%s,%s)",(bid,bookname,aname))
                mydb.commit()
                st.write("Book Added Successfully at ID:",bid)




elif(choice=="USER REGISTER"):
    usr=st.text_input("Enter a Username")
    pswd=st.text_input("Choose Password")
    cpswd=st.text_input("Confirm Password")
    regbtn=st.button("Register")


    if regbtn:
        mydb = mysql.connector.connect(host="localhost", user="root", password="123456789", database="library")
        c = mydb.cursor()
        c.execute("select * from users")

        for row in c:
            if (usr == row[0]):
                flag=False

        if(flag==True):

            if(pswd==cpswd):
                mydb = mysql.connector.connect(host="localhost", user="root", password="123456789", database="library")
                c = mydb.cursor()
                c.execute("insert into users values(%s,%s)",(usr,pswd))
                mydb.commit()
                st.write("User Registered Successfully")
            else:
                st.write("Passwords doesn't match")

