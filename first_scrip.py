Users = open("G2RHGIUSU0_20170503_0801.csv","r")
RelacionUserTTSS = open("G2RHGIGIN0_20170307_0801.csv","r")
TTSS = open("G2RHGIGRU0_20170307_0801.csv","r")
lineaDeUsuario = Users.readlines() #Guardo las lineas en linea
lineaDeRelacion = RelacionUserTTSS.readlines() #Guardo las lineas en linea
lineaDeTTSS = TTSS.readlines() #Guardo las lineas en linea
Users.close()
RelacionUserTTSS.close()
TTSS.close()
id_ttss_global = '161'
id_user_global = '390'

user_dict = {} # Diccionario de usuarios
rel_TTSS_User = {} # Diccionario relacion usuarios y TTSS
TTSS_dict = {} # Diccionario de TTSS
NombresUser = [] # Array de los Nombres de los Usuarios
NombresTTSS = [] # Array de los Nombres de las TTSS
arrayuser= []
arrayrelacion = []
arrayttss = []

# Creamos un array de usuarios 
for line in lineaDeUsuario:
	user_dict = {}
	lista = list(line.replace('~',',').split(',')) # Convierto en lista
	user_dict['ID_user'] = lista[0] # Asigno cada key de la lista a una clave del diccionario
	user_dict['matricula'] = lista[1]
	user_dict['name'] = lista[2]
	user_dict['mail'] = lista[8]
	user_dict['matr_dacfi'] = lista[9]
	arrayuser.append(user_dict)

# Creamos un array de la relacion de IDs entre usuarios y TTSS
for line in lineaDeRelacion:
	rel_TTSS_User = {}
	lista = line.replace('~',',').split(',')# Convierto en lista
	rel_TTSS_User['ID_user'] = lista[0]
	rel_TTSS_User['ID_Group'] = lista[1].replace('\n','')
	arrayrelacion.append(rel_TTSS_User)

# Creamos un array de los TTSS
for line in lineaDeTTSS:
	TTSS_dict = {}
	lista = list(line.replace('~',',').split(',')) # Convierto en lista
	TTSS_dict['ID_Group'] = lista[0]
	TTSS_dict['name'] = lista[1]
	TTSS_dict['mail'] = lista[7]
	arrayttss.append(TTSS_dict) 

# Metodo para ver que usuarios hay dentro de una TTSS
def users_in_ttss(ts):
	UsersInTTSS = []
	for dictionaries in arrayrelacion:
		if ts == dictionaries['ID_Group']:
			UsersInTTSS.append(dictionaries['ID_user'])
	return UsersInTTSS

# Metodo para ver las TTSS a las que pertenece un usuario
def TTSS_in_users(id_usr):
	TTSSInUser = []
	for dct in arrayrelacion:
		if id_usr == dct['ID_user']:
			TTSSInUser.append(dct['ID_Group'])
	return TTSSInUser

# Metodo para ver los nombres de las TTSS a raiz de su ID
def relacion_id_name_TTSS(id_ts):
	TTSS_name = []
	for d in arrayttss:
		if id_ts == d['ID_Group']:
			TTSS_name.append(d['name'])
	return TTSS_name

# Metodo para ver los nombres de usuario a raiz de su ID
def relacion_id_name_Users(id_user):
	User_Name = []
	for di in arrayuser:
		if id_user == di['ID_user']:
			User_Name.append(di['name'])
	return User_Name

# Traducimos las IDs a nombres
for n in users_in_ttss(id_ttss_global):
	NombresUser.append(relacion_id_name_Users(n))
for c in TTSS_in_users(id_user_global):
	NombresTTSS.append(relacion_id_name_TTSS(c))

print ("El usuario %s, pertenece a los siguientes TTSS: %s" % (relacion_id_name_Users(id_user_global),NombresTTSS))
print ("Los usuarios en %s son: %s" % (relacion_id_name_TTSS(id_ttss_global),NombresUser))