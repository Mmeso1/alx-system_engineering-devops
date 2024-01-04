#!/usr/bin/env ruby

# Check if an argument is provided
if ARGV.empty?
  puts "Usage: #{File.basename(__FILE__)} <executable_file>"
  exit 1
end

# Get the executable file from the command line arguments
executable_file = ARGV[0]

# Define an array of test strings
test_strings = ['hbn', 'hbon', 'hbtn', 'hbttn', 'hbtttn', 'hbttttn']

# Iterate over the test strings
test_strings.each do |test_string|
  # Run the executable with the current test string as an argument
  result = `#{executable_file} #{test_string} | cat -e`.chomp

  # Display the result
  puts "#{result}"
end

