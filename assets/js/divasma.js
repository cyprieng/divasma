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
