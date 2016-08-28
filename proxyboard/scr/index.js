// Quick & dirty toggle to demonstrate modal toggle behavior
// Loading on wdocumet Loading

$(document).ready(function(){
  $('.modal').addClass('is-visible');


  $('.modal-close').click(function(e){
    e.preventDefault();
    $('.modal').removeClass('is-visible');
  })
})

// $('.modal-toggle').on('click', function(e) {
//   e.preventDefault();
//   $('.modal').toggleClass('is-visible');
// });
