Fluorosis Risk Assessment Tool


                                 Fluorosis Analysis
                                         ( Keerti Reddy Resapu)


Project Overview:
This project aims to analyze the fluoride concentration in drinking water and assess the risk of fluorosis for individuals based on their age, gender, and region. The project uses Python, Pandas, AWS (Amazon Web Services), and user interaction to provide personalized risk assessments and preventive recommendations. The tool assesses the fluoride concentration in water sources and categorizes the risk of fluorosis from low to high, offering actionable steps to mitigate health risks.

Technologies Used:
Python: Core programming language for data analysis and user interaction.
Pandas: Data manipulation and processing library.
AWS S3: Used to retrieve water fluoridation data from the cloud.
Boto3: AWS SDK for Python to interact with AWS S3.
Project Flow:
Data Collection:
The fluoride concentration data is sourced from the CDC's 2014 Water Fluoridation Statistics file, which is stored in an AWS S3 bucket.

User Input:
Users input their postal code, age, and gender to personalize the fluorosis risk analysis.

Fluoride Concentration Analysis:
The program calculates the fluoride content in the user’s region based on their postal code and assesses the fluorosis risk as:

Low Risk: Fluoride content <= 30%
Moderate Risk: 30% < Fluoride content <= 65%
High Risk: Fluoride content > 65%
Age and Gender Effects:
Age and gender factors are considered to adjust the risk level further, giving a personalized assessment.

Preventive Recommendations:
Based on the calculated risk, the program provides customized advice for maintaining dental hygiene or seeking professional dental care.

Prerequisites:
Before running this project, ensure you have the following installed:

Python 3.x
Pandas
Boto3
AWS Account for accessing S3 bucket (if modifying the data source)
Required libraries: pip install pandas boto3
Setup:
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/fluorosis-risk-assessment.git
cd fluorosis-risk-assessment
Install Dependencies:

bash
Copy code
pip install pandas boto3
Configure AWS Credentials:
Ensure that your AWS credentials are set up. You can configure them using AWS CLI:

bash
Copy code
aws configure
Run the Program: Execute the Python script to interact with the tool:

bash
Copy code
python fluorosis_assessment.py
Code Explanation:
Step 1: Import Libraries
Importing necessary libraries like pandas for data processing and boto3 for AWS S3 interaction.

Step 2: Accessing AWS S3 Bucket
Use Boto3 to retrieve the fluoride concentration data from an S3 bucket.
Load the data into a Pandas DataFrame.
Step 3: User Input
User provides postal code, age, and gender for personalized results.
Step 4: Data Filtering & Analysis
The program filters the data by postal code and retrieves the fluoride concentration for that region.
It also calculates the impact of age and gender on fluorosis risk.
Step 5: Risk Assessment
The fluoride content is categorized into three levels: low, moderate, and high risk for fluorosis.
Step 6: Preventive Recommendations
Based on the user’s combined risk, tailored recommendations for preventive dental care are provided.
Results Output Example:
text
Copy code
Fluoride Content for Your Region: 45%
Risk Level: Moderate
Age Effect: 5% Affected
Gender Effect: 2% Affected
Combined Risk: 12% Affected
Preventive Recommendation: Maintain regular dental hygiene, consider professional advice if symptoms worsen.
Conclusion:
The Fluorosis Risk Assessment Tool empowers users to assess their fluorosis risk and take preventive actions to mitigate health risks. By analyzing fluoride levels in water, demographic factors, and providing actionable advice, the project contributes to better public health awareness and prevention.

Acknowledgements:
WebMD: Fluorosis symptoms, causes, and treatments WebMD
W3Schools: Online tutorials for Python W3Schools
AWS SDK for Python (Boto3): Official documentation and examples Boto3
CDC: 2014 Water Fluoridation Statistics CDC
