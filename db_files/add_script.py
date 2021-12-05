import random

nos = '0123456789'
domains = ['gmail','yahoo','rediffmail','protonmail','emkei']
names = open('names.txt','r').readlines()

room_desc = ['beach view','suite','two rooms','executive suite']

f = open('insert_script.sql','w')
f.write('\c hoteldb\n')

f.write('alter table DEPARTMENT drop constraint department_mgr_id_fkey;\n')
f.write('alter table EMPLOYEE drop constraint MGR_FKEY;\n')
f.write('alter table EMPLOYEE drop constraint FKEY_DNO;\n')

cmd = "INSERT INTO rooms VALUES({},{},{},'{}',{});\n"

for i in range(30):
	r_id = i+1
	floor = random.randint(1,10)
	beds = random.randint(1,3)
	desc = random.choice(room_desc)
	charge = random.randint(1500,7000)
	cmd_ = cmd.format(r_id,floor,beds,desc,charge)
	f.write(cmd_)

filled_rooms = set()
cmd = "INSERT INTO customer values({},'{}','{}',{},'{}','{}',{},{});\n"
for i in range(60):
	id = i+1
	fname,lname = names[i].strip().split()
	phno = int(''.join(random.choices(nos,k=10)))
	email = fname.lower()+lname[:2].lower()+'@'+random.choice(domains)+'.com'
	dob = str(random.randint(1,12))+'/'+str(random.randint(1,28))+'/'+str(random.randint(1960,2002))
	num_people = random.randint(1,5)
	rooms = 'NULL'
	if random.randint(0,1):
		x = random.randint(1,30)
		if x not in filled_rooms:
			filled_rooms.add(x)
			rooms = str(x)
	cmd_ = cmd.format(id,fname,lname,phno,email,dob,num_people,rooms)
	f.write(cmd_)

cmd = "INSERT INTO employee values({},'{}','{}',{},'{}',{},{},{},{});\n"
for i in range(60,len(names)):
	id = i-59
	fname,lname = names[i].strip().split()
	phno = int(''.join(random.choices(nos,k=10)))
	dob = str(random.randint(1,12))+'/'+str(random.randint(1,28))+'/'+str(random.randint(1960,2002))
	salary = random.randint(3000,100000)
	acc_num = int(''.join(random.choices(nos,k=10)))
	dept_id = random.randint(1,5)
	mgr_id = random.randint(1,5)
	if id <= 5:
		dept_id = id
		mgr_id = id
	cmd_ = cmd.format(id,fname,lname,phno,dob,salary,acc_num,dept_id,mgr_id)
	f.write(cmd_)

cmd = "INSERT INTO department VALUES('{}','{}',{},{});\n"
f.write(cmd.format('Food','Kitchen',1,1))
f.write(cmd.format('Help','Housekeeping',2,2))
f.write(cmd.format('Security','Security',3,3))
f.write(cmd.format('Accounts','Accounts',4,4))
f.write(cmd.format('Inventory','Inventory',5,5))

cmd = "INSERT INTO services VALUES({},'{}',{},'{}',{});\n"
f.write(cmd.format(1,'Cleaning room',200,'Cleaning',2))
f.write(cmd.format(2,'Get food at room',200,'Room Service',1))
f.write(cmd.format(3,'Laundry',200,'Laundry',2))

cmd = "INSERT INTO hotel VALUES('Taj',3749573940,'taj@pes.edu',1);\n"
f.write(cmd)

f.write('alter table DEPARTMENT add constraint department_mgr_ssn_fkey FOREIGN KEY (D_MANAGER_ID) REFERENCES  EMPLOYEE(E_ID);\n')
f.write('alter table EMPLOYEE add constraint MGR_FKEY FOREIGN KEY (E_MGR_ID) REFERENCES  EMPLOYEE(E_ID);\n')

f.close()
