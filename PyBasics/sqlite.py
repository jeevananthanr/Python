import sqlite3


conn = sqlite3.connect('OLX.db')

#print "Opened database successfully";

conn.execute('''CREATE TABLE SALES
         (FLAG          CHAR(1) NOT NULL,
         DATE_SOLD      INT     NOT NULL,
         PROD_ID        INT    NOT NULL,
         CAT_ID         INT    NOT NULL,
         STATE          INT    NOT NULL,
         REGION         INT    NOT NULL);''')
#print "Table created successfully";
#conn.close()

dict={}
selList=[]
qryList=[]

T=int(input())
#cur=con.cursor()
try:
    
	for i in range(T):
		(X,d,p,s)=(raw_input().strip().split(' '))
	
	
		if X=='S':
			d=int(d)
			if len(p)==1:
				prod_id=int(p)
				cat_id=0
			else:
				prod_id=int(p.split('.')[0])
				cat_id=int(p.split('.')[1])
			if len(s)==1:
				state=int(s)
				reg=0
			else:
				state=int(s.split('.')[0])
				reg=int(s.split('.')[1])
			
			conn.execute("INSERT INTO SALES VALUES(?,?,?,?,?,?)",(X,d,prod_id,cat_id,state,reg));
			conn.commit();
	
		if X=='Q':
			if len(d)==1:
				date_start=int(d)
				date_end=int(d)
			else:
				date_start=int(d.split('.')[0])
				date_end=int(d.split('.')[1])
	
			if p=='-1':
				prod_id=0
				cat_id=0
				op1='>='
				op2='>='
			elif len(p)==1:
				prod_id=int(p)
				cat_id=0
				op1='='
				op2='>='
			else:
				prod_id=int(p.split('.')[0])
				cat_id=int(p.split('.')[1])
				op1='='
				op2='='
	
			if s=='-1':
				state=0
				reg=0
				op3='>='
				op4='>='
			elif len(s)==1:
				state=int(s)
				reg=0
				op3='='
				op4='>='
			else:
				state=int(s.split('.')[0])
				reg=int(s.split('.')[1])
				op3='='
				op4='='
			
			cur1=conn.execute("select count(*) from SALES where (DATE_SOLD between ? and ?) and (PROD_ID"+op1+" ? and CAT_ID"+op2+" ?) and (STATE"+op3+" ? and REGION"+op4+" ?) ",(date_start,date_end,prod_id,cat_id,state,reg));
			
			for col in cur1:
				print col[0]#,col[1],col[2],col[3],col[4],col[5]
except RuntimeError:
	print "RuntimeError!!!!!!!"
	
finally:			

    conn.execute("Drop table SALES");            
    conn.close()

