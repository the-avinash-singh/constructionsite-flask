document.addEventListener('DOMContentLoaded', () => {
    // Intersection Observer to check if the element is in the viewport
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startAnimation();
                observer.unobserve(entry.target); // Stop observing once triggered
            }
        });
    }, { threshold: 0.5 }); // Observe when 50% of the boxes are in the viewport

    // Observe the trigger div (triggering when it reaches the viewport)
    observer.observe(document.getElementById('viewportTrigger'));

    function startAnimation() {
        // Target digits (can be any 3-digit number you want)
        const targetDigits = [5, 5, 4];

        // Add a delay before starting the animation (for example, 0.5 seconds)
        setTimeout(() => {
            animateDigit('digit3', targetDigits[2], 0); // Start from ones place (rightmost box)
            animateDigit('digit2', targetDigits[1], 500); // Start after a 500ms delay
            animateDigit('digit1', targetDigits[0], 1000); // Start after a 1000ms delay
        }, 500); // Initial delay before the animation begins
    }

    // Function to animate a single digit to its target value
    function animateDigit(elementId, targetValue, delay) {
        const element = document.getElementById(elementId);
        let currentValue = 0;

        // Create a sequence of numbers to display
        const numbers = Array.from({ length: 10 }, (_, i) => i); // [0, 1, 2, ..., 9]
        let steps = [];
        
        // Generate the steps of animation (loop from currentValue to targetValue)
        if (currentValue <= targetValue) {
            for (let i = currentValue; i <= targetValue; i++) {
                steps.push(i);
            }
        } else {
            for (let i = currentValue; i >= targetValue; i--) {
                steps.push(i);
            }
        }

        // Start the animation after a delay
        setTimeout(() => {
            let stepIndex = 0;
            let interval = setInterval(() => {
                if (stepIndex < steps.length) {
                    element.innerText = steps[stepIndex];
                    stepIndex++;
                    applyRevolverEffect(element);
                } else {
                    clearInterval(interval);
                }
            }, 200); // Interval between number steps (adjust this to make it faster or slower)
        }, delay); // Delay for each digit
    }

    // Function to apply the revolver-style effect (rotate numbers like a cylinder)
    function applyRevolverEffect(element) {
        element.style.animation = 'rotateIn .07s ease-in-out';
        element.addEventListener('animationend', () => {
            element.style.animation = ''; // Reset the animation to allow it to trigger again
        });
    }
});
