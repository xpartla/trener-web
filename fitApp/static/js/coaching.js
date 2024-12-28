document.addEventListener("DOMContentLoaded", function () {

    gsap.from(".enhanced-list li", {
            scrollTrigger: ".enhanced-list",
            duration: 1,
            y: 20,
            opacity: 0,
            stagger: 0.3,
            ease: "power2.out"
        });

});

gsap.registerPlugin(ScrollTrigger);
// Periodic emphasis
gsap.fromTo('.step',
    { scale: 1 },
    {
        scale: 1.1,
        duration: 0.4,
        ease: "power1.inOut",
        repeat: -1,
        yoyo: true,
        stagger: 2
    }
).repeatDelay(2);
