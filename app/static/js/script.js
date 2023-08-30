console.log("Shalom!, We are Connected!")
// const deleteRecipeBtn = document.querySelector('#delete-recipe-modal')
// const modalBkgd = document.querySelector('.modal-background')
// const modal = document.querySelector('.modal')
// const messageID = document.querySelector(`#contentMsg-${message_id}`).value

const editButtons = document.querySelectorAll(".edit-button");


// Loop through each edit button and add click event listener
editButtons.forEach(editButton => {
    editButton.addEventListener('click', function(e) {
        e.preventDefault()
        // Get the data-message-id attribute value
        const message_id = this.getAttribute('data-message-id');
        console.log("clicked", message_id)
        
        // Here you can call your editMsg function with the message_id
        editMsg(message_id);
    });
});

const editMsg = (message_id) => {
    const senderMessage = document.getElementById(`sender-message-${message_id}`)
    const updateMessage = document.getElementById(`update-sender-message-${message_id}`)
    // console.log('senderMessage', senderMessage)
    // console.log('updateMessage', updateMessage)
    senderMessage.style.display = 'block'
    updateMessage.style.display = 'none'
    // grabbing the SPECIFIC INPUT for the message id
    const messageInput = document.querySelector(`#contentMsg-${message_id}`);
    console.log("MESSAGE input -->", messageInput)
    console.log("MESSAGE input -->", messageInput.value)
    // todo- toggle pencil to edit or cancel edit
    // todo- grab the updated content after user types something
    let updated_input = JSON.stringify({
        "message_id": message_id,
        "content" : messageInput.value,
        "receiver_person_id" : '3884193',
    }); 

    messageInput.addEventListener('keypress', function (e) {
        if (e.key === 'Enter') {
            updateMsg(message_id, updated_input)
        }
    });
}


const updateMsg = (message_id, updated_input_json) => {
    fetch(`/dm/update/${message_id}`, {
        method : "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: updated_input_json
        // body: JSON.stringify({
        //     "message_id": message_id,
        //     "content" : 
        //     "receiver_person_id" : '3884193' 
        // })
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


