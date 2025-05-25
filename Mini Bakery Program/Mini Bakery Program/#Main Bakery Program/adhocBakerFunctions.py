import os
import datetime as dt
import sys
    

#Visual functions:
def clrLine_terminal():
    '''
    For clearing the current line.
    '''
    print("\033[1A", end="") #To clear previous written line to reprint new sentence.
    print(('\u00A0'*140))
    print("\033[1A",end="")

def cls_terminal():
    '''
    For clearing the entire terminal screen
    '''
    print("\u00A0\n\n"*5)
    os.system('cls' if os.name == 'nt' else 'clear') #To clear the entire terminal.
    print("\u00A0\n"*5)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.stdout.flush()

def list_Sorting(header:dict,listing:list):
    '''
    Used for printing csv lists in excel-like form.\n.\n
    header -> Dict with the format {header_name : column_index}\n
    listing -> Lists of list, of all rows of data.\n
    '''
    def spacing(header:dict, listing:list):
        space_cal = {}
        if not isinstance(listing[0],list):
            listing = [listing]
        for column in range(0, len(list(header.keys()))):
            itemChars = len(list(header.keys())[column]) #Initial with header length
            for row in listing:
                if len(row[column]) > itemChars: #Iterate row by row to get the num of longest item.
                    itemChars = len(row[column])
                elif len(row[column]) == 0:
                    itemChars = 0
            space_cal[column] = itemChars +1 #To leave a space so the word won't stick with the border line.
        return space_cal #Return a dictionary consist of column (keys) & lenght (values), and index lenght.

    def drawing(indexSpace:dict, headers:dict, lists:list):
        spcBar = '\u00A0'
        horLine = '\033[4m'
        verLine = '|'
        bold = '\033[1m'
        ends = '\033[0m'
        bhorLine = bold + horLine
        bverLine = ends + bold + verLine
        
        heads = list(headers.keys()) #Convert header dictionary into list.
        columns = list(indexSpace.keys()) #Retrieve the column index.
        spaces = list(indexSpace.values()) #Retrieve the spaces required.
        if not isinstance(lists[0],list):
            lists = [lists]

#First, print the headers (Seperated because headers has bold and underlines).

        indexLen = len(str(len(lists))) +2 #Get the lenght of index for display spacing purpose, +2 for '. '.
        wrrd = f'{(spcBar*indexLen)}'
        additionSpc = 0
        for i in range(0, len(columns)):
            hdWrrd = spaces[i] - len(heads[i])
            if (hdWrrd) % 2 != 0 or (hdWrrd) == 0: #Make sure it's even number so the header will be centered.
                spaces[i] = spaces[i] + 1 #At least 2 spaces and even.
                additionSpc += 1
                hdWrrd = spaces[i] - len(heads[i])
            hdWrrd = spcBar * int((hdWrrd/2)) #Num of spacebar for each side.
            hdWrrd = hdWrrd + heads[i] + hdWrrd
            if i == (len(heads)-1):#To check if it's the last item.
                temp = f'{bverLine}{bhorLine}{hdWrrd}{bverLine}{ends}'
            else:
                temp = f'{bverLine}{bhorLine}{hdWrrd}'
            wrrd = wrrd+temp
        roofLine = spcBar + f'{(spcBar*indexLen)}'+ bhorLine + ((customSum(spaces)+additionSpc) * spcBar)
        print(roofLine+ends) #Print the top line.
        print(wrrd) #Print the header column.

#Now, print the rest of the list.

        for row in range(0, len(lists)): #Outter loop by row (for each lists)
            indx = indexLen - len(str(row+1)) - 1 #Get the current empty space for index display.
            wrrd  = f'{str(row +1)}.{(indx*spcBar)}' #Now wrrd looks something like exmp: '12. '
            curList = lists[row]
            for col in range(0, len(columns)): #Inner loop by columns (each item in a list).
                
                if lists[row][col] == '-': #If item is Null, show a '-' in middle.
                    null = lists[row][col]
                    if spaces[col] % 2 == 0: #If spaces is even, add one more '-'.
                        null = '--'
                        colWord = int((spaces[col] / 2) - 1) * spcBar
                    elif spaces[col] % 2 != 0:
                        colWord = int((spaces[col] - 1) / 2) * spcBar
                    colWord = colWord + null + colWord #'-' or '==' is now in middle.
                    if row == (len(lists)-1): #When it's the last row
                        if col == (len(curList)-1):
                            temp = f'{verLine}{horLine}{colWord}{ends}{verLine}'
                        else:
                            temp = f'{verLine}{horLine}{colWord}'
                    else:
                        if col == (len(curList)-1): #When it's not the last row
                            temp = f'{verLine}{colWord}{verLine}{ends}'
                        else:
                            temp = f'{verLine}{colWord}'                 
                else:    
                    colWord = (spaces[col] - len(lists[row][col])) * spcBar #Get the empty space of current
                    colWord = curList[col] + colWord
                    if row == (len(lists)-1): #When it's the last row
                        if col == (len(curList)-1):
                            temp = f'{verLine}{horLine}{colWord}{ends}{verLine}'
                        else:
                            temp = f'{verLine}{horLine}{colWord}'
                    else:
                        if col == (len(curList)-1): #When it's not the last row
                            temp = f'{verLine}{colWord}{verLine}{ends}'
                        else:
                            temp = f'{verLine}{colWord}'
                wrrd = wrrd+temp
            print(wrrd,ends)

    try:
        if not isinstance(listing[0],list):
            listing = [listing]
    except:
        listing = []
        for leng in range(0, len(header)):
            empty = '-'
            listing.append(empty)
        listing = [listing]
    spacings = spacing(header, listing)
    drawing(spacings, header, listing)


#6 custom csv functions:
def readerCsv(filename:str): #Used within all other csv functions except writer to read and extract csv data.
    '''
    Use for reading file, returns lists of list.\n.\n
    filename -> name of the file including extension.\n
    Reads and return everything in lists of list
    '''
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Join the script directory with the filename to get the full path
    full_path = os.path.join(script_dir, filename)
    
    with open(full_path, 'r', newline='') as ReadFile:
        cReader = ReadFile.readlines()
        tempList = []
        for row in cReader:
            tempList.append(row.strip().split(','))
        return tempList

def writerCsv(fileBuffer, wlists:list): #Only used within other csv functions below it.
    '''
    Must be used within a with statement.\n_\n
    fileBuffer -> Requests a file object.\n
    wlists -> Provide list to rewrite into file.
    '''
    if not isinstance(wlists[0], list): #Make sure  it's a list of lists.
        fileBuffer.write(','.join(map(str, wlists)) + '\n')
    else:
        for rows in wlists:
            leng = len(rows)-1
            for items in range(0, len(rows)):
                fileBuffer.write(str(rows[items]))
                if items != leng:
                    fileBuffer.write(',')
            fileBuffer.write('\n')

def appdCsv(filename:str, lists:list):
    '''
    Appends given list to the bottom of the file.\n.\n
    filename -> absoulute file name with its extension.\n
    lists -> the list to be added into the file.'''
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    with open(filename, 'a', newline='') as appdFile:
        writerCsv(appdFile, lists)

def modCsv(filename:str, modLocate:dict, mods):
    '''
    Locate the position with 'modLocate' and replace the data in the cell with 'mods'.\n.\n
    modLocate -> dictionary with the format {Column:Index,Row:Index}\n
    mods -> new data for replacing
    '''
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    column, rows = list(modLocate.values())
    fixHeader = readerCsv(filename)[0]
    oriList = readerCsv(filename)[1:]
    tempList = []
    tempList.append(fixHeader)
    for i in range(0, len(oriList)):
        tmp = []
        alert = 0
        if i == rows:
            alert = 1
        for x in range(0, len(oriList[i])):
            if alert:
                if x == column:
                    oriList[i][x] = mods

            tmp.append(oriList[i][x].strip())
        tempList.append(tmp)
    with open(filename, 'w', newline='') as modNewData:
        writerCsv(modNewData, tempList)

def delRowCsv(filename:str, lists:list):
    '''
    Removes the given list out from the file.\n.\n
    filename -> Absoulute file name with its extension.\n
    lists -> Row to be removed.'''
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    oldList = readerCsv(filename)
    newList = [row for row in oldList if row != lists]
    with open(filename, 'w', newline='') as delrowFile:
        writerCsv(delrowFile, newList)

def retrive_csv(filename):
    '''
    Retrieves data in csv files and return:\n.\n
    Headers as dict -> {Column name : index of column}.\n
    Rows of data as lists of list -> [['One','Two','Three'], ['num1','num2','num3']].\n
    The csv absoulute file name. -> 'filename.csv' '''
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    fullList = readerCsv(filename)
    index = 0
    head = fullList[0]
    header = {}
    for column in head:
        header[column] = index
        index += 1
    outList = fullList[1:]
    return header, outList


#Input validation functions:
def alphaInputChecker(returnInput:bool,inputText:str,escCode:str,allowedText:str='',sen1:str='',sen2:str=''):
    '''
    Two uses, retunInput = Prompt input until valid, not returnInput = use to check validation and return boolean.\n.\n
    inputText => The input for checking when returnInput = True (doesn't matter if False).\n
    allowedText => The allowed characters to be in the input.\n
    sen1, sen2 => First and second sentence to print input prompt message (doesn't matter if not returnInput).\n
    returnInput => True: Return the input, for loop valid input prompt; False: Only return True/False based on inputText.
    '''

    if not returnInput:
        try:
            inputText = str(inputText)
            if any(i for i in inputText if not i.isalpha() and not i in allowedText):
                    return False
            return True
        except:
            return False
    senOut = sen1
    while True:
        try:
            inputText = input(senOut)
            if inputText.lower() == escCode.lower() and escCode != '':
                return None
            if any(i for i in inputText if not i.isalpha() and not i in allowedText) or inputText == None or  inputText == '' or inputText == ' ':
                    senOut = sen2
                    clrLine_terminal()
                    continue
            return inputText
        except:
            senOut = 'Invalid input detected, please try again!: '
            clrLine_terminal()
            continue

def numFormatChecker(dataCheck:str,dataType:int|float): #To convert to int or float type.
    output = None
    if dataType == int:
        try:
            output = int(dataCheck)
        except:
            output = None
    elif dataType == float:
        try:
            float(dataCheck)
            output = float(dataCheck)
        except:
            output = None
    return output

def dtFormatConverter(inputAlpha:str): #To convert alphabetic date formats to datetime format.
    '''
    Capitalize doesn't matter, just note that time are only in 24-hour format:\n.\n
    Y = year, M = month, D = date.\n
    H = hour, N = Minute
    '''
    datetimeFormats = {  #Convertable datetime formats
        'YYYY': '%Y',
        'YY': '%y',
        'MM': '%m',
        'DD': '%d',
        'HH': '%H',
        'NN': '%M',
    }
    #Converting alphabet format inputs into datetime format.
    inputAlpha = inputAlpha.upper()
    Output = inputAlpha
    try:
        for alphFormat, datetimeFormat in datetimeFormats.items():
            Output = Output.replace(alphFormat, datetimeFormat)
    except:
        return None #If error, return None
    if Output == inputAlpha: #If nothing is converted, return None
        return None
    else:
        return Output

def dateFormatChecker(dateCheck: str, datetimeFormat: str): #To check whether input date is desired format.
    if not '%' in datetimeFormat:
        datetimeFormat = dtFormatConverter(datetimeFormat) #Convert format to datetime format.
    try: #Try if possile to put input into the format.
        output = dt.datetime.strptime(dateCheck, datetimeFormat) #strptime: Convert (1)input string to time with (2)given format.
        return output.strftime(datetimeFormat) #If input valid, return input in desired format.
    except:
        return None #Else, return None to indicate invalid format or any error.

def num_check_multi(length:int, sen1:str, sen2:str, escCode:str, splits:str='', minn:int='', maxx:int='', types:str=''):
    '''
    Used to check singular or multiple numbers with conditions.\n.\n
    lenght -> How many numbers are inserted (works with splits), minimum 1.\n
    sen1, sen2 -> Sentences for prompting inputs (Uses sen2 after first input invalid).\n
    escCode -> Escape code to break out the function, returns None.\n
    splits ->  Delimiter for splitting the numbers, if it's ',', numbers are split by ','. ('' if length == 1.)\n
    minn, maxx -> Minimum / Maximum value of the given number(s) required.\n
    types -> Give '' for default as float but return int if no '.'; specify 'float' for float, 'int' for int.
    '''
    senOut = sen1
    types = str(types)
    while True:
        try:
            arr = input(senOut)
            if arr.lower() == escCode.lower() and escCode != '':
                return None
            if length > 1:
                splitting = arr.split(splits)
                if types == 'int':
                    arr = [int(x) for x in splitting]
                elif types == 'float':
                    arr = [float(x) for x in splitting]
                else:
                    arr = [float(x) if '.' in x else int(x) for x in splitting]
            else:
                if types == 'int':
                    arr = [int(arr)]
                elif types == 'float':
                    arr = [float(arr)]
                else:
                    arr = [float(arr) if '.' in arr else int(arr)]
            if len(arr) != length:
                raise ValueError
            if any(isinstance(i, float) for i in arr):
                arr = [float(i) for i in arr]
            if minn != '' and maxx != '':
                if all(minn <= i <= maxx for i in arr):
                    return arr
                else:
                    raise ValueError
            elif (minn != '' and maxx == '') or (minn == '' and maxx != ''):
                if minn != '':
                    if all(minn <= i for i in arr):
                        return arr
                if maxx != '':
                    if all(i <= maxx for i in arr):
                        return arr
                else:
                    raise ValueError
            else:
                return arr
        except:
            senOut = sen2
            clrLine_terminal()
            continue

def multiOptCheck(capsMatters:bool,prints:bool,escCode:str,sen1:str,sen2:str,options:dict):
    '''
    Allowing user to input option index or option string, with the choice of printing the options or not.\n.\n
    capsMatter -> True for capitalizing matters, False for not.\n
    prints -> True for printing the options based on the 'options' dict, False for skip.\n
    escCode -> Code for exiting, will return False. (Recommended to have special chars like '#cancel')\n
    sen1, sen2 -> Sentences for prompting inputs, uses sen2 after first input invalid.\n
    options -> Dict with the format {'Option1' : 0, 'Choice2' : 1}; if printed, value are showed in + 1.\n
    '''
    if all(isinstance(k,(int)) for k in list(options.keys())):
        lowerDict = {str(k): v.lower() for k, v in options.items()}
        alpOp = list(options.values())
        alpOpLower = list(lowerDict.values())
        numOp = list(options.keys())
    else:
        lowerDict = {k.lower(): v for k, v in options.items()}
        alpOp = list(options.keys())
        alpOpLower = list(lowerDict.keys())
        numOp = list(options.values()) 

    senOut = sen1
    if prints:
        for i in range(0, len(numOp)):
            print(f'{numOp[i]+1}. {alpOp[i]}') #Print the options in consistant format.
        print('')
    while True:
        try:
            inserts = input(senOut)
            if escCode != '':
                if inserts.lower() == escCode.lower() and escCode != '':
                    return None
            if inserts.isdigit():
                if str(int(inserts) - 1) in numOp or  int(inserts) - 1 in numOp:
                    inserts = int(inserts) - 1
                    return str(inserts) #Return back to original number.
                else:
                    raise ValueError    
            else: #Retrieve value no matter user's input  capitalized or not.
                if capsMatters:
                    if inserts in alpOp: #If letters capitalization matters, compare original.
                        try:
                            output = options.get(inserts)
                            output = int(output)
                        except:
                            output = next((key for key, val in options.items() if val == inserts),None)
                        if output == None:
                            senOut = 'Re:'+sen2
                        else:
                            return str(output)
                    else:
                        raise ValueError
                elif not capsMatters: #Else, just check for alphabets.
                    if inserts.lower() in alpOpLower:
                        try:
                            output = lowerDict.get(inserts.lower())
                            output = int(output)
                        except:
                            output = next((key for key, val in lowerDict.items() if val == inserts.lower()),None)
                        if output == None:
                            senOut = 'Re:'+sen2
                        else:
                            return str(output)
                    else:
                        raise ValueError
        except ValueError:
            clrLine_terminal()
            senOut = sen2 #Change the input sentence.
            continue

def username_Valid(forbChar:str, listCheck:list, escCode:str, minn:int, maxx:int, minAlph:int,
                    sen1:str, existSen:str, lenSen:str, forbSen:str, alphSen:str):
    '''
    For checking validation while creating username with conditions, returns valid username as string.\n.\n
    forbChar -> A string that consist of characters that are not allowed.\n
    listCheck -> Provide a list of accounts for checking existence,\n
    escCode -> Code for exiting, recommended to use with symbols like '#cancel'.\n
    minn, maxx -> Minimum / Maximum lenght for the character.\n
    minAlph -> Minimum alphabets required for username.\n
    sen1 -> The first sentence to be printed while first promting user input.\n
    existSen -> Corresponds to 'listCheck', prints when error in 'listCheck'.\n
    lenSen -> 'minn' & 'maxx' error, 'forbsen' -> 'forbChar' error, alphaSen -> 'minAlphs' error.
    '''
    senOut = sen1
    while True:
        try:
            uName = str(input(senOut))
            if uName.lower() == escCode.lower() and escCode != '':
                return None
            for row in listCheck: 
                if row == uName:
                    raise NameError
            if len(uName) < minn or len(uName) > maxx:
                raise ValueError
            if any(char in uName for char in forbChar):
                raise TabError
            if sum(i.isalpha() for i in uName) < minAlph:
                raise IndexError
            return uName
        except NameError:
            clrLine_terminal()
            senOut = existSen
            continue
        except ValueError:
            clrLine_terminal()
            senOut = lenSen
            continue
        except TabError:
            clrLine_terminal()
            senOut = forbSen
            continue
        except IndexError:
            clrLine_terminal()
            senOut = alphSen
            continue

def validPassCombination(forbChar:str, escChar:str, escSen:str, resChar:str, intRequired:bool, capsRequired:bool, 
    minChar:int, maxChar:int, sen1:str, senLenght:int, senInt:str, senCaps:str, senCharForb:str, senC1:str, senC2:str):
    '''
    For checking validation while creating password, return valid password as string.\n.\n
    forbChar -> A string consist of forbidden character in the password.\n
    escChar -> Code for exiting, recommend to use with symbols like '#exit'\n
    resChar -> Code for resetting password while on password confirmation, recommended using with symbols like '#reset'\n
    intRequired -> At least one number if True, skip if False.\n
    capsRequired -> At least one capital letter required if True, skip if False.\n
    minChar, maxChar -> Minimum / Maximum number of characters for the password.\n
    sen1 -> First sentence to be used while first prompting user input.\n
    senLenght -> 'minChar' & 'maxChar' error, senInt -> 'intRequired' error\n
    senCaps -> 'capsRequired' error, senCharForb -> 'forbChar' error\n
    senC1, senC2 -> First and retry sentence for prompting input while on password confirmtion.\n
    '''
    
    senOut = sen1
    while True:
        try:
            senOut = senOut + escSen
            chars = str(input(senOut))
            if chars.lower() == escChar.lower() and escChar != '':
                return None
            if not minChar == '':
                if len(chars) < minChar:
                    raise ValueError
            if not maxChar == '':
                if len(chars) > maxChar:
                    raise ValueError
            if intRequired:
                if not any(i in '0123456789' for i in chars):
                    raise SyntaxError
            if capsRequired:
                upps = False
                for i in chars:
                    if i.isupper():
                        upps = True
                        break
                if not upps:
                    raise NameError
            if any(i in forbChar for i in chars):
                raise IndexError
        except ValueError:
            senOut = senLenght
            clrLine_terminal()
            continue
        except SyntaxError:
            senOut = senInt
            clrLine_terminal()
            continue
        except NameError:
            senOut = senCaps
            clrLine_terminal()
            continue
        except IndexError:
            senOut = senCharForb
            clrLine_terminal()
            continue 
        
        senOut2 = senC1
        while True:
            passConf = str(input(senOut2))
            if passConf == resChar:
                senOut = sen1
                break
            if passConf == chars:
                return passConf
            else:
                senOut2 = senC2
                clrLine_terminal()
                continue

def dobFormatVerify(escCode:str, sen1:str, senInt:str, senLen:str, 
                    senYr, senMn:str, senDy:str, minY:int=0000, maxY:int=9999):
    '''
    Used to verify date with conditions and return as string (Note that the format is: YYYYMMDD).\n.\n
    escCode -> Code for skipping, suggested to use symbols like '#skip'.\n
    sen1 -> First sentence to print while prompting user input.\n
    senInt -> For while received non-integer ; senLen -> When lenght of input != 8\n
    senYr -> When year in input is out of range (vary by minY & maxY)\n
    senMn, senDy -> When month / date is out of range.\n
    minY, maxY -> To specify minimum / maximum range of year input.\n 
    '''
    senOut = sen1
    today = dt.date.today()
    print('')
    while True:
        clrLine_terminal()
        try:
            dob = input(senOut)
            if dob == escCode.lower() and escCode != '':
                return None
            dob = int(dob)
        except:
            senOut = senInt
            continue
        try:
            dob = str(dob)
            if len(dob) != 8:
                raise IndexError
            dob = dob[0] + dob[1] + dob[2] + dob[3] + '-' + dob[4] + dob[5] + '-' + dob[6] + dob[7]
            parts = dob.split("-")
            yr, mm = parts[0], parts[1]
            if today.year - int(yr) < minY or today.year - int(yr) > maxY:
                raise ValueError
            if not (0 <= int(mm) <= 13):
                raise SyntaxError
            try:
                dtForm = dt.datetime.strptime(dob, "%Y-%m-%d").date()
            except:
                senOut = senDy
                continue
            return dtForm
        except IndexError:
            senOut = senLen
            continue
        except ValueError:
            senOut = senYr
            continue
        except SyntaxError:
            senOut = senMn
            continue


#List and filtering functions:
def returnRowIndexbyList(listSearch:list,oriList:list): #Retrieve the index of the row in original list by giving a list)
    '''
    Retrieve index of the specified list in the original list, by giving an entire list.\n.\n
    listSearch -> Entire list for search within original list (Do not provide list of multiple lists).\n
    oriList -> Original list to search within.\n
    '''
    if isinstance(listSearch,list):
        if len(listSearch) > 1:
            return None
        listSearch = listSearch[0]
    for index, row in enumerate(oriList):
        if row == listSearch:
            return index
    if oriList[-1] == listSearch:
        return len(oriList)-1
    return None

def returnHeaderIndex(input:str,headers:dict): #Retrieve index of specific item in a dict. (Used for dicts after filtering)
    try:
        index = list(headers.keys()).index(input)
        return index
    except ValueError:
        return None

def returnValueIndex(inputs:str, column:int, lists:list):
    '''
    Find whether inputs is within the specified column in a list and return index.\n.\n
    inputs -> User input.\n
    column -> Specified column / header index.\n
    lists -> Lists for checking.\n
    '''
    if not isinstance(lists,list):
        lists = [lists]

    try:
        for index, rows in enumerate(lists): #Looping through all items of the column.
            if inputs == (rows[column]): #If input == item in specified position.
                return index
            else:
                continue
        return None
    except:
        return None

def resequenceHeaderPair(headerDict:dict):
    '''
    Resequence the dictionary pair to sequence from 0.
    '''
    newDict = {str(k):v for v,k in enumerate(headerDict.keys())}
    return newDict

def filterByValue(listSearch:list,dictSearch:dict,columnSpc,valueStr:str,capsMatter:bool,exactMatch:bool):
    '''
    Return a list that only contains specific value in the specific column, and return column index.\n.\n
    listSearch -> The list for filtering.\n
    dictSearch -> Dictionary for filtering.\n
    columnStr -> Specifying the column / header name or index.\n
    valueStr -> Insert the value for searching.\n
    capsMatter -> True for capital letter matters.\n
    exactMatch  -> True for the value is exact match with item, not contain.
    '''
    valueStr = str(valueStr)
    if set(valueStr) == '' or set(valueStr) == ' ':
        return None

    columnIndex = columnSpc if isinstance(columnSpc, int) else returnHeaderIndex(columnSpc,dictSearch)
    
    if capsMatter and exactMatch:
        output = [row for row in listSearch if row[columnIndex] == valueStr]
    elif not capsMatter and exactMatch:
        output = [row for row in listSearch if row[columnIndex].lower() == valueStr.lower()]
    elif capsMatter and not exactMatch:
        output = [row for row in listSearch if valueStr in row[columnIndex]]
    elif not capsMatter and not exactMatch:
        output = [row for row in listSearch if valueStr.lower() in row[columnIndex].lower()]
    if output == []:
        output = None
    return output

def filterLists(oriDict:dict,oriList:list,filters:list):
    '''
    Filter out headers that are not given and return a new header dict and data list.\n.\n
    oriDict -> Dict for headers and indexs, {'header' : index}\n
    oriList -> Full data in lists of list.\n
    filters -> List of desired headers to be included'''
    if isinstance(filters[0],list): #If given list is list of list, convert it list of strings.
        filt = []
        for i in range(0, len(filters)):
            filt.append(filters[i][0])
        filters = filt
    try: #Make sure it's a list of lists, elif empty, make a list of '-'.
        if oriList == [] or oriList == [[]]:
            raise ValueError
        elif not isinstance(oriList[0],list):
            oriList = [oriList]
    except:
        oriList = []
        for leng in range(0, len(oriDict)):
            empty = '-'
            oriList.append(empty)
        oriList = [oriList]
    filtered = [(key, value) for key, value in oriDict.items() if key in filters]
    newdicts = {} #Keeping wanted items in the list, and convert them into a new dictionary.
    for i in filtered:
        newdicts[i[0]] = i[1]
    newlists = []
    for rows in range(0, len(oriList)):
        tempList = []
        curList = oriList[rows]
        for v in newdicts.values():
            tempList.append(curList[v])
        newlists.append(tempList)
    return newdicts, newlists

def numTrackFilter(numDataType:int|float|dt.datetime,datetimeFormat:str,numSearch:str,numReference:str,
                tracing:str,traceEqual:bool,headerDict:dict,columnSearch,lists:str,returnList:bool):
    '''
    To check numbers with conditions, and return filtered list (of lists) or comparison results.\n.\n
    Works for FLOAT, INT, & DATE (e.g. format: 'YYYYMMDD', '%Y-%m-%d %H:%M', etc.)\n
    numDataType -> Give the data type to be checked, either: int, float, or datetime.\n
    datetimeFormat -> If numDataType, insert desired format here, else leave ''.\n
    numSearch -> User inputs.\n
    numReference -> Number for reference to compare (Only for if returnList == False, else leave '').\n
    tracing -> Conditions. 'a' = After, 'b' = Before, 'c' = Exactly Matches\n
    traceEqual -> True = include exact equal matches (exlude exacts if == False && tracing == 'c').\n
    headerDict -> Dict of the header for checking.\n
    columnSearch -> Column to search for the date.\n
    lists -> List of lists for checking. (Leave '' if returnList == False)\n
    returnList -> True = Return filtered list, False = Return Boolean Result.
    '''

    #Validating and converting data types...
    if not isinstance(numSearch,str):
        numSearch = str(numSearch)
    if not returnList:
        if not isinstance(numReference,str):
            numReference = str(numReference)

    if numDataType == dt.datetime: #Checking for date
        if not '%' in datetimeFormat:
            datetimeFormat = dtFormatConverter(datetimeFormat)
        numSearch = dateFormatChecker(numSearch,datetimeFormat)
        if numSearch == None:
            return None
        if not returnList:
            numReference = dateFormatChecker(numReference,datetimeFormat)
            if numReference == None:
                return None
            numReference = dt.datetime.strptime(numReference,datetimeFormat)
        numSearch = dt.datetime.strptime(numSearch,datetimeFormat)
    else: #Cheking for int or float.
        numSearch = numFormatChecker(numSearch,numDataType)
        if numSearch == None:
            return None
        if not returnList:
            numReference = numFormatChecker(numReference,numDataType)
            if numReference == None:
                return None
    
    columnIndex = columnSearch if isinstance(columnSearch, int) else returnHeaderIndex(columnSearch,headerDict)
    outpush = None
    if tracing == 'a': #Check after
        if returnList == True:
            if traceEqual:
                if numDataType == dt.datetime: #If it's date type.
                    outpush = [i for i in lists if i[columnIndex] != '-' and
                        dt.datetime.strptime(dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat),datetimeFormat)
                        >= numSearch] #Ensure both are in same format for comparisons.
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) >= numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) >= numSearch]
            elif not traceEqual:
                if numDataType == dt.datetime:
                    outpush = [i for i in lists if i[columnIndex] != '-' and
                        dt.datetime.strptime(dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat),datetimeFormat)
                        > numSearch]
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) > numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) > numSearch]
        elif not returnList:
            if traceEqual:
                if numSearch >= numReference:
                    outpush = True
                elif not numSearch >= numReference:
                    outpush = False
            elif not traceEqual:
                if numSearch > numReference:
                    outpush = True
                elif not numSearch > numReference:
                    outpush = False

    elif tracing == 'b':
        if returnList == True:
            if traceEqual:
                if numDataType == dt.datetime:
                    outpush = [i for i in lists if i[columnIndex] != '-' and 
                        dt.datetime.strptime(dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat),datetimeFormat)
                        <= numSearch]
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) <= numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) <= numSearch]
            elif not traceEqual:
                if numDataType == dt.datetime:
                    outpush = [i for i in lists if i[columnIndex] != '-' and 
                        dt.datetime.strptime(dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat),datetimeFormat)
                        <= numSearch]
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) < numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) < numSearch]
        elif not returnList:
            if traceEqual:
                if numSearch <= numReference:
                    outpush = True
                elif not numSearch <= numReference:
                    outpush = False
            elif not traceEqual:
                if numSearch < numReference:
                    outpush = True
                elif not numSearch < numReference:
                    outpush = False

    elif tracing == 'c':
        if returnList == True:
            if traceEqual:
                if numDataType == dt.datetime:
                    outpush = [i for i in lists if i[columnIndex] != '-' and 
                            dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat) == 
                            dt.datetime.strftime(numSearch,datetimeFormat)]
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) == numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) == numSearch]
            elif not traceEqual:
                if numDataType == dt.datetime:
                        outpush = [i for i in lists if i[columnIndex] != '-' and 
                            dt.datetime.fromisoformat(i[columnIndex]).strftime(datetimeFormat) != 
                            dt.datetime.strftime(numSearch,datetimeFormat)]
                elif numDataType == int:
                    outpush = [i for i in lists if i[columnIndex] != '-' and int(i[columnIndex]) != numSearch]
                elif numDataType == float:
                    outpush = [i for i in lists if i[columnIndex] != '-' and float(i[columnIndex]) != numSearch]
        elif not returnList:
            if traceEqual:
                if numSearch == numReference:
                    outpush = True
                elif not numSearch == numReference:
                    outpush = False
            elif not traceEqual:
                if numSearch != numReference:
                    outpush = True
                elif not numSearch != numReference:
                    outpush = False

    if outpush == None: #If no match found.
        return None
    elif outpush == [] or outpush == [[]]: #If no matched in list.
        return []
    else: #Return founded list or boolean result.
        return outpush


#Operator functions:
def customSum(intList:list,decimalPlaces:int=2):
    '''
    Returns sum of an array (Note that if result is float, will return string).\n
    Must give ordinary list that consist of integers or float, can be strings.\n
    decimalPlaces - > Number of decimal points to round up.
    '''
    if len(intList) == 0 or isinstance(intList[0],list):
        return None
    if any(not (x == '-' or isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.','0').isdigit())) for x in intList):
        return None
    total = 0
    for num in intList:
        if num == '-':
            num = 0
        if isinstance(num,str):
            num = float(num) if '.' in num else int(num)
        total += num
    if isinstance(total,float):
        total = f'{total:.{decimalPlaces}f}'
    return total

def customAvg(intList:list,decimalPoints:int=1):
    '''
    Returns average of an array, output is always string.\n
    Must give ordinary list that consist of integers or float only.\n
    decimalPoint -> Number of decimal points to round up (Default = 1).
    '''
    if not intList:
        return None
    if any(not (x == '-' or isinstance(x, (int, float)) or (isinstance(x, str) and x.replace('.','0').isdigit())) for x in intList):
        return None
    intList = [float(x) for x in intList if x != '-']
    total = 0
    for num in intList:
        if num == '-':
            num = 0
        if isinstance(num,str):
            num = float(num) if '.' in num else int(num)
        total += num
    if total == 0:
        return '-'
    average = float(total) / len(intList)
    return f'{average:.{decimalPoints}f}'
