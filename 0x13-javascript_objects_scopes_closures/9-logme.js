#!/usr/bin/node

let noArg = 0;

exports.logMe = function (item) {
  console.log(noArg + ': ' + item);
  noArg++;
};
