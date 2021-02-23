
var burgerFlag = false;
const burgerClick = () => {
  burgerFlag ? $(".nav-links").css("opacity","0%"):$(".nav-links").css("opacity","100%");
  burgerFlag=!burgerFlag;
}

$('.burger').click(burgerClick);



$('#add').click(function () {
  console.log("{{articles}}")

})

$('button.favourite').click(function (event) {
  id = $(event.target).attr('value')
  favNum = $(event.target).parent().parent().find('span')

  console.log(favNum.text());
  $.ajax({
    url: favouriteurl,
    cache: false,
    data: {
      articleid: id
    },
    success: function (res) {
      if (res.status == "created") {
        $(event.target).attr("class", "btn btn-primary");
        favNum.text(favNum.text() + 1);
      }
      else if (res.status == "deleted") {

        $(event.target).attr("class", "btn btn-outline-primary")
        favNum.text(favNum.text() - 1);
      }

    }
  });
})
$('button.comment').click(function () {
  id = $(this).attr('value')
  comment = $(this).prev().val()
  $.ajax({
    url: commenturl,
    cache: false,
    method: 'POST',
    data: {
      csrfmiddlewaretoken: window.CSRF_TOKEN,
      articleid: id,
      comment: comment
    },
    success: function (res) {
      console.log(res)
      var commentDiv = "<br><a href=" + profileurl + "><strong>" + username + "</strong></a>  :  " + comment
      console.log(commentDiv);
      $('div.comment').append(commentDiv)
    }
  });
})

$('span.cmnt-dlt').click(function (event) {
  id = $(this).attr('value')
  $.ajax({
    url: commenturl,
    contentType: "application/json",
    method: 'DELETE',
    beforeSend: function (xhr) {
      xhr.setRequestHeader("X-CSRFToken", window.CSRF_TOKEN);
    },
    dataType: "json",
    data: {
      commentid: id
    },
    success: function (res) {
      console.log(res);
      if (res == 200)
        $(event.target).parent().remove()
    }
  })
})