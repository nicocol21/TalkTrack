

    document.getElementById("form-action").addEventListener("submit", function(e) {
    e.preventDefault(); 
    
    let usuario = document.getElementById("email").value;
    let password = document.getElementById("password").value;


    let correoval = "correo@correo.com";
    let passwordval = "12345";


    if (usuario === correoval && password === passwordval) {
        window.location.href = "views/layout.html"; 
    } else {
        alert("Usuario o contraseña incorrectos"); 
    }
});

 
const addForm = document.getElementById ("form-action")
addForm.addEventListener("submit", (e) => {
    if (addForm.checkValidity() === false){
        e.preventDefault()
        e.stopPropagation()
        addForm.classList.add('was-validated')
        return false
     }
    })
