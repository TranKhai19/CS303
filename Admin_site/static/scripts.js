// Toggle dropdown menu
document.addEventListener('DOMContentLoaded', function() {
    var dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(function(dropdown) {
        dropdown.addEventListener('click', function() {
            this.querySelector('.dropdown-menu').classList.toggle('show');
        });
    });

    // Close dropdown when clicking outside
    window.addEventListener('click', function(e) {
        dropdowns.forEach(function(dropdown) {
            if (!dropdown.contains(e.target)) {
                dropdown.querySelector('.dropdown-menu').classList.remove('show');
            }
        });
    });
});
