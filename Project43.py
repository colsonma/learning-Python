#!/usr/bin/env python
#First Python Project

from sys import exit
from random import randint
    
class Engine(object):
 
 def __init__(self, scene_map):
     print "Engine __init__ has scene_map", scene_map
     self.scene_map = scene_map
    
 def play(self):
     current_scene = self.scene_map.opening_scene()
     print "Play's first scene", current_scene
     
     while True:
        print "\n--------"
        next_scene_name = current_scene.enter()
        print "next scene", next_scene_name
        current_scene = self.scene_map.next_scene(next_scene_name)
        print "map returns new scene", current_scene

class Player(object):
    pass

class Scene(object):
    
    def enter(self):
        print "Scene info"
        exit(1)
    
class Building(Scene):
    
    def enter(self):
        print "You wake up in a strange office building with a raging headache"
        print "like you have been on a week long bender. You hear moaning coming"
        print "from all around you. You try to recall what it was you did last night"
        print "when it hits you like a ton of bricks. ZOMBIES!"
        print "You have to make it to the top floor of this building and find the Boss"
        print "Zombie and defeat him. This means you have to get the cure from the second "
        print "floor it's in a broom closet with a numeric key pad."
        print "/n"
        print "You shakily stand up, a female zombie lumbers towards you, she stands between"
        print "you and the elevators."
        
        action = raw_input("> ")
        
        if action == "hit her in the head":
         print "Oh silly player, zombies are stronger than you. She grabs your hand and bites you"
         print "you fall to the floor and start to shake, the transformation has started."
         return 'Death'
         
        elif action == "run past her":
         print "Despite your drunken stupor you move like a cheetah, maybe it's"
         print "the adrenaline. Either way you make it to the elevator, mash the button and"
         print "the door slides open and you fall in quickly closing the door behind you."
         print "You hit 2 and the elevator begins to raise."
         return 'Second_Floor'
         
        elif action == "throw something":
         print "You pick up a stapler and toss it at the zombie, unbeknownst to you"
         print "before meeting her untimely fate this zombie was a world class hackysacker."
         print "She hacks and sacks the stapler and kicks it back at your head where it deeply"
         print "embeds."
         return 'Death'
         
        elif action == "help":
            print "You can 'hit her in the head', 'run past her' or 'throw something'"
            return 'Building'
    
        else:
            print "What are you doing?"
            return 'Building'
    
class Second_Floor(Scene):
    def enter(self):
        print "The doors open on the second floor and you step out."
        print "The air is thick with smoke, you get down and crawl towards the broom closet"
        print "You raise yourself up and You have to guess what the 3 digit"
        print "pattern is but you don't have much time air is quickly running out."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad\>]")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "Beep! Beep! Beep! BZZD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The door opens you grab the cure and race back to the elevator."
            print "You hit the up button and the doors ding open you jump on and hit floor 3"
            return 'Third_Floor'
        
        else:
            print "The door won't open, the smoke is too thick now, you can't breathe."
            return 'Death'
        

class Boss(Scene):
        def enter(self):
            print "You arrive at the third floor, and walk into the Boss' office. He is huge, and"
            print "smells of elderberries. He looks at you and begins to charge. He is fast!"
            action = raw_input("> ")
            
            if action == "use the cure":
             print "You use the cure on yourself, you feel better about yourself."
             print "Sadly the Boss is uneffected and tears you limb from limb."
             return 'Death'
            
            elif action == "throw cure at the boss":
                print "You toss the vile at the boss who jumps at it like a bass on a"
                print "warm spring night. The vile smashes in his decaying teeth and you"
                print "see a change, the boss slowly transforms into Arnold."
                print "He turns to you and says, 'Get out of here get to the choppa now'"
                return 'Winner'
            
            elif action == "help":
                print "You can 'use the cure', 'throw cure at the boss'"
                return 'Boss'
            
            else:
                print "What are you doing?"
                return 'Boss'
            
class Winner(Scene):
        def enter(self):
            print "You find an access hatch to the roof, where a chopper is waiting for you!"
            print "You jump on board and are whisked safely away to a tropical island."
            print "Congratulations your mom was right you are a winner!"
            return 'finished'
            exit(1)

    
class Death(Scene):
     jokes = [
        "You've died, tell St. Peter I said hi.",
        "Wow, are you even trying?",
        "Are you paying attention?",
        "Come on Son!"
        ]
      
     
     def enter(self):
        print Death.jokes[randint(0, len(self.jokes)-1)]
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene
     
      
        

class Map(object):
    
    scenes = {
        'Building': Building(),
        'Second_Floor': Second_Floor(),
        'Boss': Boss(),
        'Winner': Winner(),
        'Death': Death()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene
    
    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('Building')
a_game = Engine(a_map)
a_game.play()
