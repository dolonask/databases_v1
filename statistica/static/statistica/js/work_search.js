let searchBtn = document.querySelector('#search-btn');
let datas;
getRight();

/** Событие и обработчик для кнопки найти
 *  Готовит данные для запроса
 * **/
searchBtn.onclick = function () {
    let country = document.querySelector('[data-id="country"]').value;
    if(!country){
        alert('Выберите страну');
        return;
    }

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
    if(!data.length) {
        clearTable();
        return;
    };
    let td = '';
    let tr = '';
    let tr2 = '';
    let th = '';
    let d = [];
    let str = '';

    data.forEach(item => {
        let keys = Object.keys(item);
        keys.forEach((i,index) => {
            if(i.includes('id') || i.includes('date')){
                d.push(`data-n${index}=${i}`,`data-v${index}=${item[i]}`);
                d.forEach(i => {
                    str += i + ' '
                })
            } else {
                td += '<td>' + item[i] + '</td>';
            }
        });

        tr += '<tr ' + str + ' class="rowTable">' + td + '</td>';
        td = '';
        d=[];
        str='';
    });


    let keys2 = Object.keys(data[0]);
    keys2.forEach(i => {
        if(!i.includes('id') && !i.includes('date')){
           th += '<th>' + sp_fields[i] + '</td>';
        }
    });
    tr2 = '<tr>' + th + '</tr>';

    document.querySelector('#left-result').innerHTML = tr;
    document.querySelector('#left-header').innerHTML = tr2;

    let rows = document.querySelectorAll('.rowTable');

    rows.forEach(i => {
        i.onclick = getDataAttr;
    });
}

function getDataAttr(e){
    const start_date = document.querySelector('#start_date:checked') ? document.querySelector('input[data-id="start_date"]').value : '';
    const end_date = document.querySelector('#end_date:checked') ? document.querySelector('input[data-id="end_date"]').value : '';

    const obj = {...e.target.parentElement.dataset};
    let dataObjects = {};

    for (let propsName in obj){
       if(propsName.includes('n')){
           let last = propsName.substr(-1);
           let name = obj[propsName];
           let value = 'v'+last;
           dataObjects[name] = obj[value];
       }
    }

    getModalInfo({start_date, end_date, ...dataObjects});
}

function getModalInfo(obj){
   const url = document.getElementById('work_search').textContent;
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
      .then(data=>showInfoModal(data))
}

function showInfoModal(data){
    let td = '';
    let tr = '';
    data.forEach(item => {

        td += '<td>' + item['id'] + '</td>';
        td += '<td>' + item['user'] + '</td>';
        td += '<td>' + '<a href="http://130.193.53.66:8000/analytic/detail/'+ item['id'] + '" target="_blank">'  + item['case_name'] + '</a></td>';
        td += '<td>' + item['region'] + '</td>';
        td += '<td>' + item['country'] + '</td>';
        td += '<td>' + new Date(item['date_create']).toLocaleDateString() + '</td>';
        td += '<td>' + new Date(item['date_update']).toLocaleDateString() + '</td>';
        tr += '<tr>' + td + '</tr>';
        td = '';
    });

    document.querySelector('#tbody').innerHTML = tr;

    $('#myModal').modal();
}

function getRight() {
    const url = document.getElementById('work_data').textContent;
    fetch(url)
        .then(response => response.json())
        .then(data => {
            datas = data;
            showRight(data)
        })
}

function clearTable(){
    document.querySelector('#left-result > tr').remove();
}

/** Выводит список для поиска
 * @param {array} data - Данные для вывода
 * */
function showRight(data) {
    let block = '';
    data.forEach(item => {
        block += createRightElems(item.name, item.item, item.id_name);
    })

    document.querySelector('#right-result').innerHTML = block;

    let sChecks = document.querySelectorAll('.s-checks');

    let sSelects = document.querySelectorAll('.s-selects');

    sChecks.forEach(s => {
        s.onchange = showItems;
    });

    sSelects.forEach(select => {
        select.onclick = showChildBlocks;
    });

    document.querySelector('#region').onclick = function(e){
        let regions;
        if(e.target.checked){
            let select = document.querySelector('[data-id="country"]');
            let selected = [...select.selectedOptions].map(option => {
                return option.value;
            }); //айдишники стран

            console.log({data});

            data.forEach(i => {
                if(i.id_name === 'region') regions = i;
            }); //получаю регионы

            let regions2 = [];
            selected.forEach(item => {
                regions2.push(regions.item[item]);
            })

            let regionOptions = '<option value="0">Выберите</option>';
            regions2.flat().forEach(i => {
                regionOptions += `<option value="${i.id}">${i.name}</option>`;
            })
            document.querySelector('[data-id="region"]').innerHTML = regionOptions;
        }
    }
}

function showChildBlocks(e){
         let child = e.currentTarget.options[e.currentTarget.selectedIndex].dataset.child;
         e.currentTarget.nextElementSibling.innerHTML = '';

         if(child){
             let childItems = JSON.parse(e.currentTarget.options[e.currentTarget.selectedIndex].dataset.childitems);
             let name = e.currentTarget.options[e.currentTarget.selectedIndex].dataset.name;
             let id = e.currentTarget.options[e.currentTarget.selectedIndex].dataset.idopt;
             let childBlock = createRightElems(name, childItems, id);

             e.currentTarget.nextElementSibling.innerHTML = childBlock;

             let sChecks = document.querySelectorAll('.s-checks');
             sChecks.forEach(s => {
                 s.onchange = showItems;
             });

             let sSelects = document.querySelectorAll('.s-selects');
             sSelects.forEach(select => {
                 select.onchange = showChildBlocks;
             });
         }
}

/** Выводит блок для выпадающего списка
 * @param {object} e - Обьект event
 * */
function showItems(e) {
    let target = e.target.parentElement.parentElement.nextElementSibling;

    if(target.querySelectorAll('.s-checks').length){
        target.querySelectorAll('.s-checks').forEach(item => {
            item.parentElement.parentElement.parentElement.classList.add('d-none');
        })
    }
    target.classList.toggle('d-none');
    target.querySelector('select').selectedIndex = 0;
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
            itemElems += `<option data-idopt='${i.id_name || ''}' data-name="${i.name}" data-childitems='${JSON.stringify(i.item) || ''}' data-child="${i.child || ''}" value="${i.id}">${i.name}</option>`;
        })
    }

    let block = '<div class="item panel panel-primary">' +
        '<div class="item-header panel-heading">' +
        '<label class="s-label no-margin">' + name + ' <input class="s-checks" id="' + id + '" type="checkbox"></label>' +
        '</div>' +
        '<div class="item-body d-none pt-3 pb-3 panel-body">' +
        '<select data-id="' + id + '" class="form-control s-selects" id="">'+
        `<option data-name="" data-childitems="" data-child="" value="">Выберите</option>`
        + itemElems +
        '</select>' +
        '<p><p/>' +
        '</div>' +
        '</div>';


    return block;

}
