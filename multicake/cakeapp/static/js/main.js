$(document).ready(function () {
    $(".navbar-toggler>i").click(function (e) {
        e.preventDefault();
        $(".header__menu").toggleClass("d-flex");
    })
})

let btn = document.querySelectorAll('.tabs__control');
let tabsContent = document.querySelectorAll('.tabs__content-det');
let tabsContentActive = document.querySelector('.tabs__content-active')
console.log(tabsContent);
for (let i = 0; i < btn.length; i++) {
    btn[i].addEventListener('click', () => {

        for (let j = 0; j < tabsContent.length; j++) {
            console.log(tabsContent);
            tabsContent[j].style.display = 'none'
            btn[j].classList.remove('tabs__control-active');
        }
        tabsContent[i].style.display = 'flex'
        tabsContentActive.style.display = 'none'
        btn[i].classList.add('tabs__control-active');
       
    })
}

const images = document.querySelectorAll('.tabs__content-img')

for (let i = 0; i < images.length; i++) {
    images[i].addEventListener('click' , () => {
        let path = images[i].getAttribute('src') 
        window.localStorage.setItem("path", path);
    })
}

