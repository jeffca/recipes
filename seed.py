import csv

from recipes.models import Recipe
i = 1
with open('recipes.csv', 'rb') as csvfile:
    csvreader = csv.reader(x.replace('\0', '') for x in csvfile)
    for row in csvreader:
        if row[0] != 'recipe':
            print row
            Recipe.create(id=i,
                          recipe=row[0],
                          ingredients=row[3],
                          instructions=row[5],
                          menuimgurl=row[15],
                          category=row[16])
            i+=1
#
# Recipe.create(recipe="Rice pudding",
#               ingredients="3/4 cup uncooked white rice;2 cups milk, divided;1/3 cup white sugar;1/4 teaspoon salt;1 egg, beaten;2/3 cup raisins;1 tablespoon butter;1/2 teaspoon vanilla extract;",
#               instructions="In a medium saucepan, bring 1 1/2 cups water to a boil. Add rice and stir. Reduce heat,cover and simmer for 20 minutes. In another saucepan, combine the cooked rice, with 1 1/2 cups milk, sugar and salt. Cook over medium heat until thick and creamy, 15 to 20 minutes. Stir in remaining 1/2 cup milk, beaten egg and raisins. Cook 2 minutes more, stirring constantly. Remove from heat, and stir in butter and vanilla. Serve warm.",
#               menuimgurl="http://www.sprinklesomesugar.com/wp-content/uploads/2014/04/IMG_5063-2.jpg")
#
# Recipe.create(recipe="French onion soup",
#               ingredients="6 tablespoons butter; 4 large yellow onions, sliced and separated into rings; 1 tablespoon white sugar; 2 cloves garlic, minced; 1/2 cup cooking sherry; 7 cups reduced-sodium beef broth; 1 teaspoon sea salt, or to taste; 1/4 teaspoon dried thyme; 1 bay leaf; 8 slices of French bread; 1/2 cup shredded Gruyere cheese; 1/3 cup shredded Emmental cheese; 1/4 cup freshly shredded Parmesan cheese",
#               instructions="Heat butter in a large, heavy pot over medium-high heat; cook and stir onions until they become translucent, about 10 minutes. Sprinkle onions with sugar; reduce heat to medium. Cook, stirring constantly, until onions are soft and browned, at least 30 minutes. Stir in garlic and cook until fragrant, about 1 minute. Stir sherry into onion mixture and scrape bottom of pot to dissolve small bits of browned food from the pot. Transfer onions into a slow cooker and pour in beef broth. Season to taste with sea salt; stir in thyme and bay leaf. Cover cooker, set on High, and cook 4 to 6 hours. If desired, set on Low and cook 8 to 10 hours. About 10 minutes before serving, set oven rack about 8 inches from the heat source and preheat the oven's broiler. Arrange bread slices on a baking sheet. Broil bread slices until toasted, 1 to 2 minutes per side. Combine Gruyere, Emmental, Parmesan, and mozzarella cheeses in a bowl, tossing lightly. Fill oven-safe soup crocks 3/4 full of onion soup and float a bread slice in each bowl. Top with about 2 tablespoons of cheese mixture per serving. Place filled bowls onto a baking sheet and broil until cheese topping is lightly browned and bubbling, about 2 minutes.",
#               menuimgurl="http://162.61.226.249/PicOriginal/P63382612080903_5.jpg")
#
# Recipe.create(recipe="Grilled cheese",
#               ingredients="sourdough bread; gouda cheese; tomato slices; jalapenos; pickles",
#               instructions="brush oil onto the bottom of the panini press. heat the pan with oil then heat the plate. add butter to the bread. slice cheese, jalapeno and tomato slices onto the bread. combine the bread into the pan. cover the top of the sandwich with the plate. flip over. wait 2 minutes to cool",
#               menuimgurl="https://jalapenogalswayoflivingdotcom.files.wordpress.com/2013/11/grilled-cheese-tomato-soup.jpg")
#
