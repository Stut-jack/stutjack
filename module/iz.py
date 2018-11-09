import os, sys

print ("\033[1;32mMasukan UserName&Password:)")
print ("\033[1;31;1mKalo Gak Tau Pm Gw Stut-jack 081234581120")
username = 'gw'      
password = 'gans'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome Sayang", 
			sys.exit()

		else:
			print "\n\033[1;36mSalah Bego Goblok !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSok Pinter lu !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
