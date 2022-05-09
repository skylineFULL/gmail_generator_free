 импорт случайных
 время импорта

#ЗАЩИТА ПАРОЛЕМ_____________________________________

pass_combos = ['1','2','3','4','5','6','7','8','9','10',' a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
               "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z','_','-','!','@','#','$','%','^','&','*','(',')']



def pass1():
    pas1 = f'{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}{random.choice(pass_combos)}'
    печать (pas1)

#FIRST/LAST NAME_____________________________________

first_n = ['Jimmy','Edward','Sheldon','Robert','Ben','James','George','Brian','Gary','Larry','Daniel','Mark','David','William','Joshua','Ralph','Keith','Fred','Todd','Shawn','Jesse','Dale','Jacob','Ray','Clifford','Jim',
           'Alex','Greg','Tim','Zachary','Rick','Nathaniel','Brad','Cory','Neil','Cody','Chase','Jordan','Wade','Seth','Andy','Ross','Julian','Morris','Kirk','Bob','Christian','Javier','Raul','Arnold','Hairy','Ralph',
           'Logan','Jack','Aiden','Owen','Elijah','Luke','Isaac','Gabriel','Miles','Jeremiah','Ian','Carson','Axel','Bryson','Kai',"Брейден","Гэвин","Тайлер","Диего","Кевин","Броуди","Патрик","Феликс","Энцо","Джейден",
           'Mia','Ella','Scarlett','Emily','Victoria','Layla','Grace','Madison','Leah','Zoe','Stella','Hazel','Bella','Aurora','Audrey',"Сара","Каролина","Элис","Ева","Сэди","Алекса","Уиллоу","Пайпер","Куинн",
           'Eliana','Rylee','Taylor','Mary','Faith','Kayla','Arya','Lily','Morgan','Trinity','Reese','Molly','Alina','Fiona','Angelina','Amara','Juliet','Dakota','Lola','Maggie','Olvie','Thea','Ruby','Gabriela']

last_n = ['Smith','Greyson','Jones','Brown','Lopez','Johnson','Lee','Clark','Martin','Davis','Miller','Young','Torres','Evans','Cruz','Gomez','Adams','Reed','Peterson','Price','West','Ford','Pitts','Woods','Owens',
          'Olson','Simmons','Long','Bell','Peterson','Ochoa','Robbins','Higgins','Strong','Giles','Ramirez','Wilson','Roberts','Hall','Jones',"Эрнандес","Батлер","Перес","Тернер","Уокер","Флорес","Рид","Роджерс"]

def full_n():
    name = f'{random.choice(first_n)} {random.choice(last_n)}'
    печать (имя)


#EMAIL USERNAME_____________________________________

word_1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0',]

word_2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_4 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_5 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_6 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_7 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_8 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0','.']

word_9 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          '1','2','3','4','5','6','7','8','9','0',]

def em_c1():
    em1 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}@gmail.com'
    print (em1)

def em_c2():
    em2 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}@gmail.com'
    print (em2)

def em_c3():
    em3 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}{random.choice(word_8)}@gmail.com'
    print (em3)

def em_c4():
    em4 = f'{random.choice(word_1)}{random.choice(word_2)}{random.choice(word_3)}{random.choice(word_4)}{random.choice(word_5)}{random.choice(word_6)}{random.choice(word_7)}{random.choice(word_8)}{random.choice(word_9)}@gmail.com'
    print (em4)


#BIRTH_____________________________________

months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December']
days = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28']
years = ['2000','1999','1998','1997','1996','1995']

def bir_t():
    bday = f'{random.choice(months)} {random.choice(days)} {random.choice(years)}'
    print (bday)

#BANNER_____________________________________

print ('  смотри те на меня ')
print (' пусто однако хорошо ')

print('generates free gmail emails ')
print ('  made by @antichrist6  ')
start = input('eneter to start> ')

def accountf():
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c1()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c2()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c1()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c3()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    print ('-------------------------------------')
    print ('Name_________')
    full_n()
    print ('  ')
    print ('Email________')
    em_c4()
    print ('  ')
    print ('Password_____')
    pass1()
    print ('  ')
    print ('Birth________')
    bir_t()
    print ('-------------------------------------')
    time.sleep(1)
    accountf()


accountf()

