console.log('HELLO WELCOME')

console.log('HELLO WELCOME')
showTodo();
let addTodo = document.getElementById("addTodo");
addTodo.addEventListener("click", function(e) {
    let gettext = document.getElementById("work");
    let todo = localStorage.getItem("todo");
    if (todo == null) {
        todoObj = [];

    } else {
        todoObj = JSON.parse(todo)
    }
    todoObj.push(gettext.value);
    localStorage.setItem("todo", JSON.stringify(todoObj));
    gettext.value = "";
    showTodo();
})

function showTodo() {
    let todo = localStorage.getItem("todo");
    console.log(todo)
    if (todo == null) {
        todoObj = [];

    } else {
        todoObj = JSON.parse(todo)
    }
    let html = " ";
    todoObj.forEach(function(element, index) {
        html += `
        <div class="noteCard my-2 mx-2 card">
                    <div class="card-body">
                        <h5 class="card-title">Sno : ${index + 1}</h5>
                        <p class="card-text"> ${element}</p>
                        <button id="${index}" onclick="deleteTodo(this.id)" class="btn btn-outline-dark">Delete Note</button>
                    </div>
                </div>
        
        
        `

    });
    let todoEle = document.getElementById("output");
    if (todoObj.length != 0) {
        todoEle.innerHTML = html;

    } else {
        todoEle.innerHTML = `No Works Are Pending`
    }

}

function deleteTodo(index) {
    let todo = localStorage.getItem("todo");
    if (todo == null) {
        todoObj = [];

    } else {
        todoObj = JSON.parse(todo)
    }
    todoObj.splice(index, 1);
    localStorage.setItem("todo", JSON.stringify(todoObj));
    showTodo();


}

let search = document.getElementById('searchTxt');
search.addEventListener("input", function() {

    let inputVal = search.value.toLowerCase();
    // console.log('Input event fired!', inputVal);
    let noteCards = document.getElementsByClassName('noteCard');
    Array.from(noteCards).forEach(function(element) {
        let cardTxt = element.getElementsByTagName("p")[0].innerText;
        if (cardTxt.includes(inputVal)) {
            element.style.display = "block";
        } else {
            element.style.display = "none";
        }
        // console.log(cardTxt);
    })
})
