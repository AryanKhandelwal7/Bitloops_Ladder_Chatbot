# Bitloops Chatbot
The provided repository is developed by Aryan Khandelwal, who was an intern under the Ladder Internship's fall cohort of 2024. The primary purpose of this rep. is to provide all the files that were created during the making of the AI chatbot for Bitloops. The rep. consists of two main files :

1. app.py : Python file consisting the code of the chatbot
2. index.html : The UI - widget of the chatbot

To whomever reading this readme file, if you want to implement the same chatbot within your system and continue to develop it, I have provided the instructions on how I achieved this feat through this file. In case any issues arise, please feel free to contact me at aryan.fall2024@gmail.com in order to rectify any issues that persist.

# Step-by-Step Guide

**STEP 1** : __USE OpenAI's PLAYGROUND AND DEVELOP AN API KEY__

Upon developing this chatbot, it involved the usage of OpenAI's ChatGPT and it acted as the basic framework at the back-end. To import ChatGPT within your python code, you need to create an API key to have a tested ChatGPT for your personal usage. A key fact to remember is that you need to spend a minimum of $2 [Through this process, I spent $10, and realize that it was too much for its use at this state] in order to enable the incorporation of the GPT model within your code.

Please note that as this will be used for a public website where thousands of people will visit and use the chatbot, you need to adjust the amount spent accordingly on the GPT. Also, please note that this is not ChatGPT+, the instructions to do so are the following:

Go to https://platform.openai.com/chat-completions --> Upon visiting your dashboard, click the "API keys" section and create your own API key --> Upon its completion, go on to the "Usage" section and click on "Increase limit" --> Follow all the steps and proceed towards payment [For starters, I would recommend spending only $2]

**STEP 2 : COPY AND PASTE YOUR API KEY ONTO THE APP.PY FILE**

Once you have created your own OpenAI API key, copy the same and paste it within the app.py section where it is showcased as follows:

![image](https://github.com/user-attachments/assets/b771f79c-d3de-42fe-96aa-5c26c6364b67)

**STEP 3 : CREATION OF FOLDERS**

Once you have the HTML & the Python file set and complete, you wil need to organize them in a certain directory to avoid any errors & ensure a smooth run of the program. Please keep in mind that **all the file names should be kept the same for the entire duration. In case you are changing their names, please keep in mind to edit the corresponding code as well to avoid any errors.**

Upon having both your files (app.py & index.html), create a folder named as **"my-flask-app"** and store both the files within them. Once done, create a sub-folder named as "**templates**" and store the index.html file ONLY.   

Once done, you will now be able to run your .py file smoothly and ensure no errors.

**STEP 4 : RUN THE FILE**

After completing all the steps, you will be able to effectively run the file and utilize your own chatbot.

# ADDITIONAL NOTES

- Remember to use the same file / folder names for the entire duration. If the name is changed, please make sure to update the file's name in the corresponding code. (eg. if app.py is renamed as app23.py, make sure to update its name in index.html)
- To make the chatbot tailored for a different use, you can change the prompt that is displayed in the "system_msg" within the app.py code. 
