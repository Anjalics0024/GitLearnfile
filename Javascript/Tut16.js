console.log("This is tut 16");
let element = document.createElement('li');
element.className = 'childul';
console.log(element);
element.id = 'clild ele';
element.setAttribute('title', 'myTitle');
element.innerHTML= '<b>This is my Home Page</b>';


let ul = document.querySelector('ul.this');

let elem2 = document.createElement('h3');
elem2.className = 'elem2';
elem2.classId = 'Element2';
let lnode = document.createTextNode('This is for node elem2');
elem2.appendChild(lnode);
elem2.setAttribute('title','newTitle');
console.log(elem2);