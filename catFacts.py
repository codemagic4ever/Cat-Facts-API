#importing the necessary libraries
import tkinter as tk
import requests

#creating a function called get_cat_fact which tries to fetch a response from the given API website
def get_cat_fact():
    try:
        response = requests.get("https://catfact.ninja/fact")
        response.raise_for_status()
        #the response is saved as json data
        data = response.json()
        #we want specifically the fact from all the info provided so we call that
        fact = data["fact"]
        fact_label.config(text=fact)
    #if there are any exceptions to the response then it will result in an error
    except requests.exceptions.RequestException as e:
        fact_label.config(text="Error fetching cat fact")
        print(f"Error fetching cat fact: {e}")

# set up a tkinter window

window = tk.Tk()
window.title("Cat Facts")

#create a label to display cat fact
fact_label = tk.Label(window, text= "Click the button to get a cat fact", wraplength= 400, font=("Arial", 12))

#pack allows to add the widget to the window
#padding of 20 pixels
fact_label.pack(pady=20)

#create a button that calls the API when clicked
get_fact_button = tk.Button(window, text= "Get Cat Fact", command= get_cat_fact)
get_fact_button.pack(pady=10)

#start the tkinter event loop
window.mainloop()
