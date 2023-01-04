let marks = [10, 20, 30, 40, 50];
const fruits = ['orange', 'mango', 'pineapple', 'mosambi'];
const mix = ['str', 85, 86, 87, [5, 7,8]];
const array = new Array(23, 34, 44, 'APPLE');
console.log(array)
console.log(mix);
console.log(fruits);
console.log(marks[4]);
console.log(array.length);
console.log(Array.isArray([1, 2, 3]));
let value = marks.indexOf(50);
console.log(value);
let myar=[1,2,3,4,5];
console.log(myar);
myar.unshift(61)
console.log(myar);
myar.pop()
console.log(myar);
console.log(myar.splice(2, 2));
console.log(marks.reverse());
console.table(marks);
let mark1 = [60, 70, 80, 90, 100];
marks = marks.concat(mark1);
// // it will show error so we need to use let type varaible for marks now am changing it
console.log(marks);

let myobj = {
    name: 'ANEES',
    class: '3rd year BE',
    isActive: true,
    cgpa: 8.0

}
console.log(myobj);
console.table(myobj);