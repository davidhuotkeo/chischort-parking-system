let tire = $("span#tire");
let normal = $("span#normal");
let service = $("span.service");
let loading = $("div.loading");

$("label").click(function () { 
    if ($("input[value=tire]").is(":checked")) {
        tire.css("transform", "translate(175%, -50%) scale(1)");
        normal.css("transform", "translate(175%, -50%) scale(0)");
        service.css("display", "block");
    } else {
        normal.css("transform", "translate(175%, -50%) scale(1)");
        tire.css("transform", "translate(175%, -50%) scale(0)");
        service.css("display", "none");
    }
});

$("button").click(function () {
    loading.css({display: "flex"});
});
