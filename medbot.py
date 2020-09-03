import json
import random

with open("/home/pedrogregorio99/medbot/diseases.json", encoding="utf-8") as file:
    data = json.load(file)

JOKES_INPUTS = ("joke", "funny", "laugh")
JOKES_RESPONSES = ["I'm not Google.", "I'm not Alexa.", "I'm not Siri.", "Friends, Season 5, Episode 16, 11:25.", "What do you get when you cross an alien and a chicken? Eggs-traterrestrial.",
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

FACTS_INPUTS = ("fact", "facts", "something")
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

BRAIN_INPUTS = ("loss", "losing", "forgetting", "repeating myself", "sensible to light", "sensible to sound", "dizzy", "diziness") # Brain, nerves and spinal cord problems
CANCER_INPUTS = ("sore throat", "lump", "neck", "bone pain", "severe bone ache", "severe, persistent headaches", "seizures", "behavioural changes", "thickened tissue", "blood in urine", "persistent kidney pain", "difficulty in starting to pee", "weak urine flow", "needing to rush the toilet", "persistent chest infections", "coughing blood", "breathlessness", "persistent bloating", "pain in the pelvis", "pain in the stomach", "difficulty eating", "poor vision", "eye is red","red eye", "inflamed eye", "eye inflamed", "skin cancer", "indigestion", "heartburn", "burping", "stomach pain", "bloated", "indigestion", "anaemia", "weight loss", "vomiting") # Cancer
DIABETES_INPUTS = ("very thirsty", "very tired", "unexplained weight loss", "cuts or wounds that heal slowly", "high blood sugar") # Diabetes
EARS_INPUTS = ("ear","earache", "pain in the ear", "difficulty hearing", "nose bleeding", "ear pain", "pressure inside the ear", "fullness inside the ear", "some hearing loss", "blocked nose", "sinus headache", "high temperature")# Ears, nose and throat
EYES_INPUTS = ("eye", "eyes", "eye redness", "lymph node in front of ear", "blurred vision") # Eyes
HEART_INPUTS = ("chest pain", "angina pain", "arms hurting", "shoulder hurting", "nausea", "overwhelming sense of anxiety") # Heart and blood vessels
IMMUNE_INPUTS = ("sneezing", "runny nose", "blocked nose", "shortness of breath", "cough", "sore throat", "fever", "body rash", "tired") # Immune System
INFECTIONS_INPUTS = ("persistent cough", "yellow phlegm", "coughing blood", "continuous cough", "fever", "dry cough", "headache", "sudden fever", "vomiting", "vomit", "nausea", "feeling sick", "loss of appetite", "sweats", "chills", "tiredness", "swollen glands", "fatigue", "swollen tongue", "fever", "sore throat") # Infections and poisoning
KIDNEYS_INPUTS = ("persistent lower back ache", "intense pain in the back or side of abdmomen", "pain while urinating", "needing to urinate more often", "urinating", "incontinence", "peeing") # Kidneys, bladder and prostate
LUNGS_INPUTS = ("persistent cough", "cough", "wheezing", "fatigue", "shortness of breath", "headache", "tired", "difficulty breathing", "fever") # Lungs and airways
MENTAL_INPUTS = ("trouble sleeping", "nervous", "anxious", "worried", "fear", "stressed", "depressive", "suicidal", "suicide", "sad", "feeling down", "alone") # Mental Health
MOUTH_INPUTS = ("red gums", "swollen gums", "bleeding gums", "bad breath", "unpleasant taste", "loose teeth", "gum abscesses", "gum pain", "bad breath", "unpleasant taste", "teeth pain") # Mouth
MUSCLE_INPUTS = ("wrist fracture", "hip fracture", "joint pain", "joint stiffness", "joint swelling", "join warmth", "joint redness", "joint tenderness", "joint crackling sound") # Muscle, bone and joints
NUTRITIONAL_INPUTS = ("flatulence", "bloated stomach", "drymouth", "strong-smelling urine", "dizziness", "dry mouth", "less urine", "itching in the mouth", "difficulty swalloing", "diarrhoea", "lack of appetite", "never hungry", "not eating much", "haven't been eating") # Nutritional
SEXUAL_INPUTS = ("period changes", "hot flushes", "night sweats", "reduced sex drive", "vaginal dryness", "vaginal pain", "fever", "sore throat", "body rash", "pain peeing", "vagina", "penis", "unable to pee") # Sexual and Reproductive
SKIN_INPUTS = ("red skin", "itchy skin", "dry skin", "cracked skin", "skin", "burning", "stinging", "redness", "spots", "blood vessels") # Skin, hair and nails
STOMACH_INPUTS = ("itchiness", "itchy", "trouble sleeping", "feeling sick", "vomit", "vomiting", "tummy pain", "mild fever", "feeling full", "feeling heavy", "loss of appetite", "abdominal pain", "stomach cramps", "nausea", "headache") # Stomach, liver and gastrointestinal tract

def getDiseases(category):
    tell_diseases = []
    for disease in data:
        if data[disease]["category"] == category:
            tell_diseases.append(disease)

    return("🛑 " + category + "! Here are some conditions you should look for " + str(tell_diseases) + "!")

def getCategories(symptom):
    categories = []

    if symptom in BRAIN_INPUTS:
        categories.append("Brain, nerves and spinal cord")

    if symptom in CANCER_INPUTS:
        categories.append("Cancer")

    if symptom in DIABETES_INPUTS:
        categories.append("Diabetes")

    if symptom in EARS_INPUTS:
        categories.append("Ears, nose and throat")

    if symptom in EYES_INPUTS:
        categories.append("Eyes")

    if symptom in HEART_INPUTS:
        categories.append("Heart and blood vessels")

    if symptom in IMMUNE_INPUTS:
        categories.append("Immune system")

    if symptom in INFECTIONS_INPUTS:
        categories.append("Infections and poisoning")

    if symptom in KIDNEYS_INPUTS:
        categories.append("Kidneys, bladder and prostate")

    if symptom in LUNGS_INPUTS:
        categories.append("Lungs and airways")

    if symptom in MENTAL_INPUTS:
        categories.append("Mental health")

    if symptom in MOUTH_INPUTS:
        categories.append("Mouth")

    if symptom in MUSCLE_INPUTS:
        categories.append("Muscle, bone and joints")

    if symptom in NUTRITIONAL_INPUTS:
        categories.append("Nutritional")

    if symptom in SEXUAL_INPUTS:
        categories.append("Sexual and Reproductive")

    if symptom in SKIN_INPUTS:
        categories.append("Skin, hair and nails")

    if symptom in STOMACH_INPUTS:
        categories.append("Stomach, liver and gastrointestinal tract")

    if categories:
        return categories
    else:
        return False



def checkSymptoms(message):

    message = message.lower()
    symptoms = []
    answer = "Hold up! ✋ <br>"

    for word in BRAIN_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in CANCER_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in DIABETES_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in EARS_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in EYES_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in HEART_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in IMMUNE_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in INFECTIONS_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in KIDNEYS_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in LUNGS_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in MENTAL_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in MOUTH_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in MUSCLE_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in NUTRITIONAL_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in SEXUAL_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in SKIN_INPUTS:
        if word in message:
            symptoms.append(word)

        else:
            continue
    for word in STOMACH_INPUTS:
        if word in message:
            symptoms.append(word)

    symptoms = set(symptoms)

    if symptoms:
        for symptom in symptoms:
            answer = answer + "&nbsp;&nbsp;🆘 " + str(symptom.capitalize()) + " is a symptom for these conditions:<br>"
            categories = getCategories(symptom)
            for category in categories:
                answer = answer + "&nbsp;&nbsp;" + getDiseases(category) + "<br>"
        answer = answer + "&nbsp;&nbsp;You can ask me about any of these anytime."
        return answer
    else:
        return False

def checkDisease(message):
    for disease in data: # Checks all items in json file
        if disease in message or "it" in message or "that" in message: # Checks if user input has a disease in it
            return True # Disease was found

def getDisease(message):
    for disease in data: # Checks all items in json file
        if disease in message: # Checks if user input has a disease in it

            if disease == "diabetes":
                if "type 1" in message:
                    return "type 1 diabetes"

                elif "type 2" in message:
                    return "type 2 diabetes"

            if disease == "arthritis":
                if "osteoarthritis" in message:
                    return "osteoarthritis"

                elif "rheumatoid" in message:
                    return "rheumatoid arthritis"

                else:
                    return "arthritis"

            else:
                return disease # Returns the disease found


def getAnswer(user_input, disease):

    if "what is" in user_input or "whats" in user_input or "tell me about" in user_input or disease == user_input:
        return(str(data[disease]["definition"]))

    elif "cause" in user_input:
        return(str(data[disease]["causes"]))

    elif "consequence" in user_input or "treatment" in user_input or "treat" in user_input or "take care" in user_input or "get rid" in user_input:
        return(str(data[disease]["consequences"]))

    elif "prevent" in user_input or "prevention" in user_input:
        return(str(data[disease]["prevention"]))

    elif "more" in user_input:
        return(str(data[disease]["more"]))

    else:
        return("What do you wish to know? You can ask me what is " + disease + ", what can I do to prevent " + disease + ", what causes " + disease + " and where you can learn more about it. Try it out!")

def saveUnknown(message):
    with open("/home/pedrogregorio99/medbot/files/UnknownAnswers.txt", "a") as file:
        file.write(message + "\n")
