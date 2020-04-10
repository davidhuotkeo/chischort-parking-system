let addInput = $("#multiple");
let checkbox = $("input#checkbox");
let form = $('form');
let button = $('button');
let buttonDisplay = $('#display');

$(document).ready(function() {
    form.validate();
  });

checkbox.click(function() {
    if (checkbox.is(":checked")) {
        addInput.css('display', 'block')
    } else {
        addInput.css('display', 'none')
    }
})

buttonDisplay.click(function() {
    window.location.href = "/chischort/display/lane"
})
