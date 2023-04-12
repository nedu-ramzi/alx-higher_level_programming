#!/usr/bin/node

const size = parseInt(process.argv[2]);
let i;

if (isNaN(size)) {
  console.log('Missing number of occurencies');
} else {
  for (i = 0; i < size; i++) {
    console.log('C is fun');
  }
}
