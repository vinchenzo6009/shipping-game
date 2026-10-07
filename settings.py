# Cost of means of travel
l = 2
s = 1
a = 10

# distances land
addisabebaByLandToSuakin = 3*l
addisabebaByLandToKapGuardafui = 3*l
addisabebaByLandToVictoriasøen = 3*l
cairoByLandByLandToOmdurman = 4*l
congoByLandToLuanda = 3*l
congoByLandToSlavekysten = 5*l
congoByLandToWadai = 6*l
congoByLandToDarfur = 6*l
baharByLandToElGazalDarfur = 2*l
baharByLandToElGazalVictoriasøen = 2*l
dakarByLandToMarrakesh = 8*l
dakarByLandToSierraLeone = 4*l
darfurByLandToOmdurman = 3*l
darfurByLandToSuakin = 4*l
darfurByLandToSahara = 8*l
darfurByLandToWadai = 4*l
dragebjergetByLandToMocambique = 4*l
dragebjergetByLandToVictoriafaldene = 3*l
guldkystenByLandToSierraLeone = 5*l
guldkystenByLandToTimbuktu = 4*l
hvalbugtenByLandToKapstaden = 4*l
hvalbugtenByLandToVictoriafaldene = 4*l
kabaloByLandToLuanda = 4*l
kabaloByLandToVictoriasøen = 4*l
kapGuardafuiByLandToZanzibar = 6*l
luandaByLandToMocambique = 10*l
marrakeshByLandToTanger = 2*l
mocambiqueByLandToVictoriasøen = 6*l
mocambiqueByLandToVictoriafaldene = 5*l
mocambiqueByLandToZanzibar = 3*l
omdurmanByLandToTripoli = 6*l
saharaByLandToTanger = 5*l
sierraLeoneByLandToTimbuktu = 5*l
slavekystenByLandToTimbuktu = 5*l
slavekystenByLandToWadai = 7*l
tangerByLandToTunis = 5*l
tripoliByLandToTunis = 3*l

# distances sea
cairoBySeaToTunis = 5*s
cairoBySeaToSuakin = 4*s
dakarBySeaToDeKanariskeØer = 5*s
dakarBySeaToSierraLeone = 3*s
dakarBySeaToStHelena = 10*s
guldkystenBySeaToHvalbugten = 11*s
guldkystenBySeaToSlavekysten = 4*s
guldkystenBySeaToSierraLeone = 4*s
hvalbugtenBySeaToKapstaden = 3*s
hvalbugtenBySeaToStHelena = 10*s
hvalbugtenBySeaToSlavekysten = 9*s
kapGuardafuiBySeaToSuakin = 4*s
kapGuardafuiBySeaTamatave = 8*s
kapGuardafuiBySeaMocambique = 8*s
kapStMarieBySeaToKapstaden = 8*s
kapStMarieBySeaToMocambique = 3*s
kapstadenBySeaToStHelena =9*s
sierraLeoneBySeaToStHelena = 11*s
tangerBySeaToDeKanariskeØer = 3*s
tangerBySeaToTunis = 3*s

# distances air
cairoByAirToSuakin = 1*a
darfurByAirToKabalo = 1*a
darfurByAirToSuakin = 1*a
darfurByAirToTripoli = 1*a
dragebjergetByAirToKapstaden = 1*a
dragebjergetByAirToVictoriasøen = 1*a
guldkystenByAirToLuanda = 1*a
guldkystenByAirToMarrakesh = 1*a
guldkystenByAirToTripoli = 1*a
guldkystenByAirToHvalbugten = 1*a
hvalbugtenByAirToKapstaden = 1*a
kabaloByAirToKapstaden = 1*a
kapGuardafuiByAirToTamatave = 1*a
kapGuardafuiByAirToVictoriasøen = 1*a
kapStMarieByAirToKapstaden = 1*a
kapstadenByAirToStHelena = 1*a
kapstadenByAirToTamatave = 1*a
marrakeshByAirToSierraLeone = 1*a
marrakeshByAirToTanger = 1*a
sierraLeoneByAirToStHelena = 1*a
suakinByAirToVictoriasøen = 1*a
tangerByAirToTripoli = 1*a

land = {'Addisabeba': {'Suakin': addisabebaByLandToSuakin, 'Kap Guardafui': addisabebaByLandToKapGuardafui, 'Victoriasøen': addisabebaByLandToVictoriasøen},
    'Cairo': {'Omdurman': cairoByLandByLandToOmdurman},
    'Congo': {'Luanda': congoByLandToLuanda, 'Slavekysten': congoByLandToSlavekysten, 'Wadai': congoByLandToWadai, 'Darfur': congoByLandToDarfur},
    'Bahar El Gazal': {'Darfur': baharByLandToElGazalDarfur, 'Victoriasøen': baharByLandToElGazalVictoriasøen},
    'Dakar': {'Marrakesh': dakarByLandToMarrakesh, 'Sierra Leone': dakarByLandToSierraLeone},
    'Darfur': {'Bahar El Gazal': baharByLandToElGazalDarfur,'Omdurman':darfurByLandToOmdurman, 'Suakin': darfurByLandToSuakin, 'Sahara': darfurByLandToSahara, 'Wadai': darfurByLandToWadai},
    'Dragebjerget': {'Mocambique': dragebjergetByLandToMocambique, 'Victoriafaldene': dragebjergetByLandToVictoriafaldene},
    'Guldkysten': {'Sierra Leone': guldkystenByLandToSierraLeone, 'Timbuktu': guldkystenByLandToTimbuktu},
    'Hvalbugten': {'Kapstaden': hvalbugtenByLandToKapstaden, 'Victoriafaldene': hvalbugtenByLandToVictoriafaldene},
    'Kabalo': {'Luanda': kabaloByLandToLuanda, 'Victoriasøen': kabaloByLandToVictoriasøen},
    'Kap Guardafui': {'Addisabeba': addisabebaByLandToKapGuardafui, 'Zanzibar': kapGuardafuiByLandToZanzibar},
    'Kapstaden': {'Hvalbugten': hvalbugtenByLandToKapstaden},
    'Luanda': {'Congo': congoByLandToLuanda, 'Kabalo': kabaloByLandToLuanda, 'Mocambique': luandaByLandToMocambique},
    'Marrakesh': {'Tanger': marrakeshByLandToTanger, 'Dakar': dakarByLandToMarrakesh},
    'Mocambique': {'Dragebjerget': dragebjergetByLandToMocambique, 'Luanda': luandaByLandToMocambique, 'Victoriasøen': mocambiqueByLandToVictoriasøen, 'Victoriafaldene': mocambiqueByLandToVictoriafaldene, 'Zanzibar': mocambiqueByLandToZanzibar},
    'Omdurman': {'Cairo': cairoByLandByLandToOmdurman, 'Darfur': darfurByLandToOmdurman, 'Tripoli': omdurmanByLandToTripoli},
    'Sahara': {'Darfur': darfurByLandToSahara, 'Tanger': saharaByLandToTanger},
    'Sierra Leone': {'Dakar': dakarByLandToSierraLeone, 'Guldkysten': guldkystenByLandToSierraLeone, 'Timbuktu': sierraLeoneByLandToTimbuktu},
    'Slavekysten': {'Congo': congoByLandToSlavekysten, 'Timbuktu': slavekystenByLandToTimbuktu, 'Wadai': slavekystenByLandToWadai},
    'Suakin': {'Addisabeba': addisabebaByLandToSuakin, 'Darfur': darfurByLandToSuakin},
    'Tanger': {'Marrakesh': marrakeshByLandToTanger, 'Sahara': saharaByLandToTanger, 'Tunis': tangerByLandToTunis},
    'Timbuktu': {'Guldkysten': guldkystenByLandToTimbuktu, 'Sierra Leone': sierraLeoneByLandToTimbuktu, 'Slavekysten': slavekystenByLandToTimbuktu},
    'Tripoli': {'Omdurman': omdurmanByLandToTripoli, 'Tunis': tripoliByLandToTunis},
    'Tunis': {'Tanger': tangerByLandToTunis, 'Tripoli': tripoliByLandToTunis},
    'Victoriafaldene': {'Addisabeba': addisabebaByLandToVictoriasøen, 'Bahar El Gazal': baharByLandToElGazalVictoriasøen, 'Dragebjerget': dragebjergetByLandToVictoriafaldene, 'Hvalbugten': hvalbugtenByLandToVictoriafaldene, 'Kabalo': kabaloByLandToVictoriasøen},
    'Victoriasøen': {'Addisabeba': addisabebaByLandToVictoriasøen, 'Bahar El Gazal': baharByLandToElGazalVictoriasøen, 'Kabalo': kabaloByLandToVictoriasøen},
    'Wadai': {'Congo': congoByLandToWadai, 'Darfur': darfurByLandToWadai, 'Slavekysten': slavekystenByLandToWadai},
    'Zanzibar': {'Kap Guardafui': kapGuardafuiByLandToZanzibar, 'Mocambique': mocambiqueByLandToZanzibar}
}

sea = {'Cairo': {'Tunis': cairoBySeaToTunis, 'Suakin': cairoBySeaToSuakin},
    'Dakar': {'De Kanariske Øer': dakarBySeaToDeKanariskeØer, 'Sierra Leone': dakarBySeaToSierraLeone, 'St Helena': dakarBySeaToStHelena},
    'De Kanariske Øer': {'Dakar': dakarBySeaToDeKanariskeØer, 'Tanger': tangerBySeaToDeKanariskeØer},
    'Guldkysten': {'Hvalbugten': guldkystenBySeaToHvalbugten, 'Sierra Leone': guldkystenBySeaToSierraLeone, 'Slavekysten': guldkystenBySeaToSlavekysten},
    'Hvalbugten': {'Guldkysten': guldkystenBySeaToHvalbugten, 'Kapstaden': hvalbugtenBySeaToKapstaden, 'St Helena': hvalbugtenBySeaToStHelena, 'Slavekysten': hvalbugtenBySeaToSlavekysten},
    'Kap Guardafui': {'Suakin': kapGuardafuiBySeaToSuakin, 'Tamatave': kapGuardafuiBySeaTamatave, 'Mocambique': kapGuardafuiBySeaMocambique},
    'Kap St Marie': {'Kapstaden': kapStMarieBySeaToKapstaden, 'Mocambique': kapStMarieBySeaToMocambique},
    'Kapstaden': {'St Helena': kapstadenBySeaToStHelena, 'Hvalbugten': hvalbugtenBySeaToKapstaden, 'Kap St Marie': kapStMarieBySeaToKapstaden},
    'Mocambique': {'Kap Guardafui': kapGuardafuiBySeaMocambique, 'Kap St Marie': kapStMarieBySeaToMocambique},
    'Slavekysten': {'Guldkysten': guldkystenBySeaToSlavekysten, 'Hvalbugten': hvalbugtenBySeaToSlavekysten},
    'Tanger': {'De Kanariske Øer': tangerBySeaToDeKanariskeØer, 'Tunis': tangerBySeaToTunis},
    'Tunis': {'Cairo': cairoBySeaToTunis, 'Tanger': tangerBySeaToTunis},
    'Tamatave': {'Kap Guardafui': kapGuardafuiBySeaTamatave},
    'Sierra Leone': {'Dakar': dakarBySeaToSierraLeone, 'Guldkysten': guldkystenBySeaToSierraLeone, 'St Helena': sierraLeoneBySeaToStHelena},
    'St Helena': {'Dakar': dakarBySeaToStHelena, 'Hvalbugten': hvalbugtenBySeaToStHelena, 'Kapstaden': kapstadenBySeaToStHelena, 'Sierra Leone': sierraLeoneBySeaToStHelena},
    'Suakin': {'Cairo': cairoBySeaToSuakin, 'Kap Guardafui': kapGuardafuiBySeaToSuakin}
}

air = {'Cairo': {'Suakin': cairoByAirToSuakin},
    'Darfur': {'Kabalo': darfurByAirToKabalo, 'Suakin': darfurByAirToSuakin, 'Tripoli': darfurByAirToTripoli},
    'Dragebjerget': {'Kapstaden': dragebjergetByAirToKapstaden, 'Victoriasøen': dragebjergetByAirToVictoriasøen},
    'Guldkysten': {'Luanda': guldkystenByAirToLuanda, 'Marrakesh': guldkystenByAirToMarrakesh, 'Tripoli': guldkystenByAirToTripoli, 'Hvalbugten': guldkystenByAirToHvalbugten},
    'Hvalbugten': {'Guldkysten': guldkystenByAirToHvalbugten, 'Kapstaden': hvalbugtenByAirToKapstaden},
    'Kabalo': {'Darfur': darfurByAirToKabalo, 'Kapstaden': kabaloByAirToKapstaden},
    'Kap St Marie': {'Kapstaden': kapStMarieByAirToKapstaden},
    'Kapstaden': {'Dragebjerget': dragebjergetByAirToKapstaden, 'Hvalbugten': hvalbugtenByAirToKapstaden, 'Kabalo': kabaloByAirToKapstaden, 'Kap St Marie': kapStMarieByAirToKapstaden, 'St Helena': kapstadenByAirToStHelena, 'Tamatave': kapstadenByAirToTamatave},
    'Kap Guardafui': {'Tamatave': kapGuardafuiByAirToTamatave, 'Victoriasøen': kapGuardafuiByAirToVictoriasøen},
    'Luanda': {'Guldkysten': guldkystenByAirToLuanda, 'Hvalbugten': guldkystenByAirToHvalbugten},
    'Marrakesh': {'Guldkysten': guldkystenByAirToMarrakesh, 'Sierra Leone': marrakeshByAirToSierraLeone, 'Tanger': marrakeshByAirToTanger},
    'Sierra Leone': {'Marrakesh': marrakeshByAirToSierraLeone, 'St Helena': sierraLeoneByAirToStHelena},
    'St Helena': {'Kapstaden': kapstadenByAirToStHelena, 'Sierra Leone': sierraLeoneByAirToStHelena},
    'Suakin': {'Cairo': cairoByAirToSuakin, 'Darfur': darfurByAirToSuakin, 'Victoriasøen': suakinByAirToVictoriasøen},
    'Tamatave': {'Kapstaden': kapstadenByAirToTamatave, 'Kap Guardafui': kapGuardafuiByAirToTamatave},
    'Tanger': {'Marrakesh': marrakeshByAirToTanger, 'Tripoli': tangerByAirToTripoli},
    'Tripoli': {'Darfur': darfurByAirToTripoli, 'Guldkysten': guldkystenByAirToTripoli, 'Tanger': tangerByAirToTripoli},
    'Victoriasøen': {'Dragebjerget': dragebjergetByAirToVictoriasøen, 'Kap Guardafui': kapGuardafuiByAirToVictoriasøen, 'Suakin': suakinByAirToVictoriasøen}
}
