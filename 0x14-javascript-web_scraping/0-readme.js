#!/usr/bin/node
/* reads and prints the content of a file */
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data.toString().replace(/\r?\n|\r/g, ' '));
});
