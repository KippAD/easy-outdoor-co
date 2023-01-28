// Contact form js and client side valdiation
$(document).ready(function () {
    $("#contactForm").validate({
        rules: {
            subject: {
                required: true,
                minlength: 5,
            },
            email: {
                required: true,
            },
            message: {
                required: true,
                minlength: 25,
            },
        },
        messages: {
            subject: {
                required: "Please enter a subject for your query",
                minlength: "The subject must be longer than 5 characters."
            },
            email: {
                required: "Please enter your email address",
                email: "Must be an email: example@email.com"
            },
            message: {
                required: "Please enter a message",
                minlength: `You message must be longer than 25
                characters - please be descriptive`
            },

        },
    });
});
