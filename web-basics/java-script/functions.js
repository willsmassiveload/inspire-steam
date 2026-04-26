var x = 20;
var y = 30;
// definition
function add_numbers(x,y){
    sum = x + y;
    return sum;
}

//calling function
console.log(add_numbers(56,12));


function sumFirst50() {
    let sum = 0;

    for (let i = 1; i <= 50; i++) {
        sum += i;
    }

    return sum;
}

console.log(sumFirst50());