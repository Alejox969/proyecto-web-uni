var resultado;

function suma(){
     var num1 = document.getElementById("ingrese el valor 1");
     num1 = parseInt(num1);
     var num2 = prompt("ingrese el valor 2")
     num2 = parseInt(num2);
     resultado = num1 + num2;

     document.getElementById("demo").innerHTML="El resultado de "+num1+" + "+num2+" es: "+ resultado;
}

function resta(){
     var num1 = prompt("ingrese el valor 1");
     num1 = parseInt(num1);
     var num2 = prompt("ingrese el valor 2")
     num2 = parseInt(num2);
     resultado = num1 - num2;

     document.getElementById("demo").innerHTML="El resultado de "+num1+" - "+num2+" es: "+ resultado;
}

function multiplicacion(){
     var num1 = prompt("ingrese el valor 1");
     num1 = parseInt(num1);
     var num2 = prompt("ingrese el valor 2")
     num2 = parseInt(num2);
     resultado = num1 * num2;

     document.getElementById("demo").innerHTML="El resultado de "+num1+" * "+num2+" es: "+ resultado;
}

function division(){
     var num1 = prompt("ingrese el valor 1");
     num1 = parseInt(num1);
     var num2 = prompt("ingrese el valor 2")
     num2 = parseInt(num2);
     resultado = num1 / num2;

     document.getElementById("demo").innerHTML="El resultado de "+num1+" / "+num2+" es: "+ resultado;
}