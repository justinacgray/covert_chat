
$(document).ready(function () {
    // Initially hide both forms
    $('.register-form').hide();

    // Toggle Function
    $('.toggle').click(function () {
        var icon = $(this).find('i'); // Get the icon within the clicked element

        // Check if the registration form is visible
        if ($('.register-form').is(':visible')) {
            // Hide the registration form and show the login form with animation
            $('.register-form').slideUp("slow", function () {
                $('.login-form').slideDown("slow");
            });

            // Switch the icon to 'fa-code'
            icon.removeClass('fa-paint-brush').addClass('fa-times');
        } else {
            // Hide the login form and show the registration form with animation
            $('.login-form').slideUp("slow", function () {
                $('.register-form').slideDown("slow");
            });

            // Switch the icon to 'fa-paint-brush'
            icon.removeClass('fa-times').addClass('fa-paint-brush');
        }
    });
});
