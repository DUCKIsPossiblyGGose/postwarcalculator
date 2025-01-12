t1_cp = 4
t2_cp = 6
t3_cp = 8
t4_cp = 12
t5_cp = 15
t6_cp = 20
t7_cp = 25
t8_cp = 33
t9_cp = 45
t10_cp = 60
t11_cp = 80
t12_cp = 100
t13_cp = 125

tier = input("input your troop tier (ex t7, t1, t13) ")
if tier == 't1':
    cp_per_ant = t1_cp
if tier == 't2':
    cp_per_ant = t2_cp
if tier == 't3':
    cp_per_ant = t3_cp
if tier == 't4':
    cp_per_ant = t4_cp
if tier == 't5':
    cp_per_ant = t5_cp
if tier == 't6':
    cp_per_ant = t6_cp
if tier == 't7':
    cp_per_ant = t7_cp
if tier == 't8':
    cp_per_ant = t8_cp
if tier == 't9':
    cp_per_ant = t9_cp
if tier == 't10':
    cp_per_ant = t10_cp
if tier == 't11':
    cp_per_ant = t11_cp
if tier == 't12':
    cp_per_ant = t12_cp
if tier == 't13':
    cp_per_ant = t13_cp
postwar_cap = input('alright, and now i need your postwar cap (ex 1387000) ')
amount_of_ants = int(postwar_cap) / cp_per_ant
print('you can train', amount_of_ants)
time_per_ant = input("how long does it take to train one of these ants? (in seconds) ")
total_time_seconds = int(time_per_ant) * amount_of_ants
total_time_hours = total_time_seconds / 3600
print("you need ", total_time_hours, "hours of speeds ups")

print("okay, now we need to figure out how much rss you need")
food_per_ant = input("how much food does one ant take? ")
leaf_per_ant = input("how much leaf does one ant take? ")
water_per_ant = input("how much water does one ant take? ")
fungi_per_ant = input("how much fungi does one ant take? ")
total_food = int(food_per_ant) * amount_of_ants
total_leaf = int(leaf_per_ant) * amount_of_ants
total_water = int(water_per_ant) * amount_of_ants
total_fungi = int(fungi_per_ant) * amount_of_ants

print("you need", total_food, 'food', total_leaf, 'leaf', total_water, 'water', total_fungi, 'fungi')
