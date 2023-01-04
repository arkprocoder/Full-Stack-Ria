/* console.log("if else loop");
const age = 25;

if (age >= 2) {
    console.log("age is 25");
} 

if (age >= 29) {
    console.log("age is 29");
} 
else {
    console.log("age is < 29");
}



if (age === 2) {
    console.log("age is 25");
} 
else if (age === 22) {
    console.log("age is not 22");
} 
else if (age === 23) {
    console.log("age is not 23");
} 
else if (age === 24) {
    console.log("age is not 24");
} 
else {
    console.log("age is not 22")
}




let age1 = "5"; {
    if (age1 === 5) {
        console.log(true);
    } else {
        console.log(false);

    }
    if (age1 == 5) {
        console.log(true);
    } else {
        console.log(false);

    }
}

// can use booleans value also
const doesDrive = false;
if (!doesDrive) {
    console.log("can drive")
} else {
    console.log("cannot drive")
}


let bro = false;
let bro1 = false; {
    if (bro || bro1) {
        console.log("true bro")
    } else {
        console.log("false bro")
    }
}



// ternary operator
let your_age = 2;
console.log(your_age === 22 ? 'age is 22' : 'age is not 22');
// first it will check the condition if satisfy it prints or else after : colon what there it gona print;


let name=false
let name1=true
let lname=false
let fname=true
let mname=false
if(name && name1 && lname){
    console.log("if");
}
else if (name || mname || name1 && !fname){
    console.log("else if 1");
}
else if (!name1 && name || !lname && fname){
    console.log("else if 2");
}
else if (name || lname && !fname && mname){
    console.log("else if 3");
}
else{
    console.log("else");
}

*/


// switch case statements;
let your_age = 25;
switch (your_age) {
    // switch(22)
    case 18:
        console.log("you are 18")
        break;

    case 22:
        console.log("you are 22")
        break;


    case 25:
        console.log("you are 25")
        break
        

    case 30:
        console.log("you are 30")
        break;

    case 31:
        console.log("you are 31")
        break;

    default:
        console.log("unvalid");
        break;
}