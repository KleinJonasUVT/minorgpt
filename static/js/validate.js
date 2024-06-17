document.getElementById('Minor_Form').onsubmit = function(event) {
    event.preventDefault();

    const container = document.querySelector('#result');
    container.innerHTML = ''; // Clear the container before adding new items

    // Show loader
    const loadings = document.querySelectorAll('.loading');
    loadings.forEach(function(loading) {
        loading.style.display = 'block'; // Set display to 'block'
    });

    // Collect form data
    const formData = new FormData(event.target);

    // Send data to Flask backend
    fetch('/data', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log(data.result);
        // Hide loader
        loadings.forEach(function(loading) {
            loading.style.display = 'none'; // Set display to 'none'
        });

        // Assuming container is defined earlier or exists in your HTML
        const container = document.querySelector('#result');

        // Iterate over each key in the JSON object
        Object.keys(data.result).forEach(key => {
            const obj = data.result[key];
            // Create a new div for each item
            const itemDiv = document.createElement('div');
            itemDiv.className = 'item';

            // Add title
            const title = document.createElement('div');
            title.id = 'title';
            title.innerHTML = `<h1> ${key} </h1>`;
            itemDiv.appendChild(title);

            // Add description
            const description = document.createElement('div');
            description.id = 'description';
            description.textContent = obj.Description;
            itemDiv.appendChild(description);

            // Add br
            const br = document.createElement('br');
            itemDiv.appendChild(br);

            // Add school
            const school = document.createElement('div');
            school.id = 'school';
            school.innerHTML = `<strong>School:</strong> ${obj.School}`;
            itemDiv.appendChild(school);

            // Add total ECTS
            const totalECTS = document.createElement('div');
            totalECTS.id = 'totalECTS';
            totalECTS.innerHTML = `<strong>Total ECTS:</strong> ${obj.Total_ECTS}`;
            itemDiv.appendChild(totalECTS);

            // Append the item div to the container
            container.appendChild(itemDiv);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
};



