#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('No arguments');
} else {
  console.log(`${process.argv[2]}`);
}
