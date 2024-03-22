function calAngle() {
    // User inputs number of sides
    var number1 = document.getElementById('number1').value;

    
    // Calculate the size of one agle
    var angle = ((number1 - 2)* 180);

    // Display the result
    document.getElementById('result').innerText = "The sum of angles is: " + angle;
}

function caloneAngle() {
    var number1 = document.getElementById('number1').value;
    
    
    // Calculate the size of one agle
    var oneAngle = ((number1 - 2)* 180)/ number1;

    // Display the result
    document.getElementById('resultone').innerText = "The angle is: " + oneAngle;
    
}
