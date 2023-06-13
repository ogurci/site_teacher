document.addEventListener('DOMContentLoaded', function() {
    var sidebar = document.querySelector('.sidebar');
    var toggleButton = document.querySelector('.toggle-button');

    toggleButton.addEventListener('click', function() {
      sidebar.classList.toggle('active');
    });
  });