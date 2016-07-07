$(function() {
    function getData(id) {
        $.get('/admin/ajax/' + id).done(function (data) {
            console.log('hi', data)
        })
    }
    var contentType = $('#id_content_type');
    var objects = getData(contentType.val());
    var object_id = $('#id_object_id');
    var select = object_id.after($('<select>'));
    object_id.hide();
    for (var el in objects){
        select.append($('<option>'))
    }

});