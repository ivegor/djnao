$ = django.jQuery;
$(function() {
    var contentType = $('#id_content_type');
    var object_id = $('#id_object_id').hide().after($('<select>'));
    var select = object_id.next();
    var init = !! object_id.val();
    var path = window.location.pathname.match(/\/\w+\/\w+\/\w+\//)[0];

    function getData(id) {
        if (id&&isFinite(id)){
        $.get(path + 'ajax/' + id).done(function (data) {
            select.empty();
            $.each(data, function(i, v) {
                select.append($("<option>", {
                    value: v.id,
                    text: v.name
                    }));
                });
            if (init) {
                select.val(object_id.val());
                init = false
            }
            else {
                object_id.val(select.val())
            }
        })
    }}

    getData(contentType.val());

    contentType.change(function () {
        getData(contentType.val());
    });
    select.change(function () {
        object_id.val(select.val())
    })
});