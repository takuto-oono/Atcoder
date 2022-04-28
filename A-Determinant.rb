a, b = gets.split(" ").map(&:to_i)
c, d = gets.split(" ").map(&:to_i)

ans = a * d - b * c
puts ans