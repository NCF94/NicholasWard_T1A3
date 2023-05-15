# NicholasWard_T1A3

## GitHub

[GitHub Repo Link](https://github.com/NCF94/NicholasWard_T1A3)

---

## Presentaion Video

[Presentation Video Link]()

---

## Features

- User can set weekly goals they want to achieve.
- The user will have the ability to view their goals.
- The user will have the ability to add to their goal list.
- The user will have the ability to remove goals from their goal list.
- The user will be able to tick off the goals as they complete them.
- The user will be able to receive a score for their current progress.

Goals examples could be:
drink 2 litres of water a day
Get 8 hours sleep a night
Go to gym 3 times
Eat 3 meals a day
Read 10 pages of a book
10,000 steps per day
Etc…

- App will also have a bodyweight tracker.
- The user can input their body weight each week.
- The user can remove bodyweight if mistake was made.
- The user can view their whole list of weekly bodyweight entrys.
- The user can change their "pass/fail" mark, so when they view there bodyweight list. It will say if you are higher or lower then last week.

---

## Styling Guide

The styling guide I am following is Pep8.

### Styling guide reference

Guido van Rossum , Barry Warsaw , Nick Coghlan (05/07/2001) - PEP 8 – Style Guide for Python Code <https://peps.python.org/pep-0008/>.

---

## Implementaion Plan

To manage my implementaion plan, I have decided to use Trello. This will make it easier for me track my progress, and break down the creation of mt terminal app to small steps.
Here is a screen shot of my Trello Board:

![Trello Board](./docs/Trello%20Board.png)

Here you can see I have created a bunch of cards and ordered them in term of priority. Each card has a "due date", a title, a brief description of what is required and a checklist.
Below is an example of one of my cards:

![Trello Card](./docs/Trello%20card.png)

To view my whole Trello board, please click the link below.

[Here is the link to my trello page.](https://trello.com/invite/b/ly5gTvBj/ATTIa59517c6ae71ca88dbad99bf581075f8211A7952/terminal-app)

---

## Help Documentation  

### Hardware Requirements  

This application was made and tested on a Macbook Air M1.

### How to download and use the Wellness App.
  
Step 1:  
First off you want to by downloading the terminal application off of GitHub. Here is a guide on how do download a GitHub respository. <https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives>
  
Step 2:  
Then once you have downloaded the application, you want to open your terminal.  
On a Mac computer, you want to press Command and space, then search for Terminal and open it.  
On a Windows computer, you want to click on the search bar and type in Windows Terminal. Click to open the terminal.

Step 3:  
Now we want to open the folder that the application is in, to do this we want to find the file location. Simply search for the application on your computer "NicholasWard_T1A3". Make sure to move your application folder to the desktop.  
Now in your terminal, you need to navigate to the appplication folder. You can do this by typing

``` bash
cd/Desktop/NicholasWard_T1A3/src
```

This will take you to the folder where you can run the app from.

Step 4:  
Now we need to check your compiter has the correct version of python. To do this, I have written a script so you will just need to type in the terminal

```bash
./check.sh
```

  If you have Python 3.#.# then you can proceed. If you dont have python 3, or dont have python installed click the link on how to update/install it. <https://www.python.org/downloads/>

Step 5:
Okay now we get to run the app, this is quite simple. In the terminal you need to type

``` bash
./run.sh
```

Congratulations, you can now use the Wellness App!!!

### App instructions

Now the application is running, lets go through how to use it.  

You will be shown a menu, ranging from 1 - 10. Each number has a different use. Simply read the options availiable and type the corressponding number, then hit enter.

Option 1: Enter 1 to VIEW this weeks wellness goals. This is where you can view the goals you have input, and see wether they are complete or not.  

 
Option 2: Enter 2 to MARK a goal as complete. This is where you can mark your goals as complete.


Option 3: Enter 3 to ADD your own weekly goal. Here you can add your weekly goals to the list. Try keep these a short as possible, this will make marking and removing them easier.

Option 4: Enter 4 to REMOVE a weekly goal. This is where you remove your goals from the list when the week is over, or you made a mistake.

Option 5: Enter 5 to VIEW your weekly score. Your weekly score will score you on how many goals are completed out of the number of goals on your list.

Option 6: Enter 6 to ADD this weeks bodyweight. Here you can add your body weight for the week. Simple enter your weight in kgs (e.g 80kgs), the app will automatically input the date for you so you can keep track.

Option 7: Enter 7 to VIEW previous weeks bodyweight. This option will alow you to view your previous weights you have entered so you can track your progress.

Option 8: Enter 8 to MARK last weeks weight if it was lower than the previous weeks. Here you can mark your bodyweight lower then last weeks. This will depend on your goals.

Option 9: Enter 9 to REMOVE a bodyweight. This option will allow you to remove a bodyweight in the case of a mistake, or if you simply want to remove a bodyweight. All  you have to do is enter your weight (e.g 80kgs).

Option 10: Enter 10 to EXIT. Finally we have the EXIT option, by entering 10 the app will close.

Enjoy!!