async function addUser() {
    const name = prompt("Enter user's name:");
    const email = prompt("Enter user's email:");
    const response = await fetch('/add_user', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email })
    });
    const result = await response.json();
    alert(result.message);
}

async function getUsers() {
    const response = await fetch('/users');
    const users = await response.json();
    const usersList = document.getElementById('users-list');
    usersList.innerHTML = users.map(user => `<li>${user.name} (${user.email})</li>`).join('');
}
