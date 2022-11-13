"use strict";

const signupForm = document.getElementById("signup_form");
const signupFirstName = signupForm.first_name
const signupLastName = signupForm.last_name
const signupPassword = signupForm.password1
const signupEmail = signupForm.email
console.log({signupEmail})


const validate = (error) => {
    const signupFormFirstNameError = document.getElementById("signup-firstname-error-text");
    if ( signupFirstName.value.includes(' ') ) {
        error.push('First name should not contain spaces')
        signupFormFirstNameError.textContent = 'First name should not contain whitespace'
    }  else if ( signupFirstName.value === '' ) {
        error.push('First name is required')
        signupFormFirstNameError.textContent = 'First name is required' 
    } else {
        signupFormFirstNameError.textContent = ''
    } 

    const signupFormLastNameError = document.getElementById("signup-lastname-error-text");
    if ( signupLastName.value.includes(' ') ) {
        error.push('Last name should not contain spaces')
        signupFormLastNameError.textContent = 'Last name should not contain whitespace'
    } else if ( signupLastName.value === '' ) {
        error.push('Last name is required')
        signupFormLastNameError.textContent = 'Last name is required'
    } else {
        signupFormLastNameError.textContent = ''
    }

    const signupEmailError = document.getElementById('signup-email-error-text')
    if ( signupEmail.value === '') {
        error.push('Email is required')
        signupEmailError.textContent = 'Email is required'
    } else {
        signupEmailError.textContent = ''
    }


    const passwordError =  document.getElementById('signup-password-error-text')
    if ( signupPassword.value.includes(' ') ) {
        error.push('Password cannot contain spaces')
        passwordError.textContent = 'Password cannot contain whitespace'
    } else  if ( signupPassword.value === '' ) {
        error.push('Psassword is required')
        passwordError.textContent = 'Password is required'
    } else {
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

