<h1 align="center">
  Fluorosis Risk Assessment Tool
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30">
</h1>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=keerti-reddy&label=Profile%20Views&color=0e75b6&style=flat" align='right' alt="Keerti Reddy" />
</p>

<p align="center">
  <a href="https://github.com/keerti-reddy/readme-typing-svg"> 
    <img src="https://readme-typing-svg.herokuapp.com?lines=Health+Data+Analyst;Data+Visualization+Expert;Data-Driven+Innovator;Future-Focused+Analyst&center=true&width=500&height=50">
  </a>
</p>

<hr/>

## Project Overview
The **Fluorosis Risk Assessment Tool** analyzes fluoride concentrations in drinking water and provides a personalized assessment of fluorosis risk based on user-specific factors like age, gender, and region. It leverages data from CDC's Water Fluoridation Statistics and offers actionable preventive recommendations to improve dental health.

---

### 🛠️ Technologies Used
- **Python**: Core language for data analysis and user interactions.
- **Pandas**: For data manipulation and processing.
- **AWS S3**: To retrieve water fluoridation data from the cloud.
- **Boto3**: AWS SDK for Python to interact with AWS services.

### ⚙️ Project Flow
1. **Data Collection**: Water fluoridation data is sourced from the CDC's 2014 statistics and stored in an AWS S3 bucket.
2. **User Input**: Users provide their postal code, age, and gender for a tailored risk assessment.
3. **Fluoride Concentration Analysis**:
   - **Low Risk**: ≤ 30%
   - **Moderate Risk**: 30% - 65%
   - **High Risk**: > 65%
4. **Age and Gender Adjustments**: Additional risk adjustments are based on age and gender.
5. **Preventive Recommendations**: Personalized advice on maintaining dental health.

### 📋 Prerequisites
- **Python 3.x**
- **Pandas** and **Boto3**
- **AWS Account** (for S3 access)

To install dependencies:
```bash
pip install pandas boto3

🔧 Setup
Clone the Repository:
git clone https://github.com/your-username/fluorosis-risk-assessment.gitcd fluorosis-risk-assessment

Configure AWS Credentials:
aws configure

Run the Program
python fluorosis_assessment.py



