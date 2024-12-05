//digit round animation
document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                startAnimation();
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    observer.observe(document.getElementById('viewportTrigger'));

    function startAnimation() {
    
        const targetDigits = [5, 5, 4];
        setTimeout(() => {
            animateDigit('digit3', targetDigits[2], 0);
            animateDigit('digit2', targetDigits[1], 500);
            animateDigit('digit1', targetDigits[0], 1000);
        }, 500);
    }

    function animateDigit(elementId, targetValue, delay) {
        const element = document.getElementById(elementId);
        let currentValue = 0;

        const numbers = Array.from({ length: 10 }, (_, i) => i);
        let steps = [];
        
        if (currentValue <= targetValue) {
            for (let i = currentValue; i <= targetValue; i++) {
                steps.push(i);
            }
        } else {
            for (let i = currentValue; i >= targetValue; i--) {
                steps.push(i);
            }
        }

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
            }, 200);
        }, delay);
    }

    function applyRevolverEffect(element) {
        element.style.animation = 'rotateIn .07s ease-in-out';
        element.addEventListener('animationend', () => {
            element.style.animation = '';
        });
    }
});


//filter range
const budgetInput=document.getElementById('budget');
const budgetButton=document.getElementById('budget-button');
const budgetRange=document.getElementById('budget-range');
const budgetOutput=document.getElementById('budget-output');

budgetButton.addEventListener('click',()=>{
    const inputValue=parseInt(budgetInput.value);
    const min = parseInt(budgetRange.min);
    const max = parseInt(budgetRange.max);
    
    if (!isNaN(inputValue) && inputValue >= min && inputValue <= max){
        budgetRange.value=inputValue;
        budgetOutput.textContent=budgetRange.value;
    }else{
        alert('Invalid Price. Please enter a value between '+budgetRange.min+' and '+budgetRange.max);
    }
})

budgetRange.addEventListener('input',()=>{
    budgetInput.value=budgetRange.value;
    budgetOutput.textContent=budgetRange.value;
})
