// Contact form js and client side valdiation
$(document).ready(function () {
    
    // Taken from https://stackoverflow.com/questions/42229437/jquery-validation-accepts-even-if-input-contains-only-whitespaces
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
    }, "No space please and don't leave it empty");

    jQuery.validator.addMethod("lettersonly", function(value, element) {
        return this.optional(element) || /^[a-zA-Z\-]+$/i.test(value);
    }, "Letters and spaces only please");
    
    // Custom validator method taken from https://stackoverflow.com/questions/29026778/jquery-validation-method-phone-number-begin-with-plus-mark
    // and regex from https://forum.jquery.com/topic/number-and-plus-sign-only
    $.validator.addMethod("fnType", function(value, element) {
        return value.match(/^[+-]?\d+$/);
    },"Enter Valid  phone number");


    $("#userForm").validate({
        rules: {
            username: {
                required: true,
                minlength: 5,
                maxlength: 20,
                noSpace: true,
                alphanumeric: true
            },
            first_name: {
                lettersonly: true
            },
            last_name: {
                lettersonly: true
            },
            email: {
                required: true,
                email: true              
            },
            default_phone_number: {
                fnType: true
            }
        },
        messages: {
            username: {
                required: "You must have a username",
                minlength: "Your username must be longer than 5 characters.",
                maxlength: "Your username must be shorter than 20 characters.",
                noSpace: "Your username cannot contain spaces or special characters",
                alphanumeric: "Your username cannot contain spaces or special characters"
            },
            first_name: {
                lettersonly: "Your first name must only include letters or dashes",
            },
            last_name: {
                lettersonly: "Your last name must only include letters or dashes",
            },
            email: {
                required: "Please enter your email",
                email: "Must be an email: example@email.com"
            },
            default_phone_number: {
                fnType: "Your number may only contain a country code symbol (+) and numbers"
            },
        },
    });
});
