#!/usr/bin/node
/*
 * The script checks if args is not a NaN (not a number) value
 * and can be converted to an integer using the
 * isNaN() and Number.isInteger() methods.
 * If this is true, the parseInt() method is used to convert args to an integer
 * with a base of 10 (which is the default)
 */

const args = process.argv[2];

if (!isNaN(args) && Number.isInteger(Number(args))) {
  console.log(`My number: ${parseInt(args, 10)}`);
} else {
  console.log('Not a number');
}
