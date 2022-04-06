contacts= {
    "number":3,
    "students": [
        {"name":"Sarah Holderness", "email":"sarah@example.com"},
        {"name":"Mario Bernad", "email":"mario@example.com"},
        {"name":"David Carrasco", "email":"david@example.com"}

    ]
}
for student in contacts["students"]:
    print(student["email"])