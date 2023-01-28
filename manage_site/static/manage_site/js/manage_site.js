$(document).ready(function () {

    $(".data-table").DataTable();

    $(".admin-menu-link").click(function (e) {
        $(".data-table").DataTable();
        $(".nav-link").removeClass("active text-white");
        $(".admin-db").addClass("d-none");
        $(".admin-menu-link").removeClass("active");
        $(this).addClass("active");
        
        if ($(this).is(":contains('Products')"))  {
            $("#manage-products").removeClass("d-none");
        } else if ($(this).is(":contains('Stock')")) {
            $("#manage-stock").removeClass("d-none");
        } else if ($(this).is(":contains('Orders')")) {
            $("#manage-orders").removeClass("d-none");
        } else if ($(this).is(":contains('Users')")) {
            $("#manage-users").removeClass("d-none");
        } else if ($(this).is(":contains('Mailing List')")) {
            $("#manage-mailing").removeClass("d-none");
        }
    });
    
});