#!/usr/bin/env ruby
# this needs a comment?

puts ARGV[0].scan(/(?<=from:|to:|flags:).+?(?=\])/).join(',')
