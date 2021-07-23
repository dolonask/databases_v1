let searchBtn = document.querySelector('#search-btn');

getRight();

/** Событие и обработчик для кнопки найти
 *  Готовит данные для запроса
 * **/
searchBtn.onclick = function () {
    let sChecks = document.querySelectorAll('.s-checks:checked');
    let arr = [];

    sChecks.forEach(i => {
        let select = document.querySelector(`[data-id='${i.id}']`);
        let selected = [...select.selectedOptions].map(option => {return {id: option.value} });
        let obj = {id: i.id, item: selected};
        arr.push(obj);
    });

    getResult(arr);
}

/** Отправляет запрос для получение данных
 * @param {array} data - тело запроса
 * */
function getResult(data){
    document.querySelector('.loading').classList.remove('d-none');

    const url = 'http://databasesv1.herokuapp.com/migrant/data/get/';
    let options = {
        method:'POST',
        headers:{
             'Content-Type': 'application/json'
        },
        body:JSON.stringify(data)
    }

    fetch(url, options)
        .then(response => response.json())
        .then(data => showResult(data))
}

/** Показывает результат
 * @param {array} data - ответ от запроса
 * */
function showResult(data) {
    let td = '';
    let tr = '';
   data.forEach(item => {
       let keys = Object.keys(item);
       keys.forEach(i => {
           td += '<td>' + item[i] + '</td>';
       });

       tr += '<tr>' + td + '</td>';
       td = '';
   });

   document.querySelector('#left-result').innerHTML = tr;
   document.querySelector('.loading').classList.add('d-none');

}

function getRight(){
    const url = 'http://databasesv1.herokuapp.com/migrant/data/'
    fetch(url)
        .then(response => response.json())
        .then(data => showRight(data))
}

/** Выводит список для поиска
 * @param {array} data - Данные для вывода
 * */
function showRight(data) {
    let block = '';
    data.forEach(item => {
        block += createRightElems(item.name, item.item, item.id);
    })

    document.querySelector('#right-result').innerHTML = block;

    let sChecks = document.querySelectorAll('.s-checks');

    sChecks.forEach(s => {
        s.onchange = showItems;
    })

}

/** Выводит блок для выпадающего списка
 * @param {object} e - Обьект event
 * */
function showItems(e) {
    let target = e.target.parentElement.parentElement.nextElementSibling;
    target.classList.toggle('d-none');
}

/** Создает выпадающий список
 * @param {string} name - Название выпад списка
 * @param {array} item - Список с данными
 * @param {string} id - Идентификатор
 * */
function createRightElems(name, item, id) {
    let itemElems = '';

    item.forEach(i => {
        itemElems += `<option value="${i.id}">${i.name}</option>`;
    })

    let block = '<div class="item">' +
                    '<div class="item-header">' +
                        '<label>' + name + ' <input class="s-checks" id="'+ id +'" type="checkbox"></label>' +
                    '</div>' +
                    '<div class="item-body d-none pt-3 pb-3">' +
                         '<select data-id="' + id + '" class="form-control s-selects" id="" multiple>'
                             + itemElems +
                         '</select>' +
                    '</div>' +
               '</div>';


    return block;

}

function getItems(e) {
    let value = e.target.value;

    console.log(value);
}