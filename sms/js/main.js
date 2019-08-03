
users = ["Lakshman","Pradeep","Thulasi"]

function callOn(){
   message = "<h3>Status is ON</h3>"
   document.getElementById("res").innerHTML = message; 
}   
function callOff(){
    message = "<h3>Status is OFF</h3>" 
    document.getElementById("res").innerHTML = message;
}
function checkUser(){
    name = prompt("Enter your name:")
    flag = false
    for(let i=0;i<users.length;i++){
        if(name == users[i]){
            alert("Deleted record by :"+name)
            flag = true
        }
    }
    if (!flag){
       alert("You are not authorised to delete records...") 
    }
}

function register(){
    var reg = document.getElementById("reg");
    //validate()
    name = reg["name"].value
    gender = reg["gender"].value
    branch = reg["branch"].value
    
    obj = localStorage.getItem("students")
    students = []
    if(obj){
        students = JSON.parse(obj);
    }
    student = {"name":name,"gender":gender,"branch":branch}
    if(!students){
        students = []
    }
    students.push(student)
    localStorage.setItem("students",JSON.stringify(students)) 
    showData()
    
}


function showData(){
    obj = localStorage.getItem("students")
    students = []
    if(obj){
        students = JSON.parse(obj);
    }  
    
    str = "<table border='1'><tr><th>Name</th><th>Branch</th></tr>";
    for(i = 0;i<students.length;i++){
        s = students[i]
        str+="<tr>";
        str += "<td>"+s["name"]+"</td><td>"+s["branch"]+"</td>";
        str+="</tr>";
    }
    str += "</table>";
    document.getElementById("showData").innerHTML= str
}

showData()