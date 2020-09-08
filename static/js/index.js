$(document).ready(function() {
  
    $('.post-display').slick({
      slidesToShow: 1,
      slidesToScroll: 1,
      arrows: false,
      fade: true,
      asNavFor: '.post-wrapper'
    });
    $('.post-wrapper').slick({
      slidesToShow: 3,
      slidesToScroll: 1,
      asNavFor: '.post-display',
      centerMode: true,
      focusOnSelect: true,
      nextArrow: $('.next'),
      prevArrow: $('.prev'), 
    });
});