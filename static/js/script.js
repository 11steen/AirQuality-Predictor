// Dark mode functionality
document.getElementById('dark-mode-toggle').addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');
});

// Slideshow functionality
let slideIndex = 0;
const slides = document.getElementsByClassName("mySlides");

if (slides.length > 0) {
    slides[0].classList.add("active");
}

function showSlides() {
   
    for (let i = 0; i < slides.length; i++) {
        slides[i].classList.remove("active");
    }

    slideIndex = (slideIndex + 1) % slides.length;
    slides[slideIndex].classList.add("active");
}

setInterval(showSlides, 6000);
