$('#slider1, #slider2, #slider3, #slider4, #slider5, #slider6').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
        },
        1000: {
            items: 5,
            nav: true,
            loop: true,
            autoplay: true,
        }
    }
})
$('.plus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url:"/pluscart",
        data: {
            prod_id:id
        },
        success:function (data){
            eml.innerText = data.quantity
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
        }
    })
})
$('.minus-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this.parentNode.children[2]
    var qty = parseInt(eml.innerText)
    if (qty > 1) {
        $.ajax({
            type: "GET",
            url:"/minuscart",
            data: {
                prod_id:id
            },
            success:function (data){
                eml.innerText = data.quantity
                document.getElementById("amount").innerText = data.amount
                document.getElementById("total_amount").innerText = data.total_amount
            }
        })
    }
    else {
        // popping message
        alert("Quantity cannot be less than 1.");
    }
})

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this
    $.ajax({
        type: "GET",
        url:"/removecart",
        data: {
            prod_id:id
        },
        success:function (data){
            document.getElementById("amount").innerText = data.amount
            document.getElementById("total_amount").innerText = data.total_amount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})

//JQuery
$('#add-to-cart-btn').on('click', function(event) {
        event.preventDefault(); // Prevents the form from submitting
        alert('Your item has beem added to cart !!'); // Shows an alert with the message
        $('form').submit(); // Submits the form
    });
