$(document).ready(function () {
  $(".increment-btn").click(function (e) {
    e.preventDefault();
    var inc_value = $(this).closest(".product_data").find(".qty-input").val();
    var value = parseInt(inc_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < 10) {
      value++;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });

  $(".decrement-btn").click(function (e) {
    e.preventDefault();
    var dec_value = $(this).closest(".product_data").find(".qty-input").val();
    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest(".product_data").find(".qty-input").val(value);
    }
  });

  $(".addToCartBtn").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var product_qty = $(this).closest(".product_data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    // console.log(token);
    // console.log(product_id);
    // console.log(product_qty);
    $.ajax({
      type: "POST",
      url: "/add-to-cart",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        // console.log("Product added", response);
        response.status == "success"
          ? alertify.success(response.message)
          : response.status == "warning"
          ? alertify.warning(response.message)
          : response.status == "error"
          ? alertify.error(response.message)
          : response.status == "info"
          ? alertify.notify(response.message)
          : alertify.message(response.message);
        /*
                    success
                    warning
                    error
                    notify
                    message
                */
      },
    });
  });

  $(".addToWishList").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: "/add-to-wishlist",
      data: {
        product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        response.status == "success"
          ? alertify.success(response.message)
          : response.status == "warning"
          ? alertify.warning(response.message)
          : response.status == "error"
          ? alertify.error(response.message)
          : response.status == "info"
          ? alertify.notify(response.message)
          : alertify.message(response.message);
      },
    });
  });

  $(".changeQuantity").click(function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var product_qty = $(this).closest(".product_data").find(".qty-input").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();
    if (product_qty == 10 && product_qty == 1) {
      //   console.log("Mostrar");
    }
    $.ajax({
      type: "POST",
      url: "/update-cart",
      data: {
        product_id: product_id,
        product_qty: product_qty,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {},
    });
  });

  $(document).on("click", ".delete-cart-item", function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: "delete-cart-item",
      data: {
        product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        response.status == "success"
          ? alertify.success(response.message)
          : alertify.message(response.message);

        $(".carddata").load(location.href + " .carddata");
      },
    });
  });

  $(document).on("click", ".delete-wishlist-item", function (e) {
    e.preventDefault();
    var product_id = $(this).closest(".product_data").find(".prod_id").val();
    var token = $("input[name=csrfmiddlewaretoken]").val();

    $.ajax({
      type: "POST",
      url: "/delete-wishlist-item",
      data: {
        product_id,
        csrfmiddlewaretoken: token,
      },
      success: function (response) {
        response.status == "success"
          ? alertify.success(response.message)
          : response.status == "warning"
          ? alertify.warning(response.message)
          : response.status == "error"
          ? alertify.error(response.message)
          : response.status == "info"
          ? alertify.notify(response.message)
          : alertify.message(response.message);

        $(".wishdata").load(location.href + " .wishdata");
      },
    });
  });
});
