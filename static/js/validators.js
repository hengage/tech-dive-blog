"use strict";

const validate = (error) => {
    const signupForm = document.getElementById("signup_form");
    const signupFirstName = signupForm.first_name
    const signupLastName = signupForm.last_name
    const signupPassword = signupForm.password1

    const signupFormFirstNameError = document.getElementById("signup-firstname-error");
    if ( signupFirstName.value.includes(' ') ) {
        error.push('First name should not contain spaces')
        signupFormFirstNameError.textContent = 'First name should not contain whitespace'
    }   else {
        signupFormFirstNameError.textContent = ''
    } 

    const signupFormLastNameError = document.getElementById("signup-lastname-error");
    if ( signupLastName.value.includes(' ') ) {
        error.push('Last name should not contain spaces')
        signupFormLastNameError.textContent = 'Last name should not contain whitespace'
    } else {
        signupFormLastNameError.textContent = ''
    }

    const passwordError =  document.getElementById('signup-password-error')
    if ( signupPassword.value.includes(' ') ) {
        error.push('Password cannot contain spaces')
        passwordError.textContent = 'Password cannot contain whitespace'
    }   else {
        passwordError.textContent = ''
    }
}


const validateSignupFormData = () => {
    const error = new Array;
    console.log({error})

    validate(error)
  
    if (error.length > 0) {
        console.log({error})
        return false
    } 
    return true
}

