# Aaron Wylie
# Connect to PostgreSQL

import psycopg2 as p
from datetime import date
from datetime import datetime

def adder(img, user_name, location_x, location_y, location_z, bot_run):
    # --- connects to database ---
    con = p.connect(
        host='database-1.ctagzvsokrv9.us-east-2.rds.amazonaws.com',
        database='demo_1',
        user='aaronwylie',
        password='Frogybob1',
        port=5432
    )

    # --- cursor ---
    cur = con.cursor()

    # --- key finder ---
    query = "SELECT setval('django_migrations_id_seq', (SELECT MAX(id) FROM public.loginscreen_destination))"
    cur = con.cursor()
    cur.execute(query)
    row = cur.fetchone()
    key = row[0]+1

    # --- scrapes txt file ---
    # class ... accuracy
    try:
	    file = open('runs/detect/exp'+str(bot_run)+'/labels/'+str(bot_run)+'rgb.txt', 'r')
	    array_plant_dat = str.split(file.read())    
	    print("Plant --> " + array_plant_dat[0])
	    print("Accuracy --> " + array_plant_dat[5])
    except:
	    print('Not a plant')
	    return

    # --- Gets time/date ---
    # date
    today = date.today() 
    # time
    now = datetime.now() 
    current_time = now.strftime("%H:%M:%S")

    file.close()
    # --- adds data ---
    cur.execute("insert into public.loginscreen_destination (id, plant_name, img, bot_number, date, time, user_name, location_x, location_y, location_z, bot_run, plant_id, accuracy) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (key, array_plant_dat[0], img, '1', str(today), str(current_time), user_name, location_x, location_y, location_z, str(bot_run), key, array_plant_dat[5]))

    con.commit()
    # --- closes connection to database ---
    con.close()
