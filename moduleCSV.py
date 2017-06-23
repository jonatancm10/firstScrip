import csv

id_ttss_global = '161'
id_user_global = '390'
arrayttss = []
arrayrelacion = []
arrayuser = []

with open("G2RHGIUSU0_20170503_0801.csv", 'rb') as csvfile:
	user = csv.DictReader(csvfile, delimiter = '~', quotechar = '|')
	for row in user:
		arrayuser.append(row)
csvfile.close()

with open("G2RHGIGIN0_20170307_0801.csv", 'rb') as csvfile2:
	relacion = csv.DictReader(csvfile2, delimiter = '~', quotechar = '|')
	for row2 in relacion:
		arrayrelacion.append(row2)
csvfile2.close()

with open("G2RHGIGRU0_20170307_0801.csv", 'rb') as csvfile3:
	ttss = csv.DictReader(csvfile3, delimiter = '~', quotechar = '|')
	for row3 in ttss:
		arrayttss.append(row3)
csvfile3.close()

# Metodo retorna los usuarios que hay dentro de una TTSS
def users_in_ttss(ts):
	UsersInTTSS = []
	for dictionaries in arrayrelacion:
		if ts == dictionaries['ID_GRUPO']:
			UsersInTTSS.append(dictionaries['\xef\xbb\xbfID_USUARIO||'])
	return UsersInTTSS

# Metodo que retorna las TTSS a las que pertenece un usuario
def TTSS_in_users(id_usr):
	TTSSInUser = []
	for dct in arrayrelacion:
		if id_usr == dct['\xef\xbb\xbfID_USUARIO||']:
			TTSSInUser.append(dct['ID_GRUPO'])
	return TTSSInUser

print ("El usuario %s, pertenece a los siguientes TTSS: %s" % (id_user_global,TTSS_in_users(id_user_global)))
print ("Los usuarios en %s son: %s" % (id_ttss_global,users_in_ttss(id_ttss_global)))