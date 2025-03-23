function generateAgentRatings() {
    document.getElementById("loading-ratings").style.display = "block";
    document.getElementById("agent-rating-list").innerHTML = "";

    fetch("http://127.0.0.1:5000/get_agent_ratings")
        .then(response => response.json())
        .then(agents => {
            const list = document.getElementById("agent-rating-list");
            list.innerHTML = "";  // Clear old list

            agents.forEach(agent => {
                const li = document.createElement("li");
                li.innerHTML = `<strong>${agent.name}</strong> - Sales: ${agent.sales}, Reviews: ${agent.reviews}, Response: ${agent.response_time}, Rating: ${agent.rating}`;
                list.appendChild(li);
            });

            document.getElementById("loading-ratings").style.display = "none";
        })
        .catch(error => {
            console.error("Error fetching agent data:", error);
            document.getElementById("loading-ratings").innerText = "Failed to load ratings!";
        });
}

document.addEventListener("DOMContentLoaded", function () {
    fetch("http://127.0.0.1:5000/get_agent_ratings")
        .then(response => response.json())
        .then(data => {
            let tableBody = document.getElementById("agents-table");
            tableBody.innerHTML = "";  // Clear previous data

            data.forEach(agent => {
                let row = `<tr>
                    <td>${agent.name}</td>
                    <td>${agent.sales}</td>
                    <td>${agent.reviews}</td>
                    <td>${agent.response_time}</td>
                    <td>${agent.rating}</td>
                </tr>`;
                tableBody.innerHTML += row;
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});
