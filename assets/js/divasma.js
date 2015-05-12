$(function () {
  //Init bootstrap tooltip
  $('[data-toggle="tooltip"]').tooltip()

  $("#data_book #image_input").change(function(){
    var url = $("#data_book #image_input").val();
    $("<img>", {
      src: url,
      error: function() { $("#data_book .image-group").addClass("has-error"); },
      load: function() { $("#data_book #image").attr("src", url); }
    });
  });
})

/* Show a notification
 *
 * type: type of the notification(danger or success).
 *
 * text: text of the nofification
*/
function notify(type, text) {
  $("#notification").removeClass();
  $("#notification").addClass("alert alert-"+ type +" animated fadeInUp").html(text);
}
