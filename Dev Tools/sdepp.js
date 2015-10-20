'use strict';

const fs = require('fs');
const app = require('commander');
import * as R from 'ramda';

const sdepp = (function() {
  function preprocess(logfile) {
    // Read the file and remove the sketch information at the end.
    let lines = fs.readFileSync(logfile).toString().split(/\r?\n/);
    let model = [];
    let beforeSketch = true;
    R.forEach(line => {
      if (beforeSketch) {
        if (line.match(/\\\\\\---\/\/\/ Sketch/)) {
          beforeSketch = false;
        }
        else {
          model.push(line);
        }
      }
    }, lines);
    // Join lines continued with trailing backslash characters.
    const backslash = /\\/;
    let prevLine = '';
    R.forEach(line => {
      if (!R.isEmpty(prevLine)) {
          // console.log(`BEFORE ${line}`);
        line = prevLine + line.trim();
          // console.log(`AFTER ${line}`);
        prevLine = '';
      }
      const m = line.match(backslash);
      if (m) {
        if (m.index == line.length-1) {
          prevLine = line.substr(0, line.length-1);
        }
        else {
          console.error(`ERROR: backslash before end of line at position ${m.index} in ${line}`);
        }
      }
      if (R.isEmpty(prevLine)) {
        console.log(line);
      }
    }, model);
  }

  function main() {
    app
      .version('0.1.4')
      .option('-m, --model <model-file>', '.mdl model file name')
      .parse(process.argv);

    if (app.model) {
      preprocess(app.model);
    }
    else {
      app.help();
    }
    process.exit(0);
  }
  return {
    main: main
  }
}());

sdepp.main();
