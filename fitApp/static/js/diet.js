document.addEventListener("DOMContentLoaded", () => {
    const tiles = document.querySelectorAll(".tile");

    gsap.from(tiles, {
        y: -100,
        opacity: 0,
        scale: 0.5,
        duration: 1
    });

    gsap.to(tiles,{
        y:-100,
        scale: 1,
        duration: 2.5,
        ease: "back.out(.7)",
    });

    gsap.from(".enhanced-list li", {
            scrollTrigger: ".enhanced-list",
            duration: 1,
            y: 20,
            opacity: 0,
            stagger: 0.3,
            ease: "power2.out"
        });

});
