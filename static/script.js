document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("sentiment-form");
    const input = document.getElementById("user-input");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function (e) {
        e.preventDefault();
        const text = input.value.trim();

        if (!text) {
            resultDiv.innerHTML = `<p>Please type something 😊</p>`;
            return;
        }

        resultDiv.innerHTML = `<p>Analyzing emotion... 🔍</p>`;

        fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `<p>😃 <strong>Detected Emotion:</strong> ${data.sentiment}</p>`;
        })
        .catch(err => {
            resultDiv.innerHTML = `<p style="color:red;">Error connecting to server</p>`;
        });
    });
});
