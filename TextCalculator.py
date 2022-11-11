Silence = True	 # режим не вывода или вывода отладочных сообщений

OPERATORS = list('*/+-:%()') # поддерживаемые операторы

# все списки со всеми поддерживаемые числами
names1 = [
	["ноль",		0,	   '__',	   "нолевых =)",	],	  # числа от 0 до 9
          ["один",		1,	   '__',	   "первых",	],	
          ["два",		2,	    '__',	   "вторых",	],	
          ["три",		3,	    '__',	   "третьих",	],	
          ["четыре",	        4,	    '__',	   "четырвертых",],	
          ["пять",	 	5,	   '__',	   "пятых",	],	
          ["шесть",	 	6,	   '__',	   "шестых",	],	
          ["семь",	 	7,	   '__',	   "седьмых",	],	
          ["восемь",	        8,	   '__',	   "восьмых",],	
          ["девять",	        9,	   '__',	   "девятых",],	
          ]
namespec = [  # числа от 1!0! 11 до 19,	 специальные
     	
    ["одиннадцать",	 11,	        '__',	  	'одиннадцатых'],	
    ["двенадцать",	 12,	        '__',	  	"двенадцатых",	],	
    ["тринадцать",	 13,	         '__',	  	"тринадцатых",	],	
    ["четырнадцать",	 14,	        '__',	        "четырнадцатых",],	
    ["пятнадцать",	 15,	        '__',	   	"пятнадцатых",	],	
    ['шестнадцать',	 16,	        '__',	   	'шестнадцатых',	],	
    ['семнадцать',	 17,	        '__',	   	'семнадцатых',	],	
    ['восемнадцать',	 18,	        '__',	        'восемнадцатых',],	
    ["девятнадцать",	 19,	        '__',	        "девятнадцатых",],	
]


names10	 =[  # числа от 10  до 90
    ["нольноль", 	00,	     '__',	  	"нольнольнадцатых=))", 	],
    ["десять", 		10,	     '__',		"десятых", 		],
    ["двадцать", 	20,	     '__',	  	"двадцатых", 	],
    ["тридцать", 	30,	     '__',	  	"тридцатых", 	],
    ["сорок", 		40,	     '__',	  	"сороковых", 	],
    ["пятьдесят", 	50,	     '__',	  	"пятидесятых", 	],
    ["шестьдесят",	 60,	    '__',		"шестидесятых",	],
    ["семьдесят", 	70,	     '__',	  	"семидесятых", 	],
    ["восемьдесят",	 80,	    '__',		"восьмидесятых",],
    ["девяносто", 	90,	     '__',	  	"девяностых", 	],
]

names100 = [  # числа от 100 до 900
    ["нольсто :))))", 000,	     '__',	'какихтых'],
    ["сто", 100,	     '__',	  	'какихтых'],
    ["двести", 200,	     '__',	  	'какихтых'],
    ["триста", 300,	     '__',	  	'какихтых'],
    ["четыреста", 400,	     '__',	  	'какихтых'],
    ["пятьсот", 500,	     '__',	  	'какихтых'],
    ["шестьсот", 600,	     '__',	  	'какихтых'],
    ["семьсот", 700,	     '__',	  	'какихтых'],
    ["восемьсот", 800,	     '__',	  	'какихтых'],
    ["девятьсот", 900,	     '__',	  	'какихтых']
]

names1000 = [  # числа от 100 до 900
    ["0 тысяч:))))", 0000,   '__',	  	'какихтых'],
    ["тысяч", 1000,	     '__',	  	'какихтых'],
    ["2тысяч", 2000,	     '__',	  	'какихтых'],
    ["3тысяч", 3000,	     '__',	  	'какихтых'],
    ["4тысяч", 4000,	     '__',	  	'какихтых'],
    ["5тысяч", 5000,	     '__',	  	'какихтых'],
    ["6тысяч", 6000,	     '__',	  	'какихтых'],
    ["7тысяч", 7000,	     '__',	  	'какихтых'],
    ["8тысяч", 8000,	     '__',	  	'какихтых'],
    ["9тысяч", 9000,	     '__',	  	'какихтых']
]


names = {0: names1, 0.5: namespec, 1: names10, 2: names100, 3: names1000}  # для удобства индексации


for lst in names.values():  # поддержка распознавания простого ввода (цифры как в словарях)
    for elm in lst:
        elm[2] = str(elm[1]) 

 



def ValueToText(val): #интерпр 555 в пятьсот пятьдесят пять (и с минусами)
    rez = '' 
    sign = +1 
    if val<0:
         sign = -1 #если число меньше нуля, то знак меняется
         val= abs(val)
    valtxt = str(int(val)) 
    valtxt = valtxt[::-1]  
   

    speced = False # первый разряд
    ostatok = int(val) % 100  
    if ostatok in list(range(11, 19+1)):  
        print('ost', ostatok)
        speced = True
        word, digit, __ = namespec[ostatok - 10-1][:3] #
        rez = ' ' + word + rez

    
    for nomer_razryada in range(0+2*speced, len(valtxt)):
        digit = int(valtxt[nomer_razryada]) 
        if digit == 0: continue

        print('>>',nomer_razryada, digit)
        liniya_sinonimov = names[nomer_razryada][digit][:3] # 
        word, digit, _ = liniya_sinonimov
        print(digit, '=', word)
        rez = ' ' + word + rez # накапливаем результат вставляя новое словое левее сформированных

    if sign==-1:
        rez = ' минус ' + rez #трансформ с примечанием с минусом

        
    return rez 


words =  names1000[::-1] + names100 + names10 + namespec +   names1 # все существующие распознаваемые символы
def TextToValue(orgtext:str): # распознать слова в число
    txt = orgtext 
    rez = 0 # переменная накопитель для итого результата
    sign = +1 # переменная флаг знака плюс или минус

    txt = txt.strip() # убираем все лишние пробелы
    minus_chr = '' # текстовый эквивалент переменной sign
    
    # распознание необходимости минуса
    if txt[0]=='-':
        sign = -1
        minus_chr = ' -'
        txt = txt[1:]

        
    if 'минус' in txt :
        txt = txt.replace('минус', '')
        sign = -1
        minus_chr=' минус '
   

        
    words_in_txt = txt.split(' ')[::-1] # сплитит текстовые значения на отдельные слова 
    opers = ' '
     # проходится пословно сквозь введенное значение
    for i in range(len(words_in_txt)):
        word = words_in_txt[i] # очередная часть значения (разряд)

        
        for synonym_line in words: #перебирает все существующие названия чисел в базе с целью найти каждое из них в тексте
            # synonym_line - очередное слово из базы слов например 5
            if word in synonym_line: # если данное текущ слово является одним из синонимов, то берем значение факт значение группы синонимов
                
                value = synonym_line[1] # то самое значение в которое конвертим слово
                rez += value # увеличиваем итоговый результат на данное число (очеред счит разряд)
                opers+= ' + '+str(value)  # отлад инфа из каких компонент было сложено число
                #print('\t\t\t\t\t\t', word, ' in ' , elm, '+=',value)
                break                 
                
    
    if not Silence : # если детальный вывод позволен, то выводим отладочную инфу
        print('\t\t\t\t\t To Value:', orgtext, ' -> ', rez*sign,'->',minus_chr + opers)
        
    #print('\t =) ', txt, '=', rez)        
    return rez*sign # возвращаем результат * на знак( минус или плюс )


def stripp(s):  # оболочка для метода стрип к строке, нужна для map(stripp, list)
    return s.strip()


def ToValuePRO(s: str): # обвертка для функции TextToValue
    # отличается тем, что не пытается конвертировать операторы
    s = s.strip() 
    return s if s in OPERATORS else TextToValue(s) # все что не является опреатором 

    
def prepare(text:str): # отчищает первичный юзерский ввод
    formula = text.strip()  
    #formula = formula.replace('-', '+ (0-1) * ')
    # распознает операторы и заменяет на специфические знаки(символы разрыва)
    formula = formula.replace('-', '@-@').replace('+', '@+@').replace('*', '@*@')\
              .replace('/', '@/@').replace('%','@%@')\
              .replace(':', '@:@').replace('(', '@(@').replace(')', '@)@')
              #.replace('-', '+ (0-1) * ')/

    #formula = formula.replace('минус', 'плюс скобка открывается ноль минус один скобка закрывается умножить на ')
    # замена слов на знаки
    formula = formula.replace('плюс', '@+@').replace('умножить на', '@*@')\
              .replace('минус', '@-@').replace('поделить на', '@/@').replace('остаток деления на', '@%@')\
              .replace('делить нацело на', '@:@').replace('скобка открывается', '@(@').replace('скобка закрывается', '@)@')

    print('\nsys OPERATORS Recognition = \n\t',formula)  # отладочная инфа
    #preclear
    # отчистка и сжатие и распознание точек разрыва
    while '  ' in formula: 
        formula = formula.replace('  ', ' ')
    while '@ ' in formula:
        formula = formula.replace('@ ', '@')
    while ' @' in formula:
        formula = formula.replace(' @', '@')
    while '@@' in formula:
        formula = formula.replace('@@', '@') 
    formula = formula.strip('@') # уничтожение точек разрыва в самом начале и в самом конце
    print('\nsys   (x2SPACES to 1xSPACE)  (x2@@ ZIPEED to @x1)  = \n\t',formula  ) 
    print('\nsys OPEARTORS Recognition  BREAKEZONES   = \n\t',formula.replace('@', '|') ) 

    formula = formula.split('@') # разрезаем по точкам разрыва
    if formula[0] in '-+': formula.insert(0,'ноль') # если начинается с минуса или плюса, то добавляется ноль (например 0(+5))
    print(formula)

    # блок разрешения конфликтов возникающих когда два оператора идут подряд
    i = 0 
    while i < len(formula)-1: # каждый раз перерасчитывает текущую длину формулы
        elm1 =  formula[i] #получим текущий элемент и след за ним
        elm2 =  formula[i+1]
        op = elm1 in OPERATORS  # операторы ли они
        op2 = elm2 in OPERATORS
        
        if op and op2: # если два оператора идут подряд
            if '-' in [elm1,elm2]: # если хотя бы один из операторов минус
                if elm2==elm1: # если оба оператора минусы 
                    print('!!!!!!')
                    print('! !', i ,elm1,elm2, op,op2 )
                    del formula[i:i+2] # удаляем два минусы, конфликтную зону
                    formula.insert(i, '+')  # - на - дает +
                                   
                    continue # не двигаться дальше, решить здесь, затем двигаться дальше
                    
                    
                if '-'==elm1: # если минус идет первым, пример -(...)
                    print('!!!!!!')
                    print('! !', i ,elm1,elm2, op,op2 )
                    del formula[i] 
                    formula.insert(i, '*') # неявный минус подменяем на -1*
                    formula.insert(i, '-1') # пример ... 5  -(9+2)   эквивалентно 5  -1*(9+2)
                    continue # не продолжает  если сбой не произошел
                    
                if '-'==elm2: # если минус идет вторым, например 5/-1, 4*-5, 4*-() #
                    print('!!!!!!')
                    print('! !', i ,elm1,elm2, op,op2 )
                    del formula[i+1] 
                    formula.insert(i+1, '*')
                    formula.insert(i+1, '-1')                    
                    continue
        i+=1 # если нигде сбоев не произошло, перейти к след элементу формулы и его соседу для анализа
        print('! !', i ,elm1,elm2, op,op2 )
                    
        
    print('\nsys  LEXEMS =  (OPERANDS AND OPERATORS)= \n\t:',formula ) # конечный результат всей подготовки
    print('\n thesame , but UserFriendly Format  = \n\t:',user_friendly_print(formula) ) # легко читаемый для юзера

    #deBracket here 
    return formula # возвращает очищенную формулу


def calc(Formula, level=1): # вычисляет, с учетом приоритета опреаторов, не работает со скобками, тк от скобок должны быть очищена DeBracketerom
    prefix = '\t'*level + str(level)+') '

    
    print(prefix,Formula)
    Formula = list(map(ToValuePRO, Formula))
    print(prefix,Formula)
    #[ 1234  ,+  ,  1001,+  ,324 ,  / ,  3]
    priorities = { # операторы в порядке приоритета от главных к второстепенным

        #1: ['^', 'v'],
        2: ['/', '*', ':', '%'], # в том числе целочисленное деление и остаток от деления div and mod 
        3: ['-', '+']

    }
    

    # --------- GLOBAL ITERATOR FOR SOLVE-TION -----------------------------
    while len(Formula) > 1:# будет работать до тех пор пока не сведет формулу до одного финального значения
        if len(Formula) == 2 and Formula[1] not in OPERATORS: # если оператор минус потерялся - став частью числа
                                        # то мы всегда между двумя числами несвязанными оператором можем вставить плюс
                                        # -5-8 = -5 + -8
            Formula.insert(1, '+')
        print(prefix,Formula) 

            # ищет за какой взяться первым
        #--------------------------- SELECTOR--------------------------------- 
        # DECIDE WHICH ACTION TO CALCULATE FIRST/
        #MEANS - WHAT PRIOR OPERATOR IS THE MOST LEFT ONE - THOSE ONE IS TO BE FIRST
        #   or if there is no prior operatiokns at all - just take the usual operator from the left edge
        target = None
        if Formula[1] in ['*', '/', '%', ':']: # если первый оператор является оператором страшего приориета 
            need_search = False
            target = 1
        else: # значит операторы старшего приоритета предстоит найти
            # будем искать какой из них левее
            NOT_FOUND = len(Formula) + 999 # по умолчанию считаем что ни одного не найдено
            VSEH_PRIOROPERS_TARGETSPOZ = [] # в каких координатах кто был найден
            for priorOP in  ['*', '/', '%', ':']: # по очереди смотрим какие из старших операторов вообще есть
                poz = Formula.index(priorOP)  if priorOP in Formula else  NOT_FOUND # если этот оператор левее предыдущ 
                VSEH_PRIOROPERS_TARGETSPOZ.append(poz) # подшиваем позицию найденого опреатора
            closest = min(VSEH_PRIOROPERS_TARGETSPOZ) # в итоге смотрим кто из них был левее всего и с него начинаем 
            target = 1 if closest==NOT_FOUND else closest # если никого найдено не было, то берем крайний левый простейший опер по порядку


    
        show = [' '* (len(str(elm)) + 2*(type(elm)==str) + 3) for elm in Formula]
        show[target] = '^'
        print(prefix,' ' + ''.join(show))
        # -------------------------------------CALCULATOR -------------------------------------
        # do Work      ON AOP  at Formula[target +-1]
        # решим этот оператор: возьмем число слева и справа от него и выполним действия над ними
        
        a = Formula.pop(target - 1)                    # вынимаем число слева
        operator = Formula.pop(target - 1)      # вынимаем сам опреатор из формулы
        b = Formula.pop(target - 1)         # вынимаем число справа
                                    # (потом на их место будем вставлять итоговый результат)
        print(prefix,operator) 

        result = None
        print(prefix,'---EVALUATING ', a, operator, b )
        try: # в зависимости от опретаора будем выполнять действия над операндами
            if operator == '+':
                result = a + b
            elif operator == '*':
                result = a * b
            elif operator == '/':
                result = round(a / b)
            elif operator == '-':
                result = a - b
            elif operator == ':': # целочисленное деление - div
                result = a // b
            elif operator == '%': # остаток от деления - mod 
                result = a % b
            else:
                result = -99999 # ошибка, опертаор не распознан, рушим дальнейшие вычисления, возвращая 999999
                print(prefix,'   неизвестный оператор')
            # print('  успешно ')

        # на случай если поделили на ноль или подобные ошибки (корень из отрицательного и тд )
        except:       # чтобы программа не вылетила с ошибкой перехватываем программный сбой и мягко обрабатываем
            print(prefix,'   произошла ошибка математики')
            result = 99999 # 
        print('\t\t\trez = ',result)
        Formula.insert(target-1, result)

        pass#inwhile last line
    pass#while ends here



    #в итоге когда цикл выполнит все операции и сожмет всё выражение всего лишь до одного резул числа,  finally program ends next way: 
    print(prefix,'calc rez = ', Formula[0])
    return Formula[0] # возвращаем это самое единственное число
pass# def calc ends here



def user_friendly_print(_formula): # приводит формулу из списка слов в строку из цифр (5-(9*2+3))
    f = list(map(ToValuePRO,_formula)) 
    s = ''.join( [str(elm) for elm in f] )
    return '<{' + s + '}>'


def main():
    
    rez = ''
    while True: # задавать вопрос, вычислять и так по кругу
        txt = input('\n\n\n\t введите запрос для вычисления словами на русском \n>').strip() 
        print('\nПолучен  ввод = stripCleaned \n\t<'+txt + '>')

        formula = prepare(txt)
        print('\nPREAPRE REZ = \n\t',' '.join(formula))
        print('\nREADABLE REZ = \n\t',user_friendly_print(formula))
        
        global Silence # влияем на глобальеую переменную внутри функции
        Silence = False # с этого момента начинаем детализировать вывод
        val =       deBracketer(formula)   # запускает функцию распознания скобок и вычисления их содержимого вплоть до 
        print(' txt rez>', val)

  
    pass# last line of defmain
pass#def main ends

               
def deBracketer(_Formula, level=1): #разрешает индивидуально скобки одного уровня, уходит в глубь для 
    count=0 
    AreaStarts= None
    AreaEnds=None
    
    reiter = 0
    
    while '(' in _Formula: # ищет начало, конец скобок, вычисляет # покудова скобки есть, включим их
        AreaStarts= None
        AreaEnds=None
        reiter+=1
        print('  '*level,'>DEBRA',level,'/',reiter, '\n\t\t', user_friendly_print(_Formula),'\n\t\t' , _Formula  )
        
        AreaStarts= _Formula.index('(') # находим начало скобочной зоны
        count = 1
        for poz in range(AreaStarts+1,len(_Formula)): # опеределяем содержимое скоб и содержимое внутри 
            element = _Formula[poz]

            if element=='(':# увелич уровень вложенности
                count+=1
            elif element==')': # уменьшаем уровень вложенности
                count-=1
            if count==0: # когда основная скоба закрылась - заканчиваем сканирование
                AreaEnds=poz
                break
            #if ends
        #for ends
    

        print(AreaStarts,AreaEnds)  
        if AreaEnds==None: # если закрывающ скобку так и не нашли
            print('ERROR in open-close pairing.  BRACKET WAS NOT CLOSED PROPERLY')
            input('!!!!!!!!!!!!')
            break # останавливаем
        if AreaStarts  is not None and AreaEnds is not None: # если обе скобки успешно найдены
                print('    subzone..')
                from copy import deepcopy as clone
                subzone_Formula = clone(_Formula[AreaStarts+1:AreaEnds ]) # клонируем их содержимое
                del  _Formula[AreaStarts:AreaEnds+1 ] # удаляем всю скобку из формулы чтобы потом заменить ее результатом в одно значение
                subzone_result = deBracketer(subzone_Formula,level = 1+level) # результат вычисления скобки и ее возможных субскобок
                print('    subzone_rez=', subzone_result)
                _Formula.insert(AreaStarts, subzone_result) # вставляем результат вместо изначлаьной скобки
                print(level,') iteration rez INSERTION performed: ',   '\n\t\t users: ', user_friendly_print(_Formula),'\n\t\t real : ' , _Formula  )


 
        # когда уже все скобки разрешены и вычислены отдать обесскобленную формулу калькулятору 
    return ValueToText(calc(_Formula)).strip()  
 

main() # вызываем основную функцию
