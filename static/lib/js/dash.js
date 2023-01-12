//MenuToggle
let toggle = document.querySelector('.toggle');
let navigation = document.querySelector('.navigation');
let main = document.querySelector('.main');

toggle.onclick = function(){
    navigation.classList.toggle('active');
    main.classList.toggle('active');
}
//add hovered class in selected list item
let list = document.querySelectorAll('.navigation li');
list.forEach((item, indice)=>{
    item.addEventListener('click', function(){
        localStorage.setItem('itemActual', indice);
    });
})
list[localStorage.getItem('itemActual')].classList.add('hovered');
//Dropdown
let dropDowns = document.querySelectorAll('.dropdown');
dropDowns.forEach((dropDown)=>{
    dropDown.onclick = function(){
        list.forEach((item)=>{
            item.classList.remove('hovered');
        });
        this.classList.toggle('dropActive');
    }
})