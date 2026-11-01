// Keep legacy resume buttons pointed at the current public PDF.
(function () {
  const button = document.getElementById('resumePdfButton');
  if (!button) return;

  button.addEventListener('click', function () {
    const link = document.createElement('a');
    link.href = 'assets/Aaron_Bowman_Deadhang_Labor_Travel_Resume.pdf';
    link.download = 'Aaron_Bowman_Resume_Deadhang_Public.pdf';
    document.body.appendChild(link);
    link.click();
    link.remove();
  });
})();
