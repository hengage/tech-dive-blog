// "use strict";
// console.log('worked')


// const signupForm = document.getElementById("signup_form");

// const signupFormFirstNameError = document.getElementById("signup_firstname_error");
// const signupFirstname = signupForm.first_name
// console.log(signupFirstname)

// signupForm.addEventListener('submit', event => {
//     // event.preventDefault();
    
//     const namePattern = /[a-zA-Z]/

//     const isValid = signupFirstname.value.length > 0 
//     // const isValid = signupFirstname.value.length > 0 || namePattern.test(signupFirstname)
//     // const isValid =  namePattern.test(signupFirstname)

//     if (!isValid) {
//         signupFormFirstNameError.textContent = 'first name should be greater than 5'
//         return false
//     } else {
//         signupFormFirstNameError.textContent = ''
//         return true
//     }

// })


const validateSignupFormData = () => {
    const signupForm = document.getElementById("signup_form");
    const signupFirstName = signupForm.first_name
    const signupLastName = signupForm.last_name
    const signupPassword = signupForm.password1
    console.log({signupPassword: signupPassword.value})
    console.log({signupFirstName: signupFirstName.value})

    const whiteSpaceRegexPattern  = /\s/g; //Check for whitespaces
    let error = new Array;
    console.log({error})

    // Test the fields against the regex to check for whitespaces
    const firstNameContainsWhiteSPace = whiteSpaceRegexPattern.test(signupFirstName.value)
    const lastNameContainsWhiteSPace = whiteSpaceRegexPattern.test(signupLastName.value)
    const passwordContainsWhitePace = whiteSpaceRegexPattern.test(signupPassword.value)

    const signupFormFirstNameError = document.getElementById("signup-firstname-error");
    if ( firstNameContainsWhiteSPace ) {
        error = 'First name should not contain spaces'
        signupFormFirstNameError.textContent = 'First name should not contain whitespace'
        
    } else {
        signupFormFirstNameError.textContent = ''
    } 


    const signupFormLastNameError = document.getElementById("signup-lastname-error");
    if ( lastNameContainsWhiteSPace ) {
        error = 'Last name should not contain spaces'
        signupFormLastNameError.textContent = 'Last name should not contain whitespace'
    }   else {
        signupFormLastNameError.textContent = ''
    }

    let passwordError =  document.getElementById('signup-password-error')
    if ( passwordContainsWhitePace ) {
        error = 'Password cannot contain spaces'
        passwordError.textContent = 'Password cannot contain whitespace'
    } else {
        passwordError.textContent = ''
    }

    if (error?.length > 0) {
        console.log({error})
        return false
    } else {
        signupFormFirstNameError.textContent = ''
        return true
    }
}

