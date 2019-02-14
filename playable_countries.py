countries = [
    ["America","Teddy Roosevelt"],
    ["Arabia","Saladin"],
    ["Australia","John Curtin"],
    ["Aztec","Montezuma"],
    ["Brazil","Pedro II"],
    ["China","Qin Shi Huang"],
    ["Egypt","Cleopatra"],
    ["England","Queen Victoria"],
    ["France","Catherine de'Medici"],
    ["Germany","Frederick Barbossa"],
    ["Greece","Gorgo"],
    ["Greece","Perciles"],
    ["India","Gandhi"],
    ["Indonesia","Gitarja"],
    ["Japan","Hojo Tokimune"],
    ["Khmer","Jayavarman"],
    ["Kongo","Mvemba a Nzinga"],
    ["Macedon","Alexander the Great"],
    ["Norway","Harald Hardrada"],
    ["Nubia","Amanitore"],
    ["Persia","Cyrus II"],
    ["Poland","Jadwiga"],
    ["Rome","Trajan"],
    ["Russia","Peter"],
    ["Scythia","Tomyris"],
    ["Spain","Philip II"],
    ["Sumeria","Gilgamesh"]
]

countries_rise_and_fall = [
    ["Cree","Poundmaker"],
    ["The Netherlands(Dutch)","Wilhelmina"],
    ["Georgia","Tamar"],
    ["India","Chandragupta"],
    ["Korea","Seondeok"],
    ["Mapuche","Lautaro"],
    ["Mongolia","Genghis Khan"],
    ["Scottland","Robert the Bruce"],
    ["Zulu","Shaka"]
]

countries_global_storm = [
    ["Canada","Wilfrid Laurier"],
    ["England","Elanor of Aquitaine"],
    ["France","Elanor of Aquitaine"],
    ["Hungary","Matthias Corvinus"],
    ["Inca","Pachauti"],
    ["Mali","Mansa Musa"],
    ["Maori","Kupe"],
    ["Ottoman","Suleiman"],
    ["Phonecia","Dido"],
    ["Sweden","Kristina"]
]

def get_countries(rise_and_fall=False, global_storm=False, all_expansions=False):
    """
    Returns a list of the standard countries. Parameters can be set to cherry pick or include all expansion countries
    Args: rise_and_fall=False, global_storm=False, all_expansions=False
    Returns, list[['country', 'name']]
    """
    included = countries
    if rise_and_fall or all_expansions:
        for e in countries_rise_and_fall:
            included.append(e)
    if global_storm or all_expansions:
        for e in countries_global_storm:
            included.append(e)
    return included
