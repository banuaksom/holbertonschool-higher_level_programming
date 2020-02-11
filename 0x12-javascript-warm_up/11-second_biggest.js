#!/usr/bin/node
/* searches the second biggest integer in list of args */
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log('0');
} else {
  const arr = process.argv.slice(2).sort((a, b) => a - b);
  const len = arr.length;

  console.log(arr[len - 2]);
}
