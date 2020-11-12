# Backend for the character generation explorer. This is where the actual generation takes place and where data is stored.

# TO DO:
# expand this for even more character traits. Personality traits, life goals, vices, occupations, etc.
# expand and adapt this for more societies in Nebhos. e.g Tocharians, Uighurs, Hans.
# currently names can have 3 syllables only: expand this to allow more flexibility. 2 to 4 seems reasonable.

# "veiled" is a specifiable attribute here because of the setting of Nebhos, the Taklamakan desert.
# it can indicate desert-walkers' garb (merchants, pilgrims) or religious garb.

import random


# storage for appearance
appearance_male = {"hair": ("extremely long", "cropped short", "balding", "shoulder-length", "long and braided",
                            "tied in a topknot", "tied in a ponytail", "short and braided", "wild", "long and loose",
                            "long and parted", "shoulder-length and parted", "long and messy", "tightly curled",
                            "long and frizzy", "tied in a long braid", "long and ornamented"),

                   "haircolour": ("black", "grey", "greying", "auburn", "golden", "brown", "chestnut", "black", "black",
                                  "brown", "auburn", "brown", "ashen", "charcoal", "stone-grey", "white", "snow-white"),

                   "eyes": ("big and round", "small and narrow", "almond-shaped", "asymmetrical", "old and wise",
                            "deep and piercing", "saturnine", "melancholic", "sanguine"),

                   "eyecolour": ("hazel", "blue", "steel", "grey", "brown", "dark brown", "light green", "light blue",
                                 "black", "bloodshot"),

                   "nose": ("tall and prominent", "dainty", "small and round", "small and upturned", "large and hooked",
                            "short and wide", "tall and narrow", "grecian", "roman"),

                   "mouth": ("thin and pursed", "locked in a permanent scowl", "delicate", "rosebud-like", "wide", "average"),

                   "jaw": ("wide and prominent", "square-shaped", "tall and narrow", "chiseled", "soft and rounded"),

                   "skin": ("dark and sun-dried", "fair and supple", "dark and supple", "wrinkled", "mottled",
                            "light and freckled", "pallid", "bone-white"),

                   "build": ("lithe", "limber", "athletic", "toned", "muscular", "bear-like", "gaunt", "slender", "lean",
                             "stocky", "stout", "brawny", "athletic", "toned", "muscular", "gaunt", "gaunt", "lean",
                             "lean"),

                   "height": ("extremely tall", "very short", "short", "tall", "average-height", "average-height",
                              "average-height", "average-height", "average-height", "average-height", "tall", "tall",
                              "tall"),
                   }

appearance_female = {"hair": ("extremely long", "cropped short", "shoulder-length", "long and braided",
                              "tied in a topknot", "tied in a ponytail", "short and braided", "wild", "long and loose",
                              "long and parted", "shoulder-length and parted", "long and messy", "tightly curled",
                              "long and frizzy", "tied in a long braid", "long and ornamented", "lush and fragrant"),

                     "haircolour": ("black", "grey", "greying", "auburn", "golden", "brown", "chestnut", "black", "black",
                                    "brown", "auburn", "brown", "ashen", "charcoal", "stone-grey", "white", "snow-white"),

                     "eyes": ("big and round", "small and narrow", "almond-shaped", "asymmetrical", "old and wise",
                              "deep and piercing", "saturnine", "melancholic", "sanguine"),

                     "eyecolour": ("hazel", "blue", "steel", "grey", "brown", "dark brown", "light green", "light blue",
                                   "black", "bloodshot"),

                     "nose": ("tall and prominent", "dainty", "small and round", "small and upturned", "large and hooked",
                              "short and wide", "tall and narrow", "average", "grecian", "roman"),

                     "mouth": ("thin and pursed", "in a permanent scowl", "delicate", "rosebud-like", "wide", "average",
                               "full-lipped"),

                     "jaw": ("wide and prominent", "square-shaped", "tall and narrow", "chiseled", "soft and rounded"),

                     "skin": ("dark and sun-dried", "fair and supple", "dark and supple", "wrinkled", "mottled",
                              "light and freckled", "pallid", "bone-white"),

                     "build": ("lithe", "limber", "athletic", "toned", "muscular", "bear-like", "gaunt", "slender", "lean",
                               "stocky", "buxom", "voluptuous", "stout", "brawny", "buxom", "slender", "slender", "slender", "toned",
                               "lithe", "lithe", "lithe"),

                     "height": ("extremely tall", "very short", "short", "short", "tall", "average-height",
                                "average-height", "average-height", "average-height", "average-height"),
                     }

# storage for names
prefix = ("Kar", "Ark", "Sam", "S", "K", "Er", "Sar", "Sci", "Scy", "Ger", "La", "Uel", "Hh", "Ll", "Ser")
root = ("awe", "un", "an", "on", "da", )
suffix_male = ("an", "ar", "er", "ar", "ur", "dur", "mo", "ent", "kal", "al", "alos", "alo", "aro", "ro")
suffix_female = ("na", "ne", "ane", "are", "ara", "ari", "ri", "re", "tha", "thae", "the", "rae")

#for convenience... not used at the moment
pregen_names_male = ("Arkwi", "Erkent", "Kaum", "Saumo", "Samudtar", "Gerlos", "Labhos", "Uelkelmos")
pregen_names_female = ("Karwene", "Lykaske", "Scirye", "Totka", "Sana", "Menje", "Ansna")

# make a raw list of appearance traits
def generate_raw_appearance(gender):

    if gender == "male":
        return random.choice(appearance_male["hair"]), random.choice(appearance_male["haircolour"]), \
               random.choice(appearance_male["eyes"]), random.choice(appearance_male["eyecolour"]), \
               random.choice(appearance_male["nose"]), random.choice(appearance_male["mouth"]), \
               random.choice(appearance_male["jaw"]), random.choice(appearance_male["skin"]), \
               random.choice(appearance_male["build"]), random.choice(appearance_male["height"]), \

    elif gender == "female":
        return random.choice(appearance_female["hair"]), random.choice(appearance_female["haircolour"]), \
               random.choice(appearance_female["eyes"]), random.choice(appearance_female["eyecolour"]), \
               random.choice(appearance_female["nose"]), random.choice(appearance_female["mouth"]), \
               random.choice(appearance_female["jaw"]), random.choice(appearance_female["skin"]), \
               random.choice(appearance_female["build"]), random.choice(appearance_female["height"]), \

    else:
        print("Error: No gender supplied to generate_appearance().")


# construct a name from the stored segments
def generate_name(gender):
    if gender == "male":
        name = "{0}{1}{2}".format(random.choice(prefix), random.choice(root), random.choice(suffix_male))
    elif gender == "female":
        name = "{0}{1}{2}".format(random.choice(prefix), random.choice(root), random.choice(suffix_female))
    return name


# create character object for storing these infos
class Character:
    def __init__(self, gender, veiled):

        self.gender = gender  # "male" or "female"
        self.veiled = veiled  # True or False
        self.name = generate_name(self.gender)
        self.trait_list = generate_raw_appearance(self.gender)
        self.hair = self.trait_list[0]
        self.haircolour = self.trait_list[1]
        self.eyes = self.trait_list[2]
        self.eyecolour = self.trait_list[3]
        self.nose = self.trait_list[4]
        self.mouth = self.trait_list[5]
        self.jaw = self.trait_list[6]
        self.skin = self.trait_list[7]
        self.build = self.trait_list[8]
        self.height = self.trait_list[9]

        # define appropriate pronouns
        if self.gender == "male":
            self.pronoun_0 = "he"
            self.pronoun_1 = "his"
            self.pronoun_2 = "him"
            self.noun = "man"
            self.noun_young = "boy"
        else:
            self.pronoun_0 = "she"
            self.pronoun_1 = "her"
            self.pronoun_2 = "her"
            self.noun = "woman"
            self.noun_young = "girl"

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def describe_appearance(self):
        if not self.veiled:
            return "The {0}, {1} {2}'s {4} hair is {5}. {3} skin is {6}.".format(self.height, self.build,
                                                                                               self.noun,
                                                                                               self.pronoun_1.capitalize(),
                                                                                               self.haircolour, self.hair,
                                                                                               self.skin)
        else:
            return self.describe_appearance_body_veiled()

    def describe_appearance_detail(self):

        if not self.veiled:
            return "The {0}'s {2} eyes are {3}. {1} nose is {4}. {1} mouth is {5}, and {7} jaw is {6}." \
                   "".format(self.noun, self.pronoun_1.capitalize(), self.eyecolour, self.eyes, self.nose, self.mouth,
                          self.jaw, self.pronoun_1)

        else:
            return self.describe_appearance_face_veiled()

    # don't call these last two functions directly, it's done automatically if the char is veiled or not.
    def describe_appearance_face_veiled(self):
        return "This individual's face is veiled. Their {0} eyes are {1}.".format(self.eyecolour, self.eyes)

    def describe_appearance_body_veiled(self):
        return "This {0} individual is covered head-to-toe with myriad fabrics.".format(self.height)


# make a list of character objects based on user parameters

def generate_characters(n_to_make=10, gender_ratio=0.5, veiled_ratio_m=0.2, veiled_ratio_f=0.4):
    # <n_to_make : int, specify the number of characters to generate.
    # <gender_ratio> : float, specify the rough ratio of male to female. 0.9 = 90% male
    # <veiled_ratio_m/f> : float, specify the rough ratio of veiled characters to non-veiled. 0.2 = 20% veiled.

    chars_list = []

    for i in range(n_to_make):
        first_rand = random.random()
        second_rand = random.random()

        if first_rand < gender_ratio and second_rand < veiled_ratio_m:
            char = Character("male", True)
        elif first_rand < gender_ratio and second_rand > veiled_ratio_m:
            char = Character("male", False)
        elif first_rand > gender_ratio and second_rand < veiled_ratio_f:
            char = Character("female", True)
        elif first_rand > gender_ratio and second_rand > veiled_ratio_f:
            char = Character("female", False)

        chars_list.append(char)

    return chars_list


def generate_single_character(gender, veiled):
    # make a single random character, with specified gender and veil/no veil.
    char = Character(gender, veiled)
    return char


