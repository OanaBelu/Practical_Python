# Let's print the emails for students

contacts = {
    "number" : 4,
    "students" :
    [
        {"name":"Sarah Holderness", "email" : "sarah@exemple.com" },
        {"name":"Harry Potter", "email" : "harry@exemple.com" },
        {"name":"Hermione Granger", "email" : "hermione@exemple.com" },
        {"name":"Ron Weasley", "email" : "ron@exemple.com" },
    ]
}

for student in contacts["students"]:
    print(student["email"])