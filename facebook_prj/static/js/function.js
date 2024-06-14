document.addEventListener('DOMContentLoaded', function() {
    $("#post-form").on("submit", function(e) {
        e.preventDefault();
        // e.stopPropagation(); // Stop event bubbling

        let post_caption = $("#post-caption").val();
        let post_visibility = "Everyone";

        let fileInput = $("#post-thumbnail")[0];
        let file = fileInput.files[0];
        let fileName = file ? file.name : "No file selected";

        console.log("Post Caption:", post_caption);
        console.log("File Name:", fileName);

        console.log('jQuery =', $);

        let formData = new FormData();
        formData.append("post-caption", post_caption);
        formData.append("visibility", post_visibility);
        formData.append("post-thumbnail", file, fileName);

        $.ajax({
            url: "/create-post/",
            type: "POST",
            dataType: "json",
            data: formData,
            processData: false,
            contentType: false,
            success: function(res) {
                console.log("Post created successfully");
                location.reload();
                // Hide the modal using UIkit
                // UIkit.modal("#create-post-modal").hide();
            },
            error: function(err) {
                console.error("Error creating post:", err);
            }
        });
    });




    // $("#like-btn").on("click", function(e) {
    //     // e.preventDefault();
    //     console.log("Liked")


    // });
});



$(document).ready(function(){
    $(document).on("click", "#like-btn" , function(){
        // console.log("Liked")
        let btn_val = $(this).attr("data-like-btn")


        $.ajax({
            url: "/like-post/",
            dataType: "json",
            data: {
                "id" : btn_val
            },

            success: function(response){

                if(response.data.bool ===true){

                    console.log("Likes : " , response.data.likes);
                    $("#like-count" + btn_val).text(response.data.likes)
                    $(".like-btn" + btn_val).addClass("liked")
                    $(".like-btn"+btn_val).removeClass("unliked")

                }

                else{

                    console.log("Likes : " , response.data.likes);
                    $("#like-count" + btn_val).text(response.data.likes)
                    $(".like-btn" + btn_val).addClass("unliked")
                    $(".like-btn"+btn_val).removeClass("liked")


                }
               

            }


        })

    })



    $(document).on("click", "#comment-btn" , function(){

        let id = $(this).attr("data-comment-btn")
        let comment = $("#comment-input" + id).val()
        console.log(id)
        console.log(comment)

        $.ajax({
            
            url: "/comment-post/",
            dataType: "json",
            data: {
                "id" : id,
                "comment": comment,
            },

            success: function(response){
                console.log(response)

                let newComment = '<li class="comment-item">\
                <img src="'+ response.data.profile_image +'" alt="User Avatar" />\
                <div class="comment-content">\
                  <div class="author">'+ response.data.full_name +'</div>\
                  <div class="text">'+ response.data.comment +'</div>\
                  <div class="timestamp">'+ response.data.date +'</div>\
                  <div class="comment-actions">\
                    <a  id = "like-comment-btn" data-like-comment = "'+ response.data.comment_id+'"  class = "like-comment'+ response.data.comment_id+'"   style = "color: gray; cursor: pointer;"  >Like</a>\
                    <span id = "comment-likes-count'+ response.data.comment_id+'"   style = "color: gray; cursor: pointer; margin-left: 0.20rem;"  > 0</span>\
                    <a href = "#" style= "margin-left:1rem;">Reply</a>\
                  </div>\
                </div>\
              </li>\
              '

              $("#commet-div"+id).prepend(newComment)
              $("#comment-input" + id).val("")
              location.reload()
              $("#comment-count" +id).text(response.data.comment_count)

            }
        })



    })






    $(document).on("click", "#like-comment-btn", function(){
        let id = $(this).attr("data-like-comment")
        console.log("comment-id: ", id);

        $.ajax({
            url : "/like-comment/",
            dataType: "json",
            data: {
                "id" : id
            },

            success: function(response){
                if(response.data.bool === true){
                    $("#comment-likes-count"+id).text(response.data.likes)
                    $(".like-comment"+id).css("color", "#007bff")

                } else{

                    $("#comment-likes-count"+id).text(response.data.likes)
                    $(".like-comment"+id).css("color", "gray")

                }
            }

        })
    })



    // Reply comment

    $(document).on("click", "#reply-comment-btn", function(){

        let id = $(this).attr("data-reply-comment-btn")
        let reply = $("#reply-input"+id).val()

        console.log(id)
        console.log(reply)

        $.ajax({
            url : "/reply-comment/",
            dataType: "json",
            data:{
                "id" : id,
                "reply" : reply
            },
            success: function(response){
                console.log(response)
                let newReply = '<!--Reply comment-->\
                <div class = "flex mr-12" style = "margin-right: 20px; margin-top: 20px;">\
                  <div class = "w-10 h-10 rounded-full relative flex-shrink-0">\
                      <img src = "'+response.data.profile_image+'"\
                          style = "width: 40px; height: 40px;" alt = "" class = "absolute h-full rounded-full w-full">\
\
                  </div>\
\
                  <div>\
\
                      <div class = "text-gray-700 py-2 px-3 rounded-md bg-gray-100\
                          relative lg:ml-5 ml-2 lg:mr-12 dark:bg-gray-800 dark:text-gray-100">\
                          <p class = "leading-6">'+response.data.reply+'</p>\
                          <div class = "absolute w-3 h-3 top-3 -left-1 bg-gary-100\
                              transform rotate-45 dark:bg-gray-800">\
                          </div>\
\
                       </div>\
\
                  </div>\
\
              </div> \
                '

                $(".reply-div"+id).prepend(newReply)
                $("#reply-input"+id).val("")
            }
            
        })
    })









    // Delete comment

    $(document).on("click", "#delete-comment", function(){
        let id = $(this).attr("data-delete-comment")
        console.log(id)

        $.ajax({
            url: "/delete-comment/",
            dataType: "json",
            data:{
                "id": id
            },
            success: function(response){
                console.log("Comment ", id, " deleted")
                $("#comment-div"+id).addClass("d-none")
            }

        })
    })





    // Delete reply

    $(document).on("click", "#delete-reply", function(){
        let id = $(this).attr("data-delete-reply")
        console.log(id)

        $.ajax({
            url: "/delete-reply/",
            dataType: "json",
            data:{
                "id": id
            },
            success: function(response){
                console.log("Reply ", id, " deleted")
                $("#reply-div"+id).addClass("d-none")
            }

        })
    })






    $(document).on("click", "#add-friend", function(){

        let id = $(this).attr("data-friend-id")
        console.log("Added "+ id + " as friend")

        $.ajax({
            url: "/add-friend/",
            dataType: "json",
            data: {
                "id" : id
            },

            success: function(response){
                console.log(response)
                if(response.bool === true){
                    $("#friend-text").html('<i></i> Cancel Request')
                    location.reload()
                }

                if(response.bool === false){
                    $("#friend-text").html('<i></i>Add Friend')
                    location.reload()
                }
            }
        })
    })






    $(document).on("click", "#accept-friend-request", function(e){

        
        let id = $(this).attr("data-request-id")
        console.log(id)

        $.ajax({
            url: "/accept-friend-request/",
            dataType: "json",
            data:{
                "id": id
            },
            success: function(response){
                console.log(response)
                $(".reject-friend-request-hide"+id).hide()
                $(".accept-friend-request"+id).html('<i></i>Friend Request Accepted')
            }
        })




    })




    $(document).on("click", "#reject-friend-request", function(e){

        
        let id = $(this).attr("data-request-id")
        console.log(id)

        $.ajax({
            url: "/reject-friend-request/",
            dataType: "json",
            data:{
                "id": id
            },
            success: function(response){
                console.log(response)
                $(".accept-friend-request-hide"+id).hide()
                $(".reject-friend-request"+id).html('<i></i>Request Deleted')
            }
        })




    })




    $(document).on("click", "#unfriend", function(){

        let id = $(this).attr("data-unfriend")
        console.log(id)

        $.ajax({
            url: "/unfriend/",
            dataType: "json",
            data: {
                "id": id
            },

            success: function(response){
                console.log(response)
                $("#unfriend-text").html('<i></i> Friend Removed')
            }
        })


    })








})








