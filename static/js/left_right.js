$ = django.jQuery;
$(function() {
    var parent = $('#id_parent');
    var order = $('#id_order');
    temp = createSelect(10, '#id_order', order.attr('name'), order.val());
    order.replaceWith(temp);
    order = temp;
    changeLeftRight();
    changeOrder();
    parent.change(function () {
        changeLeftRight()
    });

    function createSelect(len, id, name, selected){
        var gap = 0;
        if (selected>=100&&!parent.val()){
            gap = 100
        }
        select = $('<select>');
        for (var i=1; i<=len; i++){
            select.append($('<option>',{
                value:i+gap,
                text:i
            }));
        }
        select.attr('id', id).attr('name', name).val(selected);
        return select
    }
    function changeLeftRight() {
        if (!parent.val()){
            order.after($('<select id="left_right"><option value="left">левое меню</option>' +
                      '<option value="right">правое меню</option>'));
            var lrSelect = $('#left_right');
            if(order.val()>=100){
                lrSelect.val('right')
            }else{
                lrSelect.val('left')
            }
            lrSelect.change(function(){
                changeOrder()
            })
        }else{
            $('#left_right').remove();
            order.find('option').each(
                function(){
                    $(this).attr('value', $(this).text())
                }
            )
        }
    }
    function changeOrder(){
         if ($('#left_right').val()==='right'){
             order.find('option').each(
                 function(){
                     $(this).attr('value', +$(this).text()+100)
                 })
         }else{
             order.find('option').each(
                 function(){
                     $(this).attr('value', $(this).text())
                 }
             )
         }
    }
});