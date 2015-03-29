/**
 * Fichier de scripts du panel de visu / modification des notes
 */

$( document ).ready(function() {

    $("#display-menu-btn").click( function(e) {

            var menuDisplayed = $("#display-menu-btn").hasClass("active");

            if (! menuDisplayed) {
                $("#display-menu-btn").addClass("active");

                $("#text-block").removeClass("col-md-12");
                $("#text-block").addClass("col-md-10");

                $("#param-block").removeClass("hidden");
                $("#param-block").addClass("col-md-2");
            } else {
                $("#display-menu-btn").removeClass("active");

                $("#text-block").removeClass("col-md-10");
                $("#text-block").addClass("col-md-12");

                $("#param-block").removeClass("col-md-2");
                $("#param-block").addClass("hidden");
            }
        });
});

