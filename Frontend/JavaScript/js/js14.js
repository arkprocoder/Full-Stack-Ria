let element = document.createElement('li');
console.log(element);
let text = document.createTextNode("akhil");
element.appendChild(text);
element.setAttribute("type", "square")

// let ele=document.getElementById("insert")
// ele.innerHTML=element.textContent;
// element.setAttribute("class", "childul")


let desc = document.createElement('b')
desc.id = "quotes";
console.log(desc);
desc.className = "quotes";
let insertdesc = document.createTextNode("WE WILL BE SOON MOVING ON TO DJANGO REACT");
desc.appendChild(insertdesc)

let getIdname = document.getElementById('friends')

getIdname.replaceWith(desc)
getIdname.removeAttribute("id")
getIdname.setAttribute('href', '//arkprocoder.tech')
getIdname.setAttribute('style','color:blue;')