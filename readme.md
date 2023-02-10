#NCPD Punk B.U.S.T.R.
##-powered by WorldSat

###What is this?
Due to the large number of crimes committed in Night City 'on the reg', NCPD has teamed up with WorldSat (the leading and only provider of 'Net services) to create a global repository on all denizens of Night City, with or without a SIN.

###But why?
Just like the hit short story, 'Minority Report', predicting crime is a careful and delicate science that requires thousands of man-hours, tens of thousands of people, and a subjigated and willing populace. Because nearly none of those things exist in Night City, NCPD is relying on AI to profile NC citizens and catalogue their lives, property, and social circles. You say it's unethical, we say so is crime!

###Am I in danger?
Yes! Every second at least 100 rounds of ammunition is fired in Night City. The only way to guarentee your safety and expedite the judicial execution process is to cooperate with NCPD and their retainer 'rent-a-cops'. Failure to provide proof of innocence can and will lead to, at best a lead pill to the head, or at worst a night in the slammer. Remember! It is up to you to prove your innocence, especially when our 'Punk' B.U.S.T.R. program finds you guilty.

#Okay for real, what is this?
Punk Buster is a character management program for Cyberpunk 2020. It is meant to easily keep track of your character, manage cash and humanity, and allow for easy export.

It doesn't do any of that right now. Lots of groundwork and time not playing video games has been spent trying to design a TUI program that fits my standards. Once my BS is sorted, I intend to allow homebrew rules and easy expandability.

##Goals
###CP2020 Core Book
- Please note that copyrighted material cannot be legally downloaded or distributed. The files provided are extendable for your own custom content, homebrew, or official use. If you want the copyright material in there, you gotta put it in there.


###Generic Character Sheet with Automation
- I want to allow for different character growth types with generic IP as well as skill+stat use IP growth
- I really want to be able to save and load a character sheet, that doesn't work yet
- An easy export to PDF. No clue how tf to do that!

###Character Creation Tool
- Look, lifepath is the biggest slog. I want to make an easy way to roll a life path, modify it, and finalize it.
- Need an easy way to know what stats do and which roles have which skills and what skills even do whatever.

`This whole thing is a work in progress. When it's freakin' perfect, with complete CP2020 + character creation + character sheet management + export, I'll slap a 1.0 on it. Otherwise each version will be a functional slice.

Each release will try to be backwards compatible with old saves.

Each release will be 'stable'

Each release will be stand-alone (as in it will work even if some automation or features aren't implemented yet)`

#You want to help?
I dunno, do bug reports or something. Man I'm not even at a point where the code looks good. That character.py file is almost 2000 lines long because I'm too lazy to break it out into multiple files.

Feel free to fork and merge and change stuff. But please wait for a stable release before commiting to this repo.

When it is published on Replit or whatever, feel free to donate to keep the project going.

###Had a cool idea -> make it almost all agnostic except for the UI so I can have a Terminal, Tkinter, and other types of interfaces

Would require a rewrite but that's fine. We'd lambda basic functions out to the framework's specifics.
So we would standardize the entire program (which means each framework would need the same type of widgets).
Then the class can simply dictate how to run it and the python file itself would only be handling the framework.
Very longterm type of goal. Let's just get something functional first.