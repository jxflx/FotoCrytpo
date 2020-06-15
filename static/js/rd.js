const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.links');

    burger.addEventListener('click', () => {
        nav.classList.toggle('nav-active');
    })
};

document.addEventListener('DOMContentLoaded', function() {
    navSlide()
});