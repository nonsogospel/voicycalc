const main = {
  displayValue: '0',
  firstOperand: null,
  waitingForSecondOperand: false,
  operator: null,
};

function inputDigit(digit) {
  const { displayValue, waitingForSecondOperand } = main;

  if (waitingForSecondOperand === true) {
    main.displayValue = digit;
    main.waitingForSecondOperand = false;
  } else {
    main.displayValue = displayValue === '0' ? digit : displayValue + digit;
  }
}

function inputDecimal(dot) {
  if (main.waitingForSecondOperand === true) {
  	main.displayValue = "0."
    main.waitingForSecondOperand = false;
    return
  }

  if (!main.displayValue.includes(dot)) {
    main.displayValue += dot;
  }
}

function handleOperator(nextOperator) {
  const { firstOperand, displayValue, operator } = main
  const inputValue = parseFloat(displayValue);
  
  if (operator && main.waitingForSecondOperand)  {
    main.operator = nextOperator;
    return;
  }


  if (firstOperand == null && !isNaN(inputValue)) {
    main.firstOperand = inputValue;
  } else if (operator) {
    const result = calculate(firstOperand, inputValue, operator);

    main.displayValue = `${parseFloat(result.toFixed(7))}`;
    main.firstOperand = result;
  }

  main.waitingForSecondOperand = true;
  main.operator = nextOperator;
}

function calculate(firstOperand, secondOperand, operator) {
  if (operator === '+') {
    return firstOperand + secondOperand;
  } else if (operator === '-') {
    return firstOperand - secondOperand;
  } else if (operator === '*') {
    return firstOperand * secondOperand;
  } else if (operator === '/') {
    return firstOperand / secondOperand;
  }

  return secondOperand;
}

function resetCalculator() {
  main.displayValue = '0';
  main.firstOperand = null;
  main.waitingForSecondOperand = false;
  main.operator = null;
}

function updateDisplay() {
  const display = document.querySelector('.calculator-screen');
  display.value = main.displayValue;
}

updateDisplay();

const keys = document.querySelector('.calculator-keys');
keys.addEventListener('click', event => {
  const { target } = event;
  const { value } = target;
  if (!target.matches('button')) {
    return;
  }

  switch (value) {
    case '+':
    case '-':
    case '*':
    case '/':
    case '=':
      handleOperator(value);
      break;
    case '.':
      inputDecimal(value);
      break;
    case 'all-clear':
      resetCalculator();
      break;
    default:
      if (Number.isInteger(parseFloat(value))) {
        inputDigit(value);
      }
  }

  updateDisplay();
});