/*  ---------------------------------------------------
    Template Name: Hotel Template
    Description: Hotel HTML Template
    Author: colorlib
    Author URI: https://www.colorlib.com/
    Version: 1.0
    Created: colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {

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

    /*------------------
        Preloader
    
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");
    });
    --------------------*/
    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

 







  /*** delete ads ***/
    
    const  events_date = document.getElementById('ad-detail-date')
    const timer = events_date.getAttribute('data-d')
    const ad_pk = events_date.getAttribute('data-id')
    
       //console.log(timer)
       const eventS = Date.parse(timer)
       //console.log(eventS)
        
       // Update the count down every 1 second
       var x = setInterval(function() {

       // Get today's date and time
       var now = new Date().getTime();

       // Find the distance between now and the count down date
       var distance = eventS - now;

       // Time calculations for days, hours, minutes and seconds
       var days = Math.floor(distance / (1000 * 60 * 60 * 24));
       var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
       var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
       var seconds = Math.floor((distance % (1000 * 60)) / 1000);

       // Output the result in an element with id="demo"
       //prc.innerText = days + "d " + hours + "h "
       //+ minutes + "m " + seconds + "s ";

       // If the count down is over, write some text
       if (distance < 0) {
           clearInterval(x);
           //console.log('done')
           delete_post(ad_pk)
            
        }
       }, 1000);


       function delete_post(ads_id) {
    
        $.ajax({
                type: "POST",
                url: "/delete-ads/",
                data: {
                    ads_id: ads_id,
                    
                     csrfmiddlewaretoken: csrftoken,
                },
                
                success: function(data) {
                   
                     //console.log(data)
     
     
                },
                
            });
    }



    
    
   /**** subcribe form */
  $('#plans').change(function () {
    console.log($(this).val())
   
     
    if ($(this).val() == 2000)
    {
        document.getElementById('rio').innerText=  + 200
       
    }else if ($(this).val() == 5000) {
       document.getElementById('rio').innerText= 500
    }
    else if ($(this).val() == 10000) {
       document.getElementById('rio').innerText= 1000
    }

    

  })


  function submit_form () {
    $.ajax({
        type: "POST",
        url: "/taskers/subscribe/",
        data: {
            plan: $('#plans').val(),
            csrfmiddlewaretoken: csrftoken,
        },
        
        success: function(data) {
           
             console.log(data)


        },
        
    });
  }

 
  document.getElementById("sub-btn").addEventListener("submit", function(e) {
    var PBFKey = "FLWPUBK-aa82cac8ee08f5bb206f937db274081a-X";
    
    getpaidSetup({
      PBFPubKey: PBFKey,
      customer_email: "user@example.com",
      customer_firstname: "Temi",
      customer_lastname: "Adelewa",
      custom_description: "Pay Internet",
      custom_logo: "http://localhost/communique-3/skin/frontend/ultimo/communique/custom/images/logo.svg",
      custom_title: "Communique Global System",
      amount: 2000,
      customer_phone: "234099940409",
      country: "NG",
      currency: "NGN",
      txref: "rave-123456",
      integrity_hash: "6800d2dcbb7a91f5f9556e1b5820096d3d74ed4560343fc89b03a42701da4f30",
      onclose: function() {},
      callback: function(response) {
        var flw_ref = response.tx.flwRef; // collect flwRef returned and pass to a                  server page to complete status check.
        console.log("This is the response returned after a charge", response);
        if (
          response.tx.chargeResponseCode == "00" ||
          response.tx.chargeResponseCode == "0"
        ) {
          // redirect to a success page
           submit_form()
        } else {
          // redirect to a failure page.
        }
      }
    });
  });
 






})(jQuery);


