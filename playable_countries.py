countries = [
    {"name":"America",   "leader":"Teddy roosevelt",      "image_path":"assets/teddy.png"},
    {"name":"Arabia",    "leader":"Saladin",              "image_path":"assets/saladin.png"},
    {"name":"Australia", "leader":"John Curtin",          "image_path":"assets/john.png"},
    {"name":"Aztec",     "leader":"Montezuma",            "image_path":"assets/montezuma.png"},
    {"name":"Brazil",    "leader":"Pedro II",             "image_path":"assets/pedro.png"},
    {"name":"China",     "leader":"Qin Shi Huang",        "image_path":"assets/qin_shi.png"},
    {"name":"Egypt",     "leader":"Cleopatra",            "image_path":"assets/cleopatra.png"},
    {"name":"England",   "leader":"Queen Victoria",       "image_path":"assets/victoria.png"},
    {"name":"France",    "leader":"Catherine de Medici",  "image_path":"assets/catherine.png"},
    {"name":"Germany",   "leader":"Frederick Barbarossa", "image_path":"assets/barbarossa.png"},
    {"name":"Greece",    "leader":"Gorgo",                "image_path":"assets/gorgo.png"},
    {"name":"Greece",    "leader":"Pericles",             "image_path":"assets/pericles.png"},
    {"name":"India",     "leader":"Gandhi",               "image_path":"assets/gandhi.png"},
    {"name":"Indonesia", "leader":"Gitarja",              "image_path":"assets/gitarja.png"},
    {"name":"Japan",     "leader":"Hojo Tokimune",        "image_path":"assets/hojo.png"},
    {"name":"Khmer",     "leader":"Jayavarman",           "image_path":"assets/jaya.png"},
    {"name":"Kongo",     "leader":"Mvemba a Nzinga",      "image_path":"assets/mvemba.png"},
    {"name":"Macedonia", "leader":"Alexander the Great",  "image_path":"assets/alex.png"},
    {"name":"Norway",    "leader":"Harald Hardrada",      "image_path":"assets/norway.png"},
    {"name":"Nubia",     "leader":"Amanitore",            "image_path":"assets/amani.png"},
    {"name":"Persia",    "leader":"Cyrus II",             "image_path":"assets/cyrus.png"},
    {"name":"Poland",    "leader":"Jadwiga",              "image_path":"assets/jadwiga.png"},
    {"name":"Rome",      "leader":"Trajan",               "image_path":"assets/trajan.png"},
    {"name":"Russia",    "leader":"Peter",                "image_path":"assets/peter.png"},
    {"name":"Scythia",   "leader":"Tomyris",              "image_path":"assets/tomyris.png"},
    {"name":"Spain",     "leader":"Philip II",            "image_path":"assets/philip.png"},
    {"name":"Sumeria",   "leader":"Gilgamesh",            "image_path":"assets/gilgamesh.png"}
]

countries_rise_and_fall = [
    {"name":"Cree",                      "leader":"Poundmaker",          "image_path":"assets/pound.png"},
    {"name":"The Netherlands(Dutch)",    "leader":"Wilhelmina",          "image_path":"assets/wilhelmina.png"},
    {"name":"Georgia",                   "leader":"Tamar",               "image_path":"assets/tamar.png"},
    {"name":"India",                     "leader":"Chandragupta",        "image_path":"assets/chandragupta.png"},
    {"name":"Korea",                     "leader":"Seondeok",            "image_path":"assets/seon.png"},
    {"name":"Mapuche",                   "leader":"Lautaro",             "image_path":"assets/lautaro.png"},
    {"name":"Mongolia",                  "leader":"Genghis Khan",        "image_path":"assets/khan.png"},
    {"name":"Scottland",                 "leader":"Robert de Bruce",     "image_path":"assets/bruce.png"},
    {"name":"Zulu",                      "leader":"Shaka",               "image_path":"assets/shaka.png"}
]

countries_global_storm = [
    {"name":"Canada",      "leader":"Wilfrid Laurier",       "image_path":"assets/wilfrid.png"},
    {"name":"England",     "leader":"Eleanor of Aquitaine",   "image_path":"assets/eleanor.png"},
    {"name":"France",      "leader":"Eleanor of Aquitaine",   "image_path":"assets/eleanor.png"},
    {"name":"Hungary",     "leader":"Matthias Corvinys",     "image_path":"assets/matthias.png"},
    {"name":"Inca",        "leader":"Pachacuti",              "image_path":"assets/pacha.png"},
    {"name":"Mali",        "leader":"Mansa Musa",            "image_path":"assets/mansa.png"},
    {"name":"Maori",       "leader":"Kupe",                  "image_path":"assets/kupe.png"},
    {"name":"Ottoman",     "leader":"Suleiman",              "image_path":"assets/suleiman.png"},
    {"name":"Phonecia",    "leader":"Dido",                  "image_path":"assets/dido.png"},
    {"name":"Sweden",      "leader":"Kristina",              "image_path":"assets/kristina_auf_sverige.png"}
]

def get_countries(rise_and_fall=False, global_storm=False, all_expansions=False):
    """
    Returns a list of the standard countries. Parameters can be set to cherry pick or include all expansion countries
    Args: rise_and_fall=False, global_storm=False, all_expansions=False
    Returns, list[['name', 'name']]
    """
    included = countries
    if rise_and_fall or all_expansions:
        for e in countries_rise_and_fall:
            included.append(e)
    if global_storm or all_expansions:
        for e in countries_global_storm:
            included.append(e)
    return included
