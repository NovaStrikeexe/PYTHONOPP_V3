from PonyDataBase import *

with db_session:

    id_of_client2 = input("Client id: ")  # Print Client data
    client2 = Client[id_of_client2]
    print("Name of client: ", client2.name_of_human)
    print("Surname of client: ", client2.s_name_of_human)
    print("Age of client: ", client2.age_of_human)
    print("Type of visit: ", client2.type_of_visit)
    print("---------------------------------------")
    commit()

    id_of_client1 = input("Client id: ")  # Change client data
    name_of_human = input("Input new name of client: ")
    s_name_of_human = input("Input new surname of client: ")
    age_of_human = input("Input new age of client: ")
    type_of_visit = input("Input new type of visit: ")
    client1 = Client[id_of_client1]
    client1.name_of_human = name_of_human
    client1.s_name_of_human = s_name_of_human
    client1.age_of_human = age_of_human
    client1.type_of_visit = type_of_visit
    print("Name of client: ", client1.name_of_human)
    print("Surname of client: ", client1.s_name_of_human)
    print("Age of client: ", client1.age_of_human)
    print("Type of visit: ", client1.type_of_visit)
    print("---------------------------------------")
    commit()

    id_of_client = input("Client id: ")  # Removing a person by ID
    client4 = Client[id_of_client]
    client = Client.select(lambda c: c.id == id_of_client)
    print("Name of client: ", client4.name_of_human)
    print("Surname of client: ", client4.s_name_of_human)
    print("Age of client: ", client4.age_of_human)
    print("Type of visit: ", client4.type_of_visit)
    type = input("Are you sure you want to delete the client Y/N:")
    if type == "Y":
        print("Customer data deleted")
        print("---------------------------------------")
        client.delete()
        commit()
    if type == "N":
        print("Customer data are not changed")
        print("---------------------------------------")
        commit()

    type_of_people = input("Enter the type of people the average age you want to get Client / ShootingOfficer")
    if type_of_people == "Client":
        s = avg(p.age_of_human for p in Client)
        print(s)
        commit()
    if type_of_people == " ShootingOfficer":
        s = avg(p.age_of_human for p in ShootingOfficer)
        print(s)
        commit()

