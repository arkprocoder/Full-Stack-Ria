console.log("he");
let name="ria ";
let greet="good morning";
console.log(name + greet);
let html;
html="<h1> hello ria </h1>" + "<p> it is a training institue </p>"
html=html.concat("hello");
html=html.concat(' ','ria')
console.log(html);

console.log(html.toLowerCase());
console.log(html.toUpperCase());
console.log(html.indexOf('ria'));
console.log(html[5]);
console.log(html.endsWith("ri"));
console.log(html.startsWith("ri"));
console.log(html.substring(10,15));
console.log(html.split(' '));
console.log(html.replace('hello','bye'));
console.log(html.slice(0,23));
console.log(html.slice(-1,));
console.log(html.slice());
console.log(html.slice(1,30));


let place= 'Marathalli';
let peers=[
    "manohar",
    "sriram",
    "akash",
    "bhanu"
]
let myhtml=`

<h1> Full Stack at RIA ${place} </h1>
<hr>
<h3>There are the students :</h3>
<p> ${peers} </p>

`
document.body.innerHTML+=myhtml;
// document.body.innerHTML=document.body.innerHTML + myhtml;
