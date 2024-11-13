<h1 align="center">
  Fluorosis Risk Assessment Tool
</h1>

<img src="https://github.com/kresapu/Flourosis_risk_assesment_tool/blob/main/flourosisrisk_tool.png" alt="Fluorosis Risk Assessment Tool" width="300"/>




<p align="center">
  <img src="https://komarev.com/ghpvc/?username=keerti-reddy&label=Profile%20Views&color=0e75b6&style=flat" align='right' alt="Keerti Reddy" />
</p>



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

### 🎓 Acknowledgements
CDC: 2014 Water Fluoridation Statistics
AWS SDK for Python (Boto3): Documentation and examples
WebMD: Information on fluorosis prevention

---

### 🏁 Conclusion
The **Fluorosis Risk Assessment Tool** serves as a practical solution for assessing fluoride exposure and fluorosis risk based on geographic, age, and gender-specific data. By leveraging AWS S3 for data storage and Python for analysis, this tool provides users with valuable insights and preventive recommendations tailored to their individual needs. 

This project is a step toward personalized health assessments and exemplifies how data-driven solutions can contribute to public health awareness. Future expansions could include adding real-time updates, integrating a user-friendly interface, and broadening data sources to further improve accuracy and accessibility. Together, these advancements have the potential to make impactful contributions to dental health and preventive care.

---

<p align="center">
  <i>Promoting informed health choices through data and innovation.</i>
</p>





