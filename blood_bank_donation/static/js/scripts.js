// Load dashboard statistics
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('total-donors')) {
        fetch('/api/donors')
            .then(response => response.json())
            .then(data => {
                document.getElementById('total-donors').textContent = data.length;
            })
            .catch(error => console.error('Error fetching donors:', error));
    }

    if (document.getElementById('total-donations')) {
        fetch('/api/donations')
            .then(response => response.json())
            .then(data => {
                document.getElementById('total-donations').textContent = data.length;
            })
            .catch(error => console.error('Error fetching donations:', error));
    }

    if (document.getElementById('total-inventory')) {
        fetch('/api/inventory')
            .then(response => response.json())
            .then(data => {
                const total = data.reduce((sum, item) => sum + item.quantity_ml, 0);
                document.getElementById('total-inventory').textContent = total + ' ml';
            })
            .catch(error => console.error('Error fetching inventory:', error));
    }
});

// Form validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    if (form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    }
}

// Validate donor form
validateForm('add-donor-form');

// Validate donation form
validateForm('add-donation-form');
