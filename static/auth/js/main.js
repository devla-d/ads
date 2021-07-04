
(function ($) {
    "use strict";
     /* csrf token */
     function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');


    /*==================================================================
    [ Focus input ]*/
    $('.input100').each(function(){
        $(this).on('blur', function(){
            if($(this).val().trim() != "") {
                $(this).addClass('has-val');
            }
            else {
                $(this).removeClass('has-val');
            }
        })    
    })

    $('.loginform').on('submit',function (event) {
        event.preventDefault();
        

        $.ajax({
            type: "POST",
            url: "/login/",
            data: {
                username:$('#username').val(),
                password:$('#password').val(),
                  csrfmiddlewaretoken: csrftoken,
            },
            beforeSend: function() {
              var btn = document.getElementById('log-b')
              btn.classList.add('disabled');
              document.getElementById('log-b').innerText = 'Authenticating..'
            
            },
            success: function(data) {
               
               if( data.successful)
               {
                 document.getElementById("response-msg").innerText = data.successful
                 document.getElementById('log-b').innerText = 'Ridirecting..'
                 var go_to = data.dest
                 window.location.href = go_to
               } else {
                 document.getElementById("response-msg").innerText = data.failed
                 //setTimeout(function(){ window.location.reload(); },1100);
                 var btn = document.getElementById('log-b')
                 btn.classList.remove('disabled');
                 btn.innerText= 'Login'
               }
               
 
 
            },
            /**complete: function() {
                document.getElementById('log-b').innerText = 'Ridirecting..'
                
            },*/
        });
    })


  
  
    /*==================================================================
    
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    
    var showPass = 0;
    $('.btn-show-pass').on('click', function(){
        if(showPass == 0) {
            $(this).next('input').attr('type','text');
            $(this).addClass('active');
            showPass = 1;
        }
        else {
            $(this).next('input').attr('type','password');
            $(this).removeClass('active');
            showPass = 0;
        }
        
    });
    /*==================================================================
    [ Show pass ]*/


})(jQuery);