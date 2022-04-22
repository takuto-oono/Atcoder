n, k = gets.split(' ').map(&:to_i)
(1..k).each do |i|
    digit = n.to_s.length
    
    nums = n.chars.map(&:to_i)
    
    puts nums
end