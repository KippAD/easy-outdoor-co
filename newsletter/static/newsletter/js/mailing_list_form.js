// Contact form js and client side valdiation
$(document).ready(function () {
    $('#mailingListForm').validate({
        rules: {
            name: {
                required: true,
                minlength: 5,
            },
            email: {
                required: true,
            },
        },
        messages: {
            name: {
                required: "Please enter a name",
                minlength: "The subject must be longer than 5 characters."
            },
            email: {
                required: "Please enter your email address",
                email: "Must be an email: example@email.com"
            },
        },
    });
});