import boto3
import pandas as pd

aws_access_key_id = 'AKIA22FXY6KJJWNLWMED'
aws_secret_access_key = '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'
s3_bucket = 'flouride'
s3_key = 'water_fluoridation_percentage.csv'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

try:
    # Get the object from S3
    response = s3.get_object(Bucket=s3_bucket, Key=s3_key)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(response['Body'])

    # Display DataFrame columns
    print(df.columns)

except Exception as e:
    print(f"An error occurred: {e}")


# Download the CSV file from S3
response = s3.get_object(Bucket=s3_bucket, Key=s3_key)
data = pd.read_csv(response['Body'])

# Display the DataFrame
print(data)

# Importing CSV file into a DataFrame
df = pd.read_csv("C:/Users/16032/Downloads/water_fluoridation_percentage.csv")
print(df.columns)
# User input
postalcode = input("Enter your postal code: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")


postal_code = df[df['postalcode'] == int(postalcode)]
if not postal_code.empty:
   flouridecontent = postal_code['flouridecontent'].values[0]
   print(f"Fluoride Content for Postal Code {postalcode}: {flouridecontent}%")
else:
    print(f"No data available for the entered postal code: {postalcode}")

# gender and age group prevalence from the user inputs
def age_affected(age):
    if age <= 20:
        return 43 
    elif 20 < age <= 50:
        return 32
    elif 50 < age <= 70:
        return 20
    else:
        return 5

def gender_affected(gender):
    if gender.lower() == 'male':
        return 54
    else:
        return 46
        
# Checking if the region is affected by fluorosis based on fluoride concentration
if flouridecontent <= 30:
    print("This region is not affected by fluorosis.")
elif 30 < flouridecontent <= 65:
    print("This region is affected by fluorosis.")
else:
    print("This region is affected by severe fluorosis.")
# Combine all three percentages and calculate the overall percentage    
pc = flouridecontent
age_category_result = age_affected(age)
gender_category_result = gender_affected(gender)
combine_total=age_category_result + gender_category_result + pc
combined_percentage = (combine_total/ 300 )*100

# Display the results
print(f"Age Category Effect: {age_category_result}% Affected")
print(f"Gender Effect: {gender_category_result}% Affected")
# display the combined percentage
print(f"Combined Percentage: {combined_percentage}% Affected")

#preventive methods:
if combined_percentage <= 20:
    print("Recommendation: Mild risk of fluorosis. Maintain regular dental hygiene to prevent from dental fluorosis.")
elif 20 < combined_percentage <= 50:
    print(" Recommendation: Moderate risk of fluorosis. Use fluoride-free toothpaste and consider water filtration.")
elif 50 < combined_percentage <= 75:
    print("Recommendation: High risk of fluorosis. Use fluoride-free toothpaste, consider water filtration, and consult a dentist to prevent from teeth loss.")
else:
    print("Recommendation: Severe risk of fluorosis.Seek immediate professional dental advice.")
