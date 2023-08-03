


const navToggle =document.getElementById('nav-toggle')
const ul =document.getElementsByClassName('nav')
function toggle(){
    navToggle.classList.toggle('is-active')
    ul[0].classList.toggle('show')
}