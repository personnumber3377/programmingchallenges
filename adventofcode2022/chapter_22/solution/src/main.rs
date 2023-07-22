
//use std::io;
use std::io::{self, BufRead};

// Thanks to https://stackoverflow.com/questions/56921637/how-do-i-split-a-string-using-a-rust-regex-and-keep-the-delimiters

use regex::Regex; // 1.1.8

fn split_keep<'a>(r: &Regex, text: &'a str) -> Vec<&'a str> {
    let mut result = Vec::new();
    let mut last = 0;
    for (index, matched) in text.match_indices(r) {
        if last != index {
            result.push(&text[last..index]);
        }
        result.push(matched);
        last = index + matched.len();
    }
    if last < text.len() {
        result.push(&text[last..]);
    }
    result
}


// side 0 is the base
// side 1 is the back of the cube
// side 2 is the front of the cube
// side 3 is the west side aka the side on the left
// side 4 is the east side aka the right side 
// side 5 is the top side.



fn move_up(cur_side: i32) -> i32 {
    match cur_side {
        0 => 1; // side 1 is the back of the cube
        1 => 5; // top
        2 => 0; // base
        3 => 
    }
}

fn check_col(row_lenghts: Vec<i32>, row_offsets: Vec<i32>, x: i32, y: i32) {

    //return (row_lenghts[cur_side_y_coord] <= cur_side_x_coord && row_lenghts[cur_side_y_coord] + row_lenghts[cur_side_y_coord] >= cur_side_x_coord) as bool;
    return (row_lenghts[y] <= x && row_lenghts[y] + row_lenghts[y] >= x) as bool;

}

fn search_recursive(side_coordinates: Dict<Vec<i32>>, occupied_sides: Vec<i32>, cur_side: i32, row_lenghts: Vec<i32>, row_offsets: Vec<i32>, side_len: usize, x_coord: i32, y_coord: i32) -> Dict<Vec<i32>> {

    // This marks all of the neighbours of the current side (up, down, left and right)
    let mut previous_side = cur_side;

    let mut x: i32 = x_coord;
    let mut y: i32 = y_coord;


    for mov in 0..4 {

        // Get the neighbours.

        /*
        match mov {
            0 => x += side_len; // move right
            1 => x -= side_len; // move left
            2 => y += side_len; // move up
            3 = > y -= side_len; // move down
        }
        */

        previous_side = cur_side;

        match mov {
            0 => {
                x += side_len;
                cur_side = move_right(cur_side);
            }
            1 => {
                x -= side_len;
                cur_side = move_left(cur_side);
            }
            2 => {
                y += side_len;
                cur_side = move_up(cur_side);
            }

            3 => {
                y -= side_len;
                cur_side = move_down(cur_side);
            }
        }

        // check the space.

        if side_coordinates.contains_key(cur_side) { // already checked
            cur_side = previous_side;
        }

        if check_col(row_lenghts: Vec<i32>, row_offsets: Vec<i32>, x: i32, y: i32) {
            side_coordinates.add( cur_side, Vec::new([x,y]) ); // add to the list
        }

        cur_side = previous_side;

    }

    return side_coordinates


}



// Get the cube side coordinates and cube length using the row lengths, row offsets and vertical line offsets and vertical lenghts.

fn parse_cube(row_lenghts: Vec<i32>, row_offsets: Vec<i32>, vertical_lengths: Vec<i32>, vertical_offsets: Vec<i32>) {

    // get min row length aka which is the cube length.

    let side_len: usize = row_lenghts.iter().min(); // the minimum side row length is the side length of the cube.

    //let side_coordinates: Vec<Vec<i32>> = Vec::new();
    let mut side_coordinates =  Dict::<String>::new();

    let mut cur_side = 0; // just assume that the first side is the bottom

    let mut cur_side_x_coord = row_offsets[0];
    let mut cur_side_y_coord = 0;
    
    let mut occupied_sides: Vec<i32> = Vec::new();

    let mut loop_count = 0;

    let mut sideways_move = 0;


    // loop over all of the stuff

    side_coordinates = search_recursive(side_coordinates, occupied_sides ,cur_side, row_lenghts, row_offsets, side_len, x_coord, y_coord);




    // the very first 

}



fn parse_input() -> (Vec<Vec<i32>>, Vec<i32>, Vec<i32>, Vec<i32>, Vec<i32>, Vec<i32>) {

    // Go through all the lines in stdin

    //let out_map: Vec<i32> = Vec::new();

    let mut out_map = Vec::new();

    let mut moves: Vec<i32> = Vec::new();

    let mut line_offsets: Vec<i32> = Vec::new();

    let stdin = io::stdin();
    //let mut lines = stdin.lock().lines();

    let mut lines = stdin.lock().lines();

    let mut max_x: usize = 0;

    loop {
        //println!("{}", line.unwrap());

        let cur_line = lines.next().unwrap().unwrap(); 
        println!("Current line: {}\n", cur_line);
        if cur_line.eq("") {

            break;

        }




        //let current_chars: Vec<i32> = String::from(cur_line).chars(); // Get string.

        // rent_chars[offset as usize].eq(


        //let current_chars: std::str::Chars = String::from(cur_line).chars().to_vec();

        let current_chars: Vec<char> = String::from(cur_line).chars().collect();
        if current_chars.to_vec().len() > max_x {

            max_x = current_chars.to_vec().len();
        }
        let mut offset: i32 = 0;

        // Calculate offset

        loop {
            
            //if !current_chars[offset as usize].eq(" ") {
            println!("{}", offset);
            if !(current_chars[offset as usize]== 32 as char) {
                break;

            }
            offset += 1;

        }

        // Append to offsets.

        line_offsets.push(offset);

        // let last3 = v.as_slice()[v.len()-3..].to_vec();
        // thanks to https://stackoverflow.com/questions/44549759/return-last-n-elements-of-vector-in-rust-without-mutating-the-vector

        let mut new_line: Vec<i32> = Vec::new();

        //for c in new_line.as_slice()[offset as usize..].to_vec() {
        for c in current_chars.as_slice()[offset as usize..].to_vec() {

            if c == 46 as char { // ascii character code of 46 is the dot character (".")
                new_line.push(0);
            } else {
                // assume "#" character.

                new_line.push(1);

            }


        }

        out_map.push(new_line);

    }


    let move_line = lines.next().unwrap().unwrap(); 

    // now the very last line is the line which tells all of the moves and stuff.

    // Extract integers and moves from string.

    //     let seperator = Regex::new(r"([ ,.]+)").expect("Invalid regex");

    let seperator = Regex::new(r"R|L").expect("Invalid regex");

    let move_stuff = split_keep(&seperator, &move_line);

    let mut move_lenghts: Vec<i32> = Vec::new();

    let mut count: i32 = 0;

    for m in move_stuff {
        if count % 2 == 0 {

            move_lenghts.push(m.parse::<i32>().unwrap());  // modulo two equals zero means length.

        } else {

            assert!(m.eq("L") || m.eq("R")); // Only left and right moves are allowed.
            if m.eq("L") {

                moves.push(0); // 0 == left
            } else {
                moves.push(1); // 1 == right
            }
            //moves.append(m);
        }

        count += 1;

        //move_lenghts.append()

    }


    // Now get the horizontal lengths and offsets.

    let mut horizontal_offsets: Vec<i32> = Vec::new();

    let mut horizontal_lengths: Vec<i32> = Vec::new();

    let mut y_count: i32 = 0;
    let mut intermediate: i32 = 0;
    //for x_count in 0..out_map[0].len() {  // loop through all columns
    for x_count in 0..max_x {  // loop through all columns  
        y_count = 0;
        println!("Looping with x_count {}",x_count);
        println!("max_x == {}",max_x);
        loop {
            println!("line_offsets[y_count as usize] == {:?}", line_offsets[y_count as usize]);
            if (line_offsets[y_count as usize] <= x_count as i32 && line_offsets[y_count as usize] + (out_map[y_count as usize].len() - 1) as i32 >= x_count as i32) || x_count == max_x {
                break;
            }

            y_count += 1;
        }

        horizontal_offsets.push(y_count); // offset to the line start


        //y_count = 0;
        intermediate = y_count;
        loop {
            //if line_offsets[y_count as usize] <= x_count as i32 {
            //    break;
            //}

            

            println!("y_count == {}", y_count);
            if y_count as usize == line_offsets.len() || !(line_offsets[y_count as usize] <= x_count as i32 && line_offsets[y_count as usize] + (out_map[y_count as usize].len() - 1) as i32 >= x_count as i32) {
                break;
            }

            println!("poopoo {}", (line_offsets[y_count as usize] <= x_count as i32 && line_offsets[y_count as usize] + (out_map[y_count as usize].len() - 1) as i32 >= x_count as i32));
            y_count += 1;
        }

        horizontal_lengths.push(y_count - intermediate);


    }

    //println!("horizontal_lengths: {}", horizontal_lengths);

    println!("horizontal_lengths: {:?}", horizontal_lengths);
    
    //println!("horizontal_offsets: {}", horizontal_offsets);

    println!("horizontal_offsets: {:?}", horizontal_offsets);


    //(out_map, line_offsets, moves, move_lenghts);

    (out_map, line_offsets, moves, move_lenghts, horizontal_offsets, horizontal_lengths)

}



fn main_loop(game_map: Vec<Vec<i32>>, line_offsets: Vec<i32>, mut moves: Vec<i32>, move_lenghts: Vec<i32>, vertical_offsets: Vec<i32>, vertical_lengths: Vec<i32>) -> i32 {

    let mut cur_x: i32 = line_offsets[0]; // This must be here because we start on the top.
    let mut cur_y: i32 = 0;

    let mut distance: i32 = 0;

    let mut turn = 0;

    let mut facing = 0;  // "Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^)."

    let mut counter = 0;

    let mut dx = 0;

    let mut dy = 0;

    let mut x_access = 0;

    let mut y_access = 0;

    let mut prev_x = 0;

    let mut prev_y = 0;

    moves.push(1); // final move does not matter

    for m in moves {

        // Mainloop

        distance = move_lenghts[counter];

        // Try to go forward
        println!("facing == {}", facing);
        match facing {
            0 => {
                dx = 1;
                dy = 0;
            }
            1 => {
                dx = 0;
                dy = 1;  // Y is one on the highest level and the biggest on the ground.
            }
            2 => {
                dx = -1;
                dy = 0;
            }
            3 => {
                dx = 0;
                dy = -1;
            }
            _ => {
                assert!(false); // shouldn't happen.
            }
        }

        // Try to advance
        
        println!("distance == {}", distance);
        for n in 0..distance {



            prev_x = cur_x;

            prev_y = cur_y;

            cur_x += dx;

            cur_y += dy;

            println!("cur_y before check: {}", cur_y);
            println!("cur_x before check: {}", cur_x);

            // check loop.

            // check Y

            /*

            if vertical_offsets[cur_x as usize] > cur_y { // underflow aka go up
                println!("poopoothing1");
                cur_y = (vertical_offsets[cur_x as usize]  as usize + (vertical_lengths[cur_x as usize] as usize) - 1) as i32; // loop back around
            }

            if vertical_offsets[cur_x as usize] + vertical_lengths[cur_x as usize] -1 < cur_y {
                println!("poopoothing2");
                cur_y = (vertical_offsets[cur_x as usize]  as usize) as i32;  // overflow aka go down
            } 

            // check X

            if line_offsets[cur_y as usize] > cur_x {
                cur_x = line_offsets[cur_y as usize]  as i32 + (game_map[cur_y as usize].len() - 1) as i32; // loop to the right when going left
            }

            if line_offsets[cur_y as usize] + (game_map[cur_y as usize].len() as i32) -1 < cur_x {
                cur_x = line_offsets[cur_y as usize]  as i32; // loop to the left when going right
            }

            */

            if vertical_offsets[prev_x as usize] > cur_y { // underflow aka go up
                println!("poopoothing1");
                cur_y = (vertical_offsets[prev_x as usize]  as usize + (vertical_lengths[prev_x as usize] as usize) - 1) as i32; // loop back around
            }

            if vertical_offsets[prev_x as usize] + vertical_lengths[prev_x as usize] -1 < cur_y {
                println!("poopoothing2");
                cur_y = (vertical_offsets[prev_x as usize]  as usize) as i32;  // overflow aka go down
            } 

            // check X

            if line_offsets[prev_y as usize] > cur_x {
                println!("poopoothing3");
                cur_x = line_offsets[prev_y as usize]  as i32 + (game_map[prev_y as usize].len() - 1) as i32; // loop to the right when going left
            }

            if line_offsets[prev_y as usize] + (game_map[prev_y as usize].len() as i32) -1 < cur_x {
                println!("poopoothing4");
                cur_x = line_offsets[prev_y as usize]  as i32; // loop to the left when going right
            }



            println!("line_offsets[cur_y as usize] + (game_map[cur_y as usize].len() as i32) == {}",line_offsets[cur_y as usize] + (game_map[cur_y as usize].len() as i32));

            // check block

            // actual place is cur_x, (line_offsets[cur_y]+cur_x)%game_map[cur_y].len()

            println!("cur_y: {}", cur_y);
            println!("cur_x: {}", cur_x);
            //println!("game_map.len() == {}\n",game_map.len());
            //if game_map[(cur_y as usize % game_map.len()) as usize][((line_offsets[(cur_y as usize % game_map.len()) as usize]+cur_x)%(game_map[(cur_y as usize % game_map.len()) as usize].len()) as i32) as usize] == 1 {

            //x_access = ((line_offsets[(cur_y as usize % game_map.len()) as usize]+cur_x)%(game_map[(cur_y as usize % game_map.len()) as usize].len()) as i32) as usize;
            
            //y_access = (cur_y as usize % game_map.len()) as usize
            
            //println!("(vertical_offsets[(cur_x as usize % game_map[cur_y as usize].len()) as usize]+cur_y) == {}",(vertical_offsets[(cur_x as usize % game_map[cur_y as usize].len()) as usize]+cur_y));

            //println!("(game_map[(cur_x as usize % game_map[cur_y as usize].len()) as usize].len()) == {}", (game_map[(cur_x as usize % game_map[cur_y as usize].len()) as usize].len()));
            // y_access = (offset)+(y%vertical_length)


            //y_access = ((vertical_offsets[(cur_x as usize % game_map[cur_y as usize].len()) as usize]+cur_y)%(game_map[(cur_x as usize % game_map[cur_y as usize].len()) as usize].len()) as i32) as usize;
            
            //y_access = (vertical_offsets[cur_x as usize % vertical_offsets.len()]) + (cur_y % horizontal_lengths[cur_x as usize % vertical_offsets.len()]);


            //println!("access index: {}",cur_x as usize % vertical_offsets.len());
            
            //println!("current vertical offset: {}", vertical_offsets[cur_x as usize % vertical_offsets.len()]);
            //println!("current vertical length: {}",vertical_lengths[cur_x as usize % vertical_offsets.len()]);
            
            //y_access = (vertical_offsets[cur_x as usize % vertical_offsets.len()]) as usize + (cur_y as usize % vertical_lengths[cur_x as usize % vertical_offsets.len()] as usize) as usize;


            //println!("x_access: {}", x_access);
            //println!("y_access: {}", y_access);

            x_access = cur_x - line_offsets[cur_y as usize]; // delete the offset.

            //y_access = cur_y - vertical_offsets[cur_x as usize];

            y_access = cur_y;

            println!("x_access: {}", x_access);
            println!("y_access: {}", y_access);
            println!("game_map[y_access as usize][x_access as usize] == {}",game_map[y_access as usize][x_access as usize]);
            if game_map[y_access as usize][x_access as usize] == 1 {
                // Blocked
                println!("Blocked");
                //cur_y -= dy;

                //cur_x -= dx;

                cur_x = prev_x;
                cur_y = prev_y;

                println!("cur_y: {}", cur_y);
                println!("cur_x: {}", cur_x);

                break


            }

        
        }

        if m == 0 {
            println!("Decrementing facing.");
            println!("Facing before decrement: {}", facing);

            facing -= 1; // left
            println!("Facing after decrement: {}", facing);
            // The precent sign works differently than in python. In python it is the modulo, when as in rust it is the remainder. The modulo and the remainder are the same for non-negative divisors and dividends, but for negative numbers they differ: https://stackoverflow.com/questions/31210357/is-there-a-modulus-not-remainder-function-operation
            // for example -2 % 5 = -2   , but (-2).rem_euclid(5) = 3




            //facing = facing % 4;
            facing = (facing as i32).rem_euclid(4);
            println!("Facing after modulo: {}", facing);
        } else {
            // assume right
            facing += 1;
            facing = (facing as i32).rem_euclid(4);
            //facing = facing % 4;
        }



        
        counter += 1;



    }
    facing -= 1; // reset the facing because we add one on the last cycle
    

    // Need to add one because the coordinates are one base index based

    cur_x += 1;
    cur_y += 1;

    println!("Final x: {}\n", cur_x);
    println!("Final y: {}\n", cur_y);

    let password: i32 = cur_y * 1000 + cur_x * 4 + facing;

    println!("Password should be: {}", password);

    return password;


}



fn main() {
    
    //let (game_map: Vec<i32>, line_offsets: Vec<i32>, moves: Vec<i32>, move_lenghts: Vec<i32>) = parse_input();

    //let (game_map, line_offsets, moves, move_lenghts) = parse_input();
    let (game_map, line_offsets, moves, move_lenghts, horizontal_offsets, horizontal_lengths) = parse_input();
    let mut answer: i32;

    answer = main_loop(game_map, line_offsets, moves, move_lenghts, horizontal_offsets, horizontal_lengths);

    println!("[+] Puzzle solution is: {}", answer);

    return ()
}
