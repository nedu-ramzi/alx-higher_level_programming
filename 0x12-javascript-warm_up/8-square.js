#!/usr/bin/node

const arg = process.argv[2];
const argSize = parseInt(arg);
let row;
let i;
let j;

if (!isNaN(arg) && Number.isInteger(Number(arg))) {
  for (i = 0; i < argSize; i++) {
    row = '';
    for (j = 0; j < argSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
