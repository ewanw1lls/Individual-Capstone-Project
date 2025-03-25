const editButtons = document.getElementsByClassName("btn-edit");
const reviewText = document.getElementById("id_body");
const reviewForm = document.getElementById("reviewForm");
const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(
  document.getElementById("deleteModal")
);
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the `reviewText` input/textarea
 *   with the review's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
 */

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    let reviewContent = document.getElementById(`review${reviewId}`).innerText;
    reviewText.value = reviewContent;
    submitButton.innerText = "Update";
    reviewForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the
 * deletion endpoint for the specific review.
 * - Displays a confirmation modal (`deleteModal`) to prompt
 * the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("data-review_id");
    deleteConfirm.href = `delete_review/${reviewId}`;
    deleteModal.show();
  });
}

// Code for Court Delete Button and Modal

const deleteCourtModal = new bootstrap.Modal(
  document.getElementById("deleteCourtModal")
);
const deleteCourtButtons = document.getElementsByClassName("btn-delete-court");
const deleteCourtConfirm = document.getElementById("deleteCourtConfirm");

for (let button of deleteCourtButtons) {
  button.addEventListener("click", (e) => {
    console.log("I've been clicked!");
    const courtId = e.target.getAttribute("data-court_id");
    const slug = e.target.getAttribute("data-court_slug");

    // Update the delete confirmation link with both the slug and courtId
    deleteCourtConfirm.href = `/delete_court/${slug}/${courtId}/`;

    // Show the court deletion confirmation modal
    deleteCourtModal.show();
  });
}