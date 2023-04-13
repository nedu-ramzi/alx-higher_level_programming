#!/usr/bin/node

const dict = require('./101-data').dict;

const totalList = Object.entries(dict);
const valueList = Object.values(dict);
const uniqueValue = [...new Set(valueList)];
const newDict = {};

for (const j in uniqueValue) {
  const list = [];
  for (const k in totalList) {
    if (totalList[k][1] === uniqueValue[j]) {
      list.unshift(totalList[k][0]);
    }
  }
  newDict[uniqueValue[j]] = list;
}

console.log(newDict);
