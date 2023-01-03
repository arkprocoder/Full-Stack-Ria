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