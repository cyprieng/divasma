(function( $ ){
  /* Set the selected inputs color to red. This function use the form as
  * selector.
  *
  * fields: list of field by id without '#' (ex: "field1 field2")
  */
  $.fn.setError = function(fields) {
    //Reset errors
    this.children(".form-group").each(function(){
      $(this).css("color", "#000");
      $(this).children("input").css("border-color", "#ccc");
    });

    //Set errors
    var ids = fields.split(" ");
    this.children(".form-group").each(function(){
      if($.inArray($(this).children("input").attr("id"), ids) >= 0){
        $(this).css("color", "#E46969");
        $(this).children("input").css("border-color", "#E46969");
      }
    });
  };

  /* Set all inputs color to red. This function use the form as
  * selector.
  */
  $.fn.setErrorAll = function() {
    //Reset errors
    this.children(".form-group").each(function(){
      $(this).css("color", "#000");
      $(this).children("input").css("border-color", "#ccc");
    });

    //Set errors
    this.children(".form-group").each(function(){
      $(this).css("color", "#E46969");
      $(this).children("input").css("border-color", "#E46969");
    });
  };
})( jQuery );

/*
* Validate the login form
*/
function validateLogin(){
  if(!$("#user").val() || !$("#password").val()){
    notify("danger", "Fill all inputs");
    return false;
  }
  return true;
}

/*
* Validate the register form
*/
function validateRegister(){
  if($("#username").val() && $("#password").val() && $("#repeat_password").val() && $("#email").val() && $("#repeat_email").val()){ //Check if all is filled
     if($("#username").val().length < 39 && $("#username").val().length > 3){ //Check username length
       var re = /^[a-z0-9]+-?[a-z0-9]+$/i;
       if(re.test($("#username").val())){ //Check username
         if($("#password").val() == $("#repeat_password").val()){ //Check if passwords match
           if($("#password").val().length > 7){ //Check password length
             if($("#email").val() == $("#repeat_email").val()){ //Check if emails match
               re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
               if(re.test($("#email").val())){ //Check email
                 return true;
               }
               else{
                 notify("danger", "Email is invalid");
                 $("#register").setError("email");
                 return false;
               }
             }
             else{
               notify("danger", "Emails don't match");
               $("#register").setError("email repeat_email");
               return false;
             }
           }
           else{
             notify("danger", "Password length must be at least 7");
             $("#register").setError("password");
             return false;
           }
         }
         else{
           notify("danger", "Passwords don't match");
           $("#register").setError("password repeat_password");
           return false;
         }
       }
       else{
         notify("danger", "Username must only contains alphanumerics and '-' neither at the begining or the end");
         $("#register").setError("username");
         return false;
       }
     }
     else{
       notify("danger", "Username length must be between 4 and 38");
       $("#register").setError("username");
       return false;
     }
  }
  else{
    notify("danger", "Fill all inputs");
    $("#register").setErrorAll();
    return false;
  }
}
