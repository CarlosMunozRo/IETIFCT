$(()=>{

    $body = $('body');

    if ($body.hasClass('home')) {
        $('.loader').animate({
            opacity: 0
        }, 1000, function() {
            $(this).remove();
        });
    }else if ($body.hasClass('wizard-body')) {
        $('.toggle-mobile-sidebar').click(function() {
            $('.sidebar').toggleClass('open');
    
        });
    }










    });