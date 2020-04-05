from Classes.Client import Client
from Classes.Wepons import Wepons
from Classes.ShootingOfficer import ShootingOfficer
from Classes.List_of_upgrades import List_of_upgrades
from Classes.Action import Action
from Classes.Cur_wepon import Cur_wepon
from Classes.OfficerClientWepon import OfficerClientWepon
from Classes.ShootingRange import ShotingRange
from PonyDataBase import *
from pony.orm import set_sql_debug, db_session, sum, select

id_of_client = input("Client id: ")  # Removing a person by ID
client = Client.select(lambda c: c.id == id_of_client)
client.delete()

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

id_of_client2 = input("Client id: ")  # Print Client data
client2 = Client[id_of_client2]
print("Name of client: ", client2.name_of_human)
print("Surname of client: ", client2.s_name_of_human)
print("Age of client: ", client2.age_of_human)
print("Type of visit: ", client2.type_of_visit)
