window.addEventListener("load", () => {
    const videoContainer = document.querySelector(".video-container-polygon.polygon-crop");
    videoContainer.classList.add("animate");
});


document.addEventListener('DOMContentLoaded', () => {
    // Register ScrollTrigger plugin
    gsap.registerPlugin(ScrollTrigger);

    // Animate the h2 text
    gsap.from("h2", {
        opacity: 0,
        y: 50, // Start 50px below the original position
        duration: 1.5, // Animation duration
        ease: "power3.out", // Smooth easing
        scrollTrigger: {
            trigger: "h2", // Element that triggers the animation
            start: "top 75%", // Trigger when the top of h2 is 75% down the viewport
            toggleActions: "play none none none" // Play the animation on scroll
        }
    });
});
