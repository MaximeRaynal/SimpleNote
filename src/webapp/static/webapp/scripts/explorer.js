$( document ).ready(function() {

    affectEvent();

    loadAllTags();

});

function affectEvent() {
    $("#create-note-button").click( function(e) {
        $("#edit-panel").toggleClass("edit-panel-enabled");
    });
}

function loadAllTags() {
    $.ajax({
        url: "/api/tags.json",
        method: "GET",
        dataType: "json"

    }).done(function (data) {
        $("#tags-list").empty();

        data.tagList.forEach(function (elemnt, index, array) {
            $("#tags-list").append('<button type="button" class="btn btn-default tag">' + elemnt + '</button>');
        });

    });
}