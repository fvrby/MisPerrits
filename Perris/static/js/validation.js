

function validate(){
    console.log("Hola!")
    txtName = document.getElementById("txtName");
    nameValidator = document.getElementById("nameValidator");
    if(txtName.value != "dON"){
        nameValidator.innerHTML = "uuuuu....";
    }
    else{
        nameValidator.innerHTML = "JEJEJE";
    }
}7