# places suggesting Chatbot - PlacesNearMe
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
 
 bot: The places that are close to your zipcode are as follows ["Eugene O'Neill National Historic Site", 'John Muir National Historic Site', 'Juan Bautista de Anza National Historic Trail', 'Lassen Volcanic National Park', 'Lava Beds National Monument', 'Muir Woods National Monument', 'Pinnacles National Park', 'Point Reyes National Seashore', 'Port Chicago Naval Magazine National Memorial', 'Redwood National and State Parks', 'Rosie the Riveter WWII Home Front National Historical Park', 'Tule Lake National Monument', 'Whiskeytown National Recreation Area', 'Yosemite National Park']
 
 user: more about these places
 
 bot: I am still working on this. for now you can find about them on NPS https://www.nps.gov/index.htm
 
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
 
 bot: What is your first name?
 
 user: akhila
 
 bot: I'll remember your first name akhila!. What is your last name?
 
 user: puppala
 
 bot: I'll remember your last name puppala!. what is your feedback?
 
 user: improve
 
 bot: I'll remember your feedback as love!
can I save your data into my database? if yes say |save it|
 
 user: save it
 
 bot: Thanks for the valuable feedback.
 
 user: repeat my feedback
 
 bot: your first name is akhila
 your last name is puppala
 your feedback is improve
 
 Screen Shot of my database that saved the feedback:
<img width="618" alt="Screen Shot 2022-04-25 at 10 32 55 AM" src="https://user-images.githubusercontent.com/73505100/165182385-7f029149-8af6-4485-9361-f24a21a53924.png">
 
 
