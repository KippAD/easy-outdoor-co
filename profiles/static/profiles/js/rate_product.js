// Contact form js and client side valdiation
$(document).ready(function () {
    $("input[name='rating']:checked").val();
    $("label[for='id_comment']").hide();

    $("#reviewForm").validate({
        rules: {
            subject: {
                required: true,
                minlength: 10,
                maxlength: 50,
            },
            email: {
                required: true,
                email: true ,          
            },
            comment: {
                required: true,
                minlength: 15   
            }
        },
        messages: {
            subject: {
                required: "Your message must included a subject",
                minlength: "The subject must be at least 10 characters",
                maxlength: "The subject must be shorter than 50 characters.",
            },
            email: {
                required: "Please enter your email",
                email: "Must be an email: example@email.com"
            },
            comment: {
                required: "Your message cannot be empty",
                minlength: "Your message must be at least 50 characters"
            },
        },
    });

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
                required: true,
                lettersonly: true
            },
            last_name: {
                required: true,
            },
            email: {
                required: true,
            },
        },
        messages: {
            username: {
                required: "You must have a username",
                minlength: "Your username must be longer than 5 characters.",
                maxlength: "Your username must be shorter than 12 characters.",
                noSpace: "Your username cannot contain spaces or special characters",
                alphanumeric: "Your username cannot contain spaces or special characters"
            },
            first_name: {
                required: "Please enter your first name",
                digits: "Your name cannot contain numbers"
            },
            last_name: {
                required: "Please enter your first name",
            },
            email: {
                required: "Please enter your email",
                email: "Must be an email: example@email.com"
            },
        },
    });
});
