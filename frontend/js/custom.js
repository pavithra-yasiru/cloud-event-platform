
 /* jQuery Pre loader
  -----------------------------------------------*/
$(window).load(function(){
    $('.preloader').fadeOut(1000); // set duration in brackets    
});


/* Mobile Navigation
    -----------------------------------------------*/
$(window).scroll(function() {
    if ($(".navbar").offset().top > 50) {
        $(".navbar-fixed-top").addClass("top-nav-collapse");
    } else {
        $(".navbar-fixed-top").removeClass("top-nav-collapse");
    }
});

/* API Configuration
-----------------------------------------------*/

const API = {

    EVENT: "http://13.233.81.248:30081",

    PROGRAM: "http://13.233.81.248:30082",

    REGISTRATION: "http://13.233.81.248:30084",

    ANALYTICS: "http://13.233.81.248:30085"

};

/* Global Analytics Function
-------------------------------------------*/

function sendAnalytics(eventType, page) {

    const analytics = {

        event_type: eventType,

        page: page,

        event_time: new Date().toISOString()

        };

    fetch(`${API.ANALYTICS}/analytics`, {

        method: "POST",

        headers: {

            "Content-Type": "application/json"

        },

        body: JSON.stringify(analytics)

    })

    .then(response => response.json())

    .then(data => console.log("Analytics:", data))

    .catch(error => console.error(error));

}


/* HTML document is loaded. DOM is ready.
-------------------------------------------*/

$(document).ready(function() {

    $('.navbar-collapse a').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    sendAnalytics(
        "Homepage Visit",
        "Home"
    );

 /* Parallax section
    -----------------------------------------------*/
  function initParallax() {
    $('#intro').parallax("100%", 0.1);
    $('#overview').parallax("100%", 0.3);
    $('#detail').parallax("100%", 0.2);
    $('#video').parallax("100%", 0.3);
    $('#speakers').parallax("100%", 0.1);
    $('#program').parallax("100%", 0.2);
    $('#register').parallax("100%", 0.1);
    $('#faq').parallax("100%", 0.3);
    $('#venue').parallax("100%", 0.1);
    $('#sponsors').parallax("100%", 0.3);
    $('#contact').parallax("100%", 0.2);

  }
  initParallax();


  /* Owl Carousel
  -----------------------------------------------*/
  $(document).ready(function() {
    $("#owl-speakers").owlCarousel({
      autoPlay: 6000,
      items : 4,
      itemsDesktop : [1199,2],
      itemsDesktopSmall : [979,1],
      itemsTablet: [768,1],
      itemsTabletSmall: [985,2],
      itemsMobile : [479,1],
    });
  });


  /* Back top
  -----------------------------------------------*/
    $(window).scroll(function() {
        if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
        } else {
          $('.go-top').fadeOut(200);
        }
        });   
        // Animate the scroll to top
      $('.go-top').click(function(event) {
        event.preventDefault();
      $('html, body').animate({scrollTop: 0}, 300);
      })


  /* wow
  -------------------------------*/
  new WOW({ mobile: false }).init();

  });

/* ---------------------------------------
   Registration API
---------------------------------------- */

$("#registrationForm").submit(function (e) {

    e.preventDefault();

    const registration = {

        id: Math.floor(Math.random() * 1000000),

        event_id: 1,

        attendee_name: $("#attendee_name").val(),

        email: $("#email").val(),

        phone: $("#phone").val(),

        tickets: parseInt($("#tickets").val())

    };

    fetch(`${API.REGISTRATION}/registrations`, {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify(registration)

    })

    .then(response => response.json())

    .then(data => {

        sendAnalytics(
            "Registration Submitted",
             "Registration"
             );

        alert("Registration Successful!");

        $("#registrationForm")[0].reset();

        console.log(data);

    })

    .catch(error => {

        console.error(error);

        alert("Registration Failed");

    });

});

/* ---------------------------------------
   Load Event Information
---------------------------------------- */

window.addEventListener("load", function () {

    fetch(`${API.EVENT}/events/1`)

        .then(response => {

            if (!response.ok) {
                throw new Error("Unable to load event information.");
            }

            return response.json();

        })

        .then(event => {

            document.getElementById("eventTitle").innerHTML =
                event.title;

            document.getElementById("eventDateVenue").innerHTML =
                event.date + " | " +
                event.venue + " | LKR " +
                event.ticket_price;

        })

        .catch(error => {

            console.error(error);

            document.getElementById("eventTitle").innerHTML =
                "AI Conference";

            document.getElementById("eventDateVenue").innerHTML =
                "Event information unavailable";

        });

});

/* ---------------------------------------
   Load Program Schedule
---------------------------------------- */

window.addEventListener("load", function () {

    fetch(`${API.PROGRAM}/programs`)

        .then(response => {

            if (!response.ok) {
                throw new Error("Unable to load programs.");
            }

            return response.json();

        })

        .then(programs => {

            let html = "";

            programs.forEach(program => {

                html += `
                    <div class="program-divider col-md-12 col-sm-12"></div>

                    <div class="col-md-12 col-sm-12">

                        <h3>${program.title}</h3>

                        <h4>Speaker: ${program.speaker}</h4>

                        <h6>

                            <span>
                                <i class="fa fa-clock-o"></i>
                                ${program.start_time} - ${program.end_time}
                            </span>

                        </h6>

                    </div>
                `;

            });

            document.getElementById("programList").innerHTML = html;

            // Send analytics only after programs are successfully loaded
            sendAnalytics(
                "Programs Viewed",
                "Programs"
            );

        })

        .catch(error => {

            console.error(error);

            document.getElementById("programList").innerHTML =
                "<h3>Unable to load program schedule.</h3>";

        });

});
