# Dylan Cocoletzi, CSW8 (F21)

def print_main_menu(the_menu):
    """
    Prints the character '*' 26 times then
    ask the user what they would like to do.
    After that the menu that is stored in a dictionary will
    be printed and the last line will contain 
    the character '*' 26 times
    """
    print('*' * 26)
    print('What would you like to do?')
    for key, value in the_menu.items():
        print('{} - {}'.format(key, value))
    print('*' * 26)

def check_option(option, menu):
    """
    Returns "invalid" if the provided `option`
    is not one of the keys in the given `menu`.
    Returns "valid" otherwise. If return is "invalid",
    if option is numeric, prints a warning with please message 
    about integer. If "invalid" and option not numeric, prints
    a warning and please message about invalid option.
    """
    result = 'invalid'
    for key in menu.keys():
        if key == option:
            result = 'valid'
    if result == 'invalid':
        if str(option).isnumeric() == False:
            print('WARNING: `{}` is not an integer.'.format(option))
            print('Please enter an integer.')
        else:
            print('WARNING: `{}` is an invalid option.'.format(option))
            print('Please enter a valid option.')
    return result

def list_categories(grade_categories, showID = False):
    """
    The function takes two arguments: a dictionary
    and a Boolean flag that indicates whether to
    display the category IDs.
    The first argument is a dictionary, that stores a
    numeric ID as a key for each category;
    the corresponding value for the key is
    a list that contains a category item
    with 3 elements arranged as follows: 
    * `'name'` - the name of the category,
        e.g., "quiz", "participation";
    * `'percentage'` - the percentage of the total grade,
        e.g., 25, 5, 10.5; 
    * `'grades'` - a list of numeric grades.

    By default, displays the dictionary values as
    CATEGORY NAME : PERCENTAGE%
    If showID is True, the values are displayed as
    ID - CATEGORY NAME : PERCENTAGE%
    If a dictionary is empty, prints "There are no categories."
    If a dictionary has a single category,
    prints "There is only 1 category:"
    Otherwise, prints "There are X categories:"
    where X is the number of records in the dictionary.
    Returns the number of records.
    """
    categories = 0
    for key in grade_categories.keys():
        categories += 1
    if categories == 1:
        print("There is only 1 category:")
    elif categories != 0:
        print("There are {} categories:".format(categories))
    if showID == False:
        for value in grade_categories.values():
            print("{} : {}%".format(value[0].upper(), float(value[1])))
    if showID == True:
        for key, value in grade_categories.items():
            print("{} - {} : {}%".format(key, value[0].upper(), float(value[1])))
    if bool(grade_categories) == False:
        print("There are no categories.")
    #if categories == 1:
        #print("There is only 1 category:")
    #elif categories != 0:
        #print("There are {} categories:".format(categories))
    return categories

def create_id(dict_int, offset = 0):
    """
    Return an integer ID that would be generated 
    for the next value inserted into the `db`.
    Given an empty dictionary, return the offset.
    Else, return the current max key + offset + 1 which
    is the integer ID that would be generated for the next value 
    appended into `db`. If no argument is provided for offset,
    the default argument will be 0.
    """
    key_list = []
    if bool(dict_int) == False:
        return offset
    else:
        for key in dict_int.keys():
            key_list.append(int(key))
        return max(key_list) + offset + 1

def is_numeric(val):
    '''
    Returns True if the string `val`
    contains a valid integer or a float.
    '''
    x = False
    if val.isnumeric() == True:
        x = True
    else:
        float_list = val.split('.')
        if (float_list[0].isnumeric() == True) & (float_list[-1].isnumeric() == True):
            x = True
    return x

def add_category(db, cid, info_str):
    """
    Inserts into the `db` collection (dictionary)
    `cid` - the integer category ID (the key), and its
    corresponding value, which is a list obtained from the
    `info_str` that contains two elements: the category name 
    and the corresponding percentage of the total grade.
    If the list does not contain two elements, returns -2.
    Calls is_numeric():
    If the last input value (the percentage) in `info_str`
    is not numeric (int or float), does not update the
    dictionary and returns -1 instead.
    Otherwise, returns the integer ID of the category.
    Stores the percentage as a float (not as a string).
    """
    info_list = info_str.split(" ")
    if len(info_list) != 2:
        return -2
    elif len(info_list) == 2:
        if is_numeric(info_list[-1]) != True:
            return -1
        else:
            db[cid] = [info_list[0], float(info_list[-1])]
            #print(db)
            #print(db[cid])
            return cid

def add_categories(db, max_num, id_offset):
    """
    Prompts the user to enter a single-word category name
    and the corresponding percentage of the total grade.
    Calls `create_id()` to get the ID for the category.
    Calls `add_category()`, and keeps asking the user to
    input the correct value for that category, if
    its percentage is not a number (int or float).
    """
    print(f"You can add up to {max_num} categories.")
    count = 1
    categories = 0
    bool_result = True
    while bool_result == True:
        if count == 1:
            user_input = input("::: How many categories will you add?\n> ")
        else:
            user_input = input("::: Enter a valid number of categories you plan to add\n> ")
        if is_numeric(user_input) == False:
            print("WARNING: `{}` is not a valid integer.".format(user_input))
            count += 1
        elif int(user_input) >= 10:
            for key in db.keys():
                categories += 1
            print("WARNING: Adding {} categories would exceed the allowable max.\nYou can store up to 10 categories.".format(user_input))
            print("Current total of categories is {}.".format(categories))
            bool_result = False
        elif 1 <= int(user_input) <= 9:
            for num in range(1, int(user_input) + 1):
                user_input2 = input("::: Enter the category {} name (no spaces) followed by its percentage\n> ".format(num))
                entry_list = user_input2.split(" ")
                bool_result2 = True
                bool_result3 = True
                bool_result4 = False
                while bool_result2 == True:
                    if (len(entry_list) != 2) or (is_numeric(entry_list[-1]) == False):
                        user_input3 = input("WARNING: invalid input for the name and percentage.\n::: Enter the category {} name (no spaces) followed by its percentage\n::: or enter M to return back to the menu.\n> ".format(num))
                        bool_result4 = True
                        if user_input3 == "M" or user_input3 == 'm':
                            bool_result3 = False
                            bool_result2 = False
                            bool_result = False
                        else:
                            entry_list = user_input3.split(" ")
                    elif (len(entry_list) == 2) and (is_numeric(entry_list[-1]) == True):
                        result = create_id(db, id_offset)
                        if bool_result4 == True:
                            add_category(db, result, user_input3)
                        else:
                            add_category(db, result, user_input2)
                        bool_result2 = False
                        bool_result = False
                if bool_result3 == False:
                    break
                        
def update_category(db):
    """
    Prompts the user to enter the category ID
    and then asks to enter the updated information:
    name and the corresponding percentage of the total grade.
    Calls list_categories() at the beginning of the function,
    and add_category() to update the info.
    """
    print("Below is the info for the current categories.")
    result = list_categories(db, True)
    count = 1
    bool_result = True
    if result > 0:
        while bool_result == True:
            if count == 1:
                user_input = input("::: Enter the category ID that you want to update\n> ")
            else:
                user_input = input("::: Enter the ID of the category you want to update\n::: or enter M to return back to the menu.\n> ")
                if user_input == 'M' or user_input == 'm':
                    break
            found_key = False
            for key in db.keys():
                if key == int(user_input):
                    found_key = True
            if found_key == True:
                print("Found a category with ID `{}`:".format(user_input))
                user_input2 = input("::: Enter the updated info:\n    category name followed by the percentage.\n> ")
                entry_list = user_input2.split(" ")
                if (len(entry_list) == 2) and (is_numeric(entry_list[-1]) == True):
                    add_category(db, int(user_input), user_input2)
                    bool_result = False
                elif len(entry_list) == 1:
                    print("WARNING: insufficient information for the update.\nRecord with ID `{}` was not updated!".format(user_input))
                    bool_result = False
                elif len(entry_list) == 2 and is_numeric(entry_list[-1]) == False:
                    print("WARNING: invalid input for name and/or percentage.\nRecord with ID `{}` was not updated!".format(user_input))
                    bool_result = False
            elif found_key == False:
                print("WARNING: `{}` is not an ID of an existing category.".format(user_input))
                count += 1
                bool_result = True
    
def delete_category(db):
    """
    Calls list_categories() at the beginning of the function.
    Prompts the user to enter the category ID
    and then verifies the information and selection by printing 
    that record from the `db`.
    Deletes the category and its info, once the user confirms.
    """
    print("Below is the info for the current categories.")
    result = list_categories(db, True)
    count = 1
    bool_result = True
    if result > 0:
        while bool_result == True:
            if count == 1:
                user_input = input("::: Enter the category ID that you want to delete\n> ")
            else:
                user_input = input("::: Enter the ID of the category you want to delete\n::: or enter M to return back to the menu.\n> ")
                if user_input == 'M' or user_input == 'm':
                    break
            found_key = False
            for key in db.keys():
                if key == int(user_input):
                    found_key = True
            if found_key == True:
                print("Found a category with ID `{}`:".format(user_input))
                print(db[int(user_input)])
                user_input2 = input("::: Are you sure? Type Y or N\n> ")
                if user_input2 == 'Y' or user_input2 == 'y':
                    del db[int(user_input)]
                    print("Deleted")
                    bool_result = False
                else:
                    print("Looks like you aren't 100{} sure.\nCancelling the deletion.".format('%'))
                    bool_result = False
            elif found_key == False:
                print("WARNING: `{}` is not an ID of an existing category.".format(user_input))
                count += 1
                bool_result = True

def add_grades(db):
    """
    Calls list_categories() at the beginning of the function.
    Prompts the user to enter the category ID
    and then asks to enter the grades for that category. 
    Convert the grades string to the list of float values.
    Calls add_category_grades() to insert the record.
    Does not add the grades if not all provided grades
    contain numeric scores.
    """
    print("Below is the info for the current categories.")
    result = list_categories(db, True)
    bool_result = True
    count = 1
    if result > 0:
        while bool_result == True:
            if count == 1:
                user_input = input("::: Enter the category ID for which you want to add grades\n> ")
            else:
                user_input = input("::: Enter the ID of the category to add grades to\n::: or enter M to return back to the menu.\n> ")
                if user_input == 'M' or user_input == 'm':
                    break
            found_key = False
            for key in db.keys():
                if key == int(user_input):
                    found_key = True
            #if len(db[int(user_input)]) == 2:
                #original = f"{db[int(user_input)][0]} grades []"
            #else:
                #original = f"{db[int(user_input)][0]} grades {db[int(user_input)][2]}"
            if found_key == True:
                print("You selected a {} category.".format((db[int(user_input)][0]).upper()))
                if len(db[int(user_input)]) == 3:
                    show_grades_category(db, user_input)
                user_input2 = input("::: Enter space-separated grades\n::: or enter M to return back to the menu.\n> ")
                grades = user_input2.split(" ")
                test = True
                for i in grades:
                    if is_numeric(i) == False:
                        test = False
                if user_input2 == "M" or user_input2 == 'm':
                    break
                elif test == False:
                    break
                else:
                    #print(original)
                    add_category_grades(db, user_input, user_input2)
                    if len(db[int(user_input)]) == 3:
                        print("{} grades {}".format(db[int(user_input)][1], db[int(user_input)][2]))
                #grades_list = user_input2.split(" ")
                #for i in range(len(grades_list)):
                    #grades_list[i] = is_numeric(i)
                #if False in grades_list:
                    #bool_result = False
                #else:
                    #add_category_grades(db, int(user_input), user_input2)
                    #pass #add the other function
                    print("Success! Grades for the PA category were updated.")
                    bool_result = False
            elif found_key == False:
                print("`{}` is not an ID of an existing category.".format(user_input))
                count += 1
                bool_result = True

def add_category_grades(db, cid, grades_str):
    """
    Inserts into the `db` collection (a dictionary)
    a list of grades for the provided category ID.
    The list is obtained from the grades_str.
    Calls is_numeric() to check each grade in 
    grades_str: if all provided grades were not numeric, 
    does not update the dictionary and returns -1.
    Stores the grades as a list of floats (not as strings).
    Calls show_grades_category() if the user adds grades to a category
    that already has grades added to it. 
    If a category with the provided ID already has grades
    in it, then the new grades are appended to the existing
    grades and updated information is displayed.
    Returns the number of grades that were added.
    """
    grades_list = grades_str.split(" ")
    float_list = []
    grades = 0
    for i in range(len(grades_list)):
        float_list.append(float(grades_list[i]))
        grades_list[i] = is_numeric(grades_list[i])
    if False in grades_list:
        return -1
    else:
        if len(db[int(cid)]) == 3:
            show_grades_category(db, str(cid))
            for num in float_list:
                db[int(cid)][2].append(num)
                grades += 1
            return grades
        else:
            db[int(cid)].append(float_list)
            #print(db)
            return len(db[int(cid)][2])
    

def show_grades(db):
    """
    Calls list_categories() at the beginning of the function.
    If the dictionary is empty, return from the function.
    Otherwise, prompts the user to enter the category ID or 
    enter "A" to show grades of all categories that store them
    If the provided ID is not valid, prompt the user to enter 
    a valid ID or go back to the menu using ‘M’ or ‘m’ as input.
    Calls show_grades_category() with appropriate arguments 
    to show the grades.
    """
    print("Below is the info for the current categories.")
    result = list_categories(db, True)
    bool_result = True
    count = 1
    if result > 0:
        while bool_result == True:
            if count == 1:
                user_input = input("::: Enter the category ID for which you want to see the grades\n::: or enter A to list all of them.\n> ")
            else:
                user_input = input("::: Enter a valid category ID to see the grades\n::: or enter M to return back to the menu.\n> ")
                if user_input == "M" or user_input == 'm':
                    break
            if user_input == "A" or user_input == 'a':
                show_grades_category(db, 'A')
                bool_result = False
            else:
                found_key = False
                for key in db.keys():
                    if key == int(user_input):
                        found_key = True
                if found_key == True: #Maybe fix this line
                    if is_numeric(user_input) == True:
                        show_grades_category(db, user_input)
                        bool_result = False
                elif found_key == False:
                    print("WARNING: `{}` is not an ID of an existing category.".format(user_input))
                    count += 1
                    bool_result = True

def show_grades_category(db, cid):
    """
    Displays the grades the user added into the db collection (dictionary), 
    for the provided category ID `cid`.
    If there are no grades, display "No grades were provided for category ID `cid`."
    and return 0.
    Otherwise, print the capitalized category name followed by a word "grades",
    and then a list of grades. Print the grades list without any beautification. 
    E.g.: QUIZ grades [100, 100, 95, 5, 80, 0]
    Return the number of grades in the grades list.
    """
    if is_numeric(cid) == True:
        if len(db[int(cid)]) != 3:
            print("No grades were provided for category ID `{}`.".format(cid))
            return 0
        else:
            print("{} grades {}".format((db[int(cid)][0]).upper(), db[int(cid)][2]))
    else:
        for key, value in db.items():
            if len(value) == 3:
                print("{} grades {}".format((db[key][0]).upper(), db[key][2]))

def sum_percentages(db):
    """
    Given a collection (dictionary),
    where each value is a list whose
    second element is a percentage of
    a category, returns the sum of the
    percentages.
    """
    total = 0
    for key in db.keys():
        total += db[key][1]
    return total

def get_avg_grade(grade_list):
    """
    Given a list of grades,
    returns the average value of the
    grades. Returns 0 if the list is
    empty.
    """
    if len(grade_list) == 0:
        return 0
    else:
        return sum(grade_list)/len(grade_list)
    
def grade_stats(db):
    """
    Calls list_categories() at the beginning of the function.
    Calls show_grades_category() to display the grades.
    Calls sum_percentages() to get the total percentages;
    shows a warning if they do not add up to 100.
    Calls get_avg_grade() to compute the average score for
    each category.
    Returns the computed course grade or, if there are no
    categories, returns 0.
    """
    print("Below is the info for the current categories.")
    list_categories(db)
    print()
    print("Provided grades:")
    show_grades_category(db, 'A')
    print()
    avg_list = []
    percent_list = []
    key_list = []
    grade_list = []
    if sum_percentages(db) != 100:
        print("WARNING: Category percentages don't add up to 100.\nCurrent category percentages comprise {} of the total.\n".format(float(sum_percentages(db))))
    print("Grade calculation:")
    for key in db.keys():
        if len(db[key]) == 3:
            avg_list.append(get_avg_grade(db[key][2]))
        else:
            avg_list.append(0)
    for key in db.keys():
        percent_list.append(db[key][1])
        key_list.append(db[key][0])
    for num in range(len(avg_list)):
        grade_list.append(avg_list[num] * (percent_list[num] * 0.01))
    for num in range(len(avg_list)):
        print("{} = {:.2f} * {:.2f} = {:.2f}".format((key_list[num]).upper(), avg_list[num], percent_list[num] * 0.01, grade_list[num]))
    print("Total grade = {:.2f}".format(sum(grade_list)))

def save_data(db):
    """
    Calls list_categories() at the beginning of the function.
    If there are no categories, notify the user and return 0.
    By default, save the `db` to a CSV file.
    Asks the user whether to read from the default filename
    or ask for the filename to open.
    Calls save_dict_to_csv() to create the file.
    """
    print("Below is the info for the current categories.")
    result = list_categories(db, True)
    if result == 0:
        print("Skipping the creation of an empty file.")
        return 0
    else:
        user_input = input("::: Save to the default file (grade_data.csv)? Type Y or N\n> ")
        if user_input == 'N'or user_input == 'n':
            user_input2 = input("::: Enter a filename to save database:\n> ")
            save_dict_to_csv(db, user_input2)
            print("Saving the database in {}\nDatabase contents:\n{}".format(user_input2, db))
        elif user_input == 'Y' or user_input == 'y':
            save_dict_to_csv(db, 'grade_data.csv')
            print("Saving the database in grade_data.csv\nDatabase contents:\n{}".format(db))

def save_dict_to_csv(storage, filename):
    """
    Once provided filename and storage, the dictionary will be stored
    to the provided filename. It will make user that the output to the created file
    will be formatted by id,'categoryname',percentage,thegrade all as int.
    """
    import csv
    list_dic = []
    for key, value in storage.items():
        list_dic2 = []
        list_dic2.append(key)
        if len(value) == 3:
            for i in range(len(value)):
                if isinstance(value[i], list) == True:
                    for j in value[i]:
                        list_dic2.append(j)
                else:
                    list_dic2.append(value[i])
            list_dic.append(list_dic2)
        else:
            for num in value:
                list_dic2.append(num)
            list_dic.append(list_dic2)
    with open(filename, 'w', newline = '') as f:
        for i in list_dic:
            if len(i) > 3:
                end = len(i) - 1
                for j in range(len(i)):
                    if j == end:
                        f.write(str(int(i[j])))
                    elif j == 1:
                        f.write(str(i[j]) + ',')
                    else:
                        f.write(str(int(i[j])) + ',')
                f.write("\n")
            else:
                for j in range(len(i)):
                    if j == 2:
                        f.write(str(int(i[j])))
                    elif j == 1:
                        f.write(str(i[j]) + ',')
                    else:
                        f.write(str(int(i[j])) + ',')
                f.write('\n')   

def load_dict_from_csv(filename):
    """
    Given a string containing the filename,
    Opens the file and stores its contents
    into the dictionary, which is returned
    from this function.
    The function assumes that the first element
    on each row will be an integer ID, stored
    as a key in the dictionary, and the values
    that are on the rest of the line are stored
    in a list as follows:
    [row[1], float(row[2]), [float(i) for i in row[3:]]]
    The function returns an empty dictionary
    if the CSV file is empty.
    """
    import csv
    dic = dict()
    with open(filename, 'r') as f:
        grades = csv.reader(f)
        for i in grades:
            if len(i) > 3:
                for j in range(2, len(i)):
                    i[j] = float(i[j])
                dic[int(i[0])] = [i[1], i[2], i[3:]]
            else:
                i[2] = float(i[2])
                dic[int(i[0])] = [i[1], i[2], []]
    return dic

def load_data(db):
    """
    TODO: document the functinality
    The function prompts the user if they would like the program
    to read from the default file. If yes, the function reads the file and stores the contents 
    into a dictionary. If no, the function ask the user to enter the name of 
    an existing file. If the file is not in the directory, prints warning
    message and exits the function. The dictionary created then is updated to the 
    main dictionary
    """
    import csv
    import os
    new_db = {}
    filename = "grade_data.csv"
    print(f"::: Load the default file ({filename})? Type Y or N")
    user_input = input("> ")
    if user_input == 'Y' or user_input == 'y':
        if os.path.exists(filename) == False:
            print("WARNING: Cannot find a CSV file named '{}'".format(filename))
        else:
            print("Reading the database from {}\nResulting database:".format(filename))
            new_db = load_dict_from_csv(filename)
            #print(load_dict_from_csv(filename))
            print(new_db)
    elif user_input == 'N' or user_input == 'n':
        user_input2 = input("::: Enter the name of the csv file to load.\n> ")
        if os.path.exists(user_input2) == False:
            print("WARNING: Cannot find a CSV file named '{}'".format(user_input2))
        else:
            bool_result = True
            while bool_result == True:
                if (user_input2[-1] == 'v') and (user_input2[-2] == 's') and (user_input2[-3] == 'c') and (user_input2[-4] == '.'):
                    print("Reading the database from {}\nResulting database:".format(user_input2))
                    new_db = load_dict_from_csv(user_input2)
                    print(load_dict_from_csv(user_input2))
                    bool_result = False
                else:
                    user_input2 = input("WARNING: data.txt does not end with `.csv`\n::: Enter the name of an existing csv file.\n")
    db.update(new_db)

### TODO: Make sure to call db.update() with the new_db
### to propagate the update back to the main program

if __name__ == "__main__":
    the_menu = {'1': 'List categories', '2': 'Add a category', '3': 'Update a catergory', '4': 'Delete a category', '5' : 'Add grades', '6': 'Show grades', '7': 'Grade statistics', '8': 'Save the data', '9': 'Upload data from file', 'Q': 'Quit this program'} # TODO 1: add the options from the instructions
    #main_db = {100: ['pa', 5.0, [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]], 201: ['ca', 15.0, [100.0, 100.0, 98.0, 95.0, 0.0, 100.0]], 301: ['la', 25.0, [100.0, 100.0, 100.0, 5.0, 0.0, 70.0]], 401: ['quiz', 25.0], 501: ['project', 25.0]} # stores the grading categories and info
    main_db = {101: ['quiz', 17.0]}
    max_cat = 10 # the max total num of categories a user can provide
    cat_id_offset = 100 # the starting value for the category ID in this program

    opt = None

    while True:
        print_main_menu(the_menu) # TODO: uncomment and call with the menu as an argument
        print("::: Enter an option")
        opt = input("> ")

        if opt == 'Q' or opt == 'q': # TODO 2: make Q or q quit the program
            print("Goodbye")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid": # TODO 3: implement check_option
                continue
            print("You selected option {} to > {}.".format(opt, the_menu[opt]))

            if opt == '1': # note that the menu should store the keys as strings
                list_categories(main_db)

            if opt == '2':
                add_categories(main_db, max_cat, cat_id_offset)
        
            if opt == '3':
                update_category(main_db)
        
            if opt == '4':
                delete_category(main_db)
        
            if opt == '5':
                add_grades(main_db)
        
            if opt == '6':
                show_grades(main_db)
        
            if opt == '7':
                grade_stats(main_db)
        
            if opt == '8':
                save_data(main_db)
        
            if opt == '9':
                load_data(main_db)
        
        opt = input("::: Press Enter to continue...")
    print("See you next time!")