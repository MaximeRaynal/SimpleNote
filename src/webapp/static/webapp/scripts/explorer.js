$( document ).ready(function() {

    affectEvent();

    loadAllTags();

    loadAllNote();


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

        data.forEach(function (elemnt, index, array) {
            $("#tags-list").append(
                '<button type="button" class="btn btn-default tag">' + elemnt +
                '</button>');
            $(".tag:contains(" + elemnt + ")").click(function () {
                $( this ).toggleClass("active");
            });
        });

    });
}

function loadAllNote() {
    $.ajax({
        url: "/api/notes.json",
        method: "GET",
        dataType: "json"

    }).done(function (data) {
        $("#notes-list").empty();

        data.forEach(function (elemnt, index, array) {
            $("#notes-list").append(
                '<div class="col-md-2">  \
                        <div class="panel panel-default note"> \
                            <div class="panel-heading">
                                <h3 class="panel-title">' + elemnt.name + '</h3> \
                            </div> \
                            <div class="panel-body"> \
                                <div class="media"> \
                                    <div class="media-center media-middle"> \
                                        <img class="media-object note-pic" src="{% static \'webapp/file.png\' %}" alt="File icons"> \
                                    </div> \
                                </div> \
                                <span class="note-uuid hidden">' + elemnt.uuid + '</span> \
                            </div> \
                            <div class="panel-footer clearfix"> \
                                <button type="button" class="btn btn-default action-button pull-left" > \
                                    <span class="glyphicon glyphicon-pencil"></span> \
                                </button> \
                                <button type="button" class="btn btn-default action-button pull-right" > \
                                    <span class="glyphicon glyphicon-eye-open"></span> \
                                </button> \
                            </div> \
                        </div> \
                    </div>');
        });

    });
}