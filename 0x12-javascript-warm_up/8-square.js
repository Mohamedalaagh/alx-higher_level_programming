#!/usr/bin/node
const arg = process.argv[2];
if (isNaN(parseInt(arg))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('X'.repeat(arg));
  }
}
