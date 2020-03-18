var logo = $('.top > img');
var soon = $('p.coming');
var yellowRoad = $('.middle');
var detail = $('.topdetail');
var contactWrapper = $('.contact');
var contact = $('.contact > p');
var contactLink = $('.contact-link');
var loader = $('.preloader');
var input = $('input[name="email"]');

let delayTime = 3000;

var firstTime = localStorage.getItem("first_time");
if(firstTime) {
  delayTime = 0;
  localStorage.setItem("first_time", false);
} else {
  localStorage.setItem("first_time", true);
  loader
  .transition({
    display: 'block'
  },10)
  .delay(delayTime)
  .transition({
    display: 'none'
  }, 10);
}

logo.delay(delayTime).transition({
    opacity: 1,
    transform: 'translate(0, 0)'
}, 1500);

soon.delay(delayTime).transition({
    opacity: 1,
    transform: 'translate(0, 0)'
}, 2000);

yellowRoad.delay(delayTime).animate({
    width: '100vw'
}, 1500);

detail.delay(delayTime).transition({
    opacity: 1,
    transform: 'translate(0, 0)'
}, 2000);

contactLink.hide();

contact.click(function (e) { 
    e.preventDefault();
    contactLink.toggle('slide:right');
});

contact.delay(delayTime).hover(function () {
        $(this).css({
            'background-color': '#feb16b',
            'color': '#3d3d3d'
        });
    }, function () {
        $(this).css({
            'background-color': 'transparent',
            'color': '#cccccc'
        });
    }
);

let reachNewDiv = false;

$(window).bind('scroll', function() {
    if($(window).scrollTop() >= $('.top').offset().top + $('.top').outerHeight()-window.innerHeight) {
        $('.wh-question').transition({
            transform: 'translateX(0)',
            opacity: 1
        }, 1500);
    }
});

$('div.button').click(function (e) { 
    e.preventDefault();
    $('p.story').toggle('slide:down');
});

function isValidEmailAddress(emailAddress) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(emailAddress);
}

$(input).keydown(function() {
    let val = input.val();
    if (isValidEmailAddress(val)) {
        $("button").prop("disabled", false);
    } else {
        $("button").prop("disabled", true);
    }
});
