
// console.log("loops");

// for (let i = 1; i <= 10; i++) {
//     console.log(i);
// }


// let j = 0;
// while (j < 11) {
//     console.log(j);
//     j = j + 1;

// }



let k = 0;
do {
    console.log(k + 1);
    // console.log("before while");

    k += 1;
    // k=k+1
}
while (k < 11);



// break statements

let s = 0;
do {
    if (s === 5) {
        break;
    }
    console.log(s + 1);
    s += 1;

}
 while (s < 100);

 
 
// continue statements

// let r = 0;
// console.log("-conntinue");
// do {
//     if (r === 5) {
//         r=r+1;
//         continue
//     }
//     r=r+1;
//     console.log(r);

// } while (r < 10);

// for(let i=1;i<=20;i++)
// {
//     if(i==15){
//         continue
//     }
//     console.log(i);
// }

let array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
array.forEach(function(item,index,array) {
    console.log(item,index,array);
    // can give index and array as arguements also
});
array.forEach(function(item) {
    console.log(item);
   
});
console.log("done ");


array.forEach(function(item,index) {
    console.log(item,index);
   
});
console.log("done ");



let obj = {
    name: "anees ",
    age:22,

    // cannot use = symbol and intialize;remember it
    status: 'programmer',
    college: 'svce'
}


let key;
for (key in obj) {
    console.log(`the ${key} of object is ${obj[key]}`)
    console.log(`the {name} of object is ${obj[name]}`)
    console.log(`the {name} of object is {anees}`)
}