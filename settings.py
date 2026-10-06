# Cost of means of travel
l = 2
s = 1
a = 10

# distances land
addisabebaToSuakin = 3
addisabebaToKapGuardafui = 3
addisabebaToVictoriasøen = 3
cairoToOmdurman = 4
congoToLuanda = 3
congoToSlavekysten = 5
congoToWadai = 6
congoToDarfur = 6
baharToElGazalDarfur = 2
baharToElGazalVictoriasøen = 2
dakarToMarrakesh = 8
dakarToSierraLeone = 4
darfurToOmdurman = 3
darfurToSuakin = 4
darfurToSahara = 8
darfurToWadai = 4
dragebjergetToMozambique = 4
dragebjergetToVictoriafaldene = 3
guldkystenToSierraLeone = 5
guldkystenToTimbuktu = 4
hvalbugtenToKapstaden = 4
hvalbugtenToVictoriafaldene = 4
kabaloToLuanda = 4
kabaloToVictoriasøen = 4
kapGuardafuiToZanzibar = 6
luandaToMozambique = 10
marrakeshToTanger = 2
mozambiqueToVictoriasøen = 6
mozambiqueToVictoriafaldene = 5
mozambiqueToZanzibar = 3
omdurmanToTripoli = 6
saharaToTanger = 5
sierraLeoneToTimbuktu = 5
slavekystenToTimbuktu = 5
slavekystenToWadai = 7
tangerToTunis = 5
tripoliToTunis = 3

# map['Addisabeba']['Suakin']
land = {'Addisabeba': {'Suakin': addisabebaToSuakin, 'Kap Guardafui': addisabebaToKapGuardafui, 'Victoriasøen': addisabebaToVictoriasøen},
    'Cairo': {'Omdurman': cairoToOmdurman},
    'Congo': {'Luanda': congoToLuanda, 'Slavekysten': congoToSlavekysten, 'Wadai': congoToWadai, 'Darfur': congoToDarfur},
    'Bahar El Gazal': {'Darfur': baharToElGazalDarfur, 'Victoriasøen': baharToElGazalVictoriasøen},
    'Dakar': {'Marrakesh': dakarToMarrakesh, 'Sierra Leone': dakarToSierraLeone},
    'Darfur': {'Bahar El Gazal': baharToElGazalDarfur,'Omdurman':darfurToOmdurman, 'Suakin': darfurToSuakin, 'Sahara': darfurToSahara, 'Wadai': darfurToWadai},
    'Dragebjerget': {'Mozambique': dragebjergetToMozambique, 'Victoriafaldene': dragebjergetToVictoriafaldene},
    'Guldkysten': {'Sierra Leone': guldkystenToSierraLeone, 'Timbuktu': guldkystenToTimbuktu},
    'Hvalbugten': {'Kapstaden': hvalbugtenToKapstaden, 'Victoriafaldene': hvalbugtenToVictoriafaldene},
    'Kabalo': {'Luanda': kabaloToLuanda, 'Victoriasøen': kabaloToVictoriasøen},
    'Kap Guardafui': {'Addisabeba': addisabebaToKapGuardafui, 'Zanzibar': kapGuardafuiToZanzibar},
    'Kapstaden': {'Hvalbugten': hvalbugtenToKapstaden},
    'Luanda': {'Congo': congoToLuanda, 'Kabalo': kabaloToLuanda, 'Mozambique': luandaToMozambique},
    'Marrakesh': {'Tanger': marrakeshToTanger, 'Dakar': dakarToMarrakesh},
    'Mozambique': {'Dragebjerget': dragebjergetToMozambique, 'Luanda': luandaToMozambique, 'Victoriasøen': mozambiqueToVictoriasøen, 'Victoriafaldene': mozambiqueToVictoriafaldene, 'Zanzibar': mozambiqueToZanzibar},
    'Omdurman': {'Cairo': cairoToOmdurman, 'Darfur': darfurToOmdurman, 'Tripoli': omdurmanToTripoli},
    'Sahara': {'Darfur': darfurToSahara, 'Tanger': saharaToTanger},
    'Sierra Leone': {'Dakar': dakarToSierraLeone, 'Guldkysten': guldkystenToSierraLeone, 'Timbuktu': sierraLeoneToTimbuktu},
    'Slavekysten': {'Congo': congoToSlavekysten, 'Timbuktu': slavekystenToTimbuktu, 'Wadai': slavekystenToWadai},
    'Suakin': {'Addisabeba': addisabebaToSuakin, 'Darfur': darfurToSuakin},
    'Tanger': {'Marrakesh': marrakeshToTanger, 'Sahara': saharaToTanger, 'Tunis': tangerToTunis},
    'Timbuktu': {'Guldkysten': guldkystenToTimbuktu, 'Sierra Leone': sierraLeoneToTimbuktu, 'Slavekysten': slavekystenToTimbuktu},
    'Tripoli': {'Omdurman': omdurmanToTripoli, 'Tunis': tripoliToTunis},
    'Tunis': {'Tanger': tangerToTunis, 'Tripoli': tripoliToTunis},
    'Victoriafaldene': {'Addisabeba': addisabebaToVictoriasøen, 'Bahar El Gazal': baharToElGazalVictoriasøen, 'Dragebjerget': dragebjergetToVictoriafaldene, 'Hvalbugten': hvalbugtenToVictoriafaldene, 'Kabalo': kabaloToVictoriasøen},
    'Victoriasøen': {'Addisabeba': addisabebaToVictoriasøen, 'Bahar El Gazal': baharToElGazalVictoriasøen, 'Kabalo': kabaloToVictoriasøen},
    'Wadai': {'Congo': congoToWadai, 'Darfur': darfurToWadai, 'Slavekysten': slavekystenToWadai},
    'Zanzibar': {'Kap Guardafui': kapGuardafuiToZanzibar, 'Mozambique': mozambiqueToZanzibar}
}