console.log("fetch api");

// function getDataTxt(){
//     console.log("Started getData")
//     url = "ark.txt";
//     fetch(url).then((response)=>{
//         console.log("Inside first then")
//         return response.text();
//     }).then((data)=>{
//         console.log("Inside second then")
//         console.log(data);
//     })
// }

// getDataTxt()



function getGitHubData(){

    url = "https://api.github.com/users";
    fetch(url).then((response)=>{
        
        return response.json();
    }).then((data)=>{
        
        console.log(data);
    }).then(()=>{
        console.log('data is fetched');
    })
}
// getGitHubData()


function postData(){
    url = "https://jsonplaceholder.typicode.com/posts";

    params = {
        method:'post',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: "anees rehman khan",
            body: "Developer",
            userId: 110
        })
    }
    fetch(url, params).then(response=> response.json())
    .then(data => console.log(data)
    )
}


function getData(){
    fetch('https://jsonplaceholder.typicode.com/photos')
    .then(response => response.json())
    .then(json => console.log(json))
}

postData();
getData()