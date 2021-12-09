use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

#[path = "../util/file_utils.rs"] mod file_utils;

const INPUT_PATH: &str = "input.txt";
const TEST_INPUT_PATH: &str = "src/day5/test_input.txt";
const TEST_INPUT_PART_1_OUT: u8 = 5;

fn part1() {
    let file = match File::open(TEST_INPUT_PATH) {
        Err(why) => panic!("couldn't open {}: {}", TEST_INPUT_PATH, why),
        Ok(file) => file,
    };

    // read vents list from input file
    let reader = BufReader::new(file);
    let mut vents: Vec<Vec<[i32; 2]>> = Vec::new();
    for x in reader.lines().enumerate() {
        match x.1 {
            Ok(x) => {
                let split = x.split(" -> ");
                let vec = split.collect::<Vec<&str>>();
                let mut start_split: [i32; 2] = [0; 2];
                let mut end_split: [i32; 2]  = [0; 2];
                let start_split_str: Vec<&str>= vec[0].split(",").collect::<Vec<&str>>();
                start_split[0] = start_split_str[0].parse().unwrap();
                start_split[1] = start_split_str[1].parse().unwrap();
                let end_split_str: Vec<&str>= vec[0].split(",").collect::<Vec<&str>>();
                end_split[0] = end_split_str[0].parse().unwrap();
                end_split[1] = end_split_str[1].parse().unwrap();
                vents.push(vec![start_split, end_split]);
            }
            Err(_) => {}
        }
    }

    let map: Vec<[i32; 10]> = vec![[0; 10]; 10];
    for vent in vents {
        let start: [i32; 2] = vent[0];
        let end: [i32; 2] = vent[1];
        if start[0] == end[0] {
            for i in start[1]..end[1] {
                let x1 = map[i];
                x1
                // map[i][start[0]] += 1;
            }
        } else {
           for i in start[0]..end[0] {
                // map[start[1]][i] += 1;
            }
        }
    }
}

fn main() {
    part1()
}