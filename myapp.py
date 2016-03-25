from app import app
from flask import render_template, redirect, request
import mmap
a=[]
a_list=a
a_l=a
files = "myfile.txt"
filename=files


@app.route('/reg', methods = ['GET', 'POST'])
def reg():
        if request.method == 'POST':
                global r_user
                global r_pass
                r_user = request.form['name']
                r_pass = request.form['password']
                if(r_pass=="zaid"):
                        files = "myfile.txt"
                        filename=files

                
                        reg_data = [r_user,r_pass]
                        reg_data_string = "\t".join(reg_data)

                
                        f = open(files,'a')
                        f.write(reg_data_string + "\n")
                        f.close()
                        return render_template('login.html')
                else:
                                 
                        return render_template('error.html')
        else:
                return render_template('reg.html')



@app.route('/login', methods = ['GET', 'POST'])
def login():
        if request.method == 'POST':
                c_user=request.form['name']
                user=c_user
             
                with open('myfile.txt', 'r') as searchfile:
                        for line in searchfile.readlines():
                                if user in line:
                                        return render_template('menu1.html')
                                else:
                                        return render_template('error.html')
        else:
                return render_template('login.html')
        files.close()



@app.route('/addCar', methods = ['GET', 'POST'])
def create_car():
	if request.method == 'POST': 
		c_make = request.form['make']
		c_model = request.form['model']
		c_reg = request.form['reg']
		c_year = request.form['year']
		c_engine = request.form['engine']
		c_price = request.form['price']
		c_phone = request.form['phone']
		c_email = request.form['email']

		a.append(c_make)
		a.append(c_model)
		a.append(c_reg)
		a.append(c_year)
		a.append(c_engine)
		a.append(c_price)

                log_data = [c_make,c_model,c_reg,c_year,c_engine,c_price,c_phone,c_email]
                log_data_string = "\t".join(log_data)

                filename = "cars.txt"

                f = open(filename,'a')
                f.write(log_data_string + "\n")
                f.close()
                
	
		return render_template('show_car.html',a=a_list,make=c_make, model=c_model,reg=c_reg,year=c_year,engine=c_engine,price=c_price,email=c_email,phone=c_phone)
        else:
		return render_template('create_car.html')

	


@app.route('/search', methods = ['GET', 'POST'])
def search_car():
        if request.method == 'POST':
                search_r=request.form['sreg']
                sreg=search_r
                c_p=a_list[0]
                c_p1=a_list[1]
                c_p2=a_list[2]
                c_p3=a_list[3]
                c_p4=a_list[4]
                c_p5=a_list[5]
                
               # with open('cars.txt', 'r') as searchfiles:
                        #for line in searchfiles.readlines():
                              #  if search_r in line:
                if(search_r in a_list):
                                        
                        return render_template('show.html',c=c_p,c1=c_p1,c2=c_p2,c3=c_p3,c4=c_p4,c5=c_p5)
                else:
                        return render_template('error.html')
        else:
                return render_template('search.html')



@app.route('/remove1',methods = ['GET', 'POST'])
def remove1():
        if request.method == 'POST':
                a=a_list.pop(0)
                b=a_list.pop(1)
                c=a_list.pop(2)
               #d=a_list.pop(-1)
                #a_list.pop(4)
                #f=a_list.pop(5)
                #g=a_list.pop(6)
                #=a_list.pop(7)
                c_make = request.form['make']
		c_model = request.form['model']
		c_reg = request.form['reg']
		c_year = request.form['year']
		c_engine = request.form['engine']
		c_price = request.form['price']
		c_phone = request.form['phone']
		c_email = request.form['email']
                n=c_reg
		
		a_list.append(c_make)
		a_list.append(c_model)
		a_list.append(c_reg)
		a_list.append(c_year)
		a_list.append(c_engine)
		a_list.append(c_price)
		a_list.append(c_phone)
            
		with open("cars.txt","r") as input:
                    with open("updated.txt","wb") as output: 
                        for  line in input:
                            if n in line +"\n":
                               
                               log_data = [c_make,c_model,c_reg,c_year,c_engine,c_price,c_phone,c_email]
                               log_data_string = "\t".join(log_data)
                               output.write(log_data_string+"\n")
                               
	
		return render_template('show_car.html',make=c_make, model=c_model,reg=c_reg,year=c_year,engine=c_engine,price=c_price,email=c_email,phone=a)
        else:
		return render_template('remove1.html')


@app.route('/contact', methods = ['GET', 'POST'])
def contact():
        return render_template('contact.html')       
               		
