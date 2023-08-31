class Ohrm_Locators :

    #Test_case1 (login data)
    username_inputbox = 'username' #TagName
    password_inputbox = 'password' #TagName
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' #Xpath
    logout_dropdown = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i'
    logout_button = '/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a'

    #Test_case2 (Invalid crediticals data)
    username_inputbox1 = 'username' #TagName
    password_inputbox1 = 'password' #TagName
    Login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' #Xpath

    #Test_case3 (Adding new employee detials data)  
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a' #Xpath
    add_module = '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    employee_firstname = 'firstName'  #TagName
    employee_lastname = 'lastName'    #TagName
    save_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'#Xpath

    #Test_case4 (Editing employee detials data)
    pim_module = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a' #Xpath
    employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input' 
    search_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]' 
    click_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i' 
    middle_name = 'middleName'  #TagName
    esave_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button' #Xpath

    #Test_case5 (Deleting employee detials data)
    trash_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]/i' #Xpath
    yes_delete = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]' 