# Followers Scraper

## _**Introduction**_

This program is intended to print out a list of Instagram users that do not follow you back. This program does so using Selenium and without any unlicensed APIs, making this procedure compliant with Instagram's terms of service.

## _**Prerequisties**_

Before running this program, make sure you have Python 3.10 installed and configured to your PATH variable, as well as have the browser Google Chrome and Selenium's chromedriver installed and configured. 

## _**Running**_

To run this program, type

``` 
python3 main.py
```

In your terminal. It will then prompt you for your username and password, which you should type into the terminal and proceed to press Enter once finished.

## _**Procedure**_

Once the username and password has been entered, this program will open Chrome and navigate to Instagram, and will then proceed to log into the user's account. From there, the program will navigate to the user's profile, and proceed to parse the number of followers the user has as well as how many other users the user is following. 

The program will then add the names of all followers into a set, and once that has been completed, the program will then proceed to add the names of all following into another set. Finally, the program will iterate through the following set to print out the usernames of any users who don't follow the user back. 

## _**Other Notes**_
- Do not move your cursor from the screen while the program is running. If you do so, you must quit the program, as it will continuosly try to scroll down. 

## _**Known Issues and Bugs**_

- For users with Highlight reels, the XPath for getting the number of followers/following seems to be different than for users without Highlight reels. Currently, this program only supports users with Highlight reels, however this can be changed in the future.
- Performance can be further optimized, with an algorithm that changes the interval time in which the sets are updated.

For any further questions or issues, you can reach me at zhendahu@gmail.com 
