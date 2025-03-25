const editCourtButtons = document.getElementsByClassName("btn-edit-court");
const courtText = document.getElementById("id_body");
const courtForm = document.getElementById("courtForm");
const submitButton = document.getElementById("submitButton");
const deleteCourtModal = new bootstrap.Modal(document.getElementById("deleteCourtModal"));
const deleteCourtButtons = document.getElementsByClassName("btn-delete-court");
const deleteCourtConfirm = document.getElementById("deleteCourtConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding review.
* - Populates the `reviewText` input/textarea with the review's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/

console.log("Review.js loaded");

for (let button of editCourtButtons) {
  button.addEventListener("click", (e) => {
    console.log("I've been clicked!");
    courtId = e.target.getAttribute("data-court_id");
    let courtContent = document.getElementById(`court${courtId}`).innerText;
    courtText.value = courtContent;
    submitButton.innerText = "Update";
    courtForm.setAttribute("action", `edit_court/${courtId}`);
  });
}


for (let button of deleteCourtButtons) {
    button.addEventListener("click", (e) => {
      console.log("I've been clicked!");
      const courtId = e.target.getAttribute("data-court_id");
      const slug = e.target.getAttribute("data-court_slug");
      
      // Update the delete confirmation link with both the slug and courtId
      deleteCourtConfirm.href = `/delete_court/${slug}/${courtId}/`;  // Adjusted URL for court delete
      
      // Show the court deletion confirmation modal
      deleteCourtModal.show();
    });
  }