$(function () {
  //Init bootstrap tooltip
  $('[data-toggle="tooltip"]').tooltip()

  //Image previsualization in add book form
  $("#data_book #image_input").change(function(){
    var url = $("#data_book #image_input").val();

    //Test image
    $("<img>", {
      src: url,
      error: function() { $("#data_book .image-group").addClass("has-error"); },
      load: function() { $("#data_book #image").attr("src", url); }
    });
  });

  //Show/Hide the original book form in add book form
  $("#show_hide_translation").change(function(){
    if($("#show_hide_translation").is(":checked"))
      $("#data_book .translation_data").css("display", "block");
    else
      $("#data_book .translation_data").css("display", "none");
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
