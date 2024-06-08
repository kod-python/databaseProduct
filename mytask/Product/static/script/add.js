$(document).on('click', '#add-cart', function(e) {
    e.preventDefault();

    $.ajax({
        type: 'POST',
        url: '{% url "add_to_cart" id=product.id %}',  
        data: {
            product_id: $('#add-cart').val(),
            quantity: $('#quantity').val(),
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
            action: 'post'
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



