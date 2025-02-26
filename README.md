# Cat-Facts-API

The Cat Facts App is a simple yet fun desktop application that fetches random cat facts from an API (https://catfact.ninja/fact). -- The website will call its API and access a cat fact from their server and return json data which includes the fact and length. In this case, we are only retrieving the fact.

# Features:
* Fetches random cat facts from the CatFact API (https://catfact.ninja/fact)
* Displays the fact dynamically in the application window
* Simple button-based interaction for fetching new facts
* User-friendly Tkinter GUI with a clean and minimalistic design

# Technologies Used:
* Python
* Tkinter (for GUI)
* Requests (for API calls)

# How It Works:
* The user must run the python file like usual.
* The app initializes a Tkinter window titled "Cat Facts".
* When the user clicks the "Get Cat Fact" button:
   1. A request is sent to the CatFact API.
   2. If successful, a random cat fact is extracted from the response and displayed.
   3. If the request fails, an error message is displayed instead.
* The user can click the button repeatedly to receive new facts.
