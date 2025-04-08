Fraud Detection API 🚀

📌 Overview

This project is a FastAPI-based REST API for fraud detection. The API utilizes a machine learning pipeline to predict whether a given claim is fraudulent or not.

🔧 Technologies Used

Python 3.9+
FastAPI - Web framework for building APIs
Pandas - Data processing library
Scikit-learn - Machine learning utilities
Pickle - Model serialization

📑 API Documentation

FastAPI provides interactive API documentation:
Swagger UI: http://127.0.0.1:8000/docs
Redoc UI: http://127.0.0.1:8000/redoc

🚀 Installation & Running the API

1️⃣ Clone the repository

 git clone https://github.com/yourusername/fraud-detection-api.git
 cd fraud-detection-api

2️⃣ Install dependencies

pip install -r requirements.txt

3️⃣ Start the API

uvicorn main:app --reload

🛠 API Endpoints

Method    |      Endpoint      |      Description
GET              /                    Health check endpoint
POST             /predict             Predict fraudulence of a record

🏗 Request & Response Example

📥 Request (POST /predict)

{
  "Month": "Dec",
  "WeekOfMonth": 5,
  "DayOfWeek": "Wednesday",
  "Make": "Honda",
  "AccidentArea": "Urban",
  "DayOfWeekClaimed": "Tuesday",
  "MonthClaimed": "Jan",
  "WeekOfMonthClaimed": 1,
  "Sex": "Female",
  "MaritalStatus": "Single",
  "Age": 21.0,
  "Fault": "Policy Holder",
  "PolicyType": "Sport - Liability",
  "VehicleCategory": "Sport",
  "VehiclePrice": "more than 69000",
  "PolicyNumber": 1.0,
  "RepNumber": 12,
  "Deductible": 300,
  "DriverRating": 1,
  "Days_Policy_Accident": "more than 30",
  "Days_Policy_Claim": "more than 30",
  "PastNumberOfClaims": "none",
  "AgeOfVehicle": "3 years",
  "AgeOfPolicyHolder": "26 to 30",
  "PoliceReportFiled": "No",
  "WitnessPresent": "No",
  "AgentType": "External",
  "NumberOfSuppliments": "none",
  "AddressChange_Claim": "1 year",
  "NumberOfCars": "3 to 4",
  "Year": 1994,
  "BasePolicy": "Liability"
}

📤 Response

{
  "Result": 1
}

Result: 1 indicates fraud, 0 indicates no fraud.


🏗 Future Enhancements
- add information about froud probability in /predict response,
- add the most importand details about model,

📬 Contact

For questions or suggestions, feel free to reach out via GitHub Issues.

