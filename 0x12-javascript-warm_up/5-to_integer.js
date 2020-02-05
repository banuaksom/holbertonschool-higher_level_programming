#!/usr/bin/node
/* prints the first argument if it can be converted to an integer */
if (!parseInt(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: %d', parseInt(process.argv[2]));
}
