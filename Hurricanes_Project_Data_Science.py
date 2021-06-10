# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 
'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 
'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 
'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 
'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 
1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165,
 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast',
 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
 ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
 ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
 ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
 ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], 
 ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], 
 ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'],
 ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
 ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'],
 ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
 ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], 
 ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
 ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'],
 ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M',
 '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B',
  '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:

def damage_to_floats(damages_list):
    damages_values = []
    for value in damages_list:
        multiplier = 0
        if value == 'Damages not recorded':
            damages_values.append('Damages not recorded')
        else:
            multiplier = value[-1]
            if multiplier == "M":
                damages_values.append(float(value[0:len(value)-1])*1000000)
            elif multiplier == "B":
                damages_values.append(float(value[0:len(value)-1])*1000000000)
    return damages_values
    


damages_floats = damage_to_floats(damages)
# write your construct hurricane dictionary function here:

def hurricane_dictionay_creator(names,months,years,max_sustained_winds,areas_affected,damages_floats):
    hurricane_dictionary_return = {}
    for i in range(len(names)):
        dictionary_values = {}
        dictionary_values = {"Name":names[i], "Month":months[i], "Year":years[i],"Max sutained wind":max_sustained_winds[i], "Areas affected":areas_affected[i], "Damage":damages_floats[i]}
        hurricane_dictionary_return.update({names[i]:dictionary_values})
    return hurricane_dictionary_return

hurricane_dictionary = hurricane_dictionay_creator(names,months,years,max_sustained_winds,areas_affected,damages_floats)
#print(hurricane_dictionary)
#print(hurricane_dictionary)

# write your construct hurricane by year dictionary function here:
def dictionary_key_modifcator(hurricane_dictionary,modificador = "Year"):
    año_anterior = 0
    hurricane_dictionary_year_return = {}
    dictionary_list = []
    for i in hurricane_dictionary:
        if hurricane_dictionary[i][modificador] == año_anterior:
            dictionary_list.append(hurricane_dictionary[i])
            hurricane_dictionary_year_return.update({hurricane_dictionary[i][modificador]:dictionary_list})
        else:
            dictionary_list = []
            dictionary_list.append(hurricane_dictionary[i])
            hurricane_dictionary_year_return.update({hurricane_dictionary[i][modificador]:dictionary_list})
        año_anterior = hurricane_dictionary[i][modificador]
        
    return hurricane_dictionary_year_return

hurricane_dictionary_year = dictionary_key_modifcator(hurricane_dictionary,"Year")
#print(hurricane_dictionary_year)


# write your count affected areas function here:
def count_aff_areas(areas_affected):
    dictionary_count = {}
    counter = 0
    for area in areas_affected:
        for region in area:
            if region not in dictionary_count:
                dictionary_count.update({region:1})
            elif region in dictionary_count:
                counter = dictionary_count[region]
                dictionary_count[region] = counter +1
    return dictionary_count

#print(count_aff_areas(areas_affected))
areas_affected_dictionary = count_aff_areas(areas_affected)

# write your find most affected area function here:
def most_affected_area(areas_affected_dictionary):
    sorted_dictionary = sorted(areas_affected_dictionary.items(), key = lambda x: x[1], reverse=True)
    return sorted_dictionary[0]

#print(most_affected_area(areas_affected_dictionary))

# write your greatest number of deaths function here:
def max_number_deaths(deaths):
    unique_list =[]
    repeated_list = []
    num_deaths = 0
    max_num_death_cane = ""
    for i in deaths:
        if i not in unique_list:
            unique_list.append(i)
        else: repeated_list.append(i)
    if len(repeated_list) > 0:
        
        if max(unique_list) == max(repeated_list):
            num_deaths = list(num_deaths)
            max_num_death_cane = list(max_num_death_cane)
            for i in len(deaths):
                if deaths[i] == max(unique_list):
                    num_deaths.append(deaths[i])
                    max_num_death_cane.append(names[i])
        else: 
            num_deaths = max(unique_list)
            max_num_death_cane = names[deaths.index(num_deaths)]
    else:
        num_deaths = max(unique_list)
        max_num_death_cane = names[deaths.index(num_deaths)]
    return max_num_death_cane,num_deaths

#print(max_number_deaths(deaths))


# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricane_dictionary):
    mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
    mortality_type0 = []
    mortality_type1 = []
    mortality_type2 = []
    mortality_type3 = []
    mortality_type4 = []
    mortality_type5 = []
    mortality_scale_dictionary = {}
    for i in range(len(deaths)):
        
        if deaths[i] == mortality_scale[0]:
            mortality_type0.append(hurricane_dictionary[names[i]])
        elif deaths[i] > mortality_scale[0] and deaths[i] <= mortality_scale[1] :
            mortality_type1.append(hurricane_dictionary[names[i]])
        elif deaths[i] > mortality_scale[1] and deaths[i] <= mortality_scale[2] :
            mortality_type2.append(hurricane_dictionary[names[i]])
        elif deaths[i] > mortality_scale[2] and deaths[i] <= mortality_scale[3] :
            mortality_type3.append(hurricane_dictionary[names[i]])
        elif deaths[i] > mortality_scale[3] and deaths[i] <= mortality_scale[4] :
            mortality_type4.append(hurricane_dictionary[names[i]])
        elif deaths[i] > mortality_scale[4]:
            mortality_type5.append(hurricane_dictionary[names[i]])
    
    mortality_scale_dictionary.update({0:mortality_type0, 1:mortality_type1, 2:mortality_type2, 3:mortality_type3, 4:mortality_type4, 5:mortality_type5})
    return mortality_scale_dictionary
#print(categorize_by_mortality(hurricane_dictionary))
mortality_dictionary = categorize_by_mortality(hurricane_dictionary)




# write your greatest damage function here:
def max_damage(damages_floats):
    unique_list =[]
    repeated_list = []
    greates_damage = 0
    cane_name = ""
    
    for i in damages_floats:
        if type(i) == str:
            continue
        elif i not in unique_list:
            unique_list.append(i)
        else: repeated_list.append(i)
    
    if len(repeated_list) > 0:
        
        if max(unique_list) == max(repeated_list):
            greates_damage = list(greates_damage)
            cane_name = list(cane_name)
            for i in len(damages_floats):
                if damages_floats[i] == max(unique_list):
                    greates_damage.append(damages_floats[i])
                    cane_name.append(names[i])
        else: 
            greates_damage = max(unique_list)
            cane_name = names[damages_floats.index(greates_damage)]
    else:
        greates_damage = max(unique_list)
        cane_name = names[damages_floats.index(greates_damage)]
    return cane_name, greates_damage
#print(max_damage(damages_floats))
max_damage_hurricane = max_damage(damages_floats)





# write your catgeorize by damage function here:
def hurricanes_by_damage(damages_floats):

    damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
    damage_hurricane0 = []
    damage_hurricane1 = []
    damage_hurricane2 = []
    damage_hurricane3 = []
    damage_hurricane4 = []
    damage_hurricane5 = []
    damage_hurricane_unknow = []
    damage_hurricane_dictionary = {}
    for i in range(len(damages_floats)):
        if damages_floats[i] == 'Damages not recorded':
            damage_hurricane_unknow.append(names[i])
        elif damages_floats[i] == 0:
            damage_hurricane0.append(names[i])
        elif damages_floats[i] > damage_scale[0] and damages_floats[i] < damage_scale[1] :
            damage_hurricane1.append(names[i])
        elif damages_floats[i] > damage_scale[1] and damages_floats[i] < damage_scale[2] :
            damage_hurricane2.append(names[i])
        elif damages_floats[i] > damage_scale[2] and damages_floats[i] < damage_scale[3] :
            damage_hurricane3.append(names[i])
        elif damages_floats[i] > damage_scale[3] and damages_floats[i] < damage_scale[4] :
            damage_hurricane4.append(names[i])
        elif damages_floats[i] > damage_scale[4]:
            damage_hurricane5.append(names[i])
    damage_hurricane_dictionary.update({0:damage_hurricane0, 1:damage_hurricane1, 2:damage_hurricane2, 3:damage_hurricane3, 4:damage_hurricane4, 5:damage_hurricane5, "Unknow":damage_hurricane_unknow})
    return damage_hurricane_dictionary
#print(hurricanes_by_damage(damages_floats))


