use std::io;

fn main() {
    println!("Number guessing game.");
    println!("Enter a number.");

    let mut user_input = String::new();
    io::stdin()
        .read_line(&mut user_input)
        .expect("Failed to read input line.");

    println!("The input is {}", user_input);
}
