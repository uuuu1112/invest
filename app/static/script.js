document.addEventListener("DOMContentLoaded", function() {
    const footerYear = document.getElementById("currentYear");
    const currentYear = new Date().getFullYear();
    footerYear.textContent = currentYear;
});


