n = gets.to_i


ans = 0
if n >= 1000
    ans += n - 999
end

if n >= 10 ** 6
    ans += n - 999999
end

if n >= 10 ** 9
    ans += n - 999999999
end

if n >= 10 ** 12
    ans += n - 999999999999
end

if n >= 10 ** 15
    ans += n - 999999999999999
end

puts ans








