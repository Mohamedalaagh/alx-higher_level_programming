#!/usr/bin/node
const args = process.argv;
function secBig (array) {
  array.sort((a, b) => b - a);
  return array[1];
}
if (args.length <= 3) {
  console.log(0);
} else {
  const numArray = args.slice(2).map(Number);
  console.log(secBig(numArray));
}
