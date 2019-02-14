"""Lab 3: Regexes and reformatting."""

import re

# Name: Shyan Yen

contacts = ["Kiayada D. Levy,(570)7924192,Sint-Laureins-Berchem",
            "Gretchen F. Manning,(1-656)-285-0869,Spoleto",
            "Ashton Richards,(974) 843-9297,Annapolis Royal",
            "Demetrius J. Ferguson,1-906-206-4323,Rea",
            "Blair Nelson,1-121-171-3665,Bertiolo",
            "Cynthia J. Farley,632 691 2180,Moen",
            "Nayda M. Lloyd,1-864-250-6977,Sarrev",
            "Miranda Edith Sexton,1-597-689-8316,Shipshaw",
            "Fulton Mays,(725)789-9517,Pierrefonds",
            "Shea Kim,1-697-854-4139,Bihain",
            "Emma-Mae Winters,1-137-630-5601,Gulfport",
            "Inez W. Depew,1-833-470-5664,Johnstone",
            "Darrel F. Key,1-878-918-2161,Olympia",
            "Tobias L. Stephens,1-119-939-6704,Unnao",
            "Elmo Pate,1-869-333-7341,Griesheim"]

# Final product should be
# LastName, FirstName, MiddleInitial
# Location
# (xxx)xxx-xxxx

for string in contacts:
    s0 = re.split(",",string) # split each index into separate array --> [name mid last, number, location]
    name = re.split("\s", s0[0]) # print name into separate array --> [name, mid, last]
    firstName = name[0] 
    lastName = name[len(name)-1] 
    name[0] = lastName
    name[len(name)-1] = firstName
    
    if len(name) > 2: # swap names if name array greater than 2
        midName = name[1] # first index (2nd position) assigned to midName
        name[1] = firstName # first name assigned to first index (2nd position)
        name[len(name)-1] = midName
    printName = name[0] + ", " + name[1] 
    
    if len(name) > 2: 
        printName += ", " + name[2] # add middle initial to printName string
    print(printName) # print out last name, first name, middle initial
    s0[0] = name
    print(s0[2]) # print out location
    num = re.findall("\d",s0[1])
    
    if len(num) > 10:
        num = num[1:11] # array of phone number digits
    print("(" + num[0] + num[1] + num[2] + ")" + num[3] + num[4] + num[5] + "-" + num[6] + num[7] + num[8] + num[9]) # print phone number
    
    
        
        
    
    
    
    

