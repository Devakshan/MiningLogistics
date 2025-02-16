document.addEventListener("DOMContentLoaded", function () {
    const checkbox = document.getElementById("routeCheckbox");

    // Restore checkbox state from localStorage
    if (localStorage.getItem("routeChecked") === "true") {
        checkbox.checked = true;
    }

    // Save checkbox state before submitting
    document.getElementById("myForm").addEventListener("submit", function () {
        localStorage.setItem("routeChecked", checkbox.checked);
    });
});

function updateCargoOptions() {
    document.getElementById("fcl-options").style.display = "none";
    document.getElementById("lcl-options").style.display = "none";
    document.getElementById("bulk-options").style.display = "none";
    document.getElementById("special-options").style.display = "none";

    let cargoType = document.querySelector('input[name="cargo_type"]:checked').value;
    document.getElementById(cargoType + "-options").style.display = "block";
}