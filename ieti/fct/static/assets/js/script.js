$(()=>{

    $('.list-group-item').on('click', function() {
        $('.glyphicon', this)
          .toggleClass('glyphicon-chevron-right')
          .toggleClass('glyphicon-chevron-down');
    });

    $('.loader').animate({
        opacity: 0
    }, 1000, function() {
        $(this).remove();
    });

});