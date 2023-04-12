#!/usr/bin/node

/*
 * This code first extracts the command line arguments starting from the
 * third one using process.argv.slice(2), and then converts each argument
 * to a number using map(Number).
 */

const args = process.argv.slice(2).map(Number);

if (args.length === 0 || args.length === 1) {
  console.log(0);
} else {
  let max = Number.MIN_SAFE_INTEGER;
  let secondmax = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < args.length; i++) {
    if (args[i] > max) {
      secondmax = max;
      max = args[i];
    } else if (args[i] > secondmax && args[i] !== max) {
      secondmax = args[i];
    }
  }

  console.log(secondmax);
}
