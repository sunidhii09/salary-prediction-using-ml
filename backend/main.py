from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

mlr_model = joblib.load('mlr_model.pkl')
job_title_encoder = joblib.load('job_title_encoder.pkl')
gender_encoder = joblib.load('gender_encoder.pkl')
education_level_encoder = joblib.load('education_level_encoder.pkl')

standard_scaler = joblib.load('standard_scaler.pkl')

class SalaryInput(BaseModel):
    age: int
    experience: int
    job_title: str
    gender: str
    education_level: str

@app.get("/education_titles")
async def get_education_titles():
    education_titles = list(education_level_encoder.classes_)
    return JSONResponse(content={"education_titles": education_titles})

@app.get("/job_titles")
async def get_job_titles():
    job_titles = list(job_title_encoder.classes_)
    return JSONResponse(content={"job_titles": job_titles})

@app.post("/predict_salary")
async def predict_salary(input_data: SalaryInput):
    job_title = job_title_encoder.transform([input_data.job_title])[0]
    gender = gender_encoder.transform([input_data.gender])[0]
    education_level = education_level_encoder.transform([input_data.education_level])[0]
    input_array = np.array([[input_data.age, input_data.experience, job_title, gender, education_level]])
    input_scaled = standard_scaler.transform(input_array)
    predicted_salary = mlr_model.predict(input_scaled)[0]
    return {"predicted_salary": predicted_salary}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)