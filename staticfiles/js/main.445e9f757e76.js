"use strict"


// Delete post using modal on the same page
// const deletePost = document.getElementById("delete-post");
// console.log(deletePost.href)

// deletePost?.addEventListener("click", () => {
//     document.getElementById("delete-post-form").action = deletePost.href;
// });



$(document).ready(() =>{
     /**
      Hides header on scroll down, show on scroll up
      */

    var iScrollPos = 0;
    $(window).scroll(() => {
        var iCurScrollPos = $(this).scrollTop();
        if (iCurScrollPos > iScrollPos) {
            $('header').fadeOut(500);
        } else {
            $('header').fadeIn(500);
        }
        iScrollPos = iCurScrollPos;
    });
})


