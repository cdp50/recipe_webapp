from django.shortcuts import render
import requests
# Create your views here.
# Home of my Functions. 
# admin.site.register("name of the model")


def get_recipe_id (request):
    if request.method == "POST":
        g_key = "7c8a7ecdbb68451f85463ff992469769"
        byui_key = "5a5313fdf6874562957e3fc267ae46cf"
    # how do I get the input from the user? using the request.POST will give me a dictionary with the form
        ingredients = request.POST["ingredients"].replace(" ","")
        url = "https://api.spoonacular.com/recipes/findByIngredients?ingredients="+ingredients+"&number=1&apiKey="+byui_key
    # is this how I should fetch data from the API? looks like it
        server_data_id = requests.get(url).json()
        print(server_data_id)
        print(url)
        id = server_data_id[0]["id"]
        # get_recipe_img(id)
        img_url = "https://api.spoonacular.com/recipes/"+str(id)+"/card?apiKey="+byui_key
        server_data_img = requests.get(img_url).json()
        recipe_img = {"recipe_img" : server_data_img["url"]}
        print(server_data_img)
        return render(request, "recipes/display_recipes.html", recipe_img) # this data word has to be a dictionary so I have to save the result in a dictionary
    return render(request, "recipes/display_recipes_home.html", {})

def get_random_recipe_id(request):
    if request.method == "POST":
        g_key = "7c8a7ecdbb68451f85463ff992469769"
        byui_key = "5a5313fdf6874562957e3fc267ae46cf"
        url = "https://api.spoonacular.com/recipes/random?number=1&apiKey="+byui_key
        server_data_id = requests.get(url).json()
 
        print(server_data_id["recipes"][0]["id"])
        id = server_data_id["recipes"][0]["id"] #this is giving the id fine
        img_url = "https://api.spoonacular.com/recipes/"+str(id)+"/card?apiKey="+byui_key
        server_data_img = requests.get(img_url).json()
        print("server_data")
        print("server_data")
        print("server_data")
        print("server_data")
        print("server_data")
        print("server_data")
        print("server_data")
        print(server_data_img["url"])
        recipe_img = {"recipe_img" : server_data_img["url"]}
        return render(request, "recipes/display_random_recipe.html", recipe_img)
    return render(request, "recipes/display_random_home.html", {})
    # How do I show to the user this results?





    # def get_recipe_img(id):
#     g_key = "7c8a7ecdbb68451f85463ff992469769"
#     byui_key = "5a5313fdf6874562957e3fc267ae46cf"
#     img_url = "https://api.spoonacular.com/recipes/"+id+"/card?apiKey="+g_key
#     server_data = requests.get(img_url).json()
#     recipe_img = server_data.url
    # how do I show the image to the user?
    # and how can I make it smaller?







