const email = document.getElementById("email");
const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
const submit_btn = document.getElementById("submit_btn");

const login_username = document.getElementById("login_username");
const login_password = document.getElementById("login_password");
const login_btn = document.getElementById("login_btn");

login_btn.disabled = true;

login_username.addEventListener("blur", () => {
    if (login_username.value == "") {
        login_btn.disabled = true;
        login_username.classList.add("is-invalid");
    }
    else {
        login_username.classList.remove("is-invalid");
    }
});

login_password.addEventListener("blur", () => {
    if (login_password.value == "") {
        login_btn.disabled = true;
        login_password.classList.add("is-invalid");
    }
    else {
        login_password.classList.remove("is-invalid");
        login_btn.disabled = false;
    }
})

email.addEventListener('blur', () => {
    // Validate email here
    let regex = /^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
    let str = email.value;
    console.log(regex, str);
    if (regex.test(str)) {
        email.classList.remove('is-invalid');
        validEmail = true;
    }
    else {
        email.classList.add('is-invalid');
        validEmail = false;
    }

    if (validEmail) {
        submit_btn.disabled = false;
    }
    else {
        submit_btn.disabled = true;
    }


});
