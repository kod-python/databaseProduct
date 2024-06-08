$(document).on('click', '.delete-cart-item', function(e) { 
    e.preventDefault();

    const productId = $(this).data('product-id');

    $.ajax({
        type: 'POST',
        url: `/delete-cart-item/${productId}/`, 
        data: {
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            action: 'delete'
        },
        success: function(json) {
            console.log(json);
            $(`#cart-item-${productId}`).remove();
        },
        error: function(xhr, errmsg, err) {
            console.error(`Error: ${errmsg}`);
            console.error(`Details: ${err}`);
            console.error(`Response: ${xhr.responseText}`);
        }
    });
});
