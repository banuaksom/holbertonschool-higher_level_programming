#!/usr/bin/node
/* prints the first argument passed to it */
if (process.argv.length >= 3) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
