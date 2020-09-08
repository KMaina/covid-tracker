$(document).ready(function(){
    $('form').submit(function(event){
      event.preventDefault()
      form = $("form")
  
      $.ajax({
        'url':'/profile/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
      })// END of Ajax method
      $('#id_name').val('')
      $("#id_email").val('')
      $('#id_phone').val('')
      $("#id_location").val('')
    }) // End of submit event
  
  }) // End of document ready function