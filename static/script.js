document
  .getElementById("user-form")
  .addEventListener("submit", async (event) => {
    event.preventDefault(); // Prevent default form submission

    // Collect form data from inputs
    const formData = {
      name: document.getElementById("name").value.trim(),
      age: document.getElementById("age").value.trim(),
      weight: document.getElementById("weight").value.trim(),
      height: document.getElementById("height").value.trim(),
      activity_level: document.getElementById("activity-level").value.trim(),
      fitness_goal: document.getElementById("fitness-goal").value.trim(),
      dietary_preference: document
        .getElementById("dietary-preference")
        .value.trim(),
    };

    try {
      // Send data to the backend
      const response = await fetch("/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok)
        throw new Error(
          "Failed to process the request. Please check your inputs."
        );

      // Parse response JSON
      const results = await response.json();

      // Update UI with results
      document.getElementById(
        "bmii"
      ).innerText = `BMI: ${results.bmi.bmi} (${results.bmi.category})`;

      // Fitness plan (if an array, join with line breaks)
      if (Array.isArray(results.fitness_plan)) {
        document.getElementById("fitness-details").innerText =
          results.fitness_plan.join("\n");
      } else {
        document.getElementById("fitness-details").innerText =
          results.fitness_plan;
      }

      // Diet plan details
      document.getElementById(
        "diet-details"
      ).innerText = `Calories: ${results.diet_plan.calories} kcal. Recommendation: ${results.diet_plan.dietary_recommendation}`;

      // Meal plan (if an object, iterate and display)
      const mealDetails = Object.entries(results.meal_plan)
        .map(
          ([key, value]) =>
            `${key.charAt(0).toUpperCase() + key.slice(1)}: ${value}`
        )
        .join("\n");
      document.getElementById("meal-details").innerText = mealDetails;

      // Water intake
      document.getElementById(
        "water-details"
      ).innerText = `Daily Water Intake: ${results.water_intake.water_intake_liters} liters`;

      console.log("Results:", results); // For debugging
    } catch (error) {
      console.error("Error:", error);
      alert(
        "Something went wrong while processing your request. Please try again."
      );
    }
  });
