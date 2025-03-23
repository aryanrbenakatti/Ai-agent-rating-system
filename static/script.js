function predictRating() {
    const name = document.getElementById("name").value;
    const sales = parseInt(document.getElementById("sales").value);
    const reviews = parseFloat(document.getElementById("reviews").value);
    const response_time = document.getElementById("response_time").value;

    if (!name || isNaN(sales) || isNaN(reviews)) {
        alert("Please fill in all fields correctly.");
        return;
    }

    fetch("http://127.0.0.1:5000/predict_rating", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            sales: sales,
            reviews: reviews,
            response_time: response_time
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.rating) {
            document.getElementById("predictionResult").innerHTML = `<strong>Predicted AI Rating:</strong> ${data.rating}`;
        } else {
            document.getElementById("predictionResult").innerHTML = `<strong>Error:</strong> Unable to predict rating.`;
        }
    })
    .catch(error => {
        console.error("Error predicting rating:", error);
        document.getElementById("predictionResult").innerHTML = `<strong>Error:</strong> API request failed.`;
    });
}
