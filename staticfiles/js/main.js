"use strict"

// Delete post using modal on the same page
const deletePost = document.getElementById("delete-post");

deletePost?.addEventListener("click", () => {
    document.getElementById("delete-post-form").action = deletePost.href;
    console.log('yeahh')
});
