#!/usr/bin/node
const fArg = process.argv[2];
if (isNaN(parseInt(fArg))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < fArg; i++) {
    console.log('C is fun');
  }
}
