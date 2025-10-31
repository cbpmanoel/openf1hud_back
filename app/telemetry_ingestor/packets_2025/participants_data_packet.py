import ctypes
from enum import IntEnum
from .common import ON_OFF_SETTING, PacketStructureBase, MAX_CARS


class AI_CONTROLLED(IntEnum):
    """
    Enumeration for AI controlled status.
    """
    HUMAN = 0
    AI = 1


class DRIVER_ID(IntEnum):
    """
    Enumeration for driver IDs.
    """
    CARLOS_SAINZ = 0
    DANIEL_RICCIARDO = 2
    FERNANDO_ALONSO = 3
    FELIPE_MASSA = 4
    LEWIS_HAMILTON = 7
    MAX_VERSTAPPEN = 9
    NICO_HULKENBURG = 10
    KEVIN_MAGNUSSEN = 11
    SERGIO_PEREZ = 14
    VALTTERI_BOTTAS = 15
    ESTEBAN_OCON = 17
    LANCE_STROLL = 19
    ARRON_BARNES = 20
    MARTIN_GILES = 21
    ALEX_MURRAY = 22
    LUCAS_ROTH = 23
    IGOR_CORREIA = 24
    SOPHIE_LEVASSEUR = 25
    JONAS_SCHIFFER = 26
    ALAIN_FOREST = 27
    JAY_LETOURNEAU = 28
    ESTO_SAARI = 29
    YASAR_ATIYEH = 30
    CALLISTO_CALABRESI = 31
    NAOTA_IZUMI = 32
    HOWARD_CLARKE = 33
    LARS_KAUFMANN = 34
    MARIE_LAURSEN = 35
    FLAVIO_NIEVES = 36
    KLIMEK_MICHALSKI = 38
    SANTIAGO_MORENO = 39
    BENJAMIN_COPPENS = 40
    NOAH_VISSER = 41
    GEORGE_RUSSELL = 50
    LANDO_NORRIS = 54
    CHARLES_LECLERC = 58
    PIERRE_GASLY = 59
    ALEXANDER_ALBON = 62
    RASHID_NAIR = 70
    JACK_TREMBLAY = 71
    AYRTON_SENNA = 77
    GUANYU_ZHOU = 80
    JUAN_MANUEL_CORREA = 83
    MICHAEL_SCHUMACHER = 90
    YUKI_TSUNODA = 94
    AIDAN_JACKSON = 102
    JENSON_BUTTON = 109
    DAVID_COULTHARD = 110
    OSCAR_PIASTRI = 112
    LIAM_LAWSON = 113
    RICHARD_VERSCHOOR = 116
    ENZO_FITTIPALDI = 123
    MARK_WEBBER = 125
    JACQUES_VILLENEUVE = 126
    CALLIE_MAYER = 127
    LOGAN_SARGEANT = 132
    JACK_DOOHAN = 136
    AMAURY_COREDEL = 137
    DENNIS_HAUGER = 138
    ZANE_MALONEY = 145
    VICTOR_MARTINS = 146
    OLIVER_BEARMAN = 147
    JAK_CRAWFORD = 148
    ISACK_HADJAR = 149
    ROMAN_STANEK = 152
    KUSH_MAINI = 153
    BRENDON_LEIGH = 156
    DAVID_TONIZZA = 157
    JARNO_OPMEER = 158
    LUCAS_BLAKELEY = 159
    PAUL_ARON = 160
    GABRIEL_BORTOLETO = 161
    FRANCO_COLAPINTO = 162
    TAYLOR_BARNARD = 163
    JOSHUA_DURKSEN = 164
    ANDREA_KIMI_ANTONELLI = 165
    RITOMO_MIYATA = 166
    RAFAEL_VILLAGOMEZ = 167
    ZAK_OSULLIVAN = 168
    PEPE_MARTI = 169
    SONNY_HAYES = 170
    JOSHUA_PEARCE = 171
    CALLUM_VOISIN = 172
    MATIAS_ZAGAZETA = 173
    NIKOLA_TSOLOV = 174
    TIM_TRAMNITZ = 175
    LUCA_CORTEZ = 185
    NETWORK_HUMAN = 255
    
    def __str__(self):
        return self.name.replace("_", " ").title()


class TEAM_ID(IntEnum):
    """
    Enumeration for team IDs.
    """
    MERCEDES = 0
    FERRARI = 1
    RED_BULL_RACING = 2
    WILLIAMS = 3
    ASTON_MARTIN = 4
    ALPINE = 5
    RB = 6
    HAAS = 7
    MCLAREN = 8
    SAUBER = 9
    F1_GENERIC = 41
    F1_CUSTOM_TEAM = 104
    KONNERSPORT = 129
    APXGP_24 = 142
    APXGP_25 = 154
    KONNERSPORT_24 = 155
    ART_GP_24 = 158
    CAMPOS_24 = 159
    RODIN_MOTORSPORT_24 = 160
    AIX_RACING_24 = 161
    DAMS_24 = 162
    HITECH_24 = 163
    MP_MOTORSPORT_24 = 164
    PREMA_24 = 165
    TRIDENT_24 = 166
    VAN_AMERSFOORT_RACING_24 = 167
    INVICTA_24 = 168
    MERCEDES_24 = 185
    FERRARI_24 = 186
    RED_BULL_RACING_24 = 187
    WILLIAMS_24 = 188
    ASTON_MARTIN_24 = 189
    ALPINE_24 = 190
    RB_24 = 191
    HAAS_24 = 192
    MCLAREN_24 = 193
    SAUBER_24 = 194


class NATIONALITY_ID(IntEnum):
    """
    Enumeration for driver nationality IDs.
    """
    
    AMERICAN = 1
    ARGENTINEAN = 2
    AUSTRALIAN = 3
    AUSTRIAN = 4
    AZERBAIJANI = 5
    BAHRAINI = 6
    BELGIAN = 7
    BOLIVIAN = 8
    BRAZILIAN = 9
    BRITISH = 10
    BULGARIAN = 11
    CAMEROONIAN = 12
    CANADIAN = 13
    CHILEAN = 14
    CHINESE = 15
    COLOMBIAN = 16
    COSTA_RICAN = 17
    CROATIAN = 18
    CYPRIOT = 19
    CZECH = 20
    DANISH = 21
    DUTCH = 22
    ECUADORIAN = 23
    ENGLISH = 24
    EMIRIAN = 25
    ESTONIAN = 26
    FINNISH = 27
    FRENCH = 28
    GERMAN = 29
    GHANAIAN = 30
    GREEK = 31
    GUATEMALAN = 32
    HONDURAN = 33
    HONG_KONGER = 34
    HUNGARIAN = 35
    ICELANDER = 36
    INDIAN = 37
    INDONESIAN = 38
    IRISH = 39
    ISRAELI = 40
    ITALIAN = 41
    JAMAICAN = 42
    JAPANESE = 43
    JORDANIAN = 44
    KUWAITI = 45
    LATVIAN = 46
    LEBANESE = 47
    LITHUANIAN = 48
    LUXEMBOURGER = 49
    MALAYSIAN = 50
    MALTESE = 51
    MEXICAN = 52
    MONEGASQUE = 53
    NEW_ZEALANDER = 54
    NICARAGUAN = 55
    NORTHERN_IRISH = 56
    NORWEGIAN = 57
    OMANI = 58
    PAKISTANI = 59
    PANAMANIAN = 60
    PARAGUAYAN = 61
    PERUVIAN = 62
    POLISH = 63
    PORTUGUESE = 64
    QATARI = 65
    ROMANIAN = 66
    SALVADORAN = 68
    SAUDI = 69
    SCOTTISH = 70
    SERBIAN = 71
    SINGAPOREAN = 72
    SLOVAKIAN = 73
    SLOVENIAN = 74
    SOUTH_KOREAN = 75
    SOUTH_AFRICAN = 76
    SPANISH = 77
    SWEDISH = 78
    SWISS = 79
    THAI = 80
    TURKISH = 81
    URUGUAYAN = 82
    UKRAINIAN = 83
    VENEZUELAN = 84
    BARBADIAN = 85
    WELSH = 86
    VIETNAMESE = 87
    ALGERIAN = 88
    BOSNIAN = 89
    FILIPINO = 90


class PLAYER_UDP_SETTING(IntEnum):
    """
    Enumeration for player's UDP telemetry settings.
    """
    RESTRICTED = 0
    PUBLIC = 1


class PLAYER_SHOW_ONLINE_NAMES_SETTING(ON_OFF_SETTING): ...


class PLAYER_PLATFORM(IntEnum):
    """
    Enumeration for player's platform.
    """
    STEAM = 1
    PLAYSTATION = 3
    XBOX = 4
    ORIGIN = 6
    UNKNOWN = 255


class LiveryColour(PacketStructureBase):
    """
    Structure representing the RGB livery colour of a participant.
    """
    
    _fields_ = [
        ("red", ctypes.c_uint8),    # Red component of the livery colour
        ("green", ctypes.c_uint8),  # Green component of the livery colour
        ("blue", ctypes.c_uint8),   # Blue component of the livery colour
    ]


class ParticipantData(PacketStructureBase):
    """
    Structure representing participant data.
    """
    MAX_NAME_LENGTH = 32
    MAX_CAR_COLOURS = 4

    _fields_ = [
        ("ai_controlled", ctypes.c_uint8),                  # Whether the vehicle is AI (1) or Human (0) controlled
        ("driver_id", ctypes.c_uint8),                      # Driver id (DRIVER_ID)
        ("network_id", ctypes.c_uint8),                     # Network id - unique identifier for network players
        ("team_id", ctypes.c_uint8),                        # Team id (TEAM_ID)
        ("my_team", ctypes.c_uint8),                        # My team flag - 1 = My Team, 0 = otherwise
        ("race_number", ctypes.c_uint8),                    # Race number of the car
        ("nationality", ctypes.c_uint8),                    # Nationality of the driver (NATIONALITY_ID)
        ("name", ctypes.c_char * MAX_NAME_LENGTH),          # Name of participant in UTF-8 format - null terminated
        ("your_telemetry", ctypes.c_uint8),                 # The player's UDP setting (PLAYER_UDP_SETTING)
        ("show_online_names", ctypes.c_uint8),              # The player's show online names setting (PLAYER_SHOW_ONLINE_NAMES_SETTING)
        ("tech_level", ctypes.c_uint16),                    # F1 World tech level
        ("platform", ctypes.c_uint8),                       # Player's platform (PLAYER_PLATFORM)
        ("num_colours", ctypes.c_uint8),                    # Number of colours valid for this car
        ("livery_colours", LiveryColour * MAX_CAR_COLOURS), # Colours for the car
    ]


class ParticipantsDataPacket(PacketStructureBase):
    """
    This is a list of participants in the race. If the vehicle is controlled by AI, then the name will be the
    driver name. If this is a multiplayer game, the names will be the Steam Id on PC, or the LAN name if
    appropriate.
    
    N.B. on Xbox, the names will always be the driver name, on PlayStation the name will be the LAN
    name if playing a LAN game, otherwise it will be the driver name.
    
    The array should be indexed by vehicle index.
    
    Frequency: Every 5 seconds
    Size: 1284 bytes
    Version: 1
    """

    _fields_ = [
        ("num_active_cars", ctypes.c_uint8),            # Number of active participants in the session
        ("participants", ParticipantData * MAX_CARS),   # Array of participant data
    ]