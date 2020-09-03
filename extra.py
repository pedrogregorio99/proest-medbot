import random

JOKES_INPUTS = ("joke", "funny", "fun", "laugh")
JOKES_RESPONSES = ["I'm not Google.", "I'm not Alexa.", "I'm not Siri", "Friends, Season 5, Episode 16, 11:25.", "What do you get when you cross an alien and a chicken? Eggs-traterrestrial.",
"What do you get when you cross music and an automobile? Cartune.", "How do you throw a space party? You planet!", "Why don't scientists trust atoms? Because they make up everything!",
"Why did the gym close down? It just didn't work out!", "You know what I saw today? Everything I looked at.", "Where are average things manufactured? The satisfactory.", 
"Why was six afraid of seven? Because seven ate nine.", "How do trees get online? They just log on!", "Why did the orange stop? It ran out of juice!",
"What did 0 say to 8? Nice belt!", "I never make mistakes! I thought I did once but I was actually wrong.", "Why doesn't the sun go to college? Because it has a million degrees!",
"Why are skeletons so calm? Because nothing gets under their skin.", "What's red and moves up and down? A tomato in an elevator!", "A dyslexic man walks into a bra.",
"I went to buy some camouflage trousers the other day, but I couldn’t find any.", "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.", 
"I invented a new word! Plagiarism!", "Why don’t scientists trust atoms? Because they make up everything.", "Why don’t Calculus majors throw house parties? Because you should never drink and derive.",
"What did the left eye say to the right eye? Between you and me, something smells.", "What do you call a fake noodle? An impasta.", 
"What do you call a magic dog? A labracadabrador.", "What’s orange and sounds like a carrot? A parrot.", "How did Batman name his bathroom? The Batroom.", 
"Why did the M&M go to school? It wanted to be a Smartie."]

def joke(message):
    for word in message.split():
        if word.lower() in JOKES_INPUTS:
            return random.choice(JOKES_RESPONSES)

FACTS_INPUTS = ("random", "fact")
FACTS_RESPONSES = ["Some cats are allergic to people (same but don't tell anyone this).", "M&M stands for Mars and Murrie.", "Neil Armstrong didn't say 'That's one small step for man.'", 
"You can major in wine at Cornell University.", "About 700 grapes go into one bottle of wine.", "Fear of the number 13 is called triskaidekaphobia.", 
"Banging your head against a wall for one hour burns 150 calories, but PLEASE don't do that!", "Cherophobia is an irrational fear of fun or happiness.", 
"If Pinocchio says “My Nose Will Grow Now”, it would cause a paradox.", "Heart attacks are more likely to happen on a Monday but we both knew this.", 
"In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks.", "Dead people can get goose bumps.", "A single strand of Spaghetti is called a “Spaghetto”.",
"At birth, a baby panda is smaller than a mouse.", "The world’s largest grand piano was built by a 15-year-old in New Zealand.", "Violin bows are commonly made from horse hair.", 
"In Svalbard, a remote Norwegian island, it is illegal to die.", "There is an underwater version of rugby, unsurprisingly called “underwater rugby”.", 
"Saint Lucia is the only country in the world named after a woman.", "If you heat up a magnet, it will lose its magnetism.", "The Marshal Mathers foundation for at-risk and disadvantaged youth, was founded by Eminem.", 
"The oldest unopened bottle of wine was found in a Roman tomb that is over 1,650 years old."]

def fact(message):
    for word in message.split():
        if word.lower() in FACTS_INPUTS:
            return random.choice(FACTS_RESPONSES)

def howMany(message, data):
    if "how many diseases" in message:
        return("I know " + str(len(data)) + " diseases.")

def randomD(message, data):
    if "random disease" in message:
        return("Here's one: " + random.choice(list(data.keys()))  + "!") # Returns a random disease
