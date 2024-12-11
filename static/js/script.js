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
