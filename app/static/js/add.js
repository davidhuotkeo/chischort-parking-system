let addInput = $("#multiple");
let checkbox = $("input#checkbox");
let form = $('form');
let button = $('button')

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

// form.submit(function(e) {
//     e.preventDefault()
//     var lane = $("input[name='lane']").val();
//     var price = $("input[name='price']").val();
//     var add = $("input[name='add']").val();
//     var place = $("input[name='place']").val();

//     if (lane.length < 5) {
//         $("input[name='lane']").before("<p class='error'>Enter lane id 5 letters upper</p>")
//     }
//     if (price.length < 3) {
//         $("input[name='price']").before("<p class='error'>Price 100+</p>")
//     }
//     if (add.length < 3) {
//         $("input[name='add'").before("<p class='error'>Price 100+</p>")
//     }
//     if (place.length < 1) {
//         $("input[name='place']").before("<p class='error'>Empty place</p>")
//     }

// })
