$(document).on('click', '.edit-cart-item', function(e) {
    e.preventDefault();

    const productId = $(this).data('product-id');

    $.ajax({
        type: 'POST',
        url: `/edit-cart-item/${productId}/`, 
        data: {
            quantity: $(`#quantity-${productId}`).val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            action: 'edit'
        },
        success: function(json) {
            console.log(json);
        },
        error: function(xhr, errmsg, err) {
            console.error(`Error: ${errmsg}`);
            console.error(`Details: ${err}`);
            console.error(`Response: ${xhr.responseText}`);
        }
    });
});