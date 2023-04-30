document.addEventListener('DOMContentLoaded', function () {
    let sections = document.querySelectorAll('.section');

    sections.forEach(section => {
        section.addEventListener('click', function () {
            let link = section.querySelector('a');
            window.location.href = link.href;
        });
    });
});
