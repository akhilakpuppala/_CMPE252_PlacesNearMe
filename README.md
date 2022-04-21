# Travel Agent Chatbot - BoBo
By: Akhila Puppala

This chatbot is build using Rasa Platform

Rasa Installation:
https://rasa.com/docs/rasa/installation

Prequisites: 
* Visual Studio Code installed

### **How to set up this project:**
* Download the github project into your local system. 
* With in the created virtual environment:
  * Install Rasa using the dependencies found in the dependency.txt file
  * Optional: Install Rasa X (for better UI experience)
 ```
 pip3 install rasa-x --extra-index-url https://pypi.rasa.com/simple
 ```

### **How to run the chatbot:**
* open the virtual environment
  ```
  source venv/bin/activate
  ```
In the virtual environment, open the project and run the following commands on the terminal:
* Train the chatbot
  ```
  rasa train
  ```
* Open a separate terminal and start the action server
  ```
  rasa run actions
  ```
* Chat with the bot using rasa shell or rasa x
  ```
  rasa shell
  ```
  ```
  rasa x
  ```
* to run on Slack 
   ```
  rasa run
  ```
  go to the app section,select PlacesNearMe and start making conversation
 
 ## Conversation Flow 1: Suggest Places
 user: hi
 
 bot: Hi,welcome to PlacesNearMe. here are some questions you can ask me. i.tell me about you, ii.places near me, iii.give feedback, iv.what's the weather
 
 user: places near me
 
 bot: please provide your zipcode
 
 user: 95134
 
 bot: here are the list of places you can visit near you
 
 ## Conversation Flow 2: Weather forecast
 user: hi
 
 bot: Hi,welcome to PlacesNearMe. here are some questions you can ask me. i.tell me about you, ii.places near me, iii.give feedback, iv.what's the weather
 
 user: what's the weather
 
 bot: please provide your city name
 
 user: fremont
 
 bot: the weather is 20 celcius
 
  ## Conversation Flow 2: Provide feedback
 user: hi
 
 bot: Hi,welcome to PlacesNearMe. here are some questions you can ask me. i.tell me about you, ii.places near me, iii.give feedback, iv.what's the weather
 
 user: I would like to provide you feedback
 
 bot: please provide your first name
 
 user: akhila
 
 bot: please provide your last name
 
 user: puppala
 
 bot: please provide your feedback
 
 user: improve
 
 bot: can I save this feedback?
 
 user: save it
 
 bot: thank you
 
 user: repeat my feedback
 
 bot: your first name is akhila
 your last name is puppala
 your feedback is improve
 
 