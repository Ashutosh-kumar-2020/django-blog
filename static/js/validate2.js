
    const commentContent = document.getElementById("commentContent");
    const comment_btn = document.getElementById("comment_btn");
    const CommentContainer = document.getElementById("CommentContainer");
    const submit_btn_container = document.getElementById("submit-btn-container");

    let comment_btn_disabled = true;

    commentContent.addEventListener("click", () =>{
	if(comment_btn_disabled == true)
	{
	   comment_btn.disabled = false;
	   let comment_btn_disabled = false;
	}
    });

    commentContent.addEventListener("blur", () =>{
        if(commentContent.value == "")
        {
            comment_btn.disabled = true;
	        let comment_btn_disabled = true;
            commentContent.classList.add("is-invalid");
        }
        else
        {
            commentContent.classList.remove("is-invalid");
        }
    });

