from Classes.Client import Client
from Classes.Wepons import Wepons
from Classes.ShootingOfficer import ShootingOfficer
from Classes.List_of_upgrades import List_of_upgrades
from Classes.Action import Action
from Classes.Cur_wepon import Cur_wepon
from Classes.OfficerClientWepon import OfficerClientWepon
from Classes.ShootingRange import ShotingRange
from pony.orm import *

db = Database()
db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
set_sql_debug(True)
db.generate_mapping(create_tables=True)

with db_session:
    cl1 = Client(name_of_human="Nova", s_name_of_human="Strike", age_of_human=20, type_of_visit=0)
    cl2 = Client(name_of_human="Vova", s_name_of_human="Pyke", age_of_human=30, type_of_visit=0)
    cl3 = Client(name_of_human="Lex", s_name_of_human="Strike", age_of_human=20, type_of_visit=1)
    cl4 = Client(name_of_human="Rex", s_name_of_human="Strike", age_of_human=25, type_of_visit=1)

    of1 = ShootingOfficer(name_of_human="Jacob", s_name_of_human="Wikers", age_of_human=45, work_experience="10-Years",
                          work_schedule="800/1700")

    of2 = ShootingOfficer(name_of_human="William", s_name_of_human="Wikers", age_of_human=35, work_experience="5-Years",
                          work_schedule="1200/1900")

    of3 = ShootingOfficer(name_of_human="Samuel", s_name_of_human="Wikers", age_of_human=25, work_experience="1-Years",
                          work_schedule="1200/1600")

    wep1 = Wepons(mark_of_wepon="AK47", company_constrator="KALASHNIKOV", ammo=30, calibr=7.62)
    wep2 = Wepons(mark_of_wepon="AK74", company_constrator="KALASHNIKOV", ammo=45, calibr=7.62)
    wep3 = Wepons(mark_of_wepon="AK12", company_constrator="KALASHNIKOV", ammo=30, calibr=5.56)
    wep4 = Wepons(mark_of_wepon="AK15", company_constrator="KALASHNIKOV", ammo=45, calibr=5.56)

    wep5 = Wepons(mark_of_wepon="M16", company_constrator="COLT", ammo=30, calibr=5.56)
    wep6 = Wepons(mark_of_wepon="M16A2", company_constrator="COLT", ammo=30, calibr=7.62)
    wep7 = Wepons(mark_of_wepon="M16A4", company_constrator="COLT", ammo=30, calibr=5.56)
    wep8 = Wepons(mark_of_wepon="M4A4", company_constrator="COLT", ammo=30, calibr=5.56)

    lst1 = List_of_upgrades(scope="Acog", handle="Vertical Foregrip", mag=60, type_of_mag="Exenteded",
                            type_of_bulets="Default")
    lst2 = List_of_upgrades(scope="Red dot", handle="Light Grip", mag=80, type_of_mag="Drum",
                            type_of_bulets="Expl")
    lst3 = List_of_upgrades(scope="1P69", handle="Angled Foregrip", mag=10, type_of_mag="shorted",
                            type_of_bulets="Sniper")

    cwp1 = Cur_wepon(mark_of_wepon="M16A4", company_constrator="COLT", ammo=30, calibr=7.338, list_of_upgrades=lst3)
    cwp2 = Cur_wepon(mark_of_wepon="AK15", company_constrator="KALASHNIKOV", ammo=80, calibr=5.56,
                     list_of_upgrades=lst2)
    cwp3 = Cur_wepon(mark_of_wepon="AK47", company_constrator="KALASHNIKOV", ammo=60, calibr=7.62,
                     list_of_upgrades=lst1)

    act1 = Action(type_of_action="Given")
    act2 = Action(type_of_action="Backed")

    of_cl_wp_1 = OfficerClientWepon(client=cl4, officer=of2, cur_wp=cwp3, action=act1)
    of_cl_wp_2 = OfficerClientWepon(client=cl4, officer=of2, cur_wp=cwp3, action=act2)

    s_range = ShotingRange(sum_of_active_targets=0, sum_of_all_targets=0, type_of_shooting_range=0, officer=of1)


    id_of_client = input("Client id: ")  # Удаление человека по ID
    client = Client.select(lambda c: c.id == id_of_client)
    client.delete()
