import datetime as dt
import adhocBakerFunctions as ad

def SystemProgram():
#General Features for multiple roles#
    def LoginMenu(): #The initial menu that welcomes users and prompt sign in.


        curTime = dt.datetime.now().strftime("%Y-%m-%d %H:%M") #Current time.

        def acc_Login(): #Login for all roles, after logged in, will look in accList check 'Role' then return.
            '''
            Script for logging in account, open to all roles.
            '''
            ad.cls_terminal()
            print('====Loging in system====\n')
            userAcc = input('Insert your username: ')
            while True:
                accRowIndex = ad.returnValueIndex(userAcc,nameColumn,acc_List)
                if accRowIndex == None: #Not found, then ask to retry or create account.
                    ad.cls_terminal()
                    print("Username doesn't exist!\n\n1. Retry\n2. Create Account\n3. Go back")
                    choice = ad.multiOptCheck(False,False,'#cancel', 'Select an option: ',
                    'Please insert a valid option: ', {'Retry':0,'Create Account':1, 
                                            'Create':1,'Back':2, 'Go back':2})
                    if choice == None:
                        return '#Exit'
                    if choice == '0': #Insert username again.
                        ad.cls_terminal()
                        print('===Log in menu===\n')
                        userAcc = input('Insert your username again: ')
                        continue
                    elif choice == '1': #Create an account.
                        return 'Create'
                    elif choice == '2': #Exit program.
                        return '#Exit'
                    continue
                else:
                    break
            ad.cls_terminal()
            print(f'---Loging in with {userAcc}---\n')

            while True:
                userPass = passwordChecker(userAcc,'Insert your account password: ',
                        'Incorrect password, please try again! (#cancel to return): ','#cancel',False)
                if userPass == None:
                    input('Log in cancelled! Hit ENTER to return...')
                    return '#Exit'
                elif userPass:
                    modTLoc = {'Column':lastLogColumn,'Row':accRowIndex} #Specifying position in table.
                    ad.modCsv(path_AccList,modTLoc,str(curTime)) #Update last login.
                    input('\nPassword matched! Hit ENTER to log in to menu...')
                    return userAcc
                else:
                    continue

        def acc_Create(): #Create account only for customer, because staff don't need to self-create.
            '''
            Script for customer to create account, role are only restricted to customers.
            '''
            ad.cls_terminal()
            print('---Creating account (Step 1/4)---\n')
            nameList = (row[nameColumn] for row in acc_List)
            userAcc = ad.username_Valid(r'!#$%^&*)(-+=}{][|\:;"<,>?/'+"'", nameList, '#exit', 4, 20, 3,
                            'Insert your unique username: ',
                            "Username already exist, please try again! (To cancel, insert '#exit'): ",
                            "Username should have between 4 - 20 letters! (To cancel, insert '#exit'): ",
                            "Username should not contain symbols other than '@_.'! (To cancel, insert '#exit'): ",
                            "Username should have at least 3 alphabets! (To cancel, insert '#exit'): ")
            if userAcc == None:
                return '#Exit'
            ad.cls_terminal()
            print(f'---Creating password (Step 2/4): {userAcc}---\n')
            userPass = ad.validPassCombination('\'' + r'\/#%^&*()+-=[]}{|;:"<>,?', '#cancel', " (To cancel, insert '#cancel'): ",
                        '#reset', True, True, 8, 20, 'Insert your new password.', 'Password should be between 8 - 20!', 
                        'At least one integer required!', 'At least one capital letter required!', "Only symbols !@$_. are allowed!", 
                        'Confirm your password: ', "Incorrect, try again! (Insert '#reset' to change): ")
            if userPass == None:
                print('Account registration has been cancelled.')
                return '#Exit'
            ad.cls_terminal()
            print(f'---Confirming gender (Step 3/4): {userAcc}---\n')
            options = {'Male':0,'Female':1,'Prefer not to say':2, 'Skip':2}
            print('1. Male\n2. Female\n3. Prefer not to say (skip)\n')
            userGender = ad.multiOptCheck(False,False,'', 'Select your gender: ', 
                                    'Please select a valid option!: ',options)
            if userGender == '0':
                userGender = 'Male'
            elif userGender == '1':
                userGender = 'Female'
            elif userGender == '2':
                userGender = '-'
            ad.cls_terminal()
            print(f'---Date of birth (Step 4/4): {userAcc}---\n')
            print("Insert your birthday with the following format --> yyyymmdd\nInsert '#skip' to skip step.\n")
            dob = ad.dobFormatVerify('#skip','Insert your birthday! (e.g. 20050723): ',
                            'Please insert valid integers! (e.g. 20050723): ',
                            'Birthday should consist of 8 numbers! (e.g. 20050723): ',
                            'Age should be between 12 - 120! (e.g. 20050723): ',
                            'Month is out of range, please try again! (e.g. 20050723): ',
                            'Date is out of range, please try again (e.g. 20050723): ', 12, 120)
            if dob == None:
                dob = '-'
            ad.cls_terminal()
            print(f'---New account has been created...---\n\nWelcome, {userAcc}!')
            insertion = [userAcc,userPass,'Customer',userGender,dob,curTime,'-','-']
            ad.appdCsv(path_AccList, insertion)
            return userAcc

        ad.cls_terminal()
        welcomeBanner = r"""
   __________________________________________________________________________________________________________________________
  / __          __  _                             _                    _____  _    _    _____          _        _            \
 /  \ \        / / | |                           | |             /\   |  __ \| |  | |  |  __ \        | |      (_)            \
|    \ \  /\  / /__| | ___ ___  _ __ ___   ___   | |_ ___       /  \  | |__) | |  | |  | |__) |_ _ ___| |_ _ __ _  ___  ___    |
|     \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \     / /\ \ |  ___/| |  | |  |  ___/ _` / __| __| '__| |/ _ \/ __|   |
|      \  /\  /  __/ | (_| (_) | | | | | |  __/  | || (_) |   / ____ \| |    | |__| |  | |  | (_| \__ \ |_| |  | |  __/\__ \   |
 \      \/  \/ \___|_|\___\___/|_| |_| |_|\___|   \__\___/   /_/    \_\_|     \____/   |_|   \__,_|___/\__|_|  |_|\___||___/  /
  \__________________________________________________________________________________________________________________________/
"""
        print(welcomeBanner)
        print('\033[4mYou shall sign in to start your browsing!\033[0m:\n')
        while True:
            print('1. Login\n2. Create Account\n3. Quit Program')
            select = ad.multiOptCheck(False,False,'','Choose an action: ',
                                'Please insert a valid option: ', 
                                {'Login':0,'Log in':0,'Signin':0,'Sign in':0,
                                'Create':1,'Create Account':1,'Signup':1,'Sign up':1,
                                'Quit Program':2,'Quit':2,'Exit':2})
            if select == '0': #Note that the output of the function returns int minimum starts from 0.
                acts = acc_Login()
            elif select == '1':
                acts = acc_Create()
            elif select == '2':
                return '#Exit'
            else:
                ad.clrLine_terminal()
                continue

            if acts == '#Exit' or acts == None:
                ad.cls_terminal()
                print('---Sign in page---\n')
                continue
            elif acts == 'Create':
                acts = acc_Create()
                if acts == '#Exit' or acts == None:
                    ad.cls_terminal()
                    print('---Sign in page---\n')
                    continue
                else:
                    break
            else:
                break
        return acts

    def passwordChecker(userName:str,sen1:str,sen2:str,escCode:str,renew:bool): #Function for password validation.
        accRowIndex = ad.returnValueIndex(userName,header['Username'],acc_List)
        accountRow = acc_List[accRowIndex]
        senOut = sen1
        
        while True:
            oldPass = input(senOut)
            if oldPass.lower() == escCode:
                return None
            if oldPass !=  accountRow[header['Password']]: #If password not match
                senOut = sen2
                ad.clrLine_terminal()
                continue
            else:
                if renew:
                    newPass = ad.validPassCombination('\'' + r'\/#%^&*()+-=[]}{|;:"<>,?', '#cancel', " (To cancel, insert '#cancel'): ",
                        '#reset', True, True, 8, 20, 'Insert your new password.', 'Password should be between 8 - 20!', 
                        'At least one integer required!', 'At least one capital letter required!', "Only symbols !@$_. are allowed!", 
                        'Confirm your password: ', "Incorrect, try again! (Insert '#reset' to change): ")
                    if newPass == None:
                        return None
                    else:
                        accountRow = ad.returnValueIndex(userName,nameColumn,acc_List)
                        ad.modCsv(path_AccList,{'Column':passColumn,'Row':accRowIndex},newPass)
                        break
                else:
                    break
        return True

    def employeeSettings(usersName): #Function for account information modification.

        def editPassword():
            print('---Edit Password---\n')
            newPass = passwordChecker(usersName,'Enter your old password: ',
                    'Password does not match, please try again!: ','#cancel',True)
            if newPass == None:
                input('Password has not been changed. Hit ENTER to return...')
            else:
                input('\nPassword has been successfully changed! Hit ENTER to continue...')
            return

        def editDOB():
            print("\nInsert your birthday with the following format --> yyyymmdd\nInsert '#cancel' to skip step.\n")
            newDOB = ad.dobFormatVerify('#cancel','Insert your birthday! (e.g. 20050723): ',
                        'Please insert valid integers! (e.g. 20050723): ',
                        'Birthday should consist of 8 numbers! (e.g. 20050723): ',
                        'Age should be between 12 - 120! (e.g. 20050723): ',
                        'Month is out of range, please try again! (e.g. 20050723): ',
                        'Date is out of range, please try again (e.g. 20050723): ', 12, 120)
            if newDOB == None:
                input('\nEdit of date of birth cancelled! Hit ENTER to continue...')
                return
            else:
                ad.modCsv(path_AccList,{'Column':header['DOB'],'Row':accRowIndex},str(newDOB))
                input('\nDate of birth has been updated successfully updated! Hit ENTER to continue...')
            return

        def editGender():
            oriGender = acc_List[accRowIndex][header['Gender']]
            senOut = 'Select an biological identity: '
            while True:
                if oriGender == '-':
                    oriGender = 'Hidden'
                print('---Reidentify Gender---')
                print(f'Original identity: {oriGender}')
                print('\nWhat would you like to identify as now?:')
                print('1. Male\n2. Female\n3. Prefer not to say\n4. Cancel...\n')
                choice = ad.multiOptCheck(False,False,'',senOut,'Please insert a valid option: ',
                                        {'Male':0, 'Female':1,'Prefer not to say':2,
                                        'Prefer Not':2,'Cancel...':3,'Cancel':3})
                if choice  == '0':
                    newGender = 'Male'
                elif choice =='1':
                    newGender = 'Female'
                elif choice =='2':
                    newGender = '-'
                elif choice == '3':
                    return
                if newGender == oriGender and (newGender != '-'):
                    ad.cls_terminal()
                    senOut = f'You have already identified yourselve as a {oriGender}!: '
                    continue
                break
            ad.cls_terminal()
            print('---Confirm reidentify?---\n')
            if newGender == '-':
                reconsider = ad.multiOptCheck(False,True,'',
                                'Are you sure to remain your prideful identity hidden?: '
                                , 'Please insert a valid option!: ', {'Yes':0,'No':1})
            else:
                reconsider = ad.multiOptCheck(False,True,'',
                            f'Are you sure to identify your self as a {newGender}?: '
                            , 'Please insert a valid option!: ', {'Yes':0,'No':1})
            if reconsider == '0':
                ad.modCsv(path_AccList,{'Column':header['Gender'],'Row':accRowIndex},newGender)
                if newGender == '-':
                    input('Your identity has remained anonnymous, hit ENTER to return...')
                else:
                    input('You have sucessfully discovered your new identity! Hit ENTER to continue...')
            elif reconsider == '1':
                input('Your identity has remained the same, hit ENTER to return...')
            return

        while True:
            ad.cls_terminal()
            header, acc_List = ad.retrive_csv(path_AccList)
            print('---Account Settings----\n')
            print('Edit Details:\n1. Password\n2. Birthday\n3. Gender\n4. Exit...\n')
            choice = ad.multiOptCheck(False,False,'','Insert an info to edit: ','Please insert a valid option!: ',
                                    {'Password':0,'Pass':0,'Passwords':0,
                                    'Birthday':1,'DOB':1,'Birth':1,
                                    'Gender':2,'Exit...':3,'Exit':3})
            accRowIndex = ad.returnValueIndex(usersName,header['Username'],acc_List)
            ad.cls_terminal()
            if choice  == '0':
                editPassword()
            elif choice == '1':
                editDOB()
            elif  choice == '2':
                editGender()
            elif choice == '3':
                break
        return


#Menus for all four roles#
    def ManagerMenu(username:str):
        print(f'====Welcome back dearest manager, {username}!====\n')

        def ststemAdministration(): #For managing accounts.
            #Show page naem==me
            #Show list first with filter features while enter.
            def acc_CreateMNG(): #Create for any role but customer.
                ad.cls_terminal()
                print('####Creating account for employee####\n\n')
                print('---Creating account (Step 1/4)---\n')
                nameList = (row[nameColumn] for row in acc_List)
                newEmpAcc = ad.username_Valid(r'!#$%^&*)(-+=}{][|\:;"<,>?/'+"'", nameList, '#exit', 4, 20, 3,
                                'Insert your unique username: ',
                                "Username already exist, please try again! (To cancel, insert '#exit'): ",
                                "Username should have between 4 - 20 letters! (To cancel, insert '#exit'): ",
                                "Username should not contain symbols other than '@_.'! (To cancel, insert '#exit'): ",
                                "Username should have at least 3 alphabets! (To cancel, insert '#exit'): ")
                if not newEmpAcc:
                    return '#Exit'
                ad.cls_terminal()

                print(f'---Creating password (Step 2/4): {newEmpAcc}---\n')
                newEmpPass = ad.validPassCombination('\'' + r'\/#%^&*()+-=[]}{|;:"<>,?', '#cancel', " (To cancel, insert '#cancel'): ",
                            '#reset', True, True, 8, 20, 'Insert your new password.', 'Password should be between 8 - 20!', 
                            'At least one integer required!', 'At least one capital letter required!', "Only symbols !@$_. are allowed!", 
                            'Confirm your password: ', "Incorrect, try again! (Insert '#reset' to change): ")
                if not newEmpPass:
                    input('\nAccount registration has been cancelled.')
                    return
                ad.cls_terminal()

                print(f'---Assigning role (Step3/4): {newEmpAcc}---\n')
                newEmpRole = ad.multiOptCheck(False,True,'','Assign a role for this account: ', 'Please give a valid role!: ', {'Cashier':0,'Baker':1})
                if newEmpRole == '0':
                    newEmpRole = 'Cashier'
                elif newEmpRole == '1':
                    newEmpRole = 'Baker'
                ad.cls_terminal

                print(f'---Confirming gender (Step 4/4): {newEmpAcc}---\n')
                options = {'Male':0,'Female':1,'Prefer not to say':2, 'Skip':2}
                print('1. Male\n2. Female\n3. Prefer not to say (skip)\n')
                newEmpGender = ad.multiOptCheck(False,False,'', 'Select your gender: ', 
                                        'Please select a valid option!: ',options)
                if newEmpGender == '0':
                    newEmpGender = 'Male'
                elif newEmpGender == '1':
                    newEmpGender = 'Female'
                elif newEmpGender == '2':
                    newEmpGender = '-'
                ad.cls_terminal()

                print(f'---New {newEmpRole} account has been created...---\n\nIntroducing, {newEmpAcc}!')
                insertion = [newEmpAcc,newEmpPass,newEmpRole,newEmpGender,'','','-','-']
                ad.appdCsv(path_AccList, insertion)
                input('\nHit ENTER to return...')
                return 'Customer'

            def acc_DeleteMNG():
                '''
                Script to view and delete accounts, only accesible for manager.
                '''
                ad.cls_terminal()
                print('---Account deletion---')
                delView = ['Username','Role','Gender','LastLogin']
                delHeads, delLists = ad.filterLists(header, acc_List, delView)
                ad.list_Sorting(delHeads, delLists)
                cancel = len(acc_List)
                print(f'\n{str(cancel + 1)}. Cancel deletion...')
                options = {k[0]: v for v, k in enumerate(acc_List)} #Create dict with only Username and Index.
                options['Cancel'] = cancel
                options['cancel'] = cancel
                options['Cancel deletion'] = cancel
                options['cancel deletion'] = cancel
                selDel = ad.multiOptCheck(True,False,'', '\nSelect an account for deletion: ',
                                'Please insert a valid option!: ', options)
                selDel = int(selDel)
                if selDel == cancel:
                    input('\nNothing has been removed, hit ENTER to return...')
                    return
                accRow = acc_List[selDel]
                accName = accRow[nameColumn]
                ad.cls_terminal()
                print(f'---Account deletion---\n\nAre you sure you want to delete {accName}?: ')
                options = {'Yes':0,'No':1}
                delAcc = ad.multiOptCheck(False,True,'','Confirm your action: ','Please insert the option given!: ',options)
                if delAcc == '0':
                    delAcc = True
                elif delAcc == '1':
                    delAcc = False
                ad.cls_terminal()
                if delAcc:
                    print('Deletion processing...')
                    ad.delRowCsv(path_AccList, accRow)
                    input(f'User {accName} has been succefully deleted! Hit ENTER to return...')
                    return
                elif not delAcc:
                    input('User has not been deleted. Hit ENTER to return...')
                    return

            def acc_ModifyMNG():
                ad.cls_terminal()
                print('--- Employee Account modification---')
                modAccHead, modAccList = ad.filterLists(header,acc_List,['Username','Role','LastLogin'])
                roleIndex2 = ad.returnHeaderIndex('Role',modAccHead)
                empAccCs = ad.filterByValue(modAccList,modAccHead,roleIndex2,'Cashier',True,True)
                empAccBk = ad.filterByValue(modAccList,modAccHead,roleIndex2,'Baker',True,True)
                empAccList = empAccCs + empAccBk
                ad.list_Sorting(modAccHead,empAccList)                
                cancel = len(empAccList)
                print(f'\n{str(cancel + 1)}. Cancel modification...')
                options = {k[0]: v for v, k in enumerate(empAccList)} #Create dict with only Username and Index.
                options['Cancel'] = cancel
                options['Cancel modification'] = cancel
                selEmpAcc = ad.multiOptCheck(True,False,'', 'Select an account to modify role: ',
                                        'Please insert a valid account!: ', options)
                selEmpAcc = int(selEmpAcc)
                if selEmpAcc ==cancel:
                    return
                selEmpRow  = empAccList[selEmpAcc]
                selEmpName = selEmpRow[nameColumn]
                ad.cls_terminal()
                options = {'Cashier':0,'Baker':1,'Cancel':2}
                senOutter = 'Select a role to assign: '
                while True:
                    ad.cls_terminal()
                    print(f'---Account modification---\n\nChoose a new role to assign to {selEmpName}')
                    selEmpRole = ad.multiOptCheck(False,True,'',senOutter,'Please select a valid role!: ',options)
                    if selEmpRole == '0':
                        selEmpRole = 'Cashier'

                    elif selEmpRole == '1':
                        selEmpRole = 'Baker'

                    elif selEmpRole == '2':
                        break

                    if selEmpRow[roleIndex2] == selEmpRole:
                        senOutter = f'User {selEmpName} is already a {selEmpRole}!: '
                        continue
                    else:
                        break
                oriEmpRow = ad.returnValueIndex(selEmpName,nameColumn,acc_List)
                emplocate = {'Column':header['Role'],'Row':oriEmpRow}
                ad.modCsv(path_AccList,emplocate,selEmpRole)
                input(f'\nUser {selEmpName} has been assigned to {selEmpRole}!\nHit ENTER to continue...')
                return

            while True:
                ad.cls_terminal()
                print('----System Administration----\n')
                print('\nManage user accounts: \n1. Create account for employees\n2. Delete accounts')
                print('3. Modify Employee Role\n4. Back to menu...')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                                        {'Create account for employees':0,'Create':0,'Create account':0,
                                        'Create account for employee':0,
                                        'Delete accounts':1,'Delete':1,'Delete account':1,
                                        'Modify Employee Role':2,'Modify':2,'Modify Employee':2,
                                        'Modify Employees':2,'Modify Employees Role':2,
                                        'Modify Role':2,'Role':2,'Employee Role':2,'Employees Role':2,'Roles':2,
                                        'Back to menu...':3,'Back':3,'Menu':3,'Back to menu':3})
                if chosen == '0':
                    acc_CreateMNG()
                elif chosen == '1':
                    acc_DeleteMNG()
                elif chosen == '2':
                    acc_ModifyMNG()
                elif  chosen == '3':
                    break
                continue

        def orderManagement(): #For altering order status.

            def statusModify(omHeaderi,omHeader2i,omLists2i):
                ad.cls_terminal()
                pendingLists = ad.filterByValue(omLists2i,omHeader2i,'Status','Pending',True,True) #Retrive rows that is pending.
                omPath = 'List_Order'
                if pendingLists == None:
                    return None
                ad.list_Sorting(omHeader2i,pendingLists)
                options = {v: k[0] for v, k in enumerate(pendingLists)} #Create dict with only OrderID and Index.
                cancel = len(pendingLists)
                options[cancel] = 'Cancel'
                print(f'\n{cancel + 1}. Cancel status modification...\n')
                choice = ad.multiOptCheck(False,False,'','Select a row for modification: ',
                                            'Please insert a valid option on the list!: ',options)
                choiceInt = int(choice)
                if choiceInt == cancel:
                    return False
                ad.cls_terminal()
                senOut = 'Choose an order to mark status as done: '
                while True:
                    ad.cls_terminal()
                    selOrderid = pendingLists[choiceInt][0]
                    selOrderUser = pendingLists[choiceInt][1]
                    print(f'----Selected order {selOrderid} by user {selOrderUser}----\n')
                    pendingLists = [row for row in pendingLists if row[0] == pendingLists[choiceInt][0]]
                    omHeader2i = ad.resequenceHeaderPair(omHeader2i)
                    omHeader3, omLists3 = ad.filterLists(omHeader2i,pendingLists,
                                                ['OrderItem','Quantity','TransactionDate','Status'])
                    ad.list_Sorting(omHeader3,omLists3)
                    options = {k[0]:str(v) for v, k in enumerate(omLists3)} #Create dict with only OrderID and Index.
                    cancel = len(omLists3)
                    options['Cancel'] = cancel
                    options['cancel modification'] = cancel
                    options['Cancel status modification'] = cancel
                    print(f'\n{cancel+1}. Cancel status modification...\n')
                    choice1 = ad.multiOptCheck(False,False,'#cancel',senOut,'Please insert a valid option!: ',options)
                    choice2 = int(choice1)
                    if choice2 == cancel:
                        input('\nCancelled! Nothing has been modified, hit ENTER to continue...')
                        return False
                    print(f'\nConfirm your action again?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        valueIndex2 = ad.returnRowIndexbyList([selOrderid,selOrderUser] + omLists3[choice2],omLists2i) #Search ori row index by given list.
                        ad.modCsv(omPath,{'Colomn':omHeaderi['Status'],'Row':valueIndex2},'Done')
                        input('\nSuccessfully updated status to done! Hit ENTER to continue...')
                        break
                    elif confirm == '1':
                        input('\nCancelled! Nothing has been modified. Hit ENTER to continue...')
                        break
                return False

            while True:
                ad.cls_terminal()
                print('----Order Management----')
                omHeader, omLists = ad.retrive_csv('List_Order')
                omHeader2, omLists2 = ad.filterLists(omHeader,omLists,['OrderID','Username','OrderItem',
                                            'Quantity','TransactionDate','Status'])
                ad.list_Sorting(omHeader2, omLists2)
                print("\n1. Change order status\n2. Back to Manager options\n")
                choice = ad.multiOptCheck(False,False,'','Choose an action: ','Please insert a valid option!: '
                                    ,{'Change order status':0,'Change':0,'order':0,'status':0,'order status':0,
                                        'Back to Manager options':1,'Back':1,'Manager options':1,'options':1})
                if choice == '0':
                    innerAct = statusModify(omHeader,omHeader2,omLists2)
                elif choice == '1':
                    return
                
                if innerAct == None:
                    print('---Pending list inspect---\n')
                    input('\nThere are no pending lists! Hit ENTER to continue...')
                    continue

        def financeManagement(): #For viewing financial reports.
            
            def expensesInsert():
                while True:
                    ad.cls_terminal()
                    print(f'--Recording Monthly Expense for {dateInquiry}--\n\n')
                    print('vv You may insert the following expenses, be sure to double check before entering! vv')
                    laberCost = ad.num_check_multi(1,'1- Insert the laber costs of the month (#cancel to cancel): ',
                                    '1- Please insert a valid number for laber costs! (#cancel to cancel): ','#cancel','',0,'','float')
                    if laberCost == None:
                        return None
                    laberCost = f'{laberCost[0]:.2f}'
                    ingredientCost = ad.num_check_multi(1,'2- Now, Insert the ingredient costs of the month (#cancel to cancel): ',
                                    '2- Please insert a valid amount for ingredient costs! (#cancel to cancel): ','#cancel','',0,'','float')
                    if ingredientCost == None:
                        return None
                    ingredientCost = f'{ingredientCost[0]:.2f}'
                    utilityCost = ad.num_check_multi(1,'3- Lastly, insert the utility costs of the month (#cancel to cancel): ',
                                    '3- Please insert a valid costs for utility! (#cancel to cancel): ','#cancel','',0,'','float')
                    if utilityCost == None:
                        return None
                    utilityCost = f'{utilityCost[0]:.2f}'
                    TotalCost = f'{float(laberCost) + float(ingredientCost) + float(utilityCost):.2f}'
                    newExpenseList = [f'{dateInquiry}-01',laberCost,ingredientCost,utilityCost,TotalCost]
                    ad.cls_terminal()
                    print(f'--Recording Monthly Expense for {dateInquiry}--\n\n')
                    print(f'vv Please double check the following expenses: vv{ad.list_Sorting(expenseHeadings,newExpenseList)}')
                    print(f'\n\n1. Confirm\n2. Redo\n3. Cancel...')
                    confirmed = ad.multiOptCheck(False,False,'',f'Confirm to record into expenses of {f'{dateInquiry}-01'}?: ',
                                        'Please choose yes or no!: ',{'Confirm':0,'Confirmed':0,'Redo':1,'Retry':1,'Cancel':2,'Cancel...':2})
                    if confirmed == '0':
                        ad.appdCsv(pathListExpenses,newExpenseList)
                        input('\nMonthly expenses has been successfull recorded! Hit ENTER to proceed inspecting monthly report...')
                        return
                    elif confirmed == '1':
                        continue
                    elif confirmed == '2':
                        input('\nMonthly expenses not recorded, report enquiry has been cancelled. Hit ENTER to return...')
                        return None

            def financeReport():
                financeDisplayHead = expenseHeadings
                
                ad.cls_terminal()
                if len(productFiltered) == 0: #Exist and complete will definitely be False, cashier haven't made any report too.
                    finalFinanceRow = [f'{dateInquiry}-01','-',totalExpense,'-']
                    ad.appdCsv(pathFinance,finalFinanceRow)
                    titleOut = '-- Monthly Finance Report (Incomplete) --'
                    sentenceOut = f'\n\n^^ Monthly report for {dateInquiry} was not complete, please request sales performance report from cashier! ^^'
                    refresh = True
                    
                elif not finIncomeExist and len(productFiltered) != 0:
                    finalFinanceRow = [f'{dateInquiry}-01','-',totalExpense,'-']
                    titleOut = '-- Monthly Finance Report (Incomplete) --'
                    sentenceOut = f'\n\n^^ Monthly report for {dateInquiry} was not complete, please request sales performance report from cashier! ^^'
                    refresh = False

                elif finIncomeExist and not finRowComplete: #Cashier has sent report, manager first time viewing.
                    finanaceRow = ad.retrive_csv(pathFinance)[1]
                    finanaceRowIndex = ad.returnValueIndex(f'{dateInquiry}-01',0,finanaceRow)
                    income = float(finanaceRow[finanaceRowIndex][1])
                    profits = f'{income - float(totalExpense):.2f}'
                    ad.modCsv(pathFinance,{'Column':2,'Row':finanaceRowIndex},totalExpense)
                    ad.modCsv(pathFinance,{'Column':3,'Row':finanaceRowIndex},profits)
                    finalFinanceRow = ad.retrive_csv(pathFinance)[1][finanaceRowIndex]
                    titleOut = f'-- Finance Report for {dateInquiry} --'
                    sentenceOut = f'\n\n^^ Final monthly report for {dateInquiry} ^^'
                    refresh = True

                elif finRowComplete: #Cashier has sent report, manager has also enquiried before.
                    ad.cls_terminal()
                    finalFinanceRow = ad.retrive_csv(pathFinance)[1]
                    titleOut = f'-- Finance Report for {dateInquiry} --'
                    sentenceOut = f'\n\n^^ Final monthly report for {dateInquiry} ^^' 
                    refresh = False

                newFinanceHead, newFinanceList = ad.filterLists(financeHead,finalFinanceRow,['Income','Profits'])
                newFinanceHead = ad.resequenceHeaderPair(newFinanceHead)
                newFinanceList = newFinanceList[0]
                financeDisplayList = inMonthExpense + newFinanceList
                financeDisplayHead[list(newFinanceHead.keys())[0]] = 5
                financeDisplayHead[list(newFinanceHead.keys())[1]] = 6
                print(titleOut)
                ad.list_Sorting(financeDisplayHead,financeDisplayList)
                print(sentenceOut)
                if refresh:
                    input('Page refresh required after updates. Hit ENTER to proceed...')
                    return True
                elif not refresh:
                    input('Hit ENTER to return...')
                    return

            def productReport():
                senOut = 'Select a filter to apply: '
                while True:
                    ad.cls_terminal()
                    print('-- Product Sales Performance Report --')
                    ad.list_Sorting(proReportHead,inProPerformance)
                    if not finIncomeExist:
                        input(f'\nSales performance report for {dateInquiry} not found, please request submission from cashier!\nHit ENTER to return...')
                        return
                    print('\n1. Filter by Product\n2. Filter by Sold\n3. Filter by Revenue\n4. Filter by Rating\n5. Return...\n')
                    choice = ad.multiOptCheck(False,False,'',senOut,'Please select a valid option!: ',
                                            {'Filter by Product':0,'Product':0,'by Product':0,
                                            'Filter by Sold':1,'Sold':1,'Order Item':1,'Order':1,'Item':1,
                                            'Filter by Revenue':2,'Revenue':2,'by Revenue':2,
                                            'Filter by Rating':3,'Rating':3,'by Rating':3,'Rates':3,
                                            'Return...':4,'Return':4})
                    if choice == '0':
                        focusHead = 'Product'
                        keyword = input('Enter product name to filter by: ')
                        filtering = ad.filterByValue(inProPerformance,proReportHead,focusHead,keyword,False,False)
                    elif choice == '1':
                        focusHead = 'Sold'
                        keyword = ad.num_check_multi(1,"Enter quantity sold to filter by.(-1 for '-'): ",
                                        "Please insert a valid integer for quantity! (-1 for '-'): ",'','',-1,'','int')[0]
                        if keyword == -1:
                            filtering = ad.filterByValue(inProPerformance,proReportHead,focusHead,'-',False,True)
                        else:
                            filtering = ad.numTrackFilter(int,'',keyword,'','c',True,proReportHead,focusHead,inProPerformance,True)

                    elif choice == '2':
                        focusHead = 'Revenue'
                        keyword = ad.num_check_multi(1,"Enter a revenue to filter by. (-1 for '-'): ",
                                        "Please insert a valid amount for revenue! (-1 for '-'): ",'','',-1,'','float')[0]
                        if keyword == -1:
                            filtering = ad.filterByValue(inProPerformance,proReportHead,focusHead,'-',False,True)
                        else:
                            filt1 = ad.numTrackFilter(float,'',keyword,'','a',True,proReportHead,focusHead,inProPerformance,True)
                            filtering = ad.numTrackFilter(float,'',keyword+1,'','b',False,proReportHead,focusHead,filt1,True)
                    
                    elif choice == '3':
                        focusHead = 'AverageRating'
                        keyword = ad.num_check_multi(1,"Enter a rating to filter by. (0-5, -1 for '-'): ",
                                        "Please insert between 0 - 5! (-1 for '-'): ",'','',-1,5,'float')[0]
                        if keyword == -1:
                            filtering = ad.filterByValue(inProPerformance,proReportHead,focusHead,'-',False,True)
                        else:
                            filt1 = ad.numTrackFilter(float,'',keyword,'','a',True,proReportHead,focusHead,inProPerformance,True)
                            filtering = ad.numTrackFilter(float,'',keyword+1,'','b',False,proReportHead,focusHead,filt1,True)
                    elif choice == '4':
                        return

                    ad.cls_terminal()
                    if filtering == None:
                        senOut = "\033[1mKeyword doesn't exist!\033[0m Try again: "
                    else:
                        senOut = 'Select a filter to apply: '
                        print('-- Product Sales Performance Report --')
                        ad.list_Sorting(proReportHead,filtering)
                        print(f'\n^^ Filtered by {focusHead} with keyword "{keyword}" ^^')
                        input('\nHit ENTER to retry...')
                    ad.cls_terminal()
                    continue

            while True:
                ad.cls_terminal()
                pathFinance = 'Report_Finance'
                financeHead, financeLists = ad.retrive_csv(pathFinance)
                pathReportProduct = 'Report_Product'
                proReportHead, proReportList = ad.retrive_csv(pathReportProduct)
                pathListExpenses = 'List_Expenses'
                expenseHeadings, expenseLists = ad.retrive_csv(pathListExpenses)
                print('---Monthly Report Inquiry---\n\n')
                print('vv Select a month to view finance report and sales performance: YYYY-MM (e.g. 2024-08, 2023-12) vv\n')
                senOut = 'Insert desired year-month to inspect report of the month (#cancel to cancel): '
                while True:
                    dateInquiry = input(senOut)
                    if dateInquiry.lower() == '#cancel':
                        return
                    if not dateInquiry.replace('-','0').isdigit():
                        senOut = 'Year-Month should consist of integer! Please refer to example above and try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    if not len(dateInquiry) == 7:
                        senOut = 'Date format should be YYYY-MM! Please try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    if ad.numTrackFilter(dt.datetime,'YYYY-MM',dateInquiry,dt.datetime.strftime(dt.datetime.now(),'%Y-%m'),
                                        'a',True,financeHead,'Month',financeLists,False): #To check if requested month ended.
                        senOut = 'Monthly report can only exist after the month ends! Please try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    productFiltered = ad.numTrackFilter(dt.datetime,'YYYY-MM',dateInquiry,'','c',True,
                                                    financeHead,'Month',financeLists,True)
                    if productFiltered == None:
                        senOut = 'Invalid inputs! Please refer to example above and try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    finIncomeExist = False
                    finRowComplete = False
                    finExpenseDone = False
                    if len(productFiltered) != 0: #If enquiry date existed in report.
                        if productFiltered[0][3] != '-': #If profits have already been calculated (means no missing info)
                            finRowComplete = True #Every information is complete, no calculation needed.
                        if productFiltered[0][2] != '-':
                            finExpenseDone = True
                        if productFiltered[0][1] != '-': #If cashier already submitted report.
                            finIncomeExist = True
                    dateFormat = ad.dtFormatConverter('YYYY-MM')
                    if not finExpenseDone:
                        inMonthExpense = ad.numTrackFilter(dt.datetime,dateFormat,dateInquiry,'','c',True,
                                                        expenseHeadings,'Month',expenseLists,True)[0]
                        if inMonthExpense == None: #If manager haven't key in expenses for the month.
                            print(f'Monthly expenses for {dateInquiry} have not been recorded yet, proceed to finalize costs?')
                            print('1. Yes\n2. No')
                            confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                            if confirm == '0':
                                expenseCall = expensesInsert()
                                if expenseCall == None:
                                    return
                            elif confirm == '1':
                                input(f'\nMonthly expenses for {dateInquiry} not found, report enquiry cancelled. Hit ENTER to return...')
                                return
                    inMonthExpense = ad.numTrackFilter(dt.datetime,dateFormat,dateInquiry,'','c',True,
                                                    expenseHeadings,'Month',expenseLists,True)[0]
                    totalExpense = inMonthExpense[4]
                    while True:
                        ad.cls_terminal()
                        expenseHeadings, expenseLists = ad.retrive_csv(pathListExpenses)
                        print('---Monthly Report Inquiry---\n')
                        print(f'Choose a report to view for {dateInquiry}: ')
                        print('1. General finance report\n2. Expenses report\n3. Product performance report\n4. Return to menu...')
                        review = ad.multiOptCheck(False,False,'','Choose an option: ','Please select an available option!: ',
                        {'General finance report':0,'General':0,'finance':0,'General finance':0,'finance report'
                        'Expenses report':1,'Expense report':1,'Expense':1,'Expenses':1,
                        'Product performance report':2,'Product performance':2,'Products':2,'performance report':2,'Product report':2,
                        'Return to menu...':3,'Return to menu':3,'Return menu':3,'Return':3,'menu':3,'menu...':3})

                        ad.cls_terminal()
                        if review == '0': #Finance will be calculated if first view for the month.
                            innerAct = financeReport()
                            if innerAct == True:
                                break
                            continue
                        elif review == '1': #Expenses has already been calculated above.
                            print(f'---Monthly expenses report for {dateInquiry}---')
                            ad.list_Sorting(expenseHeadings,inMonthExpense)
                            input('\nHit ENTER to view other options...')
                        elif review == '2': #If cashier haven't submit product report, return. Else, review with filtering options.
                            print(f'---Product performance report for {dateInquiry}---')
                            inProPerformance = ad.numTrackFilter(dt.datetime,dateFormat,dateInquiry,'','c',True,
                                                        proReportHead,'Month',proReportList,True)
                            if inProPerformance == None:
                                print(f'Product performance for {dateInquiry}-01 have not been recorded yet, please inform cashier to submit sales report')
                                input('Hit ENTER to view other options...')
                                continue
                            productReport()
                        elif review == '3':
                            return
                    break

        def inventoryControl(): #For managing inventory for ingredients.

            def ingredientMNG():

                def ingredientAdd():
                    ad.cls_terminal()
                    print('---Adding new ingredient---\n')
                    senOut1 = 'Insert an new ingredient to add in stock (#cancel to cancel): '
                    while True:
                        newIngr = ad.alphaInputChecker(True,'','#cancel',r' ;.()',senOut1
                                            ,'Please inesrt a valid ingredient name! (#cancel to cancel): ')
                        if newIngr == None:
                            input('\nNothing has been added. Hit ENTER to return...')
                            return
                        elif any(i for i in ingreList if newIngr.lower() == i[0].lower()):
                            senOut1 = 'Ingredient already exists! Please add something else (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        break
                    newStocked = ad.num_check_multi(1,f"Enter the current stock of {newIngr} in kg (#cancel to cancel): ",
                                                "Please insert a valid stock amount of kg! (#cancel to cancel): ",
                                                '#cancel','',0.1,'','float')
                    if newStocked == None:
                        input('\nNothing has been added. Hit ENTER to return...')
                        return
                    newStocked = newStocked[0]
                    print(f'\nConfirm adding ingredient {newIngr}, stocked {newStocked} kg?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        newAppdIng = [newIngr,str(newStocked)]
                        ad.appdCsv(pathIngredient,newAppdIng)
                        input('\nNew ingredient has been added into stocks! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been added. Hit ENTER to return...')
                        return

                def ingredientUpdate():
                    ad.cls_terminal()
                    print('---Updating Ingridient Information---')
                    ad.list_Sorting(ingreHead,ingreList)
                    option = {k[0]:v for v, k in enumerate(ingreList)}
                    print('')
                    updIngr = ad.multiOptCheck(False,False,'#cancel','Select an ingredient to update (#cancel to cancel): ',
                                            'Please choose an available ingredient to update! (#cancel): ',option)
                    if updIngr == None:
                        input('Nothing has been changed. Hit ENTER to return...')
                        return
                    updStocked = ad.num_check_multi(1,f"Enter the current stock of {ingreList[int(updIngr)][0]} in kg (#cancel to cancel): ",
                                                "Please insert a valid stock amount of kg! (#cancel to cancel): ",
                                                '#cancel','',0.1,'','float')
                    if updStocked == None:
                        input('\nNothing has been changed. Hit ENTER to return...')
                        return
                    updStocked = updStocked[0]
                    print(f'\nConfirm updating ingredient {ingreList[int(updIngr)][0]} to {updStocked} kg in stock?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        updRow = ad.returnValueIndex(updIngr,0,ingreList)
                        ad.modCsv(pathIngredient,{'Column':1,'Row':updRow},updStocked)
                        input('\nIngredient information has been updated! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been added. Hit ENTER to return...')
                        return

                def ingredientDelete():
                    ad.cls_terminal()
                    print('---Delete an ingredient---')
                    ingreOnlyHead, ingreOnlyLists = ad.filterLists(ingreHead,ingreList,['Ingredient'])
                    ad.list_Sorting(ingreOnlyHead,ingreOnlyLists)
                    print('')
                    option = {k[0]:v for v, k in enumerate(ingreList)}
                    delIngr = ad.multiOptCheck(False,False,'#cancel','Select an ingredient to remove (#cancel to cancel): ',
                                            'Please choose an existed ingredient for deletion! (#cancel to cancel): ',option)
                    if delIngr == None:
                        input('Nothing has been removed. Hit ENTER to return...')
                        return
                    delIngr = int(delIngr)
                    print(f'\nAre you sure to remove the {ingreList[delIngr][0]} from stock system?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        ad.delRowCsv(pathIngredient,ingreList[delIngr])
                        input('\nIngredient has been removed from system! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been deleted. Hit ENTER to return...')
                        return
                    return

                while True:
                    ad.cls_terminal()
                    print('---Ingredient Stock Management---\n')
                    pathIngredient = 'Inventory_Ingredient'
                    ingreHead, ingreList = ad.retrive_csv(pathIngredient)
                    print('1. Add ingredient\n2. Update ingredient stock\n3. Delete ingredient\n4. Exit...')
                    action = ad.multiOptCheck(False,False,'','Choose an operation: ',
                                            'Please choose a valid operation! i=', 
                                            {'Add new ingredient':0,'Add':0,'new':0,
                                            'Update ingredient stock':1,'Ingredient stock':1,'Stock':1,
                                            'Update stock':1,'Stocks':1,'Update':1,
                                            'Delete ingredient':2,'Delete':2,
                                            'Exit...':3,'Exit':3})
                    if action == '0':
                        ingredientAdd()
                    elif action == '1':
                        ingredientUpdate()
                    elif action == '2':
                        ingredientDelete()
                    elif action == '3':
                        break
                return
            
            def productMNG():
                
                def modifyMargin():
                    marginPercentage = int(currentMargin * 100 - 100)
                    print(f'---Modify product margin---\n\nCurrent product margin: {marginPercentage}%')
                    print('Note that every product will share the same margin, new updated margin will be applied to all current listings!\n')
                    newMargin = ad.num_check_multi(1,'Insert a new margin percentage between 10-200 (#cancel to cancel): ',
                                                'Please insert a valid margin between 10-200! (#cancel to cancel): ','#cancel',
                                                '',10,200,'int')
                    if newMargin == None:
                        return None
                    newMargin = newMargin[0]
                    ad.cls_terminal()
                    print(f"\nConfirm updating product margin to {newMargin}%?\n1. Yes\n2. No")
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        newPercentage = str(newMargin)
                        newMargin = 1 + float(newMargin) / 100
                        for index, row in enumerate(proList):
                            rowPrice = f'{int((float(row[1]) * newMargin) * 100 + 0.5) / 100:.2f}'
                            if row[3].isdigit():
                                rowFinal = f'{int(float(rowPrice) * (1 - int(row[3])/100) * 100 + 0.5) / 100:.2f}'
                            else:
                                rowFinal = rowPrice
                            ad.modCsv(pathListProduct,{'Column':2,'Row':index},rowPrice)
                            ad.modCsv(pathListProduct,{'Column':4,'Row':index},rowFinal)
                        print(f"\nProduct margin has been updated to {newPercentage}%, listings' price has been syncronized with the new margin!")
                        print('Hit ENTER to return...')
                        return newMargin
                    elif confirm == '1':
                        input(f'\nNothing has been changed, margin remained {marginPercentage}%. Hit ENTER to return...')
                        return None

                def addProduct():
                    ad.cls_terminal()
                    print('---Adding a new Product---\n')
                    senOut1 = 'Insert an new Product to add in menu(#cancel to cancel): '
                    while True:
                        newProduct = ad.alphaInputChecker(True,'','#cancel',r' ;.()',senOut1
                                            ,'Please inesrt a valid Product name! (#cancel to cancel): ')
                        if newProduct == None:
                            input('\nNothing has been added. Hit ENTER to return...')
                            return
                        elif any(i for i in proList if newProduct.lower() == i[0].lower()):
                            senOut1 = 'Product already exists! Please add something else (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        break
                    newProduct = ' '.join([word.capitalize() for word in newProduct.split()]) #Capitalize each first letter.
                    newCosts = ad.num_check_multi(1,f"Enter the cost of making for {newProduct} (#cancel to cancel): ",
                                                "Please insert a vali price! (#cancel to cancel): ",
                                                '#cancel','',0.1,'','float')
                    if newCosts == None:
                        input('\nNothing has been added. Hit ENTER to return...')
                        return
                    newCosts = newCosts[0]
                    newCosts = f'{int(newCosts * 100 + 0.5) / 100:.2f}' #Ensure it's always in 2 decimal point.
                    newPrice = f'{int((float(newCosts) * currentMargin) * 100 + 0.5) / 100:.2f}'
                    ad.cls_terminal()
                    print(f'\nConfirm adding Product{newProduct}, cost RM{newCosts}, selling for RM{newPrice}?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        newAppdIng = [newProduct,newCosts,newPrice,'-',newPrice,'-']
                        ad.appdCsv(pathListProduct,newAppdIng)
                        input('\nNew Product has been added into the menu! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been added. Hit ENTER to return...')
                        return
                    return

                def updateProduct():
                    ad.cls_terminal()
                    print('---Updating Product Detail---')
                    ad.list_Sorting(proHead,proList)
                    option = {k[0]:v for v, k in enumerate(proList)}
                    print('')
                    updProduct = ad.multiOptCheck(False,False,'#cancel','Select an product to update (#cancel to cancel): ',
                                            'Please choose an available product to update! (#cancel): ',option)
                    if updProduct == None:
                        input('Nothing has been changed. Hit ENTER to return...')
                        return
                    updCosts = ad.num_check_multi(1,f"Enter the current cost of {proList[int(updProduct)][0]} (#cancel to cancel): ",
                                                "Please insert a valid cost! (#cancel to cancel): ",
                                                '#cancel','',0.10,'','float')
                    if updCosts == None:
                        input('\nNothing has been changed. Hit ENTER to return...')
                        return
                    updCosts = updCosts[0]
                    updCosts = f'{int(updCosts * 100 + 0.5) / 100:.2f}' #Ensure it's always in 2 decimal point.
                    updPrice = f'{int((float(updCosts) * currentMargin) * 100 + 0.5) / 100:.2f}'
                    print(f"\nConfirm updating product {proList[int(updProduct)][0]}'s costs of making to RM{updCosts}?\n1. Yes\n2. No")
                    confirm = ad.multiOptCheck(False,False,'','Confirm your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        updRow = ad.returnValueIndex(updProduct,0,proList)
                        ad.modCsv(pathListProduct,{'Column':1,'Row':updRow},updCosts)
                        ad.modCsv(pathListProduct,{'Column':2,'Row':updRow},updPrice)
                        if proList[int(updProduct)][3].isdigit():
                            updFinal = f'{int(float(updPrice) * (1 - int(proList[int(updProduct)][3])/100) * 100 + 0.5) / 100:.2f}'
                            ad.modCsv(path_AccList,{'Column':4,'Row':updRow},updFinal)
                        input('\nProduct pricing details has been updated! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been added. Hit ENTER to return...')
                        return

                def deleteProduct():
                    ad.cls_terminal()
                    print('---Remove a product---')
                    productOnlyHead, productOnlyLists = ad.filterLists(proHead,proList,['Product'])
                    ad.list_Sorting(productOnlyHead,productOnlyLists)
                    print('')
                    option = {k[0]:v for v, k in enumerate(proList)}
                    delProduct = ad.multiOptCheck(False,False,'#cancel','Select an product to remove from the menu (#cancel to cancel): ',
                                            'Please choose an existed product for deletion! (#cancel to cancel): ',option)
                    if delProduct == None:
                        input('Nothing has been removed. Hit ENTER to return...')
                        return
                    delProduct = int(delProduct)
                    ad.cls_terminal()
                    print(f'\nAre you sure to remove {proList[delProduct][0]} from the menu?\n1. Yes\n2. No')
                    confirm = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if confirm == '0':
                        ad.delRowCsv(pathListProduct,proList[delProduct])
                        input('\nProduct has been removed from menu! Hit ENTER to return...')
                        return
                    elif confirm == '1':
                        input('\nNothing has been deleted. Hit ENTER to return...')
                        return
                    return

                while True:
                    ad.cls_terminal()
                    pathListProduct = 'List_Product'
                    proHead, proList = ad.retrive_csv(pathListProduct)
                    currentMargin = ad.filterLists(proHead,proList,['Cost','Price'])[1] #To get current margin price
                    currentMargin = float(currentMargin[0][1]) / float(currentMargin[0][0]) #Every product have same margin.
                    print('---Product Listing Management---\n')
                    print('1. Change margin\n2. Add product\n3. Update product detail\n4. Delete product\n5. Exit...')
                    chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                                                {'Change margin':0, 'Change':0, 'margin':0, 'margins':0, 'Change margins':0,
                                                'Add product':1,'add':1,'new':1,
                                                'Update product details':2,'Product':2,'update':2,
                                                'details':2,'update details':2,'update product':2,
                                                'Delete product':3,'Delete':3,'Exit':4,'Exit...':4})
                    ad.cls_terminal()
                    if chosen == '0':
                        newMargin = modifyMargin()
                        if newMargin != None:
                            currentMargin = newMargin
                    elif chosen == '1':
                        addProduct()
                    elif chosen == '2':
                        updateProduct()
                    elif chosen == '3':
                        deleteProduct()
                    elif chosen == '4':
                        break  
                return

        #Inventory menu that leads to ingredient and product management.
            while True:
                ad.cls_terminal()
                print('----Inventory Management----\n')
                print('1. Ingredient stock management\n2. Manage products\n3. Back to Menu...')
                chosen = ad.multiOptCheck(False,False,'','Choose an option: ',
                                        'Please insert a valid option: ',
                                        {'Manage Ingredient':0,'Ingredient':0,'Ingredients':0,'stock':0,'stocks':0,
                                        'Manage stock management':0,'Manage stock':0,'stock management':0,
                                        'Manage products':1,'Manage product':1,'Product':1,'Products':1,
                                        'Back to menu...':2,'Back':2,'Menu':2,'Back to menu':2,'Exit':2})
                if chosen == '0':
                    ingredientMNG()
                elif chosen == '1':
                    productMNG()
                elif chosen == '2':
                    input('\nHit ENTER to continue...')
                    break
            return

        def customerFeedback(): #For viewing customer feedback.

            ad.cls_terminal()
            print('----Customer Feedback Monitor----\n')
            orderDict, orderList = ad.retrive_csv('List_Order')
            feedbackDict, feedbackList = ad.filterLists(orderDict,orderList,
                                    ['OrderID','Username','OrderItem','TransactionDate','Rating','Feedback'])

            #Filter functions are ran by generator expression for efficiency.

            def filterUsername(userName:str):
                return ad.filterByValue(feedbackList,feedbackDict,'Username',userName,False,False)
            
            def filterItem(orderItem:str):
                return ad.filterByValue(feedbackList,feedbackDict,'OrderItem',orderItem,False,False)

            def filterRating(rates:int):
                if rates == 0:
                    return ad.filterByValue(feedbackList,feedbackDict,'Rating','-',False,True)
                else:
                    outputRate = ad.numTrackFilter(int,'',rates,'','c',True,feedbackDict,'Rating',feedbackList,True)
                return outputRate


            senOut = 'Choose a filter to apply: '
            while True:
                ad.list_Sorting(feedbackDict,feedbackList)
                print('\n1. Filter by Username\n2. Filter by OrderItem\n3. Filter by Rating\n4. Exit...')
                choice = ad.multiOptCheck(False,False,'',senOut,'Please select a valid option!: ',
                                        {'Filter by Username':0,'Username':0,'by Username':0,
                                        'Filter by OrderItem':1,'OrderItem':1,'Order Item':1,'Order':1,'Item':1,
                                        'Filter by Rating':2,'Rating':2,'by Rating':2,
                                        'Exit...':3,'Exit':3})

                if choice == '0':
                    focusHead = 'Username'
                    keyword = input('Enter username to filter by: ')
                    output = filterUsername(keyword)

                elif choice == '1':
                    focusHead = 'OrderItem'
                    keyword = input('Enter order item to filter by: ')
                    output = filterItem(keyword)

                elif choice == '2':
                    focusHead = 'Rating'
                    keyword = ad.num_check_multi(1,"Enter rating to filter by (1-5, 0 for '-'): ",
                                    "Please insert between 0 - 5! (0 for '-'): ",'','',0,5,'int')[0]
                    output = filterRating(keyword)

                elif choice == '3':
                    input('\nHit ENTER to exit...')
                    return
            
                ad.cls_terminal()
                if output == None:
                    senOut = "\033[1mKeyword doesn't exist!\033[0m: "
                    continue
                ad.list_Sorting(feedbackDict,output)
                print(f'\n^^ Filtered by {focusHead} with keyword "{keyword}" ^^')
                input('\nHit ENTER to continue...')
                print('\n\n')
                ad.cls_terminal()
                continue

        while True:
            print('----Manager Menu----\n')
            print('1. System Administration\n2. Order Management')
            print('3. Financial Management\n4. Inventory Control')
            print('5. Customer Feedback\n6. Account Settings\n7. Logout\n')
            choose = ad.multiOptCheck(False,False,'','Choose an operation: ',
                                    'Please insert an available operation!: ',
            {'System Administration':0,'System':0,'Admin':0,'System Admin':0,'Administration':0,
            'Order Management':1,'Order':1,
            'Financial Management':2,'Financial':2,
            'Inventory Control':3,'Inventory':3,'Control':3,
            'Customer Feedback':4,'Customer':4,'Feedback':4,
            'Account Settings':5,'Account':5,'Settings':5,'Setting':5,
            'Logout':6,'Log out':6,'Out':6})
            ad.cls_terminal()
            if choose == '0':
                ststemAdministration()
            if choose == '1':
                orderManagement()
            elif choose == '2':
                financeManagement()
            elif choose == '3':
                inventoryControl()
            elif choose == '4':
                customerFeedback()
            elif choose == '5':
                employeeSettings(username)
            elif choose == '6':
                return
            ad.cls_terminal()
            continue


    def CustomerMenu(username:str):
        print(f'====Welcome back, dear {username}!====\n')
        userCart = {k[0]:0 for k in ad.retrive_csv('List_Product')[1]} #Create a cart with all products default in 0.
        limit = 40

        def browseProduct():
            while True:
                pathListProduct = 'List_Product'
                productHead, productLists = ad.retrive_csv(pathListProduct)
                menuDisplayHead, menuDisplayList = ad.filterLists(productHead,productLists,
                                                        ['Product','Price','Discounts(%)','FinalPrice'])
                menuDisplayHead2 = ad.resequenceHeaderPair(menuDisplayHead)
                menuDisplayHead2['Latest Mothly Rating'] = len(menuDisplayHead2)
                menuDisplayHead2['Previous Monthly Sales'] = len(menuDisplayHead2)
                pathListOrder = 'Report_Product'
                proPerformHead, proPerformList = ad.retrive_csv(pathListOrder)
                productCheck = ad.filterLists(productHead,productLists,['Product'])[1]
                latestPopularity = {} #Example -> {'Product1':[4.5,30],'Prduct2':[4.2,28]}. The list consist avg rate & sold.
                for i in range(0, len(productLists)):
                    product = productCheck[i][0]
                    iProductPerform = ad.filterByValue(proPerformList,proPerformHead,'Product',product,False,True) #Exist in previous reports.
                    if iProductPerform == None:
                        latestPopularity[productCheck[i][0]] = ['-','-']
                        continue
                    preProductRate = ad.numTrackFilter(int,'',0,'','a',True,proPerformHead,'Sold',iProductPerform,True)
                    if preProductRate == None or preProductRate == [] or preProductRate == [[]]:
                        latestPopularity[productCheck[i][0]] = ['-','-']
                    else: #Previous AverageRating exist.
                        monthsReviewed = ad.filterLists(proPerformHead,preProductRate,['Month'])[1]
                        newest = dt.datetime.fromisoformat(monthsReviewed[0][0])
                        for dates in monthsReviewed:
                            if dt.datetime.fromisoformat(dates[0]) > newest:
                                newest = dt.datetime.fromisoformat(dates[0])
                        newest = dt.datetime.strftime(newest,'%Y-%m-01')
                        latestMonthPro = ad.filterByValue(preProductRate,proPerformHead,'Month',newest,False,True)
                        latestPopularity[productCheck[i][0]] = [latestMonthPro[0][4],latestMonthPro[0][2]]
                menuDisplayList2 = []
                for d in range(0, len(menuDisplayList)):
                    proName = menuDisplayList[d][0]
                    indexDict = [i for i, x in enumerate(latestPopularity.keys()) if x == proName][0]
                    menuDisplayList2.append(menuDisplayList[d]+list(latestPopularity.values())[indexDict])
                ad.cls_terminal()
                print('\n---Product Menu---')
                ad.list_Sorting(menuDisplayHead2,menuDisplayList2)
                cancel = len(menuDisplayList2)
                print(f'\n{cancel+1}. Cancel...')
                menu = {v[0]:k for k,v in enumerate(menuDisplayList2)}
                menu['cancel'] = cancel
                menu['Cancel'] = cancel
                choseProduct = ad.multiOptCheck(False,False,'#cancel','\nChoose a product to purchase (#cancel to cancel): ',
                                                    'Please choose a product from the list! (#cancel to cancel): ',menu)
                choseProduct = int(choseProduct)
                if choseProduct == cancel:
                    return
                ad.cls_terminal()
                print('---Chosen product: vvv ---')
                ad.list_Sorting(menuDisplayHead2,menuDisplayList2[choseProduct])
                print('\n')
                senOut = f'Insert a quantity to add to cart (maximum {limit}; #cancel to cancel): '
                while True:
                    quantity = ad.num_check_multi(1,senOut,
                            f'Please insert a valid quantity to add into cart! (maximum {limit}; #cancel to cancel): ',
                            '#cancel','',1,limit,'int')
                    if quantity == None:
                        input('\n\nNothing has been added. Hit ENTER to return to menu...')
                        break
                    quantity = quantity[0]
                    productName = menuDisplayList2[choseProduct][0]
                    addedQuantity = quantity + userCart.get(productName)
                    if addedQuantity > limit:
                        senOut = f'You have reached the maximum quantity ({userCart.get(productName)} in cart)! Try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    break
                if quantity == None:
                    continue
                print(f'\n\nConfirm adding product {productName}, with quantity {quantity} into shopping cart?\n1. Yes\n2. No')
                confirm = ad.multiOptCheck(False,False,'','Choose your action: ', 'Please choose yes or no!: ',
                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                if confirm == '0':
                    ad.cls_terminal()
                    userCart[productName] += quantity #Increase the quantity of the product in the cart dictionary.
                    print(f'.\n.\n.\nProduct \033[1m{productName}\033[0m, has been successfully added into shopping cart with \033[1m{quantity}\033[0m!')
                    input('Hit ENTER to continue browsing menu...')
                    continue
                elif confirm == '1':
                    input('Add to cart cancelled. Hit ENTER to return to menu...')
                    continue

        def viewCart():
            
            def modCart():
                print('--- Edit Shopping Cart ---')
                ad.list_Sorting(cartHead,inCart)
                cancel = len(inCart)
                print(f'\n{cancel+1}. Cancel...')
                cartOpts = {v[0]:k for k,v in enumerate(inCart)}
                cartOpts['cancel'] = cancel
                cartOpts['Cancel'] = cancel
                modProduct = ad.multiOptCheck(False,False,'','\nChoose a product to purchase: ',
                                                    'Please choose a product from the list!: ',cartOpts)
                modProduct = int(modProduct)
                if modProduct == cancel:
                    input('\n\nShopping Cart remained the same. Hit ENTER to return to menu...')
                    return
                ad.cls_terminal()
                modRow = inCart[modProduct]
                modProName = modRow[0]
                quantity = modRow[4]
                print('--- Edit Shopping Cart ---')
                ad.list_Sorting(cartHead,modRow)
                print('\n\n^^ Selected product ^^ Choose your action to the product from cart:')
                print('1. Change Quantity\n2. Remove from cart\n3. Cancel modification...')
                modProduct = ad.multiOptCheck(False,False,'','\nChoose a product to purchase: ',
                                        'Please choose a product from the list! (#cancel to cancel): ',
                                        {'Change Quantity':0,'Change':0,'Quantity':0,'Changes':0,
                                        'Remove from cart':1,'Remove':1,'Removes':1,'Cart':1,'Carts':1,
                                        'Cancel modification...':2,'Cancel':2,'mod':2,'Cancel modification':2})
                
                if modProduct == '2':
                    return
                ad.cls_terminal()
                if modProduct == '0':
                    print('--- Adjusting Quantity ---')
                    print(f'\n\nCurrent quantity of \033[1m{modProName}\033[0m...: \033[1m{quantity}\033[0m\n')
                    newQuantity = ad.num_check_multi(1,f'Insert new quantity between 1 - {limit} (#cancel to cancel): ',
                                    f'Please insert a valid integer between 1 - {limit}! (#cancel to cancel): ','#cancel',
                                    '',1,30,'int')
                    if newQuantity == None:
                        input('\n\nShopping Cart remained the same. Hit ENTER to return to menu...')
                        return
                    newQuantity = newQuantity[0]
                    ad.cls_terminal()
                    print('--- Adjusting Quantity ---\n\n')
                    print(f'Confirm changing quantity of \033[1m{modProName}\033[0m: {quantity} -> \033[1m{newQuantity}\033[0m?: ')
                    print('1. Yes\n2. No\n')
                    modIt = ad.multiOptCheck(False,False,'','Choose an decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if modIt == '0':
                        userCart[modProName] = newQuantity
                        input('Product quantity from cart has been updated! Hit ENTER to return to cart view...')
                        return
                    elif modIt == '1':
                        input('\n\nShopping Cart remained the same. Hit ENTER to return to menu...')
                        return
                elif modProduct == '1':
                    print('--- Removing Item in Cart... ---')
                    print(f'\nAre you sure to remove {quantity} of {modProName} from cart?\n1. Yes\n2. No\n')
                    remove = ad.multiOptCheck(False,False,'','Choose an action: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if remove == '0':
                        userCart[modProName] = 0
                        input(f'\n{modProName} has been discarded from shopping cart. Hit ENTER to return to menu...')
                    elif remove == '1':
                        input('\n\nNothing has been removed. Hit ENTER to return to cart view...')
                        return
                elif choosen == '2':   
                    return

            def payCart():
                transactTime = dt.datetime.strftime(dt.datetime.now(),'%Y-%m-%d %H:%M')
                pathOrder = 'List_Order'
                orderList = ad.retrive_csv(pathOrder)[1]
                newInvoice = orderList[-1][0][:3] + str(int(orderList[-1][0][3:]) + 1)
                print('--- Check-out Cart Items ---')
                totalPrice = ad.customSum([float(i[5]) for i in inCart],2)
                ad.list_Sorting(cartHead,inCart)
                print(f'    ___\n** |Invoice ID: \033[1m{newInvoice}\033[0m\n** |Total Payment: \033[1mRM{totalPrice}\033[0m')
                print('\n^^ Do you wish to place the following orders?\n1. Yes\n2. No\n')
                pay = ad.multiOptCheck(False,False,'','Confirm purchase: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                if pay == '0':
                    ad.cls_terminal()
                    for purchases in inCart:
                        appdOrder = [newInvoice,username,purchases[0],purchases[3],purchases[4],purchases[5],transactTime,'Pending','-']
                        ad.appdCsv(pathOrder,appdOrder)
                    print('.\n.\n.\nOrder has been placed successfully, thank you for your support!')
                    print('\n1- You will receive a notification when the order and its receipt is ready to pick up.')
                    print('2- Friendly reminder, you may check all produced invoices and receipts at: main menu > Placed Orders >...')
                    print('3- Rating will be available after receipt is generated at: ... > Placed Orders > Receipt')
                    input('\n\nHit ENTER to return to main menu...')
                    return '#Ordered'
                elif pay == '1':
                    input('Order cancelled! Hit ENTER to return to menu...')
                    return

            while True:
                ad.cls_terminal()
                pathListProduct = 'List_Product'
                productHead, productLists = ad.retrive_csv(pathListProduct)
                proShowHead, proShowLists =  ad.filterLists(productHead,productLists,['Product','Price','Discounts(%)','FinalPrice'])
                inCart = [proShowLists[i]+[str(x),f'{float(proShowLists[i][3])*x:.2f}']
                        for i, x in enumerate(list(userCart.values())) if x > 0] #Conclude the cart with total price.
                cartHead = proShowHead
                cartHead = ad.resequenceHeaderPair(cartHead)
                cartHead['Quantity'] = len(cartHead)
                cartHead['TotalPrice(RM)'] = len(cartHead)
                print('--- Shopping Cart List ---')
                ad.list_Sorting(cartHead,inCart)
                if len(inCart) == 0:
                    print('\n^^You have not added anything into the cart yet! ^^')
                    print('\n\nYou may: Back to\033[1m main menu\033[0m > select & view first option (\033[1mProduct Menu\033[0m) > \033[1mbrowse & add\033[0m your desired pastries!')
                    input('\nHit ENTER to return to menu...')
                    return
                print('\n^^ Products in your shopping cart ^^\n')
                print('1. Modify Cart Lists\n2. Place Order\n3. Back to menu...')
                choosen = ad.multiOptCheck(False,False,'','Choose an action: ','Please insert an available option!: ',
                                        {'Modify Cart Items':0,'Modify Cart':0,'Modify':0,'Cart Items':0,'Cart':0,
                                        'Carts':0,'Mod':0,'Mods':0,'Items':0,
                                        'Item':0,'Carts':0,'Modify items':0,'Modify Item':0,'Modify Cart Item':0,
                                        'Place Order':1,'Place':1,'Places':1,'Order':1,'Orders':1,
                                        'Back to menu...':2,'menu...':2,'to menu...':2,'Back':2,'to menu':2,'Back to':2,
                                        'Back to menu':2,'menu':2,'Back menu':2})
                ad.cls_terminal()
                innerAct = None
                if choosen == '0':
                    modCart()
                if choosen == '1':
                    innerAct = payCart()
                elif choosen == '2':
                    return
                if innerAct == '#Ordered':
                    return '#Ordered'

        def orderInspection():

            def invoiceView():
                ad.cls_terminal()
                invoiceID = displayOrders[inquiryInt][0]
                inSumPrice = displayOrders[inquiryInt][3]
                selOrderList = ad.filterByValue(orderLists,orderHeads,0,invoiceID,False,True)
                voiceHead1, voiceLists1 = ad.filterLists(orderHeads,selOrderList,['OrderItem','FinalPrice','Quantity','TotalPrice','Status'])
                voiceHead1 = ad.resequenceHeaderPair(voiceHead1)
                voiceHead2, voiceLists2 = ad.filterLists(orderHeads,selOrderList,['OrderID','Username','TransactionDate'])
                voiceHead2 = ad.resequenceHeaderPair(voiceHead2)
                voiceHead2['Order Status'] = len(voiceHead2)
                voiceHead2['Total Payment'] = len(voiceHead2)
                voiceLists2 = voiceLists2[0] + [status,inSumPrice]
                print('--- Invoice Inspection ---')
                ad.list_Sorting(voiceHead1,voiceLists1)
                ad.list_Sorting(voiceHead2,voiceLists2)
                input('\n\n^^ Above are your enquried order invoice! ^^\nHit ENTER to return to order history lists...')
                return

            def receiptView():
                ad.cls_terminal()
                receiptID = displayOrders[inquiryInt][0]
                reSumPrice = displayOrders[inquiryInt][3]
                selOrderList = ad.filterByValue(orderLists,orderHeads,0,receiptID,False,True)
                receiptHead1, receiptLists1 = ad.filterLists(orderHeads,selOrderList,['OrderItem','FinalPrice','Quantity','TotalPrice','Rating'])
                receiptHead1 = ad.resequenceHeaderPair(receiptHead1)
                receiptHead2, receiptLists2 = ad.filterLists(orderHeads,selOrderList,['OrderID','Username','TransactionDate'])
                receiptHead2 = ad.resequenceHeaderPair(receiptHead2)
                receiptHead2['Total Payment'] = len(receiptHead2)
                receiptHead2['Average Rating'] = len(receiptHead2)
                satisfaction = ad.customAvg([i[4] for i in receiptLists1],1)
                receiptLists2 = receiptLists2[0] + [reSumPrice,satisfaction]
                print('--- Receipt Inspection ---')
                ad.list_Sorting(receiptHead1,receiptLists1)
                ad.list_Sorting(receiptHead2,receiptLists2)
                print('\n\n^^ Above are your enquried order receipt! ^^')
                print('You are welcomed to rate your experience with each product, this could significantly assist us in improving!')
                input('\nHit ENTER to return to order history lists...')
                return

            def manageRating():
                while True:
                    ad.cls_terminal()
                    orderHeadRate, orderListsRate = ad.retrive_csv(orderPath)
                    selRatingList = ad.filterByValue(orderListsRate,orderHeadRate,0,ratingID,False,True)
                    ratingHead1, ratingLists1 = ad.filterLists(orderHeadRate,selRatingList,['OrderItem','Rating'])
                    ratingHead1 = ad.resequenceHeaderPair(ratingHead1)
                    print('--- Manage Rating ---')
                    ad.list_Sorting(ratingHead1,ratingLists1)
                    cancelling = len(ratingLists1)
                    print(f'\n{cancelling+1}. Cancel...')
                    selOpts = {v[0]:k for k,v in enumerate(displayOrders)}
                    selOpts['cancel'] = cancelling
                    selOpts['Cancel'] = cancelling
                    print('\nSelect a product from the order list to submit or edit your feedback (Feedback can only be edited within 21 days after purchase).\n')
                    rateInt = ad.multiOptCheck(False,False,'','Choose a product: ',
                                                        'Please select a product from the list!: ',selOpts)
                    rateInt = int(rateInt)
                    if rateInt == cancelling:
                        return
                    ad.cls_terminal()
                    selRateRow = ratingLists1[rateInt] #['Product','Rating']
                    selRowList = ad.filterByValue(selRatingList,orderHeadRate,'OrderItem',selRateRow[0],False,True)
                    oriRowIndex = ad.returnRowIndexbyList(selRowList,orderListsRate)
                    rateModLoc = {'Column':8,'Row':oriRowIndex}
                    if selRateRow[1] == '-': #Submit rating.
                        print('-- Submit Rating --')
                        ad.list_Sorting(ratingHead1,selRateRow)
                        print('')
                        newRate = ad.num_check_multi(1,'Insert a rating value between 0 - 5. (#cancel to cancel): ',
                                    'Please insert a valid rating value between 0 - 5! (#cancel to cancel): ','#cancel','',0,5,'int')
                        if newRate == None: #Cancelled while prompting.
                            input('\nModification cancelled, discount remained the same. Hit ENTER to continue...')
                            continue
                        ad.cls_terminal()
                        print('-- Submit Rating --')
                        ad.list_Sorting(ratingHead1,selRateRow)
                        newRate = str(newRate[0])
                        print(f'\nAre you sure to submit a rating of {newRate} for product {selRateRow[0]}?\n1. Yes\n2. No\n')
                        submit = ad.multiOptCheck(False,False,'','Confirm your choice: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                        if submit == '0': #Successfully submitted.
                            ad.modCsv(orderPath,rateModLoc,newRate)
                            input('\nReview have been successfully submitted! Hit ENTER to view back order items...')
                        elif submit == '1': #Cancelled while submitting.
                            input('\nRating submission has been cancelled. Hit ENTER to view back order items...')

                    elif selRateRow [1] != '-': #Edit or remove.
                        print('--- Edit Submitted Rating ---')
                        ad.list_Sorting(ratingHead1,selRateRow)
                        print('\nYou may edit it anytime before 21 days after purchase, double confirm before you redsubmit.')
                        print('\n1. Adjust\n2. Remove\n3. Cancel...')
                        rateInt = ad.multiOptCheck(False,False,'','Choose your action: ','Please select a valid option!: ',
                                            {'Adjust':0,'Adjusts':0,'Change':0,'Mod':0,'Modify':0,'Edit':0,
                                                'Remove':1,'Delete':1,'Del':1,'Cancel...':2,'Cancel':2})
                        ad.cls_terminal()
                        if rateInt == '0': #Changing rating.
                            print('-- Changing Rating Value --')
                            ad.list_Sorting(ratingHead1,selRateRow)
                            print('')
                            editRate = ad.num_check_multi(1,'Reinsert your new rating value between 0 - 5. (#cancel to cancel): ',
                                        'Please insert a valid rate value between 0 - 5! (#cancel to cancel): ','#cancel','',0,5,'int')
                            if editRate == None: #Cancelled while prompting.
                                input('\nModification cancelled, discount remained the same. Hit ENTER to continue...')
                                continue
                            ad.cls_terminal()
                            print('-- Changing Rating Value --')
                            ad.list_Sorting(ratingHead1,selRateRow)
                            editRate = str(editRate[0])
                            print(f'\nAre you sure to edit the a rating of product {selRateRow[0]} as: {selRateRow[1]} -> {editRate}?')
                            print('\n1. Yes\n2. No\n')
                            submit = ad.multiOptCheck(False,False,'','Confirm your changes: ','Please choose yes or no!: ',
                                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                            if submit == '0': #Successfully submitted.
                                ad.modCsv(orderPath,rateModLoc,editRate)
                                input('\nReview have been successfully submitted! Hit ENTER to view back order items...')
                            elif submit == '1': #Cancelled while submitting.
                                input('\nRating submission has been cancelled. Hit ENTER to view back order items...')

                        elif rateInt == '1': #Deleting.
                            print('--- Edit Submitted Rating ---')
                            ad.list_Sorting(ratingHead1,selRateRow)
                            print('\nAre you sure to remove this rating?\n1. Yes\n2. No\n')
                            delete = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                            if delete == '0':
                                ad.cls_terminal()
                                ad.modCsv(orderPath,rateModLoc,'-')
                                input('\n.\n.\nRating has been successfully removed! Hit ENTER to view back order items...')
                            elif delete == '1':
                                input('\n\nNothing has been removed. Hit ENTER to view back order items...')
                                continue

                        elif rateInt == '2': #Cancelled any modification.
                            input('\nReview has remained the same. Hit ENTER to return to order lists...')
                    continue

            while True:
                ad.cls_terminal()
                orderPath = 'List_Order'
                orderHeads, orderLists = ad.retrive_csv(orderPath)
                userOrderLists = ad.filterByValue(orderLists,orderHeads,1,username,True,True) #All orders by user.
                viewSelectHead, viewSelectLists = ad.filterLists(orderHeads,userOrderLists,['OrderID','OrderItem','Quantity','TotalPrice','TransactionDate','Status'])
                allOrders = ad.filterLists(viewSelectHead,viewSelectLists,['OrderID'])[1] #Only order column.
                setOrders = [list(i) for i in allOrders]
                setUserOrder = []
                added = set()
                for order in setOrders: #Remove duplicate orders.
                    orderTuple = tuple(order)
                    if orderTuple not in added:
                        added.add(orderTuple)
                        setUserOrder.append(order)
                displayOrders = [] #Sum of products, quantities & price concluded for each order IDs.
                for items in setUserOrder:
                    temp = ad.filterByValue(viewSelectLists,viewSelectHead,'OrderID',items[0],False,True)
                    sumItems = len(set([i[1] for i in temp]))
                    sumQuantity = ad.customSum([i[2] for i in temp])
                    sumPrice = ad.customSum([i[3] for i in temp],2)
                    status = 'Ongoing' if any([i[5] for i in temp if i[5] == 'Pending']) else 'Complete'
                    appdList = [items[0],str(sumItems),str(sumQuantity),str(sumPrice),temp[0][4],status]
                    displayOrders.append(appdList)
                print('\n--- View Orders History---')
                ad.list_Sorting(viewSelectHead,displayOrders)
                cancel = len(displayOrders)
                print(f'\n{cancel+1}. Cancel...')
                opts = {v[0]:k for k,v in enumerate(displayOrders)}
                opts['cancel'] = cancel
                opts['Cancel'] = cancel
                print('\nYou can view all produced invoice & receipt for further inspection, but receipts & ratings are only available after status is complete.\n')
                inquiryInt = ad.multiOptCheck(False,False,'','Select an order ID to enquiry: ',
                                                    'Please choose a product from the list!: ',opts)
                inquiryInt = int(inquiryInt)
                if inquiryInt == cancel:
                    return
                ad.cls_terminal()
                print('---Inquiry Order: ---')
                ad.list_Sorting(viewSelectHead,displayOrders[inquiryInt])
                if displayOrders[inquiryInt][5] == 'Complete':
                    print('\n\nYou may choose a dynamic digital copy to inspect for this order. vv')
                    print('1. Invoice\n2. Receipt\n3. Rating\n4. Cancel...\n')
                    view = ad.multiOptCheck(False,False,'','Choose an copy: ','Please insert a valid option!: ',
                                                {'Invoice':0,'Invoices':0,'In':0,'Voice':0,'Voices':0,
                                                'Receipt':1,'Receipts':1,
                                                'Rating':2,'Ratings':2,'Rate':2,'Rates':2,'Feedback':2,'Feedbacks':2,
                                                'Cancel...':3,'Cancel':3})
                    ad.cls_terminal()
                    if view == '0':
                        invoiceView()
                    elif view == '1':
                        receiptView()
                    elif view == '2':                        
                        ratingID = displayOrders[inquiryInt][0] #Selected OrderID
                        dtFormat = '%Y-%m-%d %H:%M'
                        timeNow = dt.datetime.strftime(dt.datetime.now() - dt.timedelta(21),dtFormat)
                        purchaseDate =ad.filterByValue(userOrderLists,orderHeads,0,ratingID,False,True)[0][6]
                        if ad.numTrackFilter(dt.datetime,dtFormat,timeNow,purchaseDate,'b',False,orderHeads,6,orderLists,False):
                            manageRating()                          
                        else:
                            input('\nYou have passed the available time range for submitting or editing ratings (within 3 weeks). Hit ENTER to try other options...\n')
                            continue
                    elif view == '3':
                        continue


                elif displayOrders[inquiryInt][5] == 'Ongoing':
                    print('\n*Due to the ongoing status, the receipt is not ready to be viewed yet...\n')
                    print('You may view the invoice if you wish.\n1. Yes\n2. No\n')
                    view = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                    if view == '0':
                        invoiceView()
                    elif view == '1':
                        continue
                    continue

        def CM_accountSettings(): #Customer Account settings

            def editPassword():
                print('---Edit Password---\n')
                newPass = passwordChecker(username,'Enter your old password: ',
                            'Password does not match, please try again!: ','#cancel',True)
                if newPass == None:
                    input('Password has not been changed. Hit ENTER to return...')
                else:
                    input('\nPassword has been successfully changed! Hit ENTER to continue...')
                return
            
            def editDOB():
                print("\nInsert your birthday with the following format --> yyyymmdd\nInsert '#cancel' to skip step.\n")
                newDOB = ad.dobFormatVerify('#cancel','Insert your birthday! (e.g. 20050723): ',
                            'Please insert valid integers! (e.g. 20050723): ',
                            'Birthday should consist of 8 numbers! (e.g. 20050723): ',
                            'Age should be between 12 - 120! (e.g. 20050723): ',
                            'Month is out of range, please try again! (e.g. 20050723): ',
                            'Date is out of range, please try again (e.g. 20050723): ', 12, 120)
                if newDOB == None:
                    input('\nEdit of date of birth cancelled! Hit ENTER to continue...')
                    return
                else:
                    ad.modCsv(path_AccList,{'Column':header['DOB'],'Row':accRowIndex},str(newDOB))
                    input('\nDate of birth has been updated successfully updated! Hit ENTER to continue...')
                return

            def editGender():
                oriGender = acc_List[accRowIndex][header['Gender']]
                senOut = 'Select an biological identity: '
                while True:
                    if oriGender == '-':
                        oriGender = 'Hidden'
                    print('---Reidentify Gender---')
                    print(f'Original identity: {oriGender}')
                    print('\nWhat would you like to identify as now?:')
                    print('1. Male\n2. Female\n3. Prefer not to say\n4. Cancel...')
                    choice = ad.multiOptCheck(False,False,'',senOut,'Please insert a valid option: ',
                                            {'Male':0, 'Female':1,'Prefer not to say':2,'Prefer Not':2,'Cancel...':3,'Cancel':3})
                    if choice  == '0':
                        newGender = 'Male'
                    elif choice =='1':
                        newGender = 'Female'
                    elif choice =='2':
                        newGender = '-'
                    elif choice == '3':
                        return
                    if newGender == oriGender and (newGender != '-'):
                        ad.cls_terminal()
                        senOut = f'You have already identified yourselve as a {oriGender}!: '
                        continue
                    break
                ad.cls_terminal()
                print('---Confirm reidentify?---\n')
                if newGender == '-':
                    reconsider = ad.multiOptCheck(False,True,'','Are you sure to remain your prideful identity hidden?: '
                                                , 'Please insert a valid option!: ', {'Yes':0,'No':1})
                else:
                    reconsider = ad.multiOptCheck(False,True,'',f'Are you sure to identify your self as a {newGender}?: '
                                                , 'Please insert a valid option!: ', {'Yes':0,'No':1})
                if reconsider == '0':
                    ad.modCsv(path_AccList,{'Column':header['Gender'],'Row':accRowIndex},newGender)
                    if newGender == '-':
                        input('Your identity has remained anonnymous, hit ENTER to return...')
                    else:
                        input('You have sucessfully discovered your new identity! Hit ENTER to continue...')
                elif reconsider == '1':
                    input('Your identity has remained the same, hit ENTER to return...')
                return

            def selfDeletation():
                ad.cls_terminal()
                print('---Account deletion---\n')
                print(f'Dear {username}...\nDo you really wish to delete your account?: ')
                options = {'Yes':0,'No':1}
                delAcc = ad.multiOptCheck(False,True,'', 'Insert your decision: ',
                                'Please insert a valid option!: ', options)
                if delAcc == '0':
                    ad.cls_terminal()
                    print('---Account deletion---\n')
                    print(f'Dear {username}...\nAre you really sure to delete your account...?: \n')
                    delAcc2 = ad.multiOptCheck(False,True,'','Reconsider your decision: ','Please insert yes or no!: ',options)
                    if delAcc2 == '0':
                        delAcc2 = True
                    else:
                        delAcc2 = False
                else:
                    delAcc2 = False
                if delAcc2 == True:
                    ad.cls_terminal()
                    print('.\n.\n.\nDeletion processing...\n')
                    acchead, accLists = ad.retrive_csv(path_AccList)
                    ad.delRowCsv(path_AccList, ad.filterByValue(accLists,acchead,'Username',username,True,True)[0])
                    input(f'User account has been deleted, farewell dear {username}! Hit ENTER to return to sign in page...')
                    return '#Exit'
                elif not delAcc2:
                    input('\n\nAccount has not been deleted. Hit ENTER to return...')
                return

            while True:
                ad.cls_terminal()
                header, acc_List = ad.retrive_csv(path_AccList)
                print('---Account Settings----\n')
                print('Edit Details:\n1. Password\n2. Birthday\n3. Gender\n4. Delete account\n5. Exit...')
                choice = ad.multiOptCheck(False,False,'','Insert an info to edit: ','Please insert a valid option!: ',
                                        {'Password':0,'Pass':0,'Passwords':0,
                                        'Birthday':1,'DOB':1,'Birth':1,'Gender':2,
                                        'Delete account':3,'Delete':3,
                                        'Exit...':4,'Exit':4})
                accRowIndex = ad.returnValueIndex(username,header['Username'],acc_List)
                inneract = None
                ad.cls_terminal()
                if choice  == '0':
                    editPassword()
                elif choice == '1':
                    editDOB()
                elif  choice == '2':
                    editGender()
                elif choice == '3':
                    inneract = selfDeletation()
                elif choice == '4':
                    break
                if inneract == '#Exit':
                    return inneract
            return

        while True:
            print('----Customer Menu----\n')
            print('1. Product Menu\n2. Shopping Cart\n3. Placed Orders\n4. Account Settings\n5. Logout')
            choose = ad.multiOptCheck(False,False,'','Choose an option: ','Please insert an available option!: ',
                                    {'Product Menu':0,'Menu':0,'Product':0,
                                    'Shopping Cart':1,'cart':1,'shop':1,'shopping':1,
                                    'order':2,'orders':2,'Placed order':2,'Placed orders':2,'Placed':2,'Place':2,
                                    'Account Settings':3,'Settings':3,'Account':3,'Account Settings':3,'Setting':3,
                                    'Logout':4,'Log out':4,'Out':4})
            ad.cls_terminal()
            semiAct = None
            if choose == '0':
                browseProduct()
            if choose == '1':
                semiAct = viewCart()
            elif choose == '2':
                orderInspection()
            elif choose == '3':
                semiAct = CM_accountSettings()
            elif choose == '4':
                break
            if semiAct == '#Ordered':
                userCart = {k[0]:0 for k in ad.retrive_csv('List_Product')[1]}
            elif semiAct == '#Exit':
                return semiAct
            ad.cls_terminal()
        return


    def CashierMenu(username:str):   
        print(f'====Welcome back dearest cashier, {username}!====\n')

        def productMenu():

            def discountManagement():
                while True:
                    ad.cls_terminal()
                    print(f'--Discount modification: {proDiscSelect[0]}--')
                    ad.list_Sorting(menuInspectHead,proDiscSelect)
                    if proDiscSelect[2] != '-': #If have discount...
                        applied = True
                    elif proDiscSelect[2] == '-': #Elif no discount...
                        applied = False

                    if applied:
                        print(f'\n\n^^ Product {proDiscSelect[0]} is currently on discount: {proDiscSelect[2]}% ^^\n')
                        print('\n1. Modify\n2. Remove\n3.Cancel modification...')
                        choice = ad.multiOptCheck(False,False,'','Select an operation: ','Please select a valid operation!: '
                            ,{'Modify':0,'Mod':0,'Remove':1,'Cancel modification...':2,'Cancel':2})
                        if choice == '2': #Cancelled on options.
                            input('\n\nNothing has been changed. Hit ENTER to return...')
                            return
                        ad.cls_terminal()
                        if choice == '0': #To modify.
                            print(f'--Modifying applied discounts...--\n\n')
                            newDisc = ad.num_check_multi(1,'Insert a discount value between 1 - 99. (#cancel to cancel): ',
                                        'Please insert a valid value between 1 - 99! (#cancel to cancel): ','#cancel','',1,99,'int')
                            if newDisc == None: #Cancelled while prompting.
                                input('\nModification cancelled, discount remained the same. Hit ENTER to continue...')
                                return
                            newDisc = newDisc[0]
                            print('\n1. Yes\n2. No')
                            reConfirm = ad.multiOptCheck(False,False,'','Are you sure to modify the offer: ','Please choose yes or no!: ',
                                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                            if reConfirm == '0': #Successfully modify.
                                finalPrice = f'{(float(proDiscSelect[1]) * (1 - float(newDisc / 100))):.2f}'
                                ad.modCsv(pathListProduct,{'Colomn':menuHead['Discounts(%)'],'Row':proDiscountInt},str(newDisc))
                                ad.modCsv(pathListProduct,{'Colomn':menuHead['FinalPrice'],'Row':proDiscountInt},finalPrice)
                                input(f'\nSuccessfully changed discount for {proDiscSelect[0]} to {newDisc}%! Hit ENTER to return...')
                                return
                            elif reConfirm == '1': #Cancelled while confirming.
                                input('\nNothing has been removed. Hit ENTER to continue...')
                                return
                            
                        elif choice == '1': #To remove
                            print(f'--Removing applied discounts...--\n\n')
                            print(f'Are you sure to remove {proDiscSelect[2]}% discount for product {proDiscSelect[0]}?\n1. Yes\n2. No')
                            confirm = ad.multiOptCheck(False,False,'','Confirm your action: ','Please choose yes or no!: ',
                                                        {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                            if confirm == '0': #Successfully removed.
                                finalPrice = proDiscSelect[1]
                                ad.modCsv(pathListProduct,{'Colomn':menuHead['Discounts(%)'],'Row':proDiscountInt},'-')
                                ad.modCsv(pathListProduct,{'Colomn':menuHead['FinalPrice'],'Row':proDiscountInt},finalPrice)
                                input('\nSuccessfully cleared off discounts! Hit ENTER to continue...')
                                return
                            elif confirm == '1': #Cancelled while confirming.
                                input('\nNothing has been removed. Hit ENTER to continue...')
                                return
                            

                    elif not applied:
                        print(f'\n\n^^ Product {proDiscSelect[0]} has no discount applied currently ^^\n')
                        newDisc = ad.num_check_multi(1,'To add discount, insert a value between 1 - 99. (#cancel to cancel): ',
                                    'Please insert a valid value between 1 - 99! (#cancel to cancel): ','#cancel','',1,99,'int')
                        if newDisc == None: #Cancelled while prompting.
                            input('\nModification cancelled, product remains its original price. Hit ENTER to continue...')
                            return
                        newDisc = newDisc[0]
                        print(f'\n\nConfirm applying {newDisc}% off to product {proDiscSelect[0]}? (Be sure you are permitted to):\n1. Yes\n2. No')
                        reConfirm = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                        if reConfirm == '0': #Successfully modify.
                            finalPrice = f'{(float(proDiscSelect[1]) * (1 - float(newDisc / 100))):.2f}'
                            ad.modCsv(pathListProduct,{'Colomn':menuHead['Discounts(%)'],'Row':proDiscountInt},str(newDisc))
                            ad.modCsv(pathListProduct,{'Colomn':menuHead['FinalPrice'],'Row':proDiscountInt},finalPrice)
                            input(f'\nSuccessfully added discount for {proDiscSelect[0]} with {newDisc}%! Hit ENTER to return...')
                            return
                        elif reConfirm == '1': #Cancelled while confirming.
                            return

            while True:
                ad.cls_terminal()
                pathListProduct = 'List_Product'
                menuHead, menuLists = ad.retrive_csv(pathListProduct)
                menuInspectHead, menuInspectLists = ad.filterLists(menuHead,menuLists,['Product','Price','Discounts(%)','FinalPrice'])
                print('---Inspecting Product Menu---')
                ad.list_Sorting(menuInspectHead,menuInspectLists)
                options = {v: k[0] for v, k in enumerate(menuInspectLists)}
                cancel = len(menuInspectLists)
                options[cancel] = 'Cancel'
                print(f'\n{cancel + 1}. Cancel status modification...\n')
                print('^^ You may apply discounts to products on the menu above after receiving permissions or request by manager ^^')
                proDiscount = ad.multiOptCheck(False,False,'','Select a product for discount modification: ',
                                            'Please select a valid option from the menu!: ',options)
                proDiscountInt = int(proDiscount)
                if proDiscountInt == cancel:
                    input('\nNothing has been modified. Hit ENTER to continue...')
                    return
                proDiscSelect = menuInspectLists[proDiscountInt]
                discountManagement()
                continue

        def receiptGeneration():
            pathListOrder = 'List_Order'
            receiptHead, receiptList = ad.retrive_csv(pathListOrder)
            orderHeadUser, orderListUser = ad.filterLists(receiptHead,receiptList,
                                                ['OrderID','Username','TransactionDate','Status'])
            orderHeadUser2 = ad.resequenceHeaderPair(orderHeadUser)
            setList2 = [list(i) for i in orderListUser]
            setUserOrder = []
            added = set()
            for order in setList2: #Remove duplicate orders.
                orderTuple = tuple(order)
                if orderTuple not in added:
                    added.add(orderTuple)
                    setUserOrder.append(order)
            setUserOrder = [i for i in setUserOrder if len(set([x[3] for x in orderListUser if x[0] == i[0]])) == 1 and i[3] == 'Done']
            orderHeadUser3, setUserOrder2 = ad.filterLists(orderHeadUser2,setUserOrder,['OrderID','Username','TransactionDate'])
            
            ad.cls_terminal()
            print('---Order Receipts Retrieval---')
            ad.list_Sorting(orderHeadUser3,setUserOrder2)
            senOut = 'Select a filter option from above to retrieve an order: '
            while True:
                print('\n1. Search by OrderID\n2. Filter by Username\n3. Filter by TransactionDate\n4. Return...\n')
                choice = ad.multiOptCheck(False,False,'',senOut,'Please select a valid option!: ',
                                        {'Search by OrderID':0,'OrderID':0,'by OrderID':0,'Order':0,'ID':0,
                                        'Filter by Username':1,'Username':1,'User':1,'name':1,
                                        'Filter by TransactionDate':2,'TransactionDate':2,'by TransactionDate':2,
                                        'Date':2,'by date':2,'dates':2,
                                        'Return to menu...':3,'Return to menu':3,'Return':3,'to menu':3,'menu':3})
                if choice == '0':
                    senOut = 'Enter an order ID to search by (#cancel to cancel): '
                    while True:
                        focusHead = 'OrderID'
                        keyword = input(senOut)
                        if keyword.lower() == '#cancel':
                            input('\nReceipt generating cancelled. Press Enter to return to menu...')
                            return
                        filtering = ad.filterByValue(setUserOrder2,orderHeadUser3,focusHead,keyword,False,False)
                        if filtering == [] or filtering == None:
                            senOut = f'Order ID {keyword} not found! Please try again (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        break
                elif choice == '1':
                    senOut = 'Enter an username to filter by (#cancel to cancel): '
                    while True:
                        focusHead = 'Username'
                        keyword = input(senOut)
                        if keyword.lower() == '#cancel':
                            input('\nReceipt generating cancelled. Press Enter to return to menu...')
                            return
                        filtering = ad.filterByValue(setUserOrder2,orderHeadUser3,focusHead,keyword,False,True)
                        if filtering == [] or filtering == None:
                            senOut = f'Username {keyword} not found! Try entering a differnt word (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        break

                elif choice == '2':
                    focusHead = 'TransactionDate'
                    senOut = "Enter a date to filter by. (format: YYYY-MM-DD, e.g. 2024-01-21, #cancel to cancel): "
                    while True:
                        keyword = input(senOut)
                        if keyword.lower() == '#cancel':
                            input('Receipt generating cancelled. Press Enter to return to menu...')
                            return
                        if not keyword.replace('-','0').isdigit():
                            senOut = 'Year-Month should consist of numbers! Try again with format: YYYY-MM-DD, e.g. 2024-01-21 (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        if not len(keyword) == 10:
                            senOut = 'Incorrect date format! Please insert with the following format: YYYY-MM-DD, e.g. 2024-01-21 (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        filtering = ad.numTrackFilter(dt.datetime,'YYYY-MM-DD',keyword,'','c',
                                                    True,orderHeadUser3,'TransactionDate',setUserOrder2,True)
                        if filtering == None:
                            senOut = 'Invalid inputs! Please insert with the following format: YYYY-MM-DD, e.g. 2024-01-21 (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        if filtering == []:
                            senOut = f'Transaction date {keyword} not found! Try again (format: YYYY-MM-DD, e.g. 2024-01-21, #cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        break
                elif choice == '3':
                    return

                ad.cls_terminal()
                print('--Configure Generating Receipt--')
                ad.list_Sorting(orderHeadUser3,filtering)
                if len(filtering) != 1:
                    idOptions = {v: k[0] for v, k in enumerate(filtering)}
                    cancel = len(filtering)
                    idOptions[cancel] = 'cancel'
                    print(f'\n{str(cancel + 1)}. Cancel...')
                    print(f'\n^^ Filtered by {focusHead} with keyword: \033[1m{keyword}\033[0m ^^')
                    selection = ad.multiOptCheck(False,False,'#cancel','Select an order ID to generate receipt (#cancel to cancel): ',
                                        'Please insert a valid option of order ID from the list! (#cancel to cancel):  ',idOptions)
                    if selection == None:
                        input('Nothing has been generated. Hit ENTER to return to menu...')
                        return
                    selection = selection[0]
                    receiptRow = filtering[int(selection)]
                    ad.cls_terminal()
                    filtering = ad.filterByValue(setUserOrder2,orderHeadUser3,'OrderID',receiptRow[0],False,True)
                    ad.list_Sorting(orderHeadUser3,filtering)
                else:
                    receiptRow = filtering[0]
                print(f'\n^^ Filtered by {focusHead} with keyword: \033[1m{keyword}\033[0m ^^')
                print('\n\nConfirm generating receipt for this order?\n1. Yes\n2. No')
                reconfirm = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                            {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                if reconfirm == '0':
                    ad.cls_terminal()
                    print('--Configure Generating Receipt--')
                    orderID = receiptRow[0]
                    genOrderList = [i for i in receiptList if i[0] == orderID]
                    p1ReceiptHead, p1ReceiptLists = ad.filterLists(receiptHead,genOrderList,
                                                ['OrderItem','FinalPrice','Quantity','TotalPrice','Rating'])
                    p1ReceiptHead = ad.resequenceHeaderPair(p1ReceiptHead)
                    p2ReceiptHead, p2ReceiptList = ad.filterLists(receiptHead,genOrderList,
                                                ['OrderID','Username','TransactionDate'])
                    p2ReceiptHead = ad.resequenceHeaderPair(p2ReceiptHead)
                    p2ReceiptList = p2ReceiptList[0]
                    sumPrice = ad.customSum([float(i[3]) for i in p1ReceiptLists],2)
                    avgRating = ad.customAvg([float(i[4]) for i in p1ReceiptLists if i[4] != '-'],1)
                    p2ReceiptHead['TotalOrderPrice'] = len(p2ReceiptHead)
                    p2ReceiptHead['AverageRating'] = len(p1ReceiptHead)
                    p2ReceiptList.append(sumPrice)
                    p2ReceiptList.append(avgRating)
                    ad.list_Sorting(p1ReceiptHead,p1ReceiptLists)
                    ad.list_Sorting(p2ReceiptHead,p2ReceiptList)
                    input(f'\nReceipt for order {orderID} is ready! Hit ENTER to print copy...')
                    print('\n.\n.\n.\nReceipt has been successfully printed! Please check it on the printing device.')
                    input('\nHit ENTER to return to menu...')
                    return
                elif reconfirm == '1':
                    input('\nReceipt has not been generated. Hit ENTER to return to menu...')
                    break

        def performanceReport():
            while True:
                ad.cls_terminal()
                pathFinance = 'Report_Finance'
                financeHead, financeLists = ad.retrive_csv(pathFinance)
                pathOrderLists = 'List_Order'
                transactionHead, transactionLists = ad.retrive_csv(pathOrderLists)
                pathReportProduct = 'Report_Product'
                proReportHead = ad.retrive_csv(pathReportProduct)[0]
                pathListProduct = 'List_Product'
                menuHead, menuLists = ad.retrive_csv(pathListProduct)
                menuLists = ad.filterLists(menuHead,menuLists,['Product'])[1]
                print('---Performance Report Generate---\n\n')
                print('vv Generate reports by specifying a year-month, insert with format: YYYY-MM (e.g. 2024-08, 2023-12) vv\n')
                senOut = 'Insert desired year-month for report generating (#cancel to cancel): '
                while True:
                    dateGenerate = input(senOut)
                    if dateGenerate.lower() == '#cancel':
                        return
                    if not dateGenerate.replace('-','0').isdigit():
                        senOut = 'Year-Month should consist of integer! Please refer to example above and try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    if not len(dateGenerate) == 7:
                        senOut = 'Date format should be YYYY-MM! Please try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    if ad.numTrackFilter(dt.datetime,'YYYY-MM',dateGenerate,dt.datetime.strftime(dt.datetime.now(),'%Y-%m'),
                                        'a',True,financeHead,'Month',financeLists,False):
                        senOut = 'Monthly report should only generate after the month ends! Please try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    productFiltered = ad.numTrackFilter(dt.datetime,'YYYY-MM',dateGenerate,'','c',True,
                                                    financeHead,'Month',financeLists,True)
                    if productFiltered == None: 
                        senOut = 'Invalid inputs! Please refer to example above and try again (#cancel to cancel): '
                        ad.clrLine_terminal()
                        continue
                    finRowExist = False
                    if len(productFiltered) != 0: #If enquiry date existed in report.
                        if productFiltered[0][1] != '-':
                            monthIncomeHead, monthIncomeLists = ad.filterLists(financeHead,productFiltered,['Month','Income'])
                            ad.list_Sorting(monthIncomeHead,monthIncomeLists)
                            input('\nIncome report have already been generated for this month! Hit ENTER to try again...')
                            break
                        else:
                            finRowExist = True
                    if len(productFiltered) == 0 or finRowExist:
                        dateFormat = ad.dtFormatConverter('YYYY-MM')
                        inquiryTransactHead, inquiryTransactLists = ad.filterLists(transactionHead,transactionLists,
                                            ['OrderItem','Quantity','TotalPrice','TransactionDate','Rating'])
                        inquiryTransactLists = ad.numTrackFilter(dt.datetime,dateFormat,dateGenerate,'','c',True,
                                                                inquiryTransactHead,'TransactionDate',inquiryTransactLists,True)
                        if inquiryTransactLists == []:
                            senOut = 'No order existed on this month! Please try again (#cancel to cancel): '
                            ad.clrLine_terminal()
                            continue
                        #Columns in List_Order.csv
                        ad.cls_terminal()
                        productNameColumn = ad.returnHeaderIndex('OrderItem',inquiryTransactHead)
                        totalPriceColumn = ad.returnHeaderIndex('TotalPrice',inquiryTransactHead)
                        quantityColumn = ad.returnHeaderIndex('Quantity',inquiryTransactHead)
                        ratingColumn = ad.returnHeaderIndex('Rating',inquiryTransactHead)
                        productSets = set(i[productNameColumn] for i in inquiryTransactLists)
                        productRecords = []
                        for i in productSets:
                            productRecords.append(i)
                        reportProducts = []
                        dateGenerate = f'{dateGenerate}-01'
                        for product in productRecords:
                            sumQuantity = ad.customSum([i[quantityColumn]
                                        for i in inquiryTransactLists if i[productNameColumn] == product])
                            sumPrice = ad.customSum([i[totalPriceColumn]
                                        for i in inquiryTransactLists if i[productNameColumn] == product])
                            avgRating = ad.customAvg([i[ratingColumn]
                                        for i in inquiryTransactLists if i[productNameColumn] == product],1)
                            recordRow = [dateGenerate,str(product),str(sumQuantity),str(sumPrice),str(avgRating)]
                            reportProducts.append(recordRow)
                        totalIncome = ad.customSum([float(i[3]) for i in reportProducts])
                        soldProducts = ad.filterLists(proReportHead,reportProducts,['Product'])[1]
                        notSoldProducts = [i[0] for i in menuLists if i[0] not in [x[0] for x in soldProducts]]
                        for products in notSoldProducts:
                            reportProducts.append([dateGenerate,products,'-','-','-'])
                        print(f'\n\n\n--- Product Sales Performance of {dateGenerate[:-3]} ---')
                        ad.list_Sorting(proReportHead,reportProducts)
                        print(f'\n-- Total Income of the month: \033[1m\033[4mRM{totalIncome}\033[0m --')
                        print("\nThis is the report of all products' sales performance and popularity, proceed to submit report?: \n1. Yes\n2. No\n")
                        confirm = ad.multiOptCheck(False,False,'','Select your decision: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Y':0,'Ye':0,'Ya':0,'No':1,'N':1,'Nope':1,'Nah':1})
                        if confirm == '1':
                            input('Report generate has been cancelled. Hit ENTER to return to menu...')
                            return
                        ad.cls_terminal()
                        if finRowExist:
                            dateFinRow = ad.returnRowIndexbyList(productFiltered,financeLists)
                            ad.modCsv(pathFinance,{'Column':1,'Row':dateFinRow},totalIncome)
                        else:
                            ad.appdCsv(pathFinance,[dateGenerate,totalIncome,'-','-'])
                        ad.appdCsv(pathReportProduct,reportProducts)
                        print(f'\n.\n.\n.\nMonthly sales performance report for {dateGenerate[:-3]} has been succesfully generated and submitted!')
                        input('Hit ENTER to return to menu...')
                        break


        while True:
            print('----Cashier Menu----\n')
            print('1. Product Menu\n2. Receipt Generation\n3. Sales Report')
            print('4. Account Settings\n5. Logout')
            choose = ad.multiOptCheck(False,False,'','Choose an option: ','Please insert an available option!: ',
                                    {'Product Menu':0,'Menu':0,'Product':0,
                                    'Receipt Generation':1,'Receipt':1,
                                    'Sales Report':2,'Report':2,'Sale':2,'Sale Report':2,'Sales':2,'Reports':2,
                                    'Account Settings':3,'Account':3,'Settings':3,'Setting':3,
                                    'Logout':4,'Log out':4,'Out':4})
            ad.cls_terminal()
            if choose == '0':
                productMenu()
            if choose == '1':
                receiptGeneration()
            elif choose == '2':
                performanceReport()
            elif choose == '3':
                employeeSettings(username)
            elif choose == '4' :
                break
            ad.cls_terminal()
        return


    def BakerMenu(username:str):
        print(f'====Welcome back dearest baker, {username}!====\n')

        def RecipeManage(): #To request creation, modification, and deletion of recipes.
            def createRecipe():
                path_createrecipe = 'Pending_Recipe'
                ad.cls_terminal()
                print('---Create New Recipe---\n')
                oldHeaders, oldLists = ad.retrive_csv('Pending_Recipe')
                ad.list_Sorting(oldHeaders,oldLists)
                print('\n1. Create a new recipe\n2. Exit')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                            {'Create a Recipe ':0,'Create':0,'Recipe':0,
                            'Back to menu...':1,'Back':1,'Exit':1,'Back to menu':1})
                if chosen == '0':
                    ad.cls_terminal()
                    print('---Creating new recipe---\n')
                    NewProduct= input('Please enter a Product Name: ')
                    NewRecipe = input('Please enter the Recipe using the following format: Step1;Step2;Step3;...: ')
                    if NewRecipe == None or len(NewRecipe) == 0:
                        NewRecipe == '-'
                    PendingRecipe = [NewProduct,NewRecipe,'Add','Pending']
                    ad.cls_terminal()
                    print(f'---Requested new Recipe: {NewProduct}---\n')
                    ad.appdCsv(path_createrecipe,PendingRecipe)
                    input('Recipe will be rewieded by the mananger for approval! Hit ENTER to return...')
                    return
                elif chosen == '1':
                    input('Hit ENTER to return...')
                    return
                return
            
            def updateRecipe():
                path_createrecipe = 'Pending_Recipe'
                ad.cls_terminal()
                print('---Update the Recipe---')
                oldHeaders, oldLists = ad.retrive_csv('Pending_Recipe')
                ad.list_Sorting(oldHeaders,oldLists)
                print('\n1. Update Recipe\n2. Exit')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                            {'Update a Recipe ':0,'Update':0,'Recipe':0,
                            'Back to menu...':1,'Back':1,'Exit':1,'Back to menu':1})
                if chosen == '0':
                    ad.cls_terminal()
                    print('---Updating recipe---\n')
                    upProduct= input('Please enter a Product Name: ')
                    upRecipe = input('Please enter the  New Recipe using the following format: Step1;Step2;Step3;...: ')
                    if upRecipe == None or len(upRecipe) == 0:
                        upRecipe == '-'
                    PendingRecipe = [upProduct,upRecipe,'Update','Pending']
                    ad.cls_terminal()
                    print(f'---Requested to Update Recipe: {upProduct}---\n')
                    ad.appdCsv(path_createrecipe,PendingRecipe)
                    input('Recipe will be rewieded by the mananger for approval! Hit ENTER to return...')
                    return
                elif chosen == '1':
                    input('Hit ENTER to return...')
                    return
                return

            def deleteRecipe():
                path_createrecipe = 'Pending_Recipe'
                ad.cls_terminal()
                print('---Delete a Recipe---')
                oldHeaders, oldLists = ad.retrive_csv('Pending_Recipe')
                ad.list_Sorting(oldHeaders,oldLists)
                print('\n1. Delete a recipe\n2. Exit')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                            {'Delete a Recipe ':0,'Delete':0,'Recipe':0,
                            'Back to menu...':1,'Back':1,'Exit':1,'Back to menu':1})
                if chosen == '0':
                    ad.cls_terminal()
                    print('---Deletting a  recipe---\n')
                    delProduct= input('Please enter a Product Name: ')
                    delRecipe = input('Please enter the Recipe using the following format: Step1;Step2;Step3;...: ')
                    if delRecipe == None or len(delRecipe) == 0:
                        delRecipe == '-'
                    PendingRecipe = [delProduct,delRecipe,'Delete','Pending']
                    ad.cls_terminal()
                    print(f'---Requested for deletion: {delProduct}---\n')
                    ad.appdCsv(path_createrecipe,PendingRecipe)
                    input('Recipe deletion will be rewieded by the mananger for approval! Hit ENTER to return...')
                    return
                elif chosen == '1':
                    input('Hit ENTER to return...')
                    return
                return
            
            print('---Choose an operation---\n')
            print('1. Create Recipe\n2. Update Recipe\n3. Delete Recipe\n4. Exit')
            chosen = ad.multiOptCheck(False,False,'','Choose an option: ','Please insert a valid option: ',
                                {'Create Recipe':0,'Create':0,
                                'Update Recipe':1,'Update':1,
                                'Delete Recipe':2,'Delete':2,
                                'Back to menu...':3,'Back':3,'Menu':3,'Back to menu':3})
            ad.cls_terminal()
            if chosen == '0':
                createRecipe()
            elif chosen == '1':
                updateRecipe()
            elif chosen == '2':
                deleteRecipe()
            elif  chosen == '3':
                return

        def inventoryCheck(): #Check availability of ingredients to determine if a product is available.
            print('---Ingredient Stock Inspection ---')
            inIngHead, inIngList = ad.retrive_csv('Inventory_Ingredient')
            ad.list_Sorting(inIngHead, inIngList)
            senOut = '\nFilter search ingredient name (#exit to exit): '
            while True:
                filterIng = input(senOut)
                if filterIng.lower() == '#exit':
                    break
                if any(i for i in filterIng if i.isdigit()):
                    senOut = 'Ingredient name should consist of alphabets! Please try again (#exit to exit).: '
                    ad.clrLine_terminal()
                    continue
                filteredList = ad.filterByValue(inIngList,inIngHead,'Ingredient',filterIng,False,False)
                if filteredList == None:
                    senOut = 'Ingredient not found! Please try again. {#exit to exit}: '
                    ad.clrLine_terminal()
                    continue
                ad.cls_terminal()
                ad.list_Sorting(inIngHead,filteredList)
                print(f'\n^^ Filtered by {filterIng} ^^')
                print('\nContinue search?\n1. Yes\n2. No')
                decision = ad.multiOptCheck(False,False,'','Choose an option: ','Please choose yes or no!: ',
                                            {'Yes':0,'Yup':0,'Y':0,'N':1,'No':1,'Nope':1})
                if decision == '0':
                    senOut = 'Insert a product name to search (#exit to exit): '
                    continue
                elif decision == '1':
                    break
            input('\nHit ENTER to return...')
            return
        
        def productionRecord(): #Record production quantities, batch, & expiration dates.

            def allBatches():

                def filterBatchID():
                    ad.cls_terminal()
                    print('---Search for Batches---')
                    print("\nFormat of BatchID is determined by key 'BA' and the date => BA(YYMMDD)\ne.g. BA240830\n")
                    senOut = 'Insert a batch ID to search (#exit to exit): '
                    while True:
                        batchSearch = input(senOut)
                        if batchSearch.lower() == '#exit':
                            input('Hit ENTER to return...')
                            break
                        if not (batchSearch.startswith('BA') and batchSearch[-6:].isdigit() and len(batchSearch) == 8):
                            senOut = 'Invalid batch ID format! Please check the example above and try again (#exit to exit): '
                            ad.clrLine_terminal()
                            continue
                        batchFiltered = ad.filterByValue(ipLists,ipHeaders,'BatchID',batchSearch,False,True)
                        if batchFiltered == None:
                            senOut = 'BatchID not found! Try searching another one (#exit to exit): '
                            ad.clrLine_terminal()
                            continue
                        ad.cls_terminal()
                        ad.list_Sorting(ipHeaders,batchFiltered)
                        print('\nContinue search?\n\n1. Yes\n2. No')
                        decision = ad.multiOptCheck(False,False,'','Choose an option: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Yup':0,'Y':0,'N':1,'No':1,'Nope':1})
                        if decision == '0':
                            print("\nFormat of BatchID is determined by key 'BA' and the date => BA(YYMMDD)\ne.g. BA240830\n")
                            senOut = 'Insert a product name to search: '
                            continue
                        elif decision == '1':
                            input('Hit ENTER to return...')
                            break
                    return

                def filterProduct():
                    ad.cls_terminal()
                    print('---Search for Product Name---')
                    senOut = 'Insert a product name to search (#exit to exit): '
                    while True:
                        productSearch = input(senOut)
                        if productSearch.lower() == '#exit':
                            input('Hit ENTER to return...')
                            break
                        if any(i for i in productSearch if i.isdigit()):
                            senOut = 'Invalid product name! Please enter a name without numbers (#exit to exit): '

                            ad.clrLine_terminal()
                            continue
                        productFiltered = ad.filterByValue(ipLists,ipHeaders,'Product',productSearch,False,True)
                        if productFiltered == None:
                            senOut = 'Product was not found, please try again! (#exit to exit): '

                            ad.clrLine_terminal
                            continue
                        ad.cls_terminal()
                        ad.list_Sorting(ipHeaders,productFiltered)
                        print('\nContinue search?\n\n1. Yes\n2. No')
                        decision = ad.multiOptCheck(False,False,'','Choose an option: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Yup':0,'Y':0,'N':1,'No':1,'Nope':1})
                        if decision == '0':
                            senOut = 'Insert a product name to search (#exit to exit): '
                            continue
                        elif decision == '1':
                            input('Hit ENTER to return...')
                            break
                    return

                def filterExpiryDate():
                    ad.cls_terminal()
                    print('---Search Product by Expiration Date---\n')
                    print('Insert a date in the format YYYYMMDD\ne.g. 20240830')
                    senOut = 'Insert a date (#exit to exit): '
                    while True:
                        expireSearch = input(senOut)
                        if not expireSearch.isdigit():
                            senOut = 'Date should consist of integer! Please refer to example above and try again: '
                            ad.clrLine_terminal()
                            continue
                        if not len(expireSearch) == 8:
                            senOut = 'Date format should be YYYY-MM-DD! Please try again: '
                        expireSearch = dt.datetime.strptime(expireSearch, "%Y-%m-%d").date()
                        productFiltered = ad.numTrackFilter(dt.datetime,'%Y-%m-%d',expireSearch,'','b',True,
                                                        ipHeaders,'ExpireDate',ipLists,True)
                        if productFiltered == None:
                            senOut = 'Product was not found, please try again!: '
                            ad.clrLine_terminal
                            continue
                        ad.cls_terminal()
                        ad.list_Sorting(ipHeaders,productFiltered)
                        print('\nContinue search?\n\n1. Yes\n2. No')
                        decision = ad.multiOptCheck(False,False,'','Choose an option: ','Please choose yes or no!: ',
                                                    {'Yes':0,'Yup':0,'Y':0,'N':1,'No':1,'Nope':1})
                        if decision == '0':
                            senOut = 'Insert a product name to search: '
                            continue
                        elif decision == '1':
                            input('Hit ENTER to return...')
                            break
                    return

                ipHeaders, ipLists = ad.retrive_csv('Inventory_Product')
                ad.list_Sorting(ipHeaders, ipLists)
                print('\n1. Filter by BatchID\n2. Filter by Product\n3. Filter by Expiry Date')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                            {'Filter by BatchID':0,'Batch':0,
                            'Filter by Product':1,'Product':1,
                            'Filter by Expiry Date':2,'Expiry Date':2,'Date':2,
                            'Back to menu...':3,'Back':3,'Menu':3})
                
                ad.cls_terminal()
                if chosen == '0':
                    filterBatchID()
                elif chosen == '1':
                    filterProduct()
                elif chosen == '2':
                    filterExpiryDate()
                elif chosen == '3':
                    return

            def createBatches():
                path_inProduct = 'Inventory_Product'
                currentTime = dt.datetime.now()
                ad.cls_terminal()
                print('---Create Production Batches---')
                oldHeaders, oldLists = ad.retrive_csv('Inventory_Product')
                ad.list_Sorting(oldHeaders,oldLists)
                print('\n1. Create a new batch\n2. Exit')
                chosen = ad.multiOptCheck(False,False,'','Choose an operation: ','Please insert a valid option: ',
                            {'Create a new batch ':0,'Create':0,'New Batch':0,
                            'Back to menu...':1,'Back':1,'Exit':1,'Back to menu':1})
                if chosen == '0':
                    NewExpiry = (currentTime + dt.timedelta(days=5)).date()
                    NewExpiry = dt.datetime.strftime(NewExpiry,"%Y-%m-%d")
                    NewBatch = dt.datetime.strftime(currentTime,"%y%m%d")
                    NewBatch = 'BA' + NewBatch
                    batchCart = {k[0]:0 for k in ad.retrive_csv('List_Product')[1]}
                    ad.cls_terminal()
                    print(f'---Creating new batch: {NewBatch}---\n')
                    NewProduct = '...'
                    NewStock = '...'
                    productHeader, productList = ad.retrive_csv('List_Product')
                    existedHead, existedLists = ad.filterLists(productHeader,productList,['Product'])
                    insertableProducts = existedLists #Dynamic list, only contains non-chosen products.
                    while True:
                        ad.list_Sorting(existedHead, insertableProducts)
                        print('')
                        productOptions = {k[0]:v for v, k in enumerate(insertableProducts)}
                        NewProduct = ad.multiOptCheck(False,False,'#cancel',
                                    'Insert a produced product Name (#cancel to cancel): ',
                                    'Product does not exist! Please insert an available product (#cancel to canel): ',
                                    productOptions)
                        if NewProduct == None:
                            input('\nHit ENTER to return...')
                            return
                        NewProduct = insertableProducts[int(NewProduct)][0]
                        NewProduced = ad.num_check_multi(1,f'Record the quantity produced for {NewProduct} (#cancel to cancel): '
                                                        ,f'Please insert a valid quantity! (#cancel to cancel): ','#cancel',
                                                        '',0,'','int')
                        if NewProduced == None:
                            input('\nBatch creation cancelled. Hit ENTER to return...')
                            return
                        NewProduced = NewProduced[0]
                        NewStock = str(NewProduced)
                        print(f'\nConfirm product {NewProduct}, produced {str(NewProduced)}?')
                        confirmation = ad.multiOptCheck(False,True,'','Choose Yes or No: ','',
                                                        {'Yes':0,'No':1})
                        if confirmation == '0':
                            ad.cls_terminal()
                            print(f'--Added product in batch: {NewBatch}--\n')
                            batchCart[NewProduct] += NewProduced
                            addedProducts =  [[k,str(v)] for k, v in batchCart.items() if v != 0]
                            tempHead = {'Product':0,'Produced':1}
                            ad.list_Sorting(tempHead,addedProducts)
                            print('')
                            addMore = ad.multiOptCheck(False,True,'','Add more?: ','Invalid decision! Add more?: ',
                                                    {'Yes':0,'No':1})
                            if addMore == '0':
                                ad.cls_terminal()
                                continue
                            if addMore == '1':
                                input('Hit ENTER to finalize...')
                                break
                        elif confirmation == '1':
                            ad.cls_terminal()
                            continue
                    ad.cls_terminal()
                    print('---Sucessfully created new batch!---')
                    for new in addedProducts:
                        ad.appdCsv(path_inProduct,[NewBatch,NewExpiry,new[0],new[1],NewStock])
                    input(f'\n.\n.\n.\nNew batch {NewBatch} has been recorded! Hit ENTER to return...')
                    return
                elif chosen == '1':
                    input('Hit ENTER to return...')
                    return

            while True:
                ad.cls_terminal()
                print('---Production Record Management---\n')
                print('1. View production records\n2. Create new batches\n3. Back to menu...')
                chosen = ad.multiOptCheck(False,False,'','Choose an option: ','Please insert a valid option: ',
                                {'View production record':0,'production record':0,'records':0,'record':0,
                                'production':0,'production records':0,'view':0,'views':0,
                                'Create new batches':1,'Create':1,'new batch':1,'new':1,'batches':1,'batch':1,
                                'Create new batch':1,'Create batch':1,'Create batches':1,
                                'Back to menu...':2,'Back':2,'Menu':2,'Back to menu':2})
                ad.cls_terminal()
                if chosen == '0':
                    allBatches()
                elif chosen == '1':
                    createBatches()
                elif chosen == '2':
                    break
            
            input('Hit ENTER to continue...')
            return

        def equipmentManagement(): #For reporting equipment issues faced by bakers.
            while True:
                print('---Facility Maintenance & Services---')
                print('\nChoose an options ')
                print('1.File a report\n2.Exit...\n')
                choose = ad.multiOptCheck(False,False,'','Choose an option: ','Please insert an available option!: ',
                                    {'Report':0,'File a report':0,'Product':0,
                                    'Exit':1,'Back':1})
                
                if choose == '0':
                    while True:
                        NewEquipmentName = input("Enter Equipment Name: ")
                        if any(i for i in NewEquipmentName if i.isdigit()):
                            print('Equipment / Facility name should not contain integers! Try again: ')
                            continue
                        else:
                            break
                    NewMalfuntion = input("Provide the problem of the equipment: ")
                    reportList = [NewEquipmentName,NewMalfuntion,'Pending']
                    ad.appdCsv('Report_Equipment',reportList)
                    input('Report have been submitted! input\nHit ENTER to continue...')
                    ad.cls_terminal()
                    continue
                elif choose == '1':
                    input('\nHit ENTER to return...')
                    break
            return


        while True:
            print('----Baker Menu----\n')
            print('1. Recipe Management\n2. Inventory Inspectation\n3. Production Record')
            print('4. Equipment Maintenance\n5. Account Settings\n6. Logout\n')
            choose = ad.multiOptCheck(False,False,'','Choose an option: ',
                                    'Please insert an available option!: ',
            {'Recipe Management':0,'Recipe':0,'Management':0,'Recipes':0,
            'Inventory Control':1,'Inventory':1,'Control':1,
            'Production Record':2,'Record':2,'Production':2,
            'Equipment':3,'Equipment Service':3,'Maintenance':3,
            'Account Settings':4,'Account':4, 'Account Setting':4,'Settings':4,'Setting':4,
            'Logout':5,'Log out':5,'Out':5})

            ad.cls_terminal()
            if choose == '0':
                RecipeManage()
            if choose == '1':
                inventoryCheck()
            elif choose == '2':
                productionRecord()
            elif choose == '3':
                equipmentManagement()
            elif choose == '4':
                employeeSettings(username)
            elif choose == '5' :
                break
            ad.cls_terminal()
            continue
        return


    while True:
        path_AccList = 'List_Account'
        header, acc_List = ad.retrive_csv(path_AccList) #Retrieved Headers + AccList, path.
        nameColumn = header['Username'] #Index of the column.
        passColumn = header['Password']
        roleColumn = header['Role']
        lastLogColumn = header['LastLogin']
        userLogged = LoginMenu()  #Returns username of the logged user.
        if userLogged == '#Exit':
            break
        elif userLogged == None:
            continue
        header, acc_List = ad.retrive_csv(path_AccList)    
        nameColumn = header['Username']    #Index of the column.
        passColumn = header['Password']
        roleColumn = header['Role']
        lastLogColumn = header['LastLogin']
        userRole = [row[roleColumn] for row in acc_List if row[nameColumn] == userLogged][0]
        ad.cls_terminal()
        if userRole == 'Manager':
            ManagerMenu(userLogged)
        elif userRole == 'Customer':
            CustomerMenu(userLogged)
        elif userRole == 'Cashier':
            CashierMenu(userLogged)
        elif userRole == 'Baker':
            BakerMenu(userLogged)
        userLogged = None
        continue
    print('\n===Until next time, see you soon!===')

SystemProgram()

