// Contact form js and client side valdiation
$(document).ready(function () {

    jQuery.validator.addMethod("lettersonly", function (value, element) {
        return this.optional(element) || /^[a-zA-Z\- ]+$/i.test(value);
    }, "Letters, spaces and dashes only please");

    // Custom validator method taken from https://stackoverflow.com/questions/29026778/jquery-validation-method-phone-number-begin-with-plus-mark
    // and regex from https://forum.jquery.com/topic/number-and-plus-sign-only
    $.validator.addMethod("fnType", function(value, element) {
        return value.match(/^[+-]?\d+$/);
    },"Enter Valid  phone number");

    
    $("#payment-form").validate({
        rules: {
            full_name: {
                required: true,
                lettersonly: true,
            },
            email: {
                required: true,
                email: true,
            },
            phone_number: {
                required: true,
                fnType: true
            },
            street_address1: {
                required: true,
            },
            town_or_city: {
                required: true,
            },
            postcode: {
                required: true,
            },
            country: {
                required: true,
            }
        },
        messages: {
            full_name: {
                required: "Please enter a name",
                lettersonly: "Your name can only contain numbers, spaces and dashes",
            },
            email: {
                required: "Please enter your email",
                email: "Must be an email: example@email.com"
            },
            phone_number: {
                required: "Please enter a phone number",
                fnType: "Your number may only contain a country code symbol (+) and numbers"
            },
            street_address1: {
                required: "Please enter a street address",
            },
            town_or_city: {
                required: "Please enter a town or city",
            },
            postcode: {
                required: "Please enter your postcode",
            },
            country: {
                required: "Please enter your country",
            },
        },
    });
});