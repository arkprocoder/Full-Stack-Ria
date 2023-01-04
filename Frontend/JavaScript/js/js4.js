let name="ria"
let data =  "[1,2,3]"
console.log(name, typeof name);
name=2
console.log(name, typeof name);
name=String(2);
console.log(name, typeof name);

let bool=String(true);
console.log(bool, typeof bool);
bool=Boolean(bool);
console.log(bool, typeof bool);
bool=Boolean('ane');
console.log(bool, typeof bool);
data=Array(data)
console.log(data, typeof data);

let array= [1,2,3,4,5];
console.log(array.length);

let i=20;
console.log(i.toString());
console.log(typeof i.toString());

let number = Number('333.456789')
number=number.toFixed(2);
console.log(number, typeof number);

let num=parseFloat('456.789');
console.log(num, typeof num);

let a="23";
let b=20;
console.log(Number(a)+b);