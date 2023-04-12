#!/usr/bin/node

/*
 * The slice(2) method is used to remove the first two arguments
 * which are the paths to the Node.js executable and the script file
 */

const [arg1, arg2] = process.argv.slice(2);

console.log(`${arg1} is ${arg2}`);
