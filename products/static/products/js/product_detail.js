$(document).ready(function () {
    $(".stock-warning").hide();

    $(".size-box:last").css("margin", 0);

    $("input:radio[name=sizes]:not(:disabled):first").attr("checked", true);
    $(".append-warning").append($(".stock-warning"));

    if ($("input[name=sizes]:checked").attr("data-stock") <= 6) {
        let key = $("input[name=sizes]:checked").val();
        $("p[data-key=" + key + "]").show();
    }

    $("input:radio[name=sizes]").change(function () {
        if ($(this).is(":checked")) {
            let key = $("input[name=sizes]:checked").val();
            let value = $("p[data-key=" + key + "]").attr("data-value");
            $(".stock-warning").hide();

            if (value < 10) {
                $("p[data-key=" + key + "]").show();
            }
        }
    });
    // Taken from css tricks : https://css-tricks.com/number-increment-buttons/
    $(".quantity-input").on("click", function () {
        var oldValue = $("#quantity").val();

        if ($(this).data("value") == "+") {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don"t allow decrementing below zero
            if (oldValue > 1) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 1;
            }
        }
        $("#quantity").val(newVal);
    });
});