#!/usr/bin/node

const lists = require('./100-data').list;

const mapList = lists.map((num, index) => num * index);

console.log(lists);
console.log(mapList);
