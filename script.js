document.getElementById('toggleButton').addEventListener('click', function() {
    var aboutSection = document.getElementById('aboutSection');
    if (aboutSection.style.display === 'none') {
      aboutSection.style.display = 'block';
    } else {
      aboutSection.style.display = 'none';
    }
  });
  