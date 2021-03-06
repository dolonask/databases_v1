let searchBtn = document.querySelector('#search-btn');
let datas;
getRight();

/** Событие и обработчик для кнопки найти
 *  Готовит данные для запроса
 * **/
searchBtn.onclick = function () {
    let sChecks = document.querySelectorAll('.s-checks:checked');
    let arr = [];

    sChecks.forEach(i => {
        let elem = document.querySelector(`[data-id='${i.id}']`);

        if(elem.localName !== 'input'){
            let selected = [...elem.selectedOptions].map(option => ({ id: option.value }) );
            arr.push({id: i.id, item: selected});
        } else{
            arr.push({ id:i.id, item:[{id:elem.value}] });
        }
    });

    getResult(arr);
}

/** Отправляет запрос для получение данных
 * @param {array} data - тело запроса
 * */
function getResult(data) {
    const url = document.getElementById('work_data_get').textContent;

    console.log({url});

    // const url = 'https://databasesv1.herokuapp.com/work/data/get/';
    // const url = 'http://localhost:8000/work/data/get/';

    let options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    }

    fetch(url, options)
        .then(response => response.json())
        .then(data => showResult(data))
}

/** Показывает результат
 * @param {array} data - ответ от запроса
 * */
function showResult(data) {

    console.log({data});
    let td = '';
    let tr = '';
    let d = [];
    let str = '';
    data.forEach(item => {
        let keys = Object.keys(item);
        console.log({keys});
        keys.forEach(i => {
            if(i.includes('id') || i.includes('date')){
                d.push(`data-${i}=${item[i]}`);

                d.forEach(i => {
                    str += i + ' '
                })
            } else{
                td += '<td>' + item[i] + '</td>';
            }
        });

        tr += '<tr ' + str + ' class="rowTable">' + td + '</td>';
        td = '';
        d=[];
        str='';
    });

    document.querySelector('#left-result').innerHTML = tr;

    let rows = document.querySelectorAll('.rowTable');

    rows.forEach(i => {
        i.onclick = getDataAttr;
    });
}

function getDataAttr(e){
    const obj = {...e.target.parentElement.dataset};

    getModalInfo(obj);
}

function getModalInfo(obj){
   const url = 'http://127.0.0.1:8000/analytic/work/search/';
   const options = {
       method:'POST',
       headers:{
           'Content-Type':'application/json'
       },
       body:JSON.stringify(obj)
   }

   fetch(url, options)
      .then(response => {
          if(response.ok){
             return response.json();
          } else {
             alert('Код ошибки: ', response.status)
          }
      })
      .then(data=>showInoModal(data))
}

function showInoModal(data){
    let td = '';
    let tr = '';
    data.forEach(item => {
        td += '<td>' + item['id'] + '</td>';
        td += '<td>' + item['user'] + '</td>';
        td += '<td>' + item['case_name'] + '</td>';
        td += '<td>' + item['region'] + '</td>';
        td += '<td>' + item['country'] + '</td>';
        td += '<td>' + new Date(item['date_create']).toLocaleDateString() + '</td>';
        td += '<td>' + new Date(item['date_update']).toLocaleDateString() + '</td>';
        tr += '<tr>' + td + '</td>';
        td = '';
    });

    document.querySelector('#tbody').innerHTML = tr;

    $('#myModal').modal();
}

function getRight() {
    const url = document.getElementById('work_data').textContent;
    // const url = 'https://databasesv1.herokuapp.com/work/data/'
    // const url = 'http://127.0.0.1:8000/work/data/';
    fetch(url)
        .then(response => response.json())
        .then(data => {
            datas = data;
            showRight(data)
        })
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
    });

    document.querySelector('#region').onclick = function(e){
        let regions;
        if(e.target.checked){
            let select = document.querySelector('[data-id="country"]');
            let selected = [...select.selectedOptions].map(option => {
                return option.value;
            }); //айдишники стран


            data.forEach(i => {
                if(i.id === 'region') regions = i;
            }); //получаю регионы

            let regions2 = [];
            selected.forEach(item => {
                regions2.push(regions.item[item]);
            })

            let regionOptions;
            regions2.flat().forEach(i => {
                regionOptions += `<option value="${i.id}">${i.name}</option>`;
            })

            document.querySelector('[data-id="region"]').innerHTML = regionOptions;
        }
    }
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
    if (id !== 'region') {
        item.forEach(i => {
            itemElems += `<option value="${i.id}">${i.name}</option>`;
        })
    }


    let block = '<div class="item panel panel-primary">' +
        '<div class="item-header panel-heading">' +
        '<label class="s-label no-margin">' + name + ' <input class="s-checks" id="' + id + '" type="checkbox"></label>' +
        '</div>' +
        '<div class="item-body d-none pt-3 pb-3 panel-body">' +
        '<select data-id="' + id + '" class="form-control s-selects" id="" multiple>'
        + itemElems +
        '</select>' +
        '</div>' +
        '</div>';


    return block;

}
