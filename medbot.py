import json
import random

with open("diseases.json", encoding="utf-8") as file:
    data = json.load(file)
    
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
            answer = answer + "🆘 " + str(symptom.capitalize()) + " is a symptom for these conditions:<br>"
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
    message = message.lower()
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
    with open("./files/UnknownAnswers.txt", "a") as file:
        file.write(message + "\n")
