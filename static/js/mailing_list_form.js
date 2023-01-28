// Contact form js and client side valdiation
$(document).ready(function () {
    // Taken from https://stackoverflow.com/questions/42229437/jquery-validation-accepts-even-if-input-contains-only-whitespaces
    jQuery.validator.addMethod("noSpace", function(value, element) { 
        return value.indexOf(" ") < 0 && value != ""; 
    }, "No space please and don't leave it empty");

    $("#mailingListForm").validate({
        rules: {
            name: {
                required: true,
            },
            email: {
                required: true,
                email: true,
                noSpace: true
            },
        },
        messages: {
            subject: {
                required: "Please enter a subject for your query",
            },
            email: {
                required: "Please enter your email address",
                email: "Must be an email: example@email.com",
                noSpace: "Your email cannot contain whitespace"
            },
        },
    });
});
