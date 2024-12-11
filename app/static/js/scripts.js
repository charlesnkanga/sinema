document.querySelectorAll(".favorite-btn").forEach((button) => {
    button.addEventListener("click", (e) => {
        e.preventDefault();
        const movieId = button.dataset.movieId;

        fetch(`/movies/${movieId}/toggle_favorite`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.status === "added") {
                    button.innerHTML = '<i class="fas fa-heart text-danger"></i>';
                } else {
                    button.innerHTML = '<i class="far fa-heart"></i>';
                }
            })
            .catch((error) => console.error("Error:", error));
    });
});