a, b = gets.split(" ").map(&:to_i)
ans_a = 0
ans_b = 0

for i in 0..3
    ans_a += a % 10
    ans_b += b % 10
    a /= 10
    b /= 10
    a.floor
    b.floor
end
if ans_a >= ans_b
    puts ans_a
else
    puts ans_b
end