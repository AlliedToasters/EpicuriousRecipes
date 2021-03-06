def get_categories(cats):
    """takes a list of categories and returns a list of
    meta-categories to help categorize each recipe by type.
    Returns a list.
    Access to categories is available via special inputs.
    if string 'get_keys' is passed as argument, returns list of meta-categories.
    if string 'get_dict' is passed as argument, returns the entire dictionary of
    meta-categories and the categories that belong to them.
    """
    categories = {
        'alcohol': [
            'campari',
            'ginger',
            'eau de vie',
            'vodka',
            'vermouth',
            'digestif',
            'non-alcoholic',
            'pernod',
            'sake',
            'triple sec',
            'chambord',
            'chartreuse',
            'champagne',
            'kirsch',
            'kahlúa',
            'bourbon',
            'marsala',
            'port',
            'sparkling wine',
            'grand marnier',
            'sherry',
            'red wine',
            'white wine',
            'grappa',
            'breadcrumbs',
            'virginia',
            'mezcal',
            'spirit',
            'whiskey',
            'portland',
            'cognac/armagnac',
            'midori',
            'amaretto',
            'bitters',
            'rosé',
            'gin',
            'fortified wine',
            'butterscotch/caramel',
            'calvados',
            'alcoholic',
            'rum',
            'frangelico',
            'scotch',
            'west virginia',
            'liqueur',
            'aperitif',
            'brandy',
            'sangria',
            'cobbler/crumble',
            'wine',
            'tequila'
        ],
        'breakfast': [
            'muffin',
            'crêpe',
            'quiche',
            'breakfast',
            'waffle',
            'omelet',
            'brunch',
            'pancake'
        ],
        'cheese': [
            'cottage cheese',
            'tomatillo',
            'tomato',
            'brie',
            'cheddar',
            'swiss cheese',
            'monterey jack',
            'fontina',
            'gouda',
            'beer',
            'feta',
            'brine',
            'parmesan',
            'mozzarella',
            'marscarpone',
            'blue cheese',
            'cheese',
            'cream cheese',
            'goat cheese',
            'ricotta',
        ],
        'cities': [
            'cambridge',
            'london',
            'kansas city',
            'boston',
            'beverly hills',
            'hollywood',
            'new orleans',
            'miami',
            'providence',
            'yonkers',
            'louisville',
            'st. louis',
            'seattle',
            'healdsburg',
            'san francisco',
            'paris',
            'brooklyn',
            'portland',
            'pasadena',
            'dallas',
            'pittsburgh',
            'aspen',
            'columbus',
            'las vegas',
            'costa mesa',
            'los angeles',
            'denver',
            'washington, d.c.',
            'houston',
            'minneapolis',
            'atlanta',
            'lancaster',
            'long beach',
            'santa monica',
            'chicago'
        ],
        'countries': [
            'italy',
            'georgia',
            'new mexico',
            'jamaica',
            'france',
            'chile',
            'philippines',
            'spain',
            'mexico',
            'chile pepper',
            'egypt',
            'australia',
            'dominican republic',
            'germany',
            'switzerland',
            'canada',
            'ireland',
            'bulgaria',
            'england',
            'guam',
            'japan',
            'israel',
            'haiti',
            'peru'
        ],
        'dairy': [
            'mayonnaise',
            'dairy free',
            'ice cream machine',
            'milk/cream',
            'butterscotch/caramel',
            'peanut butter',
            'egg',
            'egg nog',
            'eggplant',
            'cream cheese',
            'buttermilk',
            'butternut squash',
            'dairy',
            'ice cream',
            'sour cream',
            'butter'
        ],
        'dessert': [
            'frozen dessert',
            'brownie',
            'pot pie',
            '#cakeweek',
            'soufflé/meringue',
            'ice cream machine',
            'dessert',
            'pie',
            'cookie',
            'ice cream',
            'iced coffee',
            'cake',
            'cupcake',
            'candy thermometer',
            'tart',
            'pancake',
            'phyllo/puff pastry dough',
            'candy',
            'coffee grinder',
            'crêpe',
            'cookies',
            'coffee',
            'custard',
            'pastry',
            'sorbet',
            'fritter'
        ],
        'dinner': [
            'salad dressing',
            'casserole/gratin',
            'stuffing/dressing',
            'frittata',
            'chili',
            'potato salad',
            'salad',
            'stock',
            'burrito',
            'pot pie',
            'dinner',
            'hamburger',
            'pizza',
            'soup/stew',
            'tortillas',
            'stew'
        ],
        'drinks': [
            'house cocktail',
            'martini',
            'mixer',
            'steam',
            'coffee grinder',
            'cocktail',
            'punch',
            'spritzer',
            'steak',
            'tea',
            'cocktail party',
            'drink',
            'smoothie',
            'westwood',
            'coffee',
            'iced tea',
            'iced coffee',
            'drinks',
            'margarita',
            'hot drink'
        ],
        'events': [
            'kosher for passover',
            'fall',
            'party',
            'labor day',
            'winter',
            "new year's eve",
            'buffet',
            'fourth of july',
            "new year's day",
            'parade',
            'diwali',
            'oscars',
            'super bowl',
            'thanksgiving',
            'graduation',
            'persian new year',
            'birthday',
            'kentucky derby',
            'spring',
            "valentine's day",
            'hanukkah',
            'potluck',
            'backyard bbq',
            'ramadan',
            'poker/game night',
            'mardi gras',
            'tailgating',
            "st. patrick's day",
            'cocktail party',
            'rosh hashanah/yom kippur',
            'cinco de mayo',
            'halloween',
            'sukkot',
            'kwanzaa',
            "mother's day",
            'flaming hot summer',
            'picnic',
            'pacific palisades',
            'game',
            'shower',
            'wedding',
            'christmas',
            'family reunion',
            'friendsgiving',
            'christmas eve',
            'engagement party',
            'easter',
            'lunar new year',
            'summer',
            'passover',
            'oktoberfest',
            'purim',
            'anniversary',
            'back to school',
            'shavuot',
            'bastille day',
            'camping'
        ],
        'foods': [
            'soy free',
            'dip',
            'vinegar',
            'yogurt',
            'stock',
            'biscuit',
            'pot pie',
            'pizza',
            'omelet',
            'flat bread',
            'tortillas',
            'pickles',
            'muffin',
            'salad dressing',
            'cranberry sauce',
            'casserole/gratin',
            'frittata',
            'salad',
            'food processor',
            'potato salad',
            'sourdough',
            'burrito',
            'breadcrumbs',
            'salsa',
            'soy sauce',
            'sandwich theory',
            'windsor',
            'chili',
            'soy',
            'soup/stew',
            'hummus',
            'stew',
            'bread',
            'stuffing/dressing',
            'seafood',
            'freezer food',
            'sandwich',
            'sauce',
            'hamburger',
            'taco'
        ],
        'fruit': [
            'tangerine',
            'currant',
            'raisin',
            'lemon',
            'fruit juice',
            'quince',
            'apricot',
            'apple juice',
            'honeydew',
            'pineapple',
            'tomato',
            'kiwi',
            'pomegranate juice',
            'lemongrass',
            'melon',
            'tropical fruit',
            'plum',
            'cranberry sauce',
            'fruit',
            'lemon juice',
            'lime juice',
            'passion fruit',
            'guava',
            'asian pear',
            'persimmon',
            'date',
            'cranberry',
            'raspberry',
            'grapefruit',
            'prune',
            'berry',
            'blueberry',
            'dried fruit',
            'orange juice',
            'kumquat',
            'coconut',
            'lychee',
            'blackberry',
            'strawberry',
            'nectarine',
            'watermelon',
            'apple',
            'papaya',
            'cherry',
            'pear',
            'banana',
            'pomegranate',
            'lingonberry',
            'cantaloupe',
            'mango',
            'orange',
            'peach',
            'citrus',
            'lime',
            'fig',
            'grape'
        ],
        'grains': [
            'rice',
            'semolina',
            'brown rice',
            'cornmeal',
            'rye',
            'oatmeal',
            'quinoa',
            'hominy/cornmeal/masa',
            'barley',
            'bulgur',
            'wild rice',
            'bran',
            'oat',
            'goat cheese',
            'grains',
            'granola',
            'whole wheat',
            'corn'
        ],
        'greens': [
            'lettuce',
            'watercress',
            'radicchio',
            'broccoli rabe',
            'broccoli',
            'rutabaga',
            'brussel sprout',
            'mustard greens',
            'spinach',
            'celery',
            'chard',
            'leafy green',
            'cabbage',
            'bok choy',
            'kale'
        ],
        'herbs_spices': [
            'ginger',
            'mint',
            'bell pepper',
            'oregano',
            'spice',
            'poppy',
            'dill',
            'tarragon',
            'caraway',
            'clove',
            'coriander',
            'chile pepper',
            'vanilla',
            'horseradish',
            'saffron',
            'sesame oil',
            'fennel',
            'cumin',
            'herb',
            'curry',
            'parsley',
            'sesame',
            'cinnamon',
            'rosemary',
            'thyme',
            'anise',
            'hot pepper',
            'basil',
            'cilantro',
            'pepper',
            'sage',
            'nutmeg',
            'cardamom',
            'poblano',
            'mustard',
            'paprika'
        ],
        'instructions': [
            'chill',
            'bake',
            'pan-fry',
            'mixer',
            'grill',
            'double boiler',
            'ramekin',
            'boil',
            'juicer',
            'side',
            'stir-fry',
            'wok',
            'blender',
            'slow cooker',
            'skewer',
            'food processor',
            'broil',
            'smoker',
            'deep-fry',
            'grill/barbecue',
            'mandoline',
            'marinate',
            'steam',
            'sauté',
            'microwave',
            'candy thermometer',
            'mortar and pestle',
            'flaming hot summer',
            'shower',
            'roast',
            'freeze/chill',
            'fry',
            'coffee grinder',
            'marinade',
            'pressure cooker',
            'rub',
            'simmer',
            'braise',
            'poach',
            'epi loves the microwave'
        ],
        'jewish': [
            'kosher for passover',
            'rosh hashanah/yom kippur',
            'passover',
            'kosher',
            'purim',
            'hanukkah',
            'sukkot',
            'shavuot'
        ],
        'legumes': [
            'bean',
            'chickpea',
            'tamarind',
            'lentil',
            'sugar snap pea',
            'lima bean',
            'green bean',
            'legume',
            'pea',
            'peanut'
        ],
        'lunch': [
            'mayonnaise',
            'soup/stew',
            'mustard greens',
            'lunch',
            'mustard',
            'pickles'
        ],
        'meat': [
            'beef shank',
            'veal',
            'chambord',
            'duck',
            'bacon',
            'champagne',
            'pork',
            'brisket',
            'poultry',
            'lamb',
            'sausage',
            'rabbit',
            'ground lamb',
            'pork chop',
            'pork tenderloin',
            'lamb shank',
            'ground beef',
            'prosciutto',
            'lamb chop',
            'beef rib',
            'meatloaf',
            'poultry sausage',
            'goose',
            'chicken',
            'venison',
            'steak',
            'rack of lamb',
            'meatball',
            'ham',
            'quail',
            'meat',
            'hamburger',
            'pork rib',
            'beef',
            'beef tenderloin',
            'buffalo'
        ],
        'misc_descrip': [
            'kosher for passover',
            'edible gift',
            'paleo',
            'one-pot meal',
            'weelicious',
            'organic',
            '30 days of groceries',
            'healthy',
            'bon appétit',
            'high fiber',
            '#cakeweek',
            'quick and healthy',
            'condiment/spread',
            'gourmet',
            'condiment',
            'self',
            'tested & improved',
            'harpercollins',
            'bon app��tit',
            'advance prep required',
            'entertaining',
            'kid-friendly',
            'cookbooks',
            'epi + ushg',
            '22-minute meals',
            'cookbook critic',
            '#wasteless',
            'quick & easy',
            'kitchen olympics',
            'house & garden',
            'freezer food',
            'kosher',
            'cook like a diner',
            '3-ingredient recipes',
            'frankenrecipe',
            'kidney friendly',
            'epi loves the microwave',
            'leftovers'
        ],
        'nos': [
            'tree nut free',
            'peanut free',
            'dairy free',
            'soy free',
            'low sodium',
            'sugar conscious',
            'strawberry',
            'vegetarian',
            'wheat/gluten-free',
            'low fat',
            'caraway',
            'low cal',
            'no sugar added',
            'low carb',
            'vegan',
            'no-cook',
            'raw',
            'low sugar',
            'low cholesterol',
            'fat free',
            'pescatarian'
        ],
        'nuts': [
            'tree nut free',
            'hazelnut',
            'chestnut',
            'coconut',
            'seed',
            'peanut butter',
            'butternut squash',
            'macadamia nut',
            'nut',
            'pine nut',
            'almond',
            'cashew',
            'peanut',
            'nutmeg',
            'pistachio',
            'walnut',
            'tree nut'
        ],
        'pasta': [
            'noodle', 
            'couscous', 
            'lasagna', 
            'pasta', 
            'orzo', 
            'pasta maker'
        ],
        'people': [
            'nancy silverton',
            'suzanne goin',
            'emeril lagasse',
            'anthony bourdain'
        ],
        'seafood': [
            'caviar',
            'swordfish',
            'crab',
            'squid',
            'shrimp',
            'shellfish',
            'lobster',
            'bass',
            'cod',
            'oyster',
            'octopus',
            'anchovy',
            'trout',
            'salmon',
            'tilapia',
            'halibut',
            'mussel',
            'snapper',
            'sardine',
            'tuna',
            'seafood',
            'scallop',
            'clam',
            'fish'
        ],
        'snack': [
            'snack',
            'appetizer',
            'dip',
            'hummus',
            'snack week',
            "hors d'oeuvre"
        ],
        'states': [
            'washington',
            'iowa',
            'utah',
            'california',
            'georgia',
            'maryland',
            'illinois',
            'new mexico',
            'idaho',
            'rhode island',
            'maine',
            'nebraska',
            'ohio',
            'tennessee',
            'kansas city',
            'minnesota',
            'south carolina',
            'north carolina',
            'oklahoma',
            'alaska',
            'colorado',
            'arizona',
            'louisiana',
            'kentucky derby',
            'virginia',
            'hawaii',
            'wisconsin',
            'oregon',
            'pennsylvania',
            'new jersey',
            'missouri',
            'michigan',
            'florida',
            'new york',
            'new hampshire',
            'washington, d.c.',
            'connecticut',
            'indiana',
            'vermont',
            'kentucky',
            'west virginia',
            'texas',
            'alabama',
            'mississippi',
            'kansas',
            'massachusetts'
        ],
        'sweets': [
            'sugar conscious',
            'hazelnut',
            'maple syrup',
            'coffee grinder',
            'cr��me de cacao',
            'créme de cacao',
            'honeydew',
            'no sugar added',
            'low/no sugar',
            'honey',
            'jamaica',
            'coffee',
            'sugar snap pea',
            'molasses',
            'jam or jelly',
            'chocolate',
            'iced coffee',
            'low sugar',
            'phyllo/puff pastry dough'
        ],
        'veggies': [
            'yuca',
            'lettuce',
            'shallot',
            'ginger',
            'capers',
            'bell pepper',
            'endive',
            'butternut squash',
            'mushroom',
            'tomatillo',
            'tomato',
            'garlic',
            'arugula',
            'green onion/scallion',
            'cucumber',
            'asparagus',
            'lemongrass',
            'sweet potato/yam',
            'radicchio',
            'watercress',
            'radish',
            'broccoli rabe',
            'okra',
            'squash',
            'leek',
            'escarole',
            'collard greens',
            'potato salad',
            'broccoli',
            'root vegetable',
            'kale',
            'chive',
            'rutabaga',
            'olive',
            'mustard greens',
            'dorie greenspan',
            'zucchini',
            'parsnip',
            'horseradish',
            'fennel',
            'vegetable',
            'potato',
            'pumpkin',
            'turnip',
            'spinach',
            'parsley',
            'artichoke',
            'jícama',
            'beet',
            'avocado',
            'onion',
            'plantain',
            'cauliflower',
            'celery',
            'carrot',
            'cabbage',
            'jerusalem artichoke',
            'yellow squash'
        ]
    }
    if cats == 'get_keys':
        return categories.keys()
    if cats == 'get_dict':
        return categories
    result = []
    for key in categories.keys():
        for cat in cats:
            cat = cat.lower()
            if cat in categories[key]:
                result.append(key)
    return list(set(result))  #remove any duplicates  

