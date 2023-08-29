console.log("Shalom!, We are Connected!")
// const deleteRecipeBtn = document.querySelector('#delete-recipe-modal')
// const modalBkgd = document.querySelector('.modal-background')
// const modal = document.querySelector('.modal')
const receiverID = document.getElementById('_id')
const receiverMessage = document.getElementById('rec-message')
const updateMessage = document.getElementById('update_message')
const editButton = document.getElementById("edit_button");


const editMsg = (message_id) => {
    console.log("clicked", message_id)
    receiverMessage.style.display = 'block'
    updateMessage.style.display = 'none'
    fetch(`/dm/update/${message_id}`, {
        method : "POST"
    })
    .then((response) => {
        console.log("RESPONSE", response)
        response.json()
        // after success do what?

    }) 
    .then((error) => {
        console.log("ERROR", error)
    })

}
// Add a click event listener to the button
editButton.addEventListener("click", (e) => {
    e.preventDefault()
});



const openDeleteModal = (message_id) => {
    console.log("open modal")
    if(modal) {
        recipeID.innerText = recipe_id
        recipeName.innerText = recipe_name
        modal.classList.add("is-active")
    }
    
}

const closeDeleteModal = () => {
    console.log("close modal")
    if(modal) {
        modal.classList.remove("is-active")
    }
}


const deleteRecipeById = () => {
    fetch(`/recipes/delete/${recipeID.innerText}`, {
        method : "POST"
    })
    .then((response) => {
        console.log("RESPONSE", response)
        response.json()
        closeDeleteModal()
        const recipe_row = document.getElementById(recipeID.innerText)
        recipe_row.remove()
    }) 
    .then((error) => {
        console.log("ERROR", error)
    }) 
    console.log(recipeID.innerText)
}


