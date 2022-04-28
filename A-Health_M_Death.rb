m, h = gets.split(' ').map(&:to_i)
if h % m == 0
    ans = 'Yes'
else
    ans = 'No'
end
puts ans
