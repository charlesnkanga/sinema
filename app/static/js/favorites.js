document.addEventListener("DOMContentLoaded", function () {
    const forms = document.querySelectorAll(".favorite-form");

    forms.forEach((form) => {
        form.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission
            const movieId = form.dataset.movieId; // Get the movie ID

            // Make the AJAX POST request
            fetch(`/movies/${movieId}/toggle_favorite`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
            })
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then((data) => {
                    const button = form.querySelector("button");
                    if (data.status === "added") {
                        button.textContent = "Unfavorite";
                        button.classList.remove("btn-primary");
                        button.classList.add("btn-success");
                    } else if (data.status === "removed") {
                        button.textContent = "Favorite";
                        button.classList.remove("btn-success");
                        button.classList.add("btn-primary");
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                    alert("An error occurred while toggling the favorite status.");
                });
        });
    });
});