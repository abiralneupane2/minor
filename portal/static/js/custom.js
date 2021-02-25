
// burger for navbar
var burgerFlag = false; 

$('.burger').click(function(){
    burgerFlag ? $(".nav-links").css("opacity","0%"):$(".nav-links").css("opacity","100%");
    burgerFlag=!burgerFlag;
});
//burger end


//function to favourite article
$('input.favourite').click(function (event) {
  id = $(event.target).attr('value')
  favNum = $(event.target).parent().parent().find('span')
  $.ajax({
    url: favouriteurl,
    cache: false,
    data: {
      articleid: id
    },
    success: function (res) {
      if (res.status == "created") {
        $(event.target).attr("checked", "True");
        favNum.text(parseInt(favNum.text()) + 1);
      }
      else if (res.status == "deleted") {

        $(event.target).attr("checked", "False")
        favNum.text(favNum.text() - 1);
      }

    }
  });
})


//add comment button
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

//span to delete comment
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

$('button#delete').click(function(){
  let id = $(this).attr('value')
  console.log("delete pressecd");
  let check = prompt("Do you want to delete this?")
  if (check){
    $.ajax({
      url : articleUrl,
      method : 'delete',
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", window.CSRF_TOKEN);
      },
      data : {
         id :id
      }
 })
  }
})
$('button.follow-person').click(function(event){
  var personId = $(event.target).attr('value')
  $.ajax({
    url : followUrl,
    method : 'post',
    data: {
      csrfmiddlewaretoken: window.CSRF_TOKEN,
      personId : personId,
    },
    success: function(res){
      console.log(res);
      $(event.target).html(res==201?"Unfollow":"Follow")
    }
  })
})


//Javascript for modal 
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//modal javascript end
