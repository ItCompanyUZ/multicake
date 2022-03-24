

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


function plusSlides(n){
    counter+=n;
    slidefun(counter)
    resetTimer();
}

function currentSlide(n){
    counter=n
    slidefun(counter)
    resetTimer()
}


function openCity(evt, cakeType) {
    // Declare all variables
    var i, tabcontent, tablinks;
    var cake = cakeType
    console.log(cake)
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the button that opened the tab
    document.getElementById(cakeType).style.display = "block";
    evt.currentTarget.className += " active";
  }



// const postsBox = document.getElementById('filling-box')
// const fillingBox = document.getElementById('filling-box')
// const spinnerBox = document.getElementById('spinner-box') 
// const loadBtn = document.getElementById('load-btn')
// const loadBox = document.getElementById('loading-box')
// let visible = 3


// const handleGetData = () => {
//     console.log("Hi nigga")
//     $.ajax({
//         type: 'GET',
//         url: `json-list/${visible}`,
//         success: function(response){
//             console.log(response.data)
//             maxSize = response.max
//             const data = response.data
//             spinnerBox.classList.remove('not-visible')
//             setTimeout(()=>{
//                 spinnerBox.classList.add('not-visible')
//                 data.map(post=>{
//                     console.log(post.id)
//                     postsBox.innerHTML += `<div class="card p-3 mt-3 mb-3">
//                                                 ${post.name}
//                                                 <br>
//                                                 ${post.body}
//                                             </div>`
//                 })
//                 if(maxSize){
//                     console.log('done')
//                     loadBox.innerHTML = "<h4>No more posts to load</h4>"
//                 }
//             }, 500)
//         },
//         error: function(error){
//             console.log(error)
//         }
//     })
// }



// handleGetData()
// loadBtn.addEventListener('click', ()=>{
//     visible += 3
//     handleGetData()
// })









