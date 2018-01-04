function refreshPessoas() {
    $.ajax({
        type: "POST",
        url: '/getpeople',
        dataType: "JSON",
        success: function (data) {
            var table_row = '';
            for (var i = 0; i < data.length; i++) {
                var obj = data[i];
                table_row += '<tr>';
                table_row += '<td>';
                table_row += obj.id;
                table_row += '</td>';
                table_row += '<td>';
                table_row += obj.firstname
                table_row += '</td>';
                table_row += '<td>';
                table_row += obj.lastname
                table_row += '</td>';
                table_row += '<td>';
                table_row += obj.address
                table_row += '</td>';
                table_row += '<td>';
                table_row += '<input class="edit" person_id="' + obj.id + '" type="button" name="b2" value="Edit">'
                table_row += '</td>';
                table_row += '<td>';
                table_row += '<input class="delete" person_id="' + obj.id + '" type="button" name="b2" value="Delete">'
                table_row += '</td>';
                table_row += '</tr>';
            }
            $('tbody').html(table_row);
        }
    });

}

$('#reset').on('click', function () {
    $('#submit').val('Save');
    $('#id').val('');
    $('form').attr('action', '/createperson')
    $('#id').remove();
});

$('form', $(document)).submit(function (e) {
    validador()
    $.ajax({
        type: "POST",
        url: $(this).attr('action'),
        dataType: "JSON",
        contentType: "application/json;charset=utf-8",
        data: $("form").serialize(), // serializes the form's elements.
        complete: function () {
            refreshPessoas();
            $('#reset').click();
        }
    });
    e.preventDefault(); // avoid to execute the actual submit of the form.
});
$(document).on('click', '.delete', function () {
    var person_id = $(this).attr('person_id');
    $.ajax({
        type: "POST",
        url: '/deleteperson',
        dataType: "JSON",
        data: { 'id': person_id }, // serializes the form's elements.
        complete: function () {
            refreshPessoas();

        }
    });
})
$(document).on('click', '.edit', function () {
    var person_id = $(this).attr('person_id');
    input = '<input type="hidden" id="id" name="id" value="' + person_id + '">';
    $('form').append(input);
    $.ajax({
        type: "POST",
        url: '/getperson',
        dataType: "JSON",
        data: { 'id': person_id }, // serializes the form's elements.
        success: function (data) {
            console.log(data);
            $('#id').val(data.id);
            $('#firstname').val(data.firstname);
            $('#lastname').val(data.lastname);
            $('#address').val(data.address);
            $('#submit').val('Update');
            $('form').attr('action', '/editperson');

        }
    });
});
function validador(){
    console.log($("form").serialize());
}
refreshPessoas();