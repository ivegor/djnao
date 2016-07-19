$ = django.jQuery;
$(function() {
    var parent = $('#id_parent');
    var order = $('#id_order');
    function changeLeftRight() {
        if (parent.val()===''){
        order.after($('<select id="left_right"><option value="left">левое меню</option>' +
                      '<option value="right">правое меню</option>'))
        }else{
            $('#left_right').remove()
        }
    }
    // function changeOrder(){
    //     $.each(order.select(),
    //         function(){console.log(order.option)})
    //
    // }
    changeLeftRight();
    parent.change(function () {
        changeLeftRight()
    })
    // changeOrder()
});