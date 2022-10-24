$(document).ready(() => {
    
    // const navUl = document.querySelector('nav ul')
    // const burgerNav = document.getElementsByClassName('burger-nav');
    // burgerNav.addEventListener("click", function(evt) {
    //     navUl.classList.toggle('open');
    // })
});

$('.burger-nav').on('click', () => {
    $('nav ul').toggleClass("open");
    // $('nav ul').hide();
});