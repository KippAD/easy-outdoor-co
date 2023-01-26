// Contact form js and client side valdiation
$(document).ready(function () {
    $('label').hide()
    $('#id_category').addClass('form-select')

    // Change option text
    $('select option:contains("---------")').text('Category *');
    $('select option:contains("jackets_coats")').text('Jackets & Coats');
    $('select option:contains("equipment")').text('Equipment');
    $('select option:contains("trousers")').text('Trousers');
    $('select option:contains("fleeces_jumpers")').text('Fleeces & Jumpers');
    $('select option:contains("footwear")').text('Footwear');
    $('select option:contains("t-shirts")').text('T-Shirts');
    $('select option:contains("socks")').text('Socks');
    $('select option:contains("sunglasses")').text('Sunglasses');
    $('select option:contains("headwear")').text('Headwear');
    $('select option:contains("gloves")').text('Gloves');

    // Only allows letters and dashes for slug
    jQuery.validator.addMethod("lettersonly", function(value, element) {
        return this.optional(element) || /^[a-zA-Z0-9\-]+$/i.test(value);
    }, "Letters and spaces only please");

    // Form validation
    $('.productForm').validate({
        rules: {
            category: {
                required: true,
            },
            name: {
                required: true,
            },
            slug: {
                lettersonly: true
            },
            desc: {
                required: true,
            },
            price: {
                required: true,
            },
            image_url: {
                required: true,
                url: true
            },
        },
        messages: {
            category: {
                required: "Please select a category",
            },
            name: {
                required: "Please enter a product name",
            },
            slug: {
                lettersonly: "Your slug can only contain letters and dashes",
            },
            desc: {
                required: "Please enter a product description",
            },
            price: {
                required: "Please enter a product price",
            },
            image_url: {
                required: "Please enter a URL for your product image",
                url: "Must be a valid URL"
            },

        },
    });
});
