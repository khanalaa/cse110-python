
print("Adventure Game\n")

print('''      %\            %\
                  %% \          %% \           
                 %%   \        %%   \         
                %%%    \      %%%    \       
               %%%      \    %%%      \     
              %%%%       \  %%%%       \   
             %%%%         \%%%%         \ 
            %%%%%         %%%%%          \ 
           %%%%%       .-%%%%%,---------------.           
                     .'.'     |  Welcome to   |           
                  .-' /       | Adventure game|
              _.-'   :        `-------++------'
         .--'"       `.               ||
       ,'              `-._           ||       By_Aayush
      :                    `--..._____||_________
      :           
      `.           
      ''')

choice1 = input("You are walking through a dark forest and find two items:\
a MATCH and a FLASHLIGHT. Which one do you want to pick up?\n").lower()

if (choice1 == "match"):
    choice_m = input("You pick up the match and strike it, and for an instant, the forest around you is illuminated.\
You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?\n").lower()
    if (choice_m == "run"):
        choice_run = input("\nYou can either head for the RIVER, hoping water deters the bear, or climb the HILL to gain elevation and evade it.\n").lower()
        if (choice_run == "hill"):
            print("\nGame Over!!! From the top of the hill you fell down.")
        elif (choice_run == "river"):
            print("\nGame Over!!! You wade into the cold water, and the bear hesitates, but you drowned.")
        else:
            print("\nGame Over!!! Wrong input")
    if (choice_m == "hide"):
        choice_hide = input("You can either hide in the CAVE, hoping the bear won't find you, or climb the TREE, hoping it can't reach you.\n").lower()
        if (choice_hide == "cave"):
            print("\nGame Over!!! The bear finds you. And you are dead.")
        elif(choice_hide == "tree"):
            print("\nGame Over!!! You fell off the tree.")
        else:
             print("\nGame Over!!! Wrong input")

elif (choice1 == "flashlight"):
    choice_f = input("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, \
but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees \
for the thing that made the noise?\n").lower()
    if choice_f == "follow":
        choice_follow = input("You decide to follow the path, flashlight piercing the darkness. The safe, marked trail leads deeper into the forest. CONTINUE, STOP, or EXAMINE?\n").lower()
        if choice_follow == "continue":
            print("\nYou win!!! You proceed along the path, finding a serene clearing under the starry sky.")
        elif choice_follow == "stop":
            print("\nGame over!!! You pause, listening to distant sounds and bear finds you.")
        elif choice_follow == "examine":
            print("\nYou scan the ground, discovering fresh bear track and bear finds you.")
        else:
            print("\nGame Over!!! Wrong input")
    if choice_f == "look":
        choice_look = input("Curiosity leads you to look in the trees. Your flashlight reveals glowing eyes—a raccoon. OBSERVE, APPROACH, or SHINE your flashlight?\n").lower()
        if choice_look == "observe":
            print("\nGame Over!!! You quietly watch the raccoon and bear attacked you from behind.")
        elif choice_look == "approach":
            print("\nGame Over!!! You cautiously approach but cannot win the battle with bear. ")
        elif choice_look == "shine":
            print("\nGame Over!!! You use your flashlight to check for other animals and saw tiger.")
        else:
            print("\nGame Over!!! Wrong input")
else:
    print("\nGame Over!!! You are dead")