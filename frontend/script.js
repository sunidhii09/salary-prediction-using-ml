document.addEventListener("DOMContentLoaded", async function() {
    try {
        const response = await fetch("http://localhost:8000/education_titles");
        if (!response.ok) {
            throw new Error("Failed to fetch education titles");
        }
        const data = await response.json();
        const eduTitles = data.education_titles; // Ensure this key matches the server response

        const eduTitleSelect = document.getElementById("education_level");
        eduTitles.forEach(title => {
            const option = document.createElement("option");
            option.value = title;
            option.text = title;
            eduTitleSelect.add(option);
        });
    } catch (error) {
        console.error("Error fetching education titles:", error);
    }
});

document.addEventListener("DOMContentLoaded", async function() {
    try {
        const response = await fetch("http://localhost:8000/job_titles");
        if (!response.ok) {
            throw new Error("Failed to fetch job titles");
        }
        const data = await response.json();
        const jobTitles = data.job_titles;

        const jobTitleSelect = document.getElementById("job_title");
        jobTitles.forEach(title => {
            const option = document.createElement("option");
            option.value = title;
            option.text = title;
            jobTitleSelect.add(option);
        });
    } catch (error) {
        console.error("Error fetching job titles:", error);
    }
});

document.getElementById("salary-form").addEventListener("submit", async function(event) {
    event.preventDefault();

    const age = document.getElementById("age").value;
    const experience = document.getElementById("experience").value;
    const job_title = document.getElementById("job_title").value;
    const gender = document.getElementById("gender").value;
    const education_level = document.getElementById("education_level").value;

    if (isNaN(age) || age < 18 || age >= 75) {
        const resultDiv = document.getElementById("result");
        resultDiv.classList.add("error-message");
        resultDiv.innerText = "Please enter a valid age between 18 and 75.";
        return; // Exit the function if age is invalid
    }


    if (experience>=age){
        const resultDiv = document.getElementById("result");
        resultDiv.innerText = "Please enter valid number of experience years.";
        resultDiv.classList.add("error-message");
        return;
    }

    try {
        const response = await fetch("http://localhost:8000/predict_salary", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ age, experience, job_title, gender, education_level })
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        const resultDiv = document.getElementById("result");
        resultDiv.classList.remove("error-message"); // Remove error class if any
        resultDiv.innerText = `Predicted Salary: $${data.predicted_salary}`;
    } catch (error) {
        console.error("There was a problem with the fetch operation:", error);
        const resultDiv = document.getElementById("result");
        resultDiv.classList.add("error-message");
        resultDiv.innerText = "An error occurred while predicting salary. Please try again.";
    }
});
