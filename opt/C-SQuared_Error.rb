n = gets.to_i
sum = 0

sum_squared = 0
A = gets.split(' ').map(&:to_i)

A.each do |a|
    sum += a
    sum_squared += a * a
end

ans = n * sum_squared - sum * sum
puts ans