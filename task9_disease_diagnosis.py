"""
Task 9: Disease Diagnosis Program
This program diagnoses a disease based on user symptoms.
"""

# Welcome message
print("===== Welcome to Jeshi Hospital =====")

# Patient details
name = input("Enter patient name: ")
gender = input("Enter gender: ")
age = input("Enter age: ")
residence = input("Enter place of residence: ")

# Symptoms input
symptom1 = input("Enter symptom 1: ").lower()
symptom2 = input("Enter symptom 2: ").lower()

# Diagnosis logic
if (symptom1 == "fever" and symptom2 == "headache") or \
   (symptom1 == "headache" and symptom2 == "fever"):
    diagnosis = "Malaria"

elif (symptom1 == "fever" and symptom2 == "abdominal pain") or \
     (symptom1 == "abdominal pain" and symptom2 == "fever"):
    diagnosis = "Typhoid"

elif (symptom1 == "cough" and symptom2 == "chest pain") or \
     (symptom1 == "chest pain" and symptom2 == "cough"):
    diagnosis = "Pneumonia"

elif (symptom1 == "fatigue" and symptom2 == "frequent urination") or \
     (symptom1 == "frequent urination" and symptom2 == "fatigue"):
    diagnosis = "Diabetes"

else:
    diagnosis = "Condition not recognized. Please consult a doctor."

# Output
print("\n===== Diagnosis Result =====")
print("Patient Name:", name)
print("Gender:", gender)
print("Age:", age)
print("Residence:", residence)

print("\nSymptoms Entered:")
print("Symptom 1:", symptom1)
print("Symptom 2:", symptom2)

print("\nDiagnosis:", diagnosis)