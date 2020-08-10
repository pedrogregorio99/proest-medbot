import json
import random


with open("diseases.json", encoding="utf-8") as file:
    data = json.load(file)
    
JOKES_INPUTS = ("joke", "funny", "laugh")
JOKES_RESPONSES = ["I'm not Google.", "I'm not Alexa.", "I'm not Siri", "Friends, Season 5, Episode 16, 11:25.", "What do you get when you cross an alien and a chicken? Eggs-traterrestrial.",
"What do you get when you cross music and an automobile? Cartune.", "How do you throw a space party? You planet!", "Why don't scientists trust atoms? Because they make up everything!",
"Why did the gym close down? It just didn't work out!", "You know what I saw today? Everything I looked at.", "Where are average things manufactured? The satisfactory.", 
"Why was six afraid of seven? Because seven ate nine.", "How do trees get online? They just log on!", "Why did the orange stop? It ran out of juice!",
"What did 0 say to 8? Nice belt!", "I never make mistakes! I thought I did once but I was actually wrong.", "Why doesn't the sun go to college? Because it has a million degrees!",
"Why are skeletons so calm? Because nothing gets under their skin.", "What's red and moves up and down? A tomato in an elevator!", "A dyslexic man walks into a bra."]

def joke(message):
    for word in message.split():
        if word.lower() in JOKES_INPUTS:
            return random.choice(JOKES_RESPONSES)

FACTS_INPUTS = ("random fact", "fact")
FACTS_RESPONSES = ["Some cats are allergic to people (same but don't tell anyone this).", "M&M stands for Mars and Murrie.", "Neil Armstrong didn't say 'That's one small step for man.'", 
"You can major in wine at Cornell University.", "About 700 grapes go into one bottle of wine.", "Fear of the number 13 is called triskaidekaphobia.", 
"Banging your head against a wall for one hour burns 150 calories, but PLEASE don't do that!", "Cherophobia is an irrational fear of fun or happiness.", 
"If Pinocchio says “My Nose Will Grow Now”, it would cause a paradox.", "Heart attacks are more likely to happen on a Monday but we both knew this.", 
"In 2017 more people were killed from injuries caused by taking a selfie than by shark attacks."]

def fact(message):
    for word in message.split():
        if word.lower() in FACTS_INPUTS:
            return random.choice(FACTS_RESPONSES)

BRAIN_INPUTS = ("loss", "losing", "forgetting", "repeating myself") # Brain, nerves and spinal cord problems
CANCER_INPUTS = ("bone pain", "severe bone ache", "severe, persistent headaches", "seizures", "behavioural changes", "thickened tissue", "blood in urine", "persistent kidney pain", "difficulty in starting to pee", "weak urine flow", "needing to rush the toilet") # Cancer
DIABETES_INPUTS = ("very thirsty", "very tired", "unexplained weight loss", "cuts or wounds that heal slowly") # Diabetes
EARS_INPUTS = ("ear","earache", "pain in the ear", "difficulty hearing", "nose bleeding", "ear pain", "pressure inside the ear", "fullness inside the ear", "some hearing loss", "blocked nose", "sinus headache", "high temperature")# Ears, nose and throat
EYES_INPUTS = ("eye", "eyes", "eye redness", "lymph node in front of ear", "blurred vision") # Eyes
HEART_INPUTS = ("chest pain", "angina pain", "arms hurting", "shoulder hurting", "nausea", "overwhelming sense of anxiety") # Heart and blood vessels
IMMUNE_INPUTS = ("sneezing", "runny nose", "blocked nose", "shortness of breath", "cough", "sore throat", "fever", "body rash", "tired") # Immune System
INFECTIONS_INPUTS = ("persistent cough", "yellow phlegm", "coughing blood", "continuous cough", "fever", "dry cough", "headache", "sudden fever", "vomiting", "nausea", "feeling sick", "loss of appetite", "sweats", "chills", "tiredness") # Infections and poisoning
KIDNEYS_INPUTS = ("persistent lower back ache", "intense pain in the back or side of abdmomen", "pain while urinating", "needing to urinate more often") # Kidneys, bladder and prostate
LUNGS_INPUTS = ("persistent cough", "cough", "wheezing", "fatigue", "shortness of breath", "headache", "tired", "difficulty breathing", "fever") # Lungs and airways
MENTAL_INPUTS = ("nervous", "anxious", "worried", "fear", "stressed", "depressive") # Mental Health
MOUTH_INPUTS = ("red gums", "swollen gums", "bleeding gums", "bad breath", "unpleasant taste", "loose teeth", "gum abscesses", "gum pain") # Mouth
MUSCLE_INPUTS = ("wrist fracture", "hip fracture", "joint pain", "joint stiffness", "joint swelling", "join warmth", "joint redness", "joint tenderness", "joint crackling sound") # Muscle, bone and joints
NUTRITIONAL_INPUTS = ("flatulence", "bloated stomach", "drymouth", "strong-smelling urine", "dizziness", "dry mouth", "less urine", "itching in the mouth", "difficulty swalloing", "diarrhoea") # Nutritional
SEXUAL_INPUTS = ("period changes", "hot flushes", "night sweats", "reduced sex drive", "vaginal dryness", "vaginal pain", "fever", "sore throat", "body rash") # Sexual and Reproductive
STOMACH_INPUTS = ("feeling sick", "vomiting", "diarrhoea", "tummy pain", "mild fever", "feeling full", "feeling heavy", "loss of appetite", "abdominal pain", "stomach cramps", "nausea", "headache") # Stomach, liver and gastrointestinal tract

def getDiseases(category):
    tell_diseases = []
    for disease in data:
        if data[disease]["category"] == category:
            tell_diseases.append(disease)

    return("Sounds like a " + category + " kind of problem. Here are some conditions you should look for " + str(tell_diseases) + "!")

def checkSymptoms(message):
    message = message.lower()
    categories = []
    for word in BRAIN_INPUTS:
        if word in message:
            categories.append("Brain, nerves and spinal cord")
        else:
            continue
    for word in CANCER_INPUTS:
        if word in message:
            categories.append("Cancer")
        else:
            continue
    for word in DIABETES_INPUTS:
        if word in message:
            categories.append("Diabetes")
        else:
            continue
    for word in EARS_INPUTS:
        if word in message:
            categories.append("Ears, nose and throat")
        else:
            continue
    for word in EYES_INPUTS:
        if word in message:
            categories.append("Eyes")
        else:
            continue
    for word in HEART_INPUTS:
        if word in message:
            categories.append("Heart and blood vessels")
        else:
            continue
    for word in IMMUNE_INPUTS:
        if word in message:
            categories.append("Immune system")
        else:
            continue
    for word in INFECTIONS_INPUTS:
        if word in message:
            categories.append("Infections and poisoning")
        else:
            continue
    for word in KIDNEYS_INPUTS:
        if word in message:
            categories.append("Kidneys, bladder and prostate")
        else:
            continue
    for word in LUNGS_INPUTS:
        if word in message:
            categories.append("Lungs and airways")
        else:
            continue
    for word in MENTAL_INPUTS:
        if word in message:
            categories.append("Mental health")
        else:
            continue
    for word in MOUTH_INPUTS:
        if word in message:
            categories.append("Mouth")
        else:
            continue
    for word in MUSCLE_INPUTS:
        if word in message:
            categories.append("Muscle, bone and joints")
        else:
            continue
    for word in NUTRITIONAL_INPUTS:
        if word in message:
            categories.append("Nutritional")
        else:
            continue
    for word in SEXUAL_INPUTS:
        if word in message:
            categories.append("Sexual and reproductive")
        else:
            continue
    for word in STOMACH_INPUTS:
        if word in message:
            categories.append("Stomach, liver and gastrointestinal tract")
    categories = set(categories)
    if categories:
        answer = ""
        for category in categories:
            answer = answer + getDiseases(category) + "\n"
        return answer
    else:
        return False

def checkDisease(message):
    message = message.lower()
    for disease in data: # Checks all items in json file
        if disease in message: # Checks if user input has a disease in it
            return True # Disease was found

def getDisease(message):
    message = message.lower()
    for disease in data: # Checks all items in json file
        if disease in message: # Checks if user input has a disease in it
            return disease # Returns the disease found

def getAnswer(user_input, disease):
    user_input = user_input.lower()

    if "what is" in user_input or disease == user_input:
        return(str(data[disease]["definition"]))

    elif "symptom" in user_input:
        return(str(data[disease]["symptoms"]))

    elif "cause" in user_input:
        return(str(data[disease]["causes"]))

    elif "consequence" in user_input or "treatment" in user_input or "treat" in user_input or "take care" in user_input:
        return(str(data[disease]["consequences"]))

    elif "prevent" in user_input or "prevention" in user_input:
        return(str(data[disease]["prevention"]))

    elif "more" in user_input:
        return(str(data[disease]["more"]))

    else:
        return("What do you wish to know? You can ask me what is " + disease + " , what can I do to prevent " + disease + ", what causes " + disease + " and where you can learn more about it. Try it out!")

def saveUnknown(message):
    with open("./files/UnknownAnswers.txt", "a") as file:
        file.write(message + "\n")