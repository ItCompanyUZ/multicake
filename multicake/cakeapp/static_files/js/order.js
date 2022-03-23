const orderImg = document.querySelector('.order__img')
const orderTitle = document.querySelector('.order__content-info-title')
const orderPhotoPath = document.querySelector('.order-photo')
const orderPrice = document.querySelector('.order__content-img-title')
let path =  window.localStorage.getItem("path") 
let img = path ?? 'img/default.jpg'
let title = path.split('/')[1].split('-')[1].split('~').join(' ')

orderImg.setAttribute('src', img)
orderPhotoPath.setAttribute('value', img)
orderTitle.innerText = title
if(title == 'Пирожные и десерты' || title == 'Домашняя выпечка') {
    orderPrice.innerText = ''
}